"""
Geo-KTF static site generator.

Run:
    python generate_geo_ktf_site.py

Outputs (repo root, GitHub Pages ready):
    index.html
    data/geo_ktf.json
    .nojekyll

UCGIS-style explorer: zoomable circle packing on the left,
concept / tool explanations on the right.
"""

from pathlib import Path
import json

from tool_catalog import TOOL_INFO
from category_descriptions import CATEGORY_DESCRIPTIONS


def leaf(name, tools, description=""):
    return {
        "name": name,
        "description": description
        or f"{name}: geospatial concept mapped to representative tools and operations.",
        "tools": tools,
    }


def group(name, children, description="", goal_verb="", goal=""):
    node = {
        "name": name,
        "description": description
        or f"{name}: browse nested concepts and the tools linked to each.",
        "children": children,
    }
    if goal_verb:
        node["goal_verb"] = goal_verb
    if goal:
        node["goal"] = goal
    return node


def enrich_category_descriptions(node, path=None):
    """Attach 2-3 sentence descriptions to leaf categories."""
    path = (path or []) + [node["name"]]
    key = " › ".join(path)
    if "tools" in node and key in CATEGORY_DESCRIPTIONS:
        node["description"] = CATEGORY_DESCRIPTIONS[key]
    for child in node.get("children", []):
        enrich_category_descriptions(child, path)
    return node


GEO_KTF_DATA = {
    "name": "Geo-KTF",
    "description": (
        "Geo Knowledge Tool Framework: six pillars that move from understanding "
        "foundations, to doing operations, applying workflows, ensuring quality, "
        "delivering outputs, and enabling analysis with providers."
    ),
    "children": [
        group(
            "Basic Geospatial Knowledge",
            [
                group(
                    "Relationship",
                    [
                        leaf(
                            "Spatial relationships",
                            [
                                "Buffer", "Clip", "Intersection", "Difference", "Union", "Dissolve",
                                "Centroids", "Convex hull", "Voronoi polygons", "Split with lines",
                                "Line intersections", "Join attributes by location",
                                "Join attributes by nearest", "Extract by location",
                                "ST_Buffer", "ST_Intersects", "ST_Contains", "ST_Within",
                                "ST_Overlaps", "ST_Touches", "ST_Crosses", "ST_DWithin",
                                "geopandas.overlay()", "geopandas.sjoin()", "geopandas.sjoin_nearest()",
                            ],
                            "How features relate in space: containment, overlap, proximity, and overlay.",
                        ),
                        leaf(
                            "Scale",
                            [
                                "Simplify", "Generalize", "Create grid",
                                "Generate points (pixel centroids) inside polygons",
                                "gdaladdo", "gdalbuildvrt", "gdal_retile",
                            ],
                            "Representation and processing across spatial resolutions and levels of detail.",
                        ),
                        leaf(
                            "Uncertainty",
                            [
                                "Random points in extent", "Random points in polygons",
                                "Random selection", "QGIS Print Layout", "QGIS Reports",
                                "QGIS Label settings", "QGIS Style Manager",
                            ],
                            "Sampling, stochastic variation, and communicating uncertainty in outputs.",
                        ),
                        leaf(
                            "Distance",
                            [
                                "Distance matrix", "Distance to nearest hub",
                                "DBSCAN clustering", "Heatmap / kernel density estimation",
                                "ST_Intersects", "ST_DWithin", "ST_Contains",
                                "geopandas.sjoin()", "geopandas.overlay()",
                            ],
                            "Metric and topological distance as a basis for nearness and density analysis.",
                        ),
                    ],
                    "Spatial relationships, scale, uncertainty, and distance concepts.",
                ),
                group(
                    "Data Models",
                    [
                        leaf(
                            "Vector",
                            [
                                "ogrinfo", "ogr2ogr", "geopandas.read_file()", "geopandas.read_postgis()",
                                "geopandas.to_file()", "geopandas.to_crs()", "geopandas.overlay()",
                                "geopandas.sjoin()", "geopandas.sjoin_nearest()", "geopandas.to_parquet()",
                                "ST_Transform", "ST_IsValid", "ST_IsValidDetail",
                            ],
                            "Points, lines, and polygons with attributes and topology.",
                        ),
                        leaf(
                            "Raster",
                            [
                                "gdalinfo", "gdal_translate", "gdalwarp", "gdalbuildvrt", "gdal_merge",
                                "gdal_calc", "gdal_contour", "gdal_proximity", "gdal_fillnodata",
                                "gdal_polygonize", "rasterio.open()", "rasterio.mask.mask()",
                                "rasterio.features.rasterize()", "rasterio.merge.merge()",
                            ],
                            "Grid-based continuous or categorical surfaces.",
                        ),
                        leaf(
                            "Point Cloud",
                            [
                                "PDAL pipeline", "readers.las", "filters.crop", "filters.range",
                                "filters.reprojection", "writers.las", "writers.gdal",
                            ],
                            "Dense 3D point measurements such as LiDAR.",
                        ),
                        leaf(
                            "Mesh",
                            [
                                "Mesh Calculator", "Export mesh edges", "Export mesh faces",
                                "Export mesh on grid", "QGIS 3D Map View",
                            ],
                            "Surface meshes for 3D geometry and visualization.",
                        ),
                        leaf(
                            "TIN",
                            ["TIN Interpolation", "Delaunay triangulation"],
                            "Triangulated irregular networks for terrain and interpolation.",
                        ),
                        leaf(
                            "DEM",
                            [
                                "gdaldem hillshade", "gdaldem slope", "gdaldem aspect",
                                "gdaldem roughness", "gdaldem TRI", "gdaldem TPI",
                                "gdal_contour", "gdal_viewshed",
                            ],
                            "Digital elevation models and derived terrain surfaces.",
                        ),
                        leaf(
                            "Network",
                            [
                                "pgr_dijkstra", "pgr_aStar", "pgr_drivingDistance", "pgr_dijkstraVia",
                                "pgr_KSP", "pgr_dijkstraCostMatrix", "pgr_dijkstraNear",
                                "pgr_dijkstraNearCost",
                            ],
                            "Graph models for routes, costs, and connectivity.",
                        ),
                    ],
                    "Core geospatial data structures and their processing ecosystems.",
                ),
                group(
                    "Coordinate Reference Systems",
                    [
                        leaf(
                            "Geographic",
                            [
                                "pyproj.CRS", "pyproj.Transformer", "geopandas.to_crs()",
                                "ST_Transform", "gdalwarp", "projinfo",
                            ],
                            "Defining locations on the ellipsoid versus planar projected systems.",
                        ),
                        leaf(
                            "Datums",
                            [
                                "pyproj.CRS", "pyproj.Transformer", "ST_Transform",
                                "gdalwarp", "projinfo",
                            ],
                            "Datum definitions and transforming between reference frames.",
                        ),
                        leaf(
                            "Vertical CRS",
                            ["pyproj.CRS", "gdalinfo"],
                            "Height and depth reference systems.",
                        ),
                        leaf(
                            "Units",
                            ["pyproj.CRS", "gdalinfo", "ogrinfo"],
                            "Linear and angular units carried by CRS definitions.",
                        ),
                        leaf(
                            "Common CRS Errors",
                            [
                                "pyproj.Transformer(always_xy=True)", "geopandas.to_crs()",
                                "ST_Transform", "gdalwarp", "Reproject layer",
                            ],
                            "Axis order, missing CRS, and incorrect reprojection pitfalls.",
                        ),
                    ],
                    "How location is referenced, transformed, and validated.",
                ),
                group(
                    "Data Quality",
                    [
                        leaf(
                            "Metadata",
                            ["gdalinfo", "ogrinfo", "geopandas.read_file()", "rasterio.open()"],
                            "Descriptive information about datasets and processing context.",
                        ),
                        leaf(
                            "Lineage",
                            ["QGIS Processing History", "QGIS Processing Log"],
                            "Provenance of how data and results were produced.",
                        ),
                        leaf(
                            "Accuracy",
                            ["gdalinfo", "ogrinfo", "pyproj.CRS", "pyproj.Transformer"],
                            "Positional correctness of geospatial measurements and locations.",
                        ),
                        leaf(
                            "Validity",
                            [
                                "QGIS Geometry Checker Plugin", "Check Geometries",
                                "Fix Geometries", "ST_IsValid", "ST_IsValidDetail",
                            ],
                            "Geometric correctness and repair of invalid features.",
                        ),
                    ],
                    "Trust, fitness for use, and documentation of geospatial data.",
                ),
                group(
                    "Spatial Analysis",
                    [
                        leaf(
                            "Vector Analysis",
                            [
                                "Buffer", "Clip", "Intersection", "Difference", "Union", "Dissolve",
                                "Centroids", "Convex hull", "Voronoi polygons", "Split with lines",
                                "Line intersections", "Join attributes by location",
                                "Join attributes by nearest", "Extract by location",
                                "Distance matrix", "Distance to nearest hub",
                            ],
                            "Operations on vector geometries and attributes.",
                        ),
                        leaf(
                            "Raster Analysis",
                            [
                                "Raster Calculator", "gdal_calc", "gdal_proximity",
                                "gdal_fillnodata", "gdal_polygonize", "gdalwarp", "gdal_translate",
                            ],
                            "Map algebra and raster transformations.",
                        ),
                        leaf(
                            "Terrain Analysis",
                            [
                                "gdaldem slope", "gdaldem aspect", "gdaldem hillshade",
                                "gdaldem roughness", "gdaldem TRI", "gdaldem TPI",
                                "gdal_contour", "gdal_viewshed",
                            ],
                            "Derivatives and landform metrics from elevation surfaces.",
                        ),
                        leaf(
                            "Network Analysis",
                            [
                                "pgr_dijkstra", "pgr_aStar", "pgr_drivingDistance",
                                "pgr_dijkstraVia", "pgr_KSP", "pgr_dijkstraCostMatrix",
                            ],
                            "Path finding, catchment, and cost analysis on networks.",
                        ),
                        leaf(
                            "Spatial Statistics",
                            [
                                "DBSCAN clustering", "Heatmap / kernel density estimation",
                                "Distance matrix", "Distance to nearest hub",
                            ],
                            "Pattern, density, and clustering summaries of spatial distributions.",
                        ),
                        leaf(
                            "Spatial Interpolation",
                            ["TIN Interpolation", "IDW Interpolation", "gdal_grid"],
                            "Estimating continuous surfaces from discrete observations.",
                        ),
                    ],
                    "Core analytical families spanning vector, raster, network, and statistics.",
                ),
                group(
                    "Ethics",
                    [
                        leaf(
                            "Privacy",
                            [
                                "ogr2ogr", "geopandas.to_file()", "geopandas.to_parquet()",
                                "gdalinfo", "ogrinfo", "QGIS Print Layout", "QGIS Reports",
                                "QGIS Processing History", "QGIS Processing Log",
                            ],
                            "Responsible use, licensing, dissemination, and standards compliance.",
                        ),
                    ],
                    "Ethical, legal, and governance dimensions of geospatial practice.",
                ),
            ],
            "Foundational geospatial concepts, data models, CRS, quality, analysis, and governance.",
            goal_verb="Understand",
            goal="The foundations of geospatial analysis.",
        ),
        group(
            "Analytical Capabilities",
            [
                leaf("Data Inspection", ["gdalinfo", "ogrinfo", "geopandas.read_file()", "geopandas.read_postgis()", "rasterio.open()", "pdal pipeline"], "Inspect structure, extent, CRS, and content of geospatial datasets."),
                leaf("Data Conversion", ["ogr2ogr", "gdal_translate", "gdalwarp", "gdalbuildvrt", "geopandas.to_file()", "geopandas.to_parquet()", "geopandas.to_postgis()"], "Transform formats, encodings, and storage targets."),
                leaf("CRS Management", ["pyproj.CRS", "pyproj.Transformer", "projinfo", "ST_Transform", "geopandas.to_crs()", "gdalwarp"], "Assign, inspect, and reproject coordinate reference systems."),
                leaf("Vector Processing", ["Buffer", "Clip", "Intersection", "Difference", "Union", "Dissolve", "Merge Vector Layers", "Multipart to Singleparts", "Split Vector Layer", "Join attributes by location", "Join attributes by nearest", "Extract by location", "Simplify"], "Geometry and attribute operations on vector layers."),
                leaf("Raster Processing", ["Raster Calculator", "gdal_calc", "gdal_translate", "gdalwarp", "gdal_proximity", "gdal_fillnodata", "gdal_polygonize", "gdal_contour", "gdalbuildvrt", "gdal_merge"], "Raster resampling, algebra, mosaics, and conversions."),
                leaf("Database Processing", ["ST_Buffer", "ST_Intersects", "ST_DWithin", "ST_Transform", "ST_IsValid", "geopandas.read_postgis()", "geopandas.to_postgis()", "DuckDB ST_Read"], "In-database geospatial read/write and processing."),
                leaf("Spatial SQL", ["ST_Intersects", "ST_Contains", "ST_Within", "ST_Buffer", "ST_DWithin", "ST_Intersection", "ST_Distance", "ST_Transform"], "Declarative spatial queries using SQL geometry functions."),
                leaf("Geocoding", ["openrouteservice geocoding", "Nominatim", "Google Geocoding API", "ArcGIS Geocoding Service"], "Convert between place names/addresses and coordinates."),
                leaf("Routing", ["Shortest Path", "Service Area", "Distance Matrix", "pgr_dijkstra", "pgr_aStar", "pgr_drivingDistance", "openrouteservice directions"], "Compute paths, costs, and travel directions on networks."),
                leaf("Accessibility", ["Service Area", "Distance Matrix", "openrouteservice isochrones", "pgr_drivingDistance"], "Measure reachability by time, distance, or impedance."),
                leaf("Remote Sensing", ["gdal_translate", "gdalwarp", "gdal_calc", "gdalbuildvrt", "rasterio.mask.mask()", "rasterio.features.rasterize()", "OTB BandMath", "OTB KMeansClassification", "OTB ComputeImagesStatistics"], "Process Earth observation imagery and derived products."),
                leaf("Spatial Statistics", ["esda.Moran", "esda.Moran_Local", "esda.Geary", "esda.GetisOrd", "libpysal.weights", "Heatmap (Kernel Density Estimation)"], "Quantify spatial autocorrelation, hotspots, and density."),
                leaf("Spatial Interpolation", ["IDW Interpolation", "TIN Interpolation", "gdal_grid", "PyKrige"], "Predict values at unsampled locations."),
                leaf("Spatial Clustering", ["DBSCAN clustering", "K-means clustering", "scikit-learn DBSCAN"], "Group observations by spatial and/or attribute similarity."),
                leaf("Cartography", ["QGIS Style Manager", "QGIS Symbol Selector", "QGIS Print Layout", "QGIS Reports", "QGIS Server"], "Visual encoding and map production."),
                leaf("Reporting", ["QGIS Print Layout", "QGIS Reports", "QGIS Processing Log"], "Document methods, results, and reproducible outputs."),
            ],
            "Software-independent operations bridging concepts and executable tools.",
            goal_verb="Action",
            goal="The operations to achieve objectives.",
        ),
        group(
            "Workflow",
            [
                leaf("Site Selection", ["Buffer", "Clip", "Intersection", "Join attributes by location", "Raster Calculator", "Weighted Overlay"], "Combine criteria to identify candidate locations."),
                leaf("Suitability Analysis", ["Raster Calculator", "gdal_calc", "Weighted Overlay", "Fuzzy Overlay", "QGIS Model Designer"], "Score locations against multi-criteria suitability models."),
                leaf("Catchment Analysis", ["Service Area", "pgr_drivingDistance", "openrouteservice isochrones", "Distance Matrix"], "Delineate areas served by facilities or outlets."),
                leaf("Accessibility Analysis", ["Shortest Path", "Service Area", "Distance Matrix", "openrouteservice directions", "openrouteservice matrices"], "Evaluate ease of reaching destinations."),
                leaf("Demographic Enrichment", ["Join attributes by location", "geopandas.sjoin()", "ST_Intersects", "ST_Contains"], "Attach population or socioeconomic attributes to features."),
                leaf("Hazard Assessment", ["Slope", "Aspect", "Hillshade", "Raster Calculator", "ST_Intersects"], "Map exposure and susceptibility to hazards."),
                leaf("Environmental Assessment", ["Buffer", "Intersection", "Raster Calculator", "gdal_proximity", "gdal_fillnodata"], "Evaluate environmental conditions and impacts."),
                leaf("Infrastructure Planning", ["Shortest Path", "Service Area", "Distance Matrix", "Buffer", "ST_DWithin"], "Support planning of networks and facilities."),
                leaf("Land Use Analysis", ["Clip", "Intersection", "Union", "Dissolve", "Raster Calculator"], "Characterize and compare land-use patterns."),
                leaf("Change Detection", ["gdalwarp", "gdal_translate", "Raster Calculator", "OTB BandMath", "gdalbuildvrt"], "Compare multi-temporal datasets to find change."),
                leaf("Terrain Analysis", ["Slope", "Aspect", "Hillshade", "TRI", "TPI", "Roughness", "Viewshed", "Contour"], "Derive landform metrics from elevation data."),
                leaf("Hydrological Analysis", ["Fill sinks", "Watershed", "Flow accumulation", "Flow direction"], "Model surface water flow and drainage."),
                leaf("Visibility Analysis", ["Viewshed"], "Determine what can be seen from a viewpoint."),
                leaf("Remote Sensing Classification", ["OTB TrainImagesClassifier", "OTB KMeansClassification", "OTB BandMath"], "Assign classes to pixels or objects from imagery."),
                leaf("Urban Growth Analysis", ["Raster Calculator", "Change Detection", "Kernel Density Estimation"], "Track and interpret urban expansion patterns."),
            ],
            "Reusable analytical workflows that combine capabilities for real tasks.",
            goal_verb="Apply",
            goal="Reusable workflows for real-world tasks.",
        ),
        group(
            "Validation",
            [
                leaf("Geometry Validation", ["Check Geometries", "Fix Geometries", "QGIS Geometry Checker", "ST_IsValid", "ST_IsValidDetail", "geometry.is_valid (Shapely)"], "Detect and repair invalid geometries."),
                leaf("CRS Validation", ["pyproj.CRS", "pyproj.Transformer", "projinfo", "ST_Transform", "gdalwarp", "Reproject Layer"], "Confirm CRS assignment and correct transformations."),
                leaf("Metadata Validation", ["gdalinfo", "ogrinfo", "rio info", "geopandas.read_file()"], "Check completeness and consistency of metadata."),
                leaf("Schema Validation", ["ogrinfo", "geopandas.read_file()", "geopandas.read_postgis()", "Refactor Fields", "Delete Duplicate Geometries"], "Validate fields, types, and structural integrity."),
                leaf("Topology Validation", ["Check Geometries", "Fix Geometries", "ST_IsValid", "ST_IsValidDetail", "geometry.is_valid"], "Ensure topological rules and consistency."),
                leaf("Data Quality Assessment", ["Basic Statistics for Fields", "Field Statistics", "gdalinfo", "ogrinfo"], "Summarize quality indicators across datasets."),
                leaf("Statistical Validation", ["esda.Moran", "esda.Moran_Local", "esda.Geary", "esda.GetisOrd", "libpysal.weights"], "Validate spatial patterns with inferential diagnostics."),
                leaf("Result Validation", ["QGIS Processing History", "QGIS Processing Log", "QGIS Reports", "qgis_process"], "Audit analytical outputs and processing trails."),
                leaf("Risk Detection", ["ST_IsValid", "ST_IsValidDetail", "pyproj.Transformer(always_xy=True)", "gdalinfo"], "Flag high-risk data defects before downstream use."),
            ],
            "Quality, correctness, and reproducibility checks for data and outputs.",
            goal_verb="Ensure",
            goal="Quality and reliability of results.",
        ),
        group(
            "Output Framework",
            [
                leaf("Tables", ["geopandas.to_file()", "geopandas.to_parquet()", "geopandas.to_postgis()", "ogr2ogr"], "Tabular exports of attributes and summaries."),
                leaf("GIS Files", ["ogr2ogr", "gdal_translate", "gdalwarp", "geopandas.to_file()", "geopandas.to_parquet()"], "Interoperable geospatial file deliverables."),
                leaf("Reports", ["QGIS Reports", "QGIS Print Layout"], "Narrative and figure-based analysis reports."),
                leaf("Dashboards", ["QGIS Server", "MapLibre GL JS"], "Interactive operational views of spatial results."),
                leaf("APIs", ["QGIS Server", "GeoServer", "PostGIS", "DuckDB Spatial"], "Programmatic access to spatial data and services."),
                leaf("Metadata", ["gdalinfo", "ogrinfo", "rio info"], "Machine- and human-readable dataset descriptions."),
                leaf("Logs & Reproducibility", ["QGIS Processing History", "QGIS Processing Log", "qgis_process"], "Artifacts that support rerunning and auditing workflows."),
            ],
            "Deliverables and channels for data, APIs, reports, and reproducibility.",
            goal_verb="Deliver",
            goal="Outputs for decision making and sharing.",
        ),
        group(
            "Provider Registry",
            [
                leaf("Geospatial Libraries", ["GDAL / OGR", "GeoPandas", "Shapely", "Rasterio", "Fiona", "PyProj", "PDAL", "PySAL", "OTB (Orfeo ToolBox)"], "Core libraries used to implement geospatial operations."),
                leaf("Network Analysis", ["pgRouting", "openrouteservice", "OSRM", "Valhalla"], "Routing engines and network analysis providers."),
                leaf("Cloud", ["Apache Sedona", "GeoParquet", "Cloud Optimized GeoTIFF (COG)", "AWS"], "Scalable formats and engines for large spatial data."),
                leaf("Basemap", ["OpenStreetMap", "Overture Maps", "Natural Earth", "Microsoft Planetary Computer", "Government Open Data APIs"], "Reference basemaps and open geospatial data sources."),
                leaf("Web Mapping", ["MapLibre GL JS", "OpenLayers", "Leaflet", "GeoServer"], "Clients and servers for interactive web maps."),
                leaf("AI", ["scikit-learn", "XGBoost", "PyTorch", "TensorFlow", "Segment Anything Model (SAM)"], "ML frameworks applied to geospatial tasks."),
            ],
            "Software ecosystems, libraries, and infrastructure behind the tools.",
            goal_verb="Enable",
            goal="Resources and platforms to power analysis.",
        ),
    ],
}


INDEX_HTML = '<!DOCTYPE html>\n<html lang="en">\n<head>\n  <meta charset="UTF-8" />\n  <meta name="viewport" content="width=device-width, initial-scale=1.0" />\n  <title>Geo-KTF: Knowledge Visualization and Search</title>\n  <script src="https://cdn.tailwindcss.com"></script>\n  <script src="https://cdn.jsdelivr.net/npm/d3@7.9.0/dist/d3.min.js"></script>\n  <style>\n    :root {\n      --ink: #1c2430;\n      --muted: #5b6775;\n      --line: #d7dde5;\n      --wash: #f3f6f9;\n      --accent: #1f4e79;\n    }\n    body {\n      margin: 0;\n      color: var(--ink);\n      background:\n        radial-gradient(circle at 12% 8%, #e8eef5 0%, transparent 42%),\n        radial-gradient(circle at 88% 0%, #edf3ea 0%, transparent 36%),\n        var(--wash);\n      font-family: Georgia, "Iowan Old Style", "Palatino Linotype", Palatino, serif;\n    }\n    .ui-sans { font-family: "Avenir Next", "Segoe UI", "Helvetica Neue", Helvetica, Arial, sans-serif; }\n    #viz-wrap {\n      position: relative;\n      height: min(78vh, calc(100vh - 7rem));\n      min-height: 520px;\n      overflow: hidden;\n      touch-action: none;\n      cursor: grab;\n      background: linear-gradient(180deg, #f7fafc 0%, #eef3f8 100%);\n    }\n    #viz-wrap.is-panning { cursor: grabbing; }\n    #pack-svg { width: 100%; height: 100%; display: block; }\n    .pack-label {\n      pointer-events: none;\n      text-anchor: middle;\n      dominant-baseline: middle;\n      fill: #1c2430;\n      font-family: "Avenir Next", "Segoe UI", Helvetica, Arial, sans-serif;\n      font-weight: 650;\n      paint-order: stroke;\n      stroke: rgba(255,255,255,0.82);\n      stroke-width: 2px;\n    }\n    .pack-circle { cursor: pointer; }\n    .pack-circle:hover { stroke-width: 2.6px !important; }\n    .crumb-btn:hover { color: var(--accent); }\n    .tool-card {\n      border: 1px solid var(--line);\n      background: #fff;\n      border-radius: 14px;\n      padding: 0.95rem 1.05rem;\n    }\n    .tool-blurb {\n      margin-top: 0.55rem;\n      font-size: 0.9rem;\n      line-height: 1.55;\n      color: #3a4553;\n    }\n    .child-link { color: #1f4e79; }\n    .child-link:hover { text-decoration: underline; }\n    .goal-banner {\n      margin-top: 1rem;\n      border: 1px solid rgba(28, 36, 48, 0.12);\n      border-radius: 16px;\n      padding: 0.95rem 1.05rem;\n    }\n    .goal-verb {\n      display: inline-block;\n      font-size: 0.7rem;\n      font-weight: 700;\n      letter-spacing: 0.14em;\n      text-transform: uppercase;\n      color: #1c2430;\n      background: rgba(255,255,255,0.72);\n      border-radius: 999px;\n      padding: 0.2rem 0.55rem;\n    }\n    .goal-grid {\n      display: grid;\n      gap: 0.65rem;\n      margin-top: 0.85rem;\n    }\n    .goal-item {\n      border: 1px solid rgba(28, 36, 48, 0.12);\n      border-radius: 12px;\n      padding: 0.7rem 0.85rem;\n      cursor: pointer;\n      text-align: left;\n      width: 100%;\n      transition: filter 0.15s ease, transform 0.15s ease;\n    }\n    .goal-item:hover { filter: brightness(0.97); transform: translateY(-1px); }\n    .hint-pill {\n      position: absolute;\n      right: 1rem;\n      bottom: 1rem;\n      z-index: 5;\n      background: rgba(255,255,255,0.92);\n      border: 1px solid #d7dde5;\n      border-radius: 999px;\n      padding: 0.4rem 0.8rem;\n      font-size: 12px;\n      color: #5b6775;\n      pointer-events: none;\n    }\n  </style>\n</head>\n<body>\n  <div class="min-h-screen">\n    <header class="ui-sans border-b border-slate-200/80 bg-white/85 backdrop-blur px-4 py-4 sm:px-6 lg:px-8">\n      <div class="mx-auto flex max-w-[1400px] flex-col gap-2 sm:flex-row sm:items-end sm:justify-between">\n        <div>\n          <h1 class="text-2xl font-semibold tracking-tight text-slate-900 sm:text-3xl">\n            Geo-KTF: Knowledge Visualization and Search\n          </h1>\n        </div>\n        <div id="stats" class="ui-sans flex gap-4 text-sm text-slate-600"></div>\n      </div>\n    </header>\n\n    <main class="mx-auto grid max-w-[1400px] gap-0 lg:grid-cols-[minmax(0,1.2fr)_minmax(340px,0.8fr)]">\n      <section class="border-b border-slate-200 lg:border-b-0 lg:border-r">\n        <div class="ui-sans relative z-10 flex flex-wrap items-center gap-2 px-4 pt-4">\n          <div class="flex flex-wrap items-center gap-2 rounded-full bg-white/95 px-3 py-1.5 text-sm text-slate-600 shadow-sm ring-1 ring-slate-200">\n            <button id="btn-back" class="crumb-btn font-medium text-slate-800 disabled:text-slate-400" disabled>Back</button>\n            <button id="btn-reset" class="crumb-btn text-slate-500">Reset</button>\n            <span class="text-slate-300">/</span>\n            <div id="breadcrumb" class="flex flex-wrap items-center gap-1"></div>\n          </div>\n        </div>\n        <div id="viz-wrap">\n          <svg id="pack-svg" role="img" aria-label="Geo-KTF circle packing visualization"></svg>\n        </div>\n      </section>\n\n      <aside class="ui-sans bg-white/75 px-5 py-6 sm:px-7 lg:max-h-[calc(100vh-6.5rem)] lg:overflow-y-auto">\n        <div id="detail"></div>\n      </aside>\n    </main>\n  </div>\n\n  <script id="geo-ktf-data" type="application/json">__DATA__</script>\n  <script id="tool-info" type="application/json">__TOOLS__</script>\n  <script>\n    const raw = JSON.parse(document.getElementById("geo-ktf-data").textContent);\n    const TOOL_INFO = JSON.parse(document.getElementById("tool-info").textContent);\n\n    const COLORS = ["#9ec5e8","#f2d28b","#b9d7a5","#f0b7a4","#cbb6e4","#9fd3d0"];\n\n    function countTools(node) {\n      if (node.tools) return node.tools.length;\n      return (node.children || []).reduce((s, c) => s + countTools(c), 0);\n    }\n    function countLeaves(node) {\n      if (node.tools) return 1;\n      return (node.children || []).reduce((s, c) => s + countLeaves(c), 0);\n    }\n    function flattenLeaves(node) {\n      if (node.tools) return [node];\n      return (node.children || []).flatMap(flattenLeaves);\n    }\n\n    const leaves = flattenLeaves(raw);\n    const totalTools = new Set(leaves.flatMap((l) => l.tools)).size;\n    document.getElementById("stats").innerHTML = `\n      <div><span class="font-semibold text-slate-900">${raw.children.length}</span> sections</div>\n      <div><span class="font-semibold text-slate-900">${leaves.length}</span> concepts</div>\n      <div><span class="font-semibold text-slate-900">${totalTools}</span> unique tools</div>\n    `;\n\n    const wrap = document.getElementById("viz-wrap");\n    const svg = d3.select("#pack-svg");\n    const g = svg.append("g");\n\n    let width = 800, height = 800;\n    function resize() {\n      const rect = wrap.getBoundingClientRect();\n      width = Math.max(480, rect.width);\n      height = Math.max(480, rect.height);\n      svg.attr("viewBox", `0 0 ${width} ${height}`);\n    }\n    resize();\n\n    const hierarchy = d3.hierarchy(raw)\n      .sum((d) => (d.tools ? Math.max(d.tools.length, 3) : 0))\n      .sort((a, b) => (b.value || 0) - (a.value || 0));\n\n    const root = d3.pack().size([width, height]).padding((d) => (d.depth < 2 ? 8 : 4))(hierarchy);\n    let focus = root;\n    let selected = root;\n\n    root.eachBefore((d) => {\n      if (d.depth === 0) d.color = "#e8eef4";\n      else if (d.depth === 1) d.color = COLORS[d.parent.children.indexOf(d) % COLORS.length];\n      else d.color = d3.color(d.parent.color).brighter(0.28 + d.depth * 0.05).formatHex();\n    });\n\n    const node = g.selectAll("circle")\n      .data(root.descendants().slice(1))\n      .join("circle")\n      .attr("class", "pack-circle")\n      .attr("cx", (d) => d.x)\n      .attr("cy", (d) => d.y)\n      .attr("r", (d) => d.r)\n      .attr("fill", (d) => (d.children ? d.color : "#ffffff"))\n      .attr("fill-opacity", (d) => (d.children ? 0.9 : 0.98))\n      .attr("stroke", (d) => (d.children ? d3.color(d.color).darker(0.4) : "#8e9bab"))\n      .attr("stroke-width", 1.2)\n      .each(function(d) {\n        d3.select(this).selectAll("title").data([d.data.name]).join("title").text((t) => t);\n      });\n\n    const label = g.selectAll("text")\n      .data(root.descendants().slice(1))\n      .join("text")\n      .attr("class", "pack-label")\n      .attr("x", (d) => d.x)\n      .attr("y", (d) => d.y)\n      .style("display", "none");\n\n    // Free mouse zoom + pan\n    const zoomBehavior = d3.zoom()\n      .scaleExtent([0.35, 48])\n      .clickDistance(8)\n      .filter((event) => {\n        if (event.type === "wheel") return true;\n        // ignore right/middle buttons\n        return !event.ctrlKey && !event.button;\n      })\n      .on("start", (event) => {\n        if (event.sourceEvent && event.sourceEvent.type !== "wheel") {\n          wrap.classList.add("is-panning");\n        }\n      })\n      .on("end", () => wrap.classList.remove("is-panning"))\n      .on("zoom", (event) => {\n        g.attr("transform", event.transform);\n        updateLabels(event.transform.k);\n      });\n\n    svg.call(zoomBehavior);\n    wrap.addEventListener("wheel", (e) => e.preventDefault(), { passive: false });\n\n    // Click-to-open with drag threshold (works with d3.zoom)\n    let pointerDown = null;\n    node\n      .style("pointer-events", "all")\n      .on("pointerdown", (event, d) => {\n        pointerDown = { x: event.clientX, y: event.clientY, id: d };\n      })\n      .on("click", (event, d) => {\n        // Ignore click if this was a pan gesture\n        if (pointerDown && pointerDown.id === d) {\n          const moved = Math.hypot(event.clientX - pointerDown.x, event.clientY - pointerDown.y);\n          pointerDown = null;\n          if (moved > 8) return;\n        }\n        event.stopPropagation();\n        openNode(d);\n      });\n\n    svg.on("dblclick.zoom", null); // disable default d3 double-click zoom reset\n    svg.on("dblclick", (event) => {\n      event.preventDefault();\n      if (focus.parent) openNode(focus.parent, true);\n      else resetView();\n    });\n\n    document.getElementById("btn-back").addEventListener("click", () => {\n      if (focus.parent) openNode(focus.parent, true);\n    });\n    document.getElementById("btn-reset").addEventListener("click", () => resetView());\n\n    function fitTo(d, animate = true) {\n      focus = d;\n      const pad = 1.12;\n      const k = Math.min(width, height) / (d.r * 2 * pad);\n      const x = width / 2 - d.x * k;\n      const y = height / 2 - d.y * k;\n      const transform = d3.zoomIdentity.translate(x, y).scale(k);\n      const t = svg.transition().duration(animate ? 500 : 0);\n      t.call(zoomBehavior.transform, transform)\n        .on("end", () => updateLabels(d3.zoomTransform(svg.node()).k));\n      // also update immediately for duration 0 / first frame\n      updateLabels(k);\n      document.getElementById("btn-back").disabled = !focus.parent;\n    }\n\n    function openNode(d, forceFit = false) {\n      selected = d;\n      renderDetail(d);\n      renderBreadcrumb(d);\n      if (d.children) fitTo(d, true);\n      else if (forceFit && d.parent) fitTo(d.parent, true);\n      else if (!d.children && d.parent && focus !== d.parent) fitTo(d.parent, true);\n      // highlight selected\n      node.attr("stroke-width", (n) => (n === d ? 2.8 : 1.2))\n          .attr("stroke", (n) => (n === d ? "#1f4e79" : (n.children ? d3.color(n.color).darker(0.4) : "#8e9bab")));\n    }\n\n    function resetView() {\n      openNode(root, true);\n      fitTo(root, true);\n    }\n\n    function wrapLabel(text, radiusPx) {\n      // Always prefer full readable names; wrap long phrases onto multiple lines.\n      const maxChars = Math.max(5, Math.floor(radiusPx / 11));\n      if (text.length <= maxChars) return [text];\n      const words = text.split(/\\s+/);\n      if (words.length === 1) return [text]; // never truncate single words like "Scale"\n      const lines = [];\n      let line = "";\n      for (const w of words) {\n        const next = line ? line + " " + w : w;\n        if (next.length > maxChars && line) {\n          lines.push(line);\n          line = w;\n        } else line = next;\n      }\n      if (line) lines.push(line);\n      return lines.slice(0, 4);\n    }\n\n    function updateLabels(k) {\n      const scale = k || 1;\n      label.each(function (d) {\n        const el = d3.select(this);\n        const isChildOfFocus = d.parent === focus;\n        const isSelectedLeaf = d === selected && !d.children;\n        const visible = isChildOfFocus || isSelectedLeaf;\n        if (!visible) {\n          el.style("display", "none");\n          return;\n        }\n        const rPx = d.r * scale;\n        if (rPx < 28) {\n          el.style("display", "none");\n          return;\n        }\n        const lines = wrapLabel(d.data.name, rPx).slice(0, 2);\n        const font = Math.max(7, Math.min(9.5, rPx / 11));\n        el.style("display", "block")\n          .style("font-size", font + "px")\n          .attr("x", d.x)\n          .attr("y", d.y)\n          .selectAll("tspan").remove();\n        el.selectAll("tspan")\n          .data(lines)\n          .join("tspan")\n          .attr("x", d.x)\n          .attr("dy", (_, i) => (i === 0 ? `${-((lines.length - 1) * 0.55)}em` : "1.15em"))\n          .text((t) => t);\n      });\n    }\n\n    function pathOf(d) {\n      return d.ancestors().reverse().map((n) => n.data.name);\n    }\n\n    function toolMeta(name) {\n      return TOOL_INFO[name] || {\n        source: "Geo-KTF registry",\n        blurb: "Representative geospatial tool or operation linked to this concept.",\n      };\n    }\n\n    function renderBreadcrumb(d) {\n      const parts = d.ancestors().reverse();\n      const el = document.getElementById("breadcrumb");\n      el.innerHTML = parts.map((n, i) => {\n        const name = n.data.name;\n        const short = name.length > 30 ? name.slice(0, 29) + "…" : name;\n        return `<button class="crumb-btn ${i === parts.length - 1 ? "font-semibold text-slate-900" : "text-slate-500"}">${escapeHtml(short)}</button>`;\n      }).join(\'<span class="text-slate-300 mx-0.5">/</span>\');\n      el.querySelectorAll("button").forEach((btn, i) => {\n        btn.addEventListener("click", () => openNode(parts[i], true));\n      });\n    }\n\n    function renderDetail(d) {\n      const data = d.data;\n      const tools = data.tools || [];\n      const children = d.children || [];\n      const path = pathOf(d).join(" › ");\n      let goalHtml = "";\n      if (data.goal_verb && data.goal) {\n        const sectionColor = d.color || COLORS[Math.max(0, d.depth === 1 ? d.parent.children.indexOf(d) : 0)] || "#e8eef4";\n        goalHtml = `\n          <div class="goal-banner" style="background:${sectionColor}">\n            <div class="goal-verb">${escapeHtml(data.goal_verb)}</div>\n            <p class="mt-2 text-[0.98rem] leading-6 text-slate-800">${escapeHtml(data.goal)}</p>\n          </div>`;\n      } else if (d.depth === 0) {\n        const pillars = (d.children || []).filter((c) => c.data.goal_verb);\n        if (pillars.length) {\n          goalHtml = `\n            <div class="mt-5">\n              <h3 class="text-xs font-semibold uppercase tracking-[0.14em] text-slate-500">Framework goals</h3>\n              <p class="mt-2 text-sm leading-6 text-slate-600">Each major circle has a purpose in the Geo-KTF pipeline.</p>\n              <div class="goal-grid">\n                ${pillars.map((c, i) => `\n                  <button class="goal-item" data-child="${escapeHtml(c.data.name)}" style="background:${c.color || COLORS[i % COLORS.length]}">\n                    <div class="goal-verb">${escapeHtml(c.data.goal_verb)}</div>\n                    <div class="mt-1.5 text-sm font-semibold text-slate-900">${escapeHtml(c.data.name)}</div>\n                    <div class="mt-1 text-sm leading-5 text-slate-700">${escapeHtml(c.data.goal)}</div>\n                  </button>`).join("")}\n              </div>\n            </div>`;\n        }\n      }\n\n      // Root overview already shows Framework goals cards; skip duplicate Subtopics list there.\n      const childrenHtml = (children.length && d.depth > 0) ? `\n        <div class="mt-6">\n          <h3 class="text-xs font-semibold uppercase tracking-[0.14em] text-slate-500">Subtopics [${children.length}]</h3>\n          <ul class="mt-3 space-y-2">\n            ${children.map((c) => `\n              <li>\n                <button class="child-link text-left" data-child="${escapeHtml(c.data.name)}">${escapeHtml(c.data.name)}</button>\n                <span class="ml-2 text-xs text-slate-400">${countTools(c.data)} tools</span>\n              </li>`).join("")}\n          </ul>\n        </div>` : "";\n\n      const toolsHtml = tools.length ? `\n        <div class="mt-6">\n          <h3 class="text-xs font-semibold uppercase tracking-[0.14em] text-slate-500">Tools [${tools.length}]</h3>\n          <p class="mt-2 text-sm leading-6 text-slate-600">Where each tool comes from, and what it does.</p>\n          <div class="mt-3 space-y-2.5">\n            ${tools.map((t) => {\n              const meta = toolMeta(t);\n              return `<div class="tool-card">\n                <div class="flex flex-wrap items-baseline justify-between gap-2">\n                  <div class="font-semibold text-slate-900">${escapeHtml(t)}</div>\n                  <div class="text-[11px] uppercase tracking-wide text-slate-500">${escapeHtml(meta.source)}</div>\n                </div>\n                <p class="tool-blurb">${escapeHtml(meta.blurb)}</p>\n              </div>`;\n            }).join("")}\n          </div>\n        </div>` : "";\n\n      document.getElementById("detail").innerHTML = `\n        <h2 class="text-2xl font-semibold tracking-tight text-slate-900">${escapeHtml(data.name)}</h2>\n        <p class="mt-2 text-xs text-slate-400">${escapeHtml(path)}</p>\n        <p class="mt-4 text-[0.98rem] leading-7 text-slate-700">${escapeHtml(data.description || "")}</p>\n        ${goalHtml}\n        <div class="mt-5 grid grid-cols-2 gap-3">\n          <div class="rounded-2xl border border-slate-200 bg-slate-50 px-4 py-3">\n            <div class="text-xs uppercase tracking-wide text-slate-500">Concepts</div>\n            <div class="mt-1 text-xl font-semibold">${countLeaves(data)}</div>\n          </div>\n          <div class="rounded-2xl border border-slate-200 bg-slate-50 px-4 py-3">\n            <div class="text-xs uppercase tracking-wide text-slate-500">Tools</div>\n            <div class="mt-1 text-xl font-semibold">${countTools(data)}</div>\n          </div>\n        </div>\n        ${childrenHtml}\n        ${toolsHtml}\n      `;\n\n      document.querySelectorAll("[data-child]").forEach((btn) => {\n        btn.addEventListener("click", () => {\n          const child = children.find((c) => c.data.name === btn.getAttribute("data-child"));\n          if (child) openNode(child);\n        });\n      });\n    }\n\n    function escapeHtml(str) {\n      return String(str)\n        .replaceAll("&", "&amp;")\n        .replaceAll("<", "&lt;")\n        .replaceAll(">", "&gt;")\n        .replaceAll(\'"\', "&quot;");\n    }\n\n    window.addEventListener("resize", () => {\n      // keep current camera; only update svg box\n      resize();\n    });\n\n    selected = root;\n    focus = root;\n    fitTo(root, false);\n    renderDetail(root);\n    renderBreadcrumb(root);\n    updateLabels(d3.zoomTransform(svg.node()).k || 1);\n  </script>\n</body>\n</html>\n'

def build_site(output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "data").mkdir(parents=True, exist_ok=True)

    enrich_category_descriptions(GEO_KTF_DATA)
    data_json = json.dumps(GEO_KTF_DATA, ensure_ascii=False, indent=2)
    tools_json = json.dumps(TOOL_INFO, ensure_ascii=False, indent=2)
    html = INDEX_HTML.replace("__DATA__", data_json).replace("__TOOLS__", tools_json)

    (output_dir / "index.html").write_text(html, encoding="utf-8")
    (output_dir / "data" / "geo_ktf.json").write_text(data_json, encoding="utf-8")
    (output_dir / "data" / "tool_info.json").write_text(tools_json, encoding="utf-8")
    (output_dir / ".nojekyll").touch()


if __name__ == "__main__":
    out = Path(__file__).resolve().parent
    build_site(out)
    print(out)
