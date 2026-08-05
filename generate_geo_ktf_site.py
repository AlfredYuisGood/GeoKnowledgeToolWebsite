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
        "Geo-KTF (Geospatial Knowledge to Tool) organises geospatial practice into six pillars "
        "that follow a practical path: Understand foundations (Basic Geospatial Knowledge), "
        "Act with operations (Analytical Capabilities), Apply reusable workflows (Workflow), "
        "Ensure quality (Validation), Deliver outputs (Output), and Enable the work with "
        "software and data providers (Provider Registry). Concepts are kept separate from tools, "
        "so one idea can map to several equivalent implementations across QGIS, GDAL, PostGIS, "
        "Python, and related stacks. That separation makes it easier to learn what to do before "
        "choosing software, compare options fairly, and move from theory to executable practice."
    ),
    "children": [
        group(
            "Basic Geospatial Knowledge",
            [
                group(
                    "Relationship",
                    [
                        leaf(
                            "Overlay",
                            [
                                "Buffer", "Clip", "Intersection", "Difference", "Union", "Dissolve",
                                "Split with lines", "Line intersections",
                                "geopandas.overlay()", "ST_Buffer", "ST_Intersection",
                            ],
                            "Geometric set operations that reshape features by buffer, clip, and overlay.",
                        ),
                        leaf(
                            "Adjacency",
                            [
                                "ST_Touches", "ST_Overlaps", "ST_Crosses",
                                "Line intersections", "Extract by location",
                            ],
                            "Neighbor and boundary-sharing relationships without requiring containment.",
                        ),
                        leaf(
                            "Containment",
                            [
                                "ST_Contains", "ST_Within", "Extract by location",
                                "geopandas.sjoin()", "Clip",
                            ],
                            "Inside/outside relationships such as contains and within.",
                        ),
                        leaf(
                            "Distance",
                            [
                                "Distance Matrix", "Distance to nearest hub",
                                "Join attributes by nearest", "ST_Distance", "ST_DWithin",
                                "geopandas.sjoin_nearest()",
                            ],
                            "Measured nearness and proximity between features.",
                        ),
                        leaf(
                            "Connectivity",
                            [
                                "pgr_dijkstra", "pgr_aStar", "pgr_KSP",
                                "pgr_drivingDistance", "openrouteservice directions",
                            ],
                            "Network-path connectivity between places.",
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
                                "Random selection",
                            ],
                            "Sampling and stochastic variation used to represent uncertainty.",
                        ),
                    ],
                    "How features relate through overlay, topology, distance, connectivity, scale, and uncertainty.",
                ),
                group(
                    "Data Models",
                    [
                        leaf(
                            "Vector",
                            [
                                "ogrinfo", "ogr2ogr", "geopandas.read_file()",
                                "geopandas.read_postgis()", "geopandas.to_file()",
                                "geopandas.to_parquet()", "geopandas.to_postgis()",
                            ],
                            "Points, lines, and polygons with attributes and topology.",
                        ),
                        leaf(
                            "Raster",
                            [
                                "gdalinfo", "gdal_translate", "gdalwarp", "gdalbuildvrt",
                                "gdal_merge", "rasterio.open()", "rasterio.merge.merge()",
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
                        leaf(
                            "Temporal Data",
                            [
                                "gdalbuildvrt", "gdal_translate", "ogr2ogr",
                                "geopandas.read_file()", "GeoParquet",
                            ],
                            "Time-stamped and multi-temporal geospatial datasets for trend and change analysis.",
                        ),
                        leaf(
                            "Hex Grid",
                            [
                                "Create grid", "geopandas.sjoin()", "ST_Intersects",
                                "Join attributes by location",
                            ],
                            "Discrete tessellation models (e.g., hexagonal grids) for aggregation and indexing.",
                        ),
                        leaf(
                            "Trajectory",
                            [
                                "Shortest Path", "pgr_dijkstra", "pgr_dijkstraVia",
                                "pgr_aStar", "openrouteservice directions",
                            ],
                            "Movement paths and ordered location sequences for mobility analysis.",
                        ),
                        leaf(
                            "3D",
                            [
                                "QGIS 3D Map View", "Export mesh faces", "Export mesh edges",
                                "Mesh Calculator",
                            ],
                            "Three-dimensional urban object models and surfaces for visualization and analysis.",
                        ),
                        leaf(
                            "Spatial Indexing",
                            [
                                "CREATE INDEX USING GIST", "ST_GeoHash", "PostGIS",
                            ],
                            "Index structures that accelerate spatial search and joins.",
                        ),
                        leaf(
                            "Knowledge Graph",
                            [
                                "GeoSPARQL", "RDFLib", "Apache Jena",
                            ],
                            "Linked spatial entities and relationships for semantic queries.",
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
                            [
                                "pyproj.CRS", "pyproj.Transformer", "projinfo",
                                "gdalinfo", "ogrinfo", "ST_Transform", "gdalwarp",
                            ],
                            "Height and depth reference systems.",
                        ),
                        leaf(
                            "Units",
                            [
                                "pyproj.CRS", "projinfo", "gdalinfo", "ogrinfo",
                                "geopandas.to_crs()", "ST_Transform", "ST_Length", "ST_Area",
                            ],
                            "Linear and angular units carried by CRS definitions.",
                        ),
                        leaf(
                            "Common CRS Errors",
                            [
                                "pyproj.Transformer(always_xy=True)", "geopandas.set_crs()",
                                "geopandas.to_crs()", "ST_SetSRID", "ST_Transform",
                                "Assign projection", "Reproject Layer", "gdalwarp", "projinfo",
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
                            ["gdalinfo", "ogrinfo", "rio info", "geopandas.read_file()", "rasterio.open()"],
                            "Descriptive information about datasets and processing context.",
                        ),
                        leaf(
                            "Lineage",
                            [
                                "QGIS Processing History", "QGIS Processing Log",
                                "qgis_process", "QGIS Model Designer",
                            ],
                            "Provenance of how data and results were produced.",
                        ),
                        leaf(
                            "Precision",
                            [
                                "gdalinfo", "Simplify", "Generalize",
                                "gdal_translate", "Create grid", "gdaladdo",
                                "Snap geometries to grid",
                            ],
                            "How finely locations and values are represented (resolution and detail), not closeness to truth.",
                        ),
                        leaf(
                            "Validity",
                            [
                                "QGIS Geometry Checker Plugin", "Check Geometries",
                                "Fix Geometries", "ST_IsValid", "ST_IsValidDetail",
                            ],
                            "Geometric correctness and repair of invalid features.",
                        ),
                        leaf(
                            "Standards",
                            [
                                "GeoNetwork", "ISO 19115", "FGDC CSDGM", "pygeometa",
                            ],
                            "Metadata and content standards that make geospatial data discoverable and interoperable.",
                        ),
                        leaf(
                            "Uncertainty Modeling",
                            [
                                "Fuzzy Overlay", "Monte Carlo simulation",
                                "Random selection", "Random points in extent",
                            ],
                            "Representing and propagating error, vagueness, and stochastic variation.",
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
                                "Line intersections",
                                "Join attributes by nearest", "Extract by location",
                                "Distance Matrix", "Distance to nearest hub",
                            ],
                            "Operations on vector geometries and attributes.",
                        ),
                        leaf(
                            "Raster Analysis",
                            [
                                "Raster Calculator", "gdal_calc", "gdal_proximity",
                                "gdal_fillnodata", "gdal_polygonize", "gdalwarp", "gdal_translate",
                                "tobler.area_interpolate()",
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
                                "Shortest Path", "Service Area", "openrouteservice directions",
                            ],
                            "Path finding, catchment, and cost analysis on networks.",
                        ),
                    ],
                    "Core analytical families spanning vector, raster, network, and terrain.",
                ),
            ],
            "Foundational geospatial concepts, data models, CRS, quality, and analysis.",
            goal_verb="Understand",
            goal="Foundations: data models, CRS, relationships, quality ideas, and core analysis concepts.",
        ),
        group(
            "Analytical Capabilities",
            [
                leaf("Data Inspection", ["gdalinfo", "ogrinfo", "geopandas.read_file()", "geopandas.read_postgis()", "rasterio.open()", "PDAL pipeline"], "Inspect structure, extent, CRS, and content of geospatial datasets."),
                leaf(
                    "Data Acquisition",
                    [
                        "QField", "ODK Collect", "Georeferencer", "GPSBabel",
                        "OpenDroneMap", "iD Editor", "JOSM",
                    ],
                    "Capture, collect, and georeference new geospatial observations from field, GNSS, imagery, and VGI.",
                ),
                leaf("Data Conversion", ["ogr2ogr", "gdal_translate", "gdalwarp", "gdalbuildvrt", "geopandas.to_file()", "geopandas.to_parquet()", "geopandas.to_postgis()"], "Transform formats, encodings, and storage targets."),
                leaf("CRS Management", ["pyproj.CRS", "pyproj.Transformer", "projinfo", "ST_Transform", "geopandas.to_crs()", "geopandas.set_crs()", "Assign projection", "gdalwarp"], "Assign, inspect, and reproject coordinate reference systems."),
                leaf("Vector Processing", ["Buffer", "Clip", "Intersection", "Difference", "Union", "Dissolve", "Merge Vector Layers", "Multipart to Singleparts", "Split Vector Layer", "Join attributes by nearest", "Simplify"], "Geometry and attribute operations on vector layers."),
                leaf("Raster Processing", ["Raster Calculator", "gdal_calc", "gdal_translate", "gdalwarp", "gdal_proximity", "gdal_fillnodata", "gdal_polygonize", "gdal_contour", "gdalbuildvrt", "gdal_merge"], "Raster resampling, algebra, mosaics, and conversions."),
                leaf("Database Processing", ["ST_Buffer", "ST_Intersects", "ST_DWithin", "ST_Transform", "ST_IsValid", "geopandas.read_postgis()", "geopandas.to_postgis()", "DuckDB ST_Read"], "In-database geospatial read/write and processing."),
                leaf("Spatial SQL", ["ST_Intersects", "ST_Contains", "ST_Within", "ST_Buffer", "ST_DWithin", "ST_Intersection", "ST_Distance", "ST_Transform"], "Declarative spatial queries using SQL geometry functions."),
                leaf("Geocoding", ["openrouteservice geocoding", "Nominatim", "Google Geocoding API", "ArcGIS Geocoding Service"], "Convert between place names/addresses and coordinates."),
                leaf("Routing", ["Shortest Path", "pgr_dijkstra", "pgr_aStar", "pgr_KSP", "openrouteservice directions"], "Compute paths, costs, and travel directions on networks."),
                leaf("Accessibility", ["Service Area", "Distance Matrix", "openrouteservice isochrones", "openrouteservice matrices", "pgr_drivingDistance"], "Measure reachability by time, distance, or impedance."),
                leaf(
                    "Location-Allocation",
                    [
                        "v.net.alloc", "OD Matrix from Layers as Lines (m:n)",
                        "Distance Matrix", "ortools.routing", "Service Area",
                    ],
                    "Choose facility locations and assign demand to minimize travel cost or maximize coverage.",
                ),
                leaf(
                    "Remote Sensing",
                    [
                        "gdal_translate", "gdalwarp", "gdalbuildvrt", "gdal_calc",
                        "rasterio.mask.mask()", "OTB BandMath", "OTB ComputeImagesStatistics",
                        "OpenDroneMap", "Structure from Motion", "PDAL pipeline", "writers.gdal",
                        "OTB TrainImagesClassifier", "OTB KMeansClassification",
                        "Segment Anything Model (SAM)",
                        "OTB ComputeConfusionMatrix", "scikit-learn.metrics",
                        "Extract by location", "Random points in polygons",
                    ],
                    "Process Earth observation imagery from preparation through classification and accuracy checks.",
                ),
                leaf("Spatial Statistics", ["esda.Moran", "esda.Moran_Local", "esda.Geary", "esda.GetisOrd", "libpysal.weights", "Heatmap (Kernel Density Estimation)"], "Quantify spatial autocorrelation, hotspots, and density."),
                leaf(
                    "Spatial Regression",
                    [
                        "mgwr.GWR", "spreg.OLS", "spreg.ML_Lag", "spreg.ML_Error",
                        "libpysal.weights",
                    ],
                    "Model relationships while accounting for spatial dependence and local variation.",
                ),
                leaf(
                    "Point Pattern Analysis",
                    [
                        "pointpats.PointPattern", "pointpats.centrography",
                        "Heatmap (Kernel Density Estimation)", "DBSCAN clustering",
                        "Random points in extent",
                    ],
                    "Describe and test the arrangement of point events in space.",
                ),
                leaf(
                    "Multi-Criteria Evaluation",
                    [
                        "Weighted Overlay", "Fuzzy Overlay", "Reclassify by table",
                        "Raster Calculator", "gdal_calc",
                    ],
                    "Combine weighted criteria layers to rank or select suitable locations.",
                ),
                leaf(
                    "Spatial Interpolation",
                    [
                        "IDW Interpolation", "TIN Interpolation", "gdal_grid", "PyKrige",
                        "Multilevel B-Spline Interpolation", "Thin plate spline",
                    ],
                    "Predict values at unsampled locations.",
                ),
                leaf(
                    "Clustering",
                    [
                        "DBSCAN clustering", "K-means clustering",
                        "scikit-learn DBSCAN", "scikit-learn KMeans", "HDBSCAN",
                        "ST_ClusterDBSCAN", "ST_ClusterKMeans", "ST_ClusterWithin",
                    ],
                    "Group observations by spatial and/or attribute similarity.",
                ),
                leaf(
                    "Cartography",
                    [
                        "QGIS Style Manager", "QGIS Symbol Selector", "QGIS Label settings",
                        "QGIS Print Layout", "graduated renderer", "categorized renderer",
                        "gdaldem hillshade", "Contour", "gdal_contour", "QGIS 3D Map View",
                    ],
                    "Visual encoding and map design for communication.",
                ),
                leaf(
                    "Space-Time Analysis",
                    [
                        "MovingPandas", "QGIS Temporal Controller",
                        "GeoParquet", "gdalbuildvrt", "openrouteservice directions",
                    ],
                    "Analyze how locations, attributes, and movements change through time.",
                ),
                leaf(
                    "Trajectory Analysis",
                    [
                        "Shortest Path", "pgr_dijkstra", "pgr_aStar", "pgr_dijkstraVia",
                        "openrouteservice directions", "MovingPandas",
                    ],
                    "Analyze movement paths, route behavior, and network-constrained travel.",
                ),
                leaf(
                    "Geocomputation",
                    [
                        "mesa", "NetLogo", "Cellular Automata", "QGIS Model Designer",
                    ],
                    "Simulate spatial processes with agents, cellular models, and iterative rules.",
                ),
            ],
            "Software-independent operations bridging concepts and executable tools.",
            goal_verb="Act",
            goal="Operations: the software-independent steps used to process, analyse, and map spatial data.",
        ),
        group(
            "Workflow",
            [
                leaf(
                    "Site Selection",
                    [
                        "Buffer", "Clip", "Intersection", "Extract by location",
                        "Raster Calculator", "Weighted Overlay", "Dissolve",
                    ],
                    "Combine criteria to identify candidate locations.",
                ),
                leaf(
                    "Suitability Analysis",
                    [
                        "Raster Calculator", "gdal_calc", "Weighted Overlay",
                        "Fuzzy Overlay", "QGIS Model Designer", "Reclassify by table",
                    ],
                    "Score locations against multi-criteria suitability models.",
                ),
                leaf(
                    "Catchment Analysis",
                    [
                        "Service Area", "pgr_drivingDistance", "openrouteservice isochrones",
                    ],
                    "Delineate areas served by facilities or outlets.",
                ),
                leaf(
                    "Accessibility Analysis",
                    [
                        "Service Area", "Distance Matrix",
                        "openrouteservice matrices", "openrouteservice isochrones",
                        "pgr_drivingDistance",
                    ],
                    "Evaluate ease of reaching destinations.",
                ),
                leaf(
                    "Demographic Enrichment",
                    [
                        "geopandas.sjoin()", "geopandas.sjoin_nearest()",
                        "Join attributes by location", "Join attributes by nearest",
                        "Extract by location", "ST_Intersects", "ST_Contains", "ST_Within",
                    ],
                    "Attach population or socioeconomic attributes to features.",
                ),
                leaf(
                    "Hazard Assessment",
                    [
                        "gdaldem slope", "gdaldem aspect", "gdaldem hillshade",
                        "Raster Calculator", "gdal_proximity", "Buffer", "Intersection",
                    ],
                    "Map exposure and susceptibility to hazards.",
                ),
                leaf(
                    "Environmental Assessment",
                    [
                        "Buffer", "Clip", "Intersection", "Raster Calculator",
                        "gdal_proximity", "gdal_calc", "gdal_fillnodata",
                    ],
                    "Evaluate environmental conditions and impacts.",
                ),
                leaf(
                    "Infrastructure Planning",
                    [
                        "Shortest Path", "Service Area", "Distance Matrix",
                        "Buffer", "ST_DWithin", "pgr_dijkstra", "openrouteservice directions",
                    ],
                    "Support planning of networks and facilities.",
                ),
                leaf(
                    "Change Detection",
                    [
                        "gdalwarp", "gdal_translate", "gdal_calc", "Raster Calculator",
                        "OTB BandMath", "gdalbuildvrt",
                    ],
                    "Compare multi-temporal datasets to find change.",
                ),
                leaf(
                    "Hydrological Analysis",
                    [
                        "Fill sinks", "Flow direction", "Flow accumulation",
                        "Watershed", "Channel network", "Strahler order",
                    ],
                    "Model surface water flow and drainage.",
                ),
                leaf(
                    "Visibility Analysis",
                    [
                        "Viewshed", "gdal_viewshed",
                    ],
                    "Determine what can be seen from a viewpoint.",
                ),
                leaf(
                    "Remote Sensing Classification",
                    [
                        "OTB TrainImagesClassifier", "OTB KMeansClassification",
                        "OTB BandMath", "OTB ComputeImagesStatistics",
                        "gdal_calc", "Segment Anything Model (SAM)",
                    ],
                    "Assign classes to pixels or objects from imagery.",
                ),
                leaf(
                    "Urban Growth Analysis",
                    [
                        "Raster Calculator", "gdal_calc", "OTB BandMath",
                        "Heatmap (Kernel Density Estimation)", "DBSCAN clustering",
                        "gdalwarp", "gdalbuildvrt", "Intersection",
                    ],
                    "Track and interpret urban expansion patterns.",
                ),
            ],
            "Reusable analytical workflows that combine capabilities for real tasks.",
            goal_verb="Apply",
            goal="Workflows: repeatable chains of operations for common real-world geospatial tasks.",
        ),
        group(
            "Validation",
            [
                leaf("Geometry Validation", ["Check Geometries", "Fix Geometries", "QGIS Geometry Checker", "ST_IsValid", "ST_IsValidDetail", "geometry.is_valid (Shapely)"], "Detect and repair invalid geometries."),
                leaf("CRS Validation", ["pyproj.CRS", "pyproj.Transformer", "pyproj.Transformer(always_xy=True)", "projinfo", "ST_Transform", "geopandas.to_crs()", "geopandas.set_crs()", "gdalwarp", "gdalinfo", "ogrinfo", "Reproject Layer", "Assign projection"], "Confirm CRS assignment and correct transformations."),
                leaf("Metadata Validation", ["gdalinfo", "ogrinfo", "rio info", "geopandas.read_file()"], "Check completeness and consistency of metadata."),
                leaf("Schema Validation", ["ogrinfo", "geopandas.read_file()", "geopandas.read_postgis()", "Refactor Fields"], "Validate fields, types, and structural integrity."),
                leaf("Topology Validation", ["ST_Touches", "ST_Overlaps", "ST_Crosses", "Extract by location", "Delete Duplicate Geometries", "Check Geometries"], "Ensure topological rules and consistency between features."),
                leaf("Statistical Validation", ["esda.Moran", "esda.Moran_Local", "esda.Geary", "esda.GetisOrd", "libpysal.weights"], "Validate spatial patterns with inferential diagnostics."),
                leaf(
                    "Accuracy Assessment",
                    [
                        "OTB ComputeConfusionMatrix", "scikit-learn.metrics",
                        "Extract by location", "Random points in polygons",
                    ],
                    "Validate classified or predicted outputs against reference samples.",
                ),
                leaf("Result Validation", ["QGIS Processing History", "QGIS Processing Log", "qgis_process", "Basic Statistics for Fields", "Field Statistics"], "Audit analytical outputs and processing trails."),
            ],
            "Quality, correctness, and reproducibility checks for data and outputs.",
            goal_verb="Ensure",
            goal="Quality: checks that data, CRS, geometry, and results are valid and trustworthy.",
        ),
        group(
            "Output",
            [
                leaf("Tables", ["geopandas.to_file()", "geopandas.to_parquet()", "geopandas.to_postgis()", "ogr2ogr", "Basic Statistics for Fields", "Field Statistics"], "Tabular exports of attributes and summaries."),
                leaf("GIS Files", ["ogr2ogr", "gdal_translate", "gdalwarp", "gdalbuildvrt", "gdal_merge", "gdal_retile", "geopandas.to_file()", "geopandas.to_parquet()"], "Interoperable geospatial file deliverables."),
                leaf("Reports", ["QGIS Reports", "QGIS Print Layout"], "Narrative and figure-based analysis reports."),
                leaf("Story Maps", ["ArcGIS StoryMaps", "QGIS Print Layout", "MapLibre GL JS"], "Narrative spatial storytelling that combines maps, text, and media."),
                leaf("Dashboards", ["QGIS Server", "MapLibre GL JS", "Leaflet", "OpenLayers", "GeoServer"], "Interactive operational views of spatial results."),
                leaf(
                    "APIs",
                    [
                        "QGIS Server", "GeoServer", "PostGIS", "DuckDB Spatial",
                        "openrouteservice", "OSRM", "Nominatim",
                        "Google Geocoding API", "ArcGIS Geocoding Service",
                    ],
                    "Programmatic access to spatial data and services.",
                ),
            ],
            "Deliverables and channels for data, APIs, reports, and sharing.",
            goal_verb="Deliver",
            goal="Outputs: tables, files, maps, reports, APIs, and other products for sharing and decisions.",
        ),
        group(
            "Provider Registry",
            [
                leaf(
                    "Geospatial Libraries",
                    [
                        "GDAL / OGR", "GeoPandas", "Shapely", "Rasterio", "Fiona", "PyProj",
                        "PDAL", "PySAL", "OTB (Orfeo ToolBox)", "DuckDB Spatial", "PostGIS",
                        "Apache Sedona", "OSRM", "pgRouting", "openrouteservice", "Valhalla",
                        "segment-geospatial (samgeo)",
                    ],
                    "Core libraries and engines used to implement geospatial operations.",
                ),
                leaf(
                    "Cloud",
                    [
                        "Apache Sedona", "GeoParquet", "Cloud Optimized GeoTIFF (COG)", "AWS",
                        "Google Earth Engine", "ArcGIS Online",
                    ],
                    "Scalable cloud platforms, formats, and compute for large spatial data.",
                ),
                leaf(
                    "SDI / Catalogs",
                    [
                        "GeoNetwork", "CKAN", "STAC", "pystac", "Microsoft Planetary Computer",
                    ],
                    "Catalogs and spatial data infrastructures for discovery and access.",
                ),
                leaf(
                    "Notebooks",
                    [
                        "Jupyter Notebook", "Google Colab", "ArcGIS Notebooks",
                    ],
                    "Literate computing environments for reproducible geospatial analysis.",
                ),
                leaf(
                    "Development",
                    [
                        "Python for GIS", "R for GIS", "JavaScript for GIS",
                        "QGIS Model Designer", "qgis_process",
                    ],
                    "Languages and tooling used to build geospatial scripts and applications.",
                ),
                leaf("Basemap", ["OpenStreetMap", "Google Maps", "Overture Maps", "Natural Earth", "Microsoft Planetary Computer", "Government Open Data APIs"], "Reference basemaps and open geospatial data sources."),
                leaf("Web Mapping", ["MapLibre GL JS", "OpenLayers", "Leaflet", "GeoServer", "QGIS Server"], "Clients and servers for interactive web maps."),
                leaf(
                    "AI",
                    [
                        "scikit-learn", "XGBoost", "LightGBM", "Keras",
                        "PyTorch", "TensorFlow", "TorchGeo", "Raster Vision",
                        "Hugging Face Transformers", "Ultralytics YOLO",
                        "Segment Anything Model (SAM)",
                    ],
                    "ML frameworks and model tools applied to geospatial tasks.",
                ),
            ],
            "Software ecosystems, libraries, and infrastructure behind the tools.",
            goal_verb="Enable",
            goal="Providers: libraries, platforms, catalogues, and data sources that power the analysis stack.",
        ),
    ],
}


INDEX_HTML = '<!DOCTYPE html>\n<html lang="en">\n<head>\n  <meta charset="UTF-8" />\n  <meta name="viewport" content="width=device-width, initial-scale=1.0" />\n  <title>Geospatial Knowledge to Tool: Knowledge Visualization and Search</title>\n  <script src="https://cdn.tailwindcss.com"></script>\n  <script src="https://cdn.jsdelivr.net/npm/d3@7.9.0/dist/d3.min.js"></script>\n  <style>\n    :root {\n      --ink: #1c2430;\n      --muted: #5b6775;\n      --line: #d7dde5;\n      --wash: #f3f6f9;\n      --accent: #1f4e79;\n    }\n    body {\n      margin: 0;\n      color: var(--ink);\n      background:\n        radial-gradient(circle at 12% 8%, #e8eef5 0%, transparent 42%),\n        radial-gradient(circle at 88% 0%, #edf3ea 0%, transparent 36%),\n        var(--wash);\n      font-family: Georgia, "Iowan Old Style", "Palatino Linotype", Palatino, serif;\n    }\n    .ui-sans { font-family: "Avenir Next", "Segoe UI", "Helvetica Neue", Helvetica, Arial, sans-serif; }\n    #viz-wrap {\n      position: relative;\n      margin-top: 0.35rem;\n      height: min(78vh, calc(100vh - 7rem));\n      min-height: 520px;\n      overflow: hidden;\n      touch-action: none;\n      cursor: grab;\n      background: linear-gradient(180deg, #f7fafc 0%, #eef3f8 100%);\n    }\n    #viz-wrap.is-panning { cursor: grabbing; }\n    #pack-svg { width: 100%; height: 100%; display: block; }\n    .pack-label {\n      pointer-events: none;\n      text-anchor: middle;\n      dominant-baseline: middle;\n      fill: #1c2430;\n      font-family: "Avenir Next", "Segoe UI", Helvetica, Arial, sans-serif;\n      font-weight: 650;\n      paint-order: stroke;\n      stroke: rgba(255,255,255,0.82);\n      stroke-width: 2px;\n    }\n    .pack-circle { cursor: pointer; }\n    .pack-circle:hover { stroke-width: 2.6px !important; }\n    .crumb-btn:hover { color: var(--accent); }\n    .tool-card {\n      border: 1px solid var(--line);\n      background: #fff;\n      border-radius: 14px;\n      padding: 0.95rem 1.05rem;\n    }\n    .cite-section {\n      border-top: 1px solid var(--line);\n      background: rgba(255,255,255,0.72);\n    }\n    .cite-section h2 {\n      font-size: 1.05rem;\n      font-weight: 650;\n      letter-spacing: -0.01em;\n      color: var(--ink);\n      margin: 0;\n    }\n    .cite-section .cite-lead {\n      margin: 0.55rem 0 1rem;\n      color: var(--muted);\n      font-size: 0.92rem;\n      line-height: 1.55;\n      max-width: none;\n      width: 100%;\n    }\n    .cite-list {\n      margin: 0;\n      padding: 0;\n      list-style: none;\n      display: grid;\n      gap: 0.7rem;\n    }\n    .cite-list li {\n      font-size: 0.88rem;\n      line-height: 1.55;\n      color: #334155;\n      padding-left: 1.1rem;\n      position: relative;\n    }\n    .cite-list li::before {\n      content: "•";\n      position: absolute;\n      left: 0;\n      color: #7b8794;\n    }\n    .cite-list a, .cite-lead a {\n      color: var(--accent);\n      text-decoration: underline;\n      text-underline-offset: 2px;\n    }\n    .cite-list a:hover { color: #163a5c; }\n    .tool-relation {\n      margin: 0.45rem 0 0;\n      color: #1f4e79;\n      font-size: 0.9rem;\n      line-height: 1.55;\n      font-weight: 500;\n    }\n    .tool-blurb {\n      margin-top: 0.55rem;\n      font-size: 0.9rem;\n      line-height: 1.55;\n      color: #3a4553;\n    }\n    .child-link { color: #1f4e79; }\n    .child-link:hover { text-decoration: underline; }\n    .goal-banner {\n      margin-top: 1rem;\n      border: 1px solid rgba(28, 36, 48, 0.12);\n      border-radius: 16px;\n      padding: 0.95rem 1.05rem;\n    }\n    .goal-verb {\n      display: inline-block;\n      font-size: 0.7rem;\n      font-weight: 700;\n      letter-spacing: 0.14em;\n      text-transform: uppercase;\n      color: #1c2430;\n      background: rgba(255,255,255,0.72);\n      border-radius: 999px;\n      padding: 0.2rem 0.55rem;\n    }\n    .goal-grid {\n      display: grid;\n      gap: 0.65rem;\n      margin-top: 0.85rem;\n    }\n    .goal-item {\n      border: 1px solid rgba(28, 36, 48, 0.12);\n      border-radius: 12px;\n      padding: 0.7rem 0.85rem;\n      cursor: pointer;\n      text-align: left;\n      width: 100%;\n      transition: filter 0.15s ease, transform 0.15s ease;\n    }\n    .goal-item:hover { filter: brightness(0.97); transform: translateY(-1px); }\n    .pack-circle.is-dim { opacity: 0.14; }\n    .pack-circle.is-match { stroke-width: 2.8px !important; stroke: #1f4e79 !important; }\n    .pack-label.is-dim { opacity: 0.2; }\n    #viz-search::-webkit-search-cancel-button { cursor: pointer; }\n        .hint-pill {\n      position: absolute;\n      right: 1rem;\n      bottom: 1rem;\n      z-index: 5;\n      background: rgba(255,255,255,0.92);\n      border: 1px solid #d7dde5;\n      border-radius: 999px;\n      padding: 0.4rem 0.8rem;\n      font-size: 12px;\n      color: #5b6775;\n      pointer-events: none;\n    }\n  </style>\n</head>\n<body>\n  <div class="min-h-screen">\n    <header class="ui-sans border-b border-slate-200/80 bg-white/85 backdrop-blur px-4 py-4 sm:px-6 lg:px-8">\n      <div class="mx-auto flex max-w-[1400px] flex-col gap-2 sm:flex-row sm:items-end sm:justify-between">\n        <div>\n          <h1 class="text-2xl font-semibold tracking-tight text-slate-900 sm:text-3xl">\n            Geospatial Knowledge to Tool: Knowledge Visualization and Search\n          </h1>\n        </div>\n        <div class="ui-sans flex shrink-0 items-center justify-end gap-3 sm:gap-4">\n          <img src="mapai.svg" alt="MapAI" class="h-10 w-auto max-h-11 max-w-[160px] object-contain object-right sm:h-11" />\n          <img src="cfrc.jpg" alt="CFRC" class="h-10 w-auto max-h-11 max-w-[120px] rounded-sm object-contain object-left sm:h-11" />\n        </div>\n      </div>\n    </header>\n\n    <main class="mx-auto grid max-w-[1400px] gap-0 lg:grid-cols-[minmax(0,1.2fr)_minmax(340px,0.8fr)]">\n      <section class="border-b border-slate-200 lg:border-b-0 lg:border-r">\n        <div class="ui-sans relative z-10 mb-3 flex flex-nowrap items-center gap-2 px-4 pt-4 pb-1">\n          <div class="flex min-w-0 flex-wrap items-center gap-2 rounded-full bg-white/95 px-3 py-1.5 text-sm text-slate-600 shadow-sm ring-1 ring-slate-200">\n            <button id="btn-back" class="crumb-btn font-medium text-slate-800 disabled:text-slate-400" disabled>Back</button>\n            <button id="btn-reset" class="crumb-btn text-slate-500">Reset</button>\n            <span class="text-slate-300">/</span>\n            <div id="breadcrumb" class="flex flex-wrap items-center gap-1"></div>\n          </div>\n          <div class="ml-auto flex min-w-[200px] max-w-md flex-1 items-center gap-2 rounded-full bg-white/95 px-3 py-1.5 text-sm shadow-sm ring-1 ring-slate-200">\n            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" aria-hidden="true" class="shrink-0 text-slate-400">\n              <circle cx="11" cy="11" r="6.5" stroke="currentColor" stroke-width="1.8"></circle>\n              <path d="M16.5 16.5L21 21" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"></path>\n            </svg>\n            <input id="viz-search" type="search" autocomplete="off" spellcheck="false"\n              placeholder="Search concepts &amp; tools…"\n              class="w-full bg-transparent text-slate-800 placeholder:text-slate-400 outline-none" />\n            <span id="search-meta" class="shrink-0 text-[11px] text-slate-400"></span>\n          </div>\n        </div>\n        <div id="viz-wrap">\n          <svg id="pack-svg" role="img" aria-label="Geo-KTF circle packing visualization"></svg>\n        </div>\n      </section>\n\n      <aside class="ui-sans bg-white/75 px-5 py-6 sm:px-7 lg:max-h-[calc(100vh-6.5rem)] lg:overflow-y-auto">\n        <div id="detail"></div>\n      </aside>\n    </main>\n\n    <footer class="ui-sans">\n      <div class="cite-section">\n        <div class="mx-auto max-w-[1400px] px-4 py-8 sm:px-6 lg:px-8">\n          <h2>Contact us</h2>\n          <p class="cite-lead">\n            We welcome potential collaboration on AI, geospatial, and city-related research and projects.\n            Please contact us at <a href="mailto:xxx@unsw.edu.au">xxx@unsw.edu.au</a>.\n            Suggestions regarding our framework are more than welcome.\n          </p>\n        </div>\n      </div>\n      <div class="cite-section" style="border-top:none;padding-top:0">\n      <div class="mx-auto max-w-[1400px] px-4 pb-8 sm:px-6 lg:px-8">\n        <h2>References</h2>\n        <p class="cite-lead">\n          Geo-KTF maps geospatial concepts to representative tools. Tool descriptions and capabilities\n          are informed by the official documentation and project materials of the software ecosystems below.\n          Please cite the original projects when using these tools in research or production work.\n        </p>\n        <ul class="cite-list">\n          <li><strong>QGIS</strong> — QGIS.org. <em>QGIS Geographic Information System</em>. Open Source Geospatial Foundation. Documentation: <a href="https://docs.qgis.org/" target="_blank" rel="noopener noreferrer">https://docs.qgis.org/</a></li>\n          <li><strong>GDAL/OGR</strong> — GDAL/OGR contributors. <em>GDAL — Geospatial Data Abstraction Library</em>. OSGeo. Documentation: <a href="https://gdal.org/" target="_blank" rel="noopener noreferrer">https://gdal.org/</a></li>\n          <li><strong>PROJ</strong> — PROJ contributors. <em>PROJ coordinate transformation software library</em>. OSGeo. Documentation: <a href="https://proj.org/" target="_blank" rel="noopener noreferrer">https://proj.org/</a></li>\n          <li><strong>PostGIS</strong> — PostGIS Project Steering Committee. <em>PostGIS — Spatial and Geographic Objects for PostgreSQL</em>. OSGeo. Documentation: <a href="https://postgis.net/documentation/" target="_blank" rel="noopener noreferrer">https://postgis.net/documentation/</a></li>\n          <li><strong>pgRouting</strong> — pgRouting Community. <em>pgRouting — Routing on PostgreSQL/PostGIS</em>. Documentation: <a href="https://docs.pgrouting.org/" target="_blank" rel="noopener noreferrer">https://docs.pgrouting.org/</a></li>\n          <li><strong>GeoPandas</strong> — GeoPandas developers. <em>GeoPandas</em>. Documentation: <a href="https://geopandas.org/" target="_blank" rel="noopener noreferrer">https://geopandas.org/</a></li>\n          <li><strong>Shapely</strong> — Shapely developers. <em>Shapely: manipulation and analysis of geometric objects</em>. Documentation: <a href="https://shapely.readthedocs.io/" target="_blank" rel="noopener noreferrer">https://shapely.readthedocs.io/</a></li>\n          <li><strong>Rasterio</strong> — Mapbox / Rasterio contributors. <em>Rasterio: access to geospatial raster data</em>. Documentation: <a href="https://rasterio.readthedocs.io/" target="_blank" rel="noopener noreferrer">https://rasterio.readthedocs.io/</a></li>\n          <li><strong>PDAL</strong> — PDAL contributors. <em>Point Data Abstraction Library</em>. Documentation: <a href="https://pdal.io/" target="_blank" rel="noopener noreferrer">https://pdal.io/</a></li>\n          <li><strong>PySAL</strong> — Rey, S. J., et al. <em>Python Spatial Analysis Library (PySAL)</em>. Documentation: <a href="https://pysal.org/" target="_blank" rel="noopener noreferrer">https://pysal.org/</a></li>\n          <li><strong>Orfeo ToolBox (OTB)</strong> — CNES / OTB community. <em>Orfeo ToolBox</em>. Documentation: <a href="https://www.orfeo-toolbox.org/" target="_blank" rel="noopener noreferrer">https://www.orfeo-toolbox.org/</a></li>\n          <li><strong>openrouteservice</strong> — HeiGIT / openrouteservice. <em>openrouteservice API</em>. Documentation: <a href="https://openrouteservice.org/" target="_blank" rel="noopener noreferrer">https://openrouteservice.org/</a></li>\n          <li><strong>OSRM</strong> — Project OSRM. <em>Open Source Routing Machine</em>. Documentation: <a href="https://project-osrm.org/" target="_blank" rel="noopener noreferrer">https://project-osrm.org/</a></li>\n          <li><strong>Valhalla</strong> — Valhalla contributors. <em>Valhalla Open Source Routing Engine</em>. Documentation: <a href="https://valhalla.github.io/valhalla/" target="_blank" rel="noopener noreferrer">https://valhalla.github.io/valhalla/</a></li>\n          <li><strong>MapLibre GL JS</strong> — MapLibre contributors. <em>MapLibre GL JS</em>. Documentation: <a href="https://maplibre.org/" target="_blank" rel="noopener noreferrer">https://maplibre.org/</a></li>\n          <li><strong>Leaflet</strong> — Agafonkin, V., et al. <em>Leaflet — an open-source JavaScript library for interactive maps</em>. Documentation: <a href="https://leafletjs.com/" target="_blank" rel="noopener noreferrer">https://leafletjs.com/</a></li>\n          <li><strong>OpenLayers</strong> — OpenLayers contributors / OSGeo. <em>OpenLayers</em>. Documentation: <a href="https://openlayers.org/" target="_blank" rel="noopener noreferrer">https://openlayers.org/</a></li>\n          <li><strong>GeoServer</strong> — GeoServer contributors / OSGeo. <em>GeoServer</em>. Documentation: <a href="https://docs.geoserver.org/" target="_blank" rel="noopener noreferrer">https://docs.geoserver.org/</a></li>\n          <li><strong>Apache Sedona</strong> — Apache Sedona. <em>Sedona: a cluster computing system for processing large-scale spatial data</em>. Documentation: <a href="https://sedona.apache.org/" target="_blank" rel="noopener noreferrer">https://sedona.apache.org/</a></li>\n          <li><strong>DuckDB Spatial</strong> — DuckDB Labs / DuckDB Spatial extension authors. <em>DuckDB Spatial</em>. Documentation: <a href="https://duckdb.org/docs/extensions/spatial.html" target="_blank" rel="noopener noreferrer">https://duckdb.org/docs/extensions/spatial.html</a></li>\n          <li><strong>scikit-learn</strong> — Pedregosa, F., et al. <em>Scikit-learn: Machine Learning in Python</em>. Documentation: <a href="https://scikit-learn.org/" target="_blank" rel="noopener noreferrer">https://scikit-learn.org/</a></li>\n          <li><strong>OpenStreetMap</strong> — OpenStreetMap contributors. <em>OpenStreetMap</em>. <a href="https://www.openstreetmap.org/copyright" target="_blank" rel="noopener noreferrer">https://www.openstreetmap.org/copyright</a></li>\n          <li><strong>UCGIS Body of Knowledge</strong> — University Consortium for Geographic Information Science. <em>GIS&amp;T Body of Knowledge</em> (visual inspiration for the circle-packing knowledge explorer). <a href="https://gistbok.ucgis.org/" target="_blank" rel="noopener noreferrer">https://gistbok.ucgis.org/</a></li>\n        </ul>\n      </div>\n      </div>\n    </footer>\n  </div>\n\n  <script id="geo-ktf-data" type="application/json">__DATA__</script>\n  <script id="tool-info" type="application/json">__TOOLS__</script>\n  <script>\n    const raw = JSON.parse(document.getElementById("geo-ktf-data").textContent);\n    const TOOL_INFO = JSON.parse(document.getElementById("tool-info").textContent);\n\n    const COLORS = ["#9ec5e8","#f2d28b","#b9d7a5","#f0b7a4","#cbb6e4","#9fd3d0"];\n\n    function countTools(node) {\n      if (node.tools) return node.tools.length;\n      return (node.children || []).reduce((s, c) => s + countTools(c), 0);\n    }\n    function countLeaves(node) {\n      if (node.tools) return 1;\n      return (node.children || []).reduce((s, c) => s + countLeaves(c), 0);\n    }\n    function flattenLeaves(node) {\n      if (node.tools) return [node];\n      return (node.children || []).flatMap(flattenLeaves);\n    }\n\n    const leaves = flattenLeaves(raw);\n    const totalTools = new Set(leaves.flatMap((l) => l.tools)).size;\nconst wrap = document.getElementById("viz-wrap");\n    const svg = d3.select("#pack-svg");\n    const g = svg.append("g");\n\n    let width = 800, height = 800;\n    function resize() {\n      const rect = wrap.getBoundingClientRect();\n      width = Math.max(480, rect.width);\n      height = Math.max(480, rect.height);\n      svg.attr("viewBox", `0 0 ${width} ${height}`);\n    }\n    resize();\n\n    const hierarchy = d3.hierarchy(raw)\n      .sum((d) => (d.tools ? Math.max(d.tools.length, 3) : 0))\n      .sort((a, b) => (b.value || 0) - (a.value || 0));\n\n    const root = d3.pack().size([width, height]).padding((d) => (d.depth < 2 ? 8 : 4))(hierarchy);\n    let focus = root;\n    let selected = root;\n\n    root.eachBefore((d) => {\n      if (d.depth === 0) d.color = "#e8eef4";\n      else if (d.depth === 1) d.color = COLORS[d.parent.children.indexOf(d) % COLORS.length];\n      else d.color = d3.color(d.parent.color).brighter(0.28 + d.depth * 0.05).formatHex();\n    });\n\n    const node = g.selectAll("circle")\n      .data(root.descendants().slice(1))\n      .join("circle")\n      .attr("class", "pack-circle")\n      .attr("cx", (d) => d.x)\n      .attr("cy", (d) => d.y)\n      .attr("r", (d) => d.r)\n      .attr("fill", (d) => (d.children ? d.color : "#ffffff"))\n      .attr("fill-opacity", (d) => (d.children ? 0.9 : 0.98))\n      .attr("stroke", (d) => (d.children ? d3.color(d.color).darker(0.4) : "#8e9bab"))\n      .attr("stroke-width", 1.2)\n      .each(function(d) {\n        d3.select(this).selectAll("title").data([d.data.name]).join("title").text((t) => t);\n      });\n\n    const label = g.selectAll("text")\n      .data(root.descendants().slice(1))\n      .join("text")\n      .attr("class", "pack-label")\n      .attr("x", (d) => d.x)\n      .attr("y", (d) => d.y)\n      .style("display", "none");\n\n    // Free mouse zoom + pan\n    const zoomBehavior = d3.zoom()\n      .scaleExtent([0.35, 48])\n      .clickDistance(8)\n      .filter((event) => {\n        if (event.type === "wheel") return true;\n        // ignore right/middle buttons\n        return !event.ctrlKey && !event.button;\n      })\n      .on("start", (event) => {\n        if (event.sourceEvent && event.sourceEvent.type !== "wheel") {\n          wrap.classList.add("is-panning");\n        }\n      })\n      .on("end", () => wrap.classList.remove("is-panning"))\n      .on("zoom", (event) => {\n        g.attr("transform", event.transform);\n        updateLabels(event.transform.k);\n      });\n\n    svg.call(zoomBehavior);\n    wrap.addEventListener("wheel", (e) => e.preventDefault(), { passive: false });\n\n    // Click-to-open with drag threshold (works with d3.zoom)\n    let pointerDown = null;\n    node\n      .style("pointer-events", "all")\n      .on("pointerdown", (event, d) => {\n        pointerDown = { x: event.clientX, y: event.clientY, id: d };\n      })\n      .on("click", (event, d) => {\n        // Ignore click if this was a pan gesture\n        if (pointerDown && pointerDown.id === d) {\n          const moved = Math.hypot(event.clientX - pointerDown.x, event.clientY - pointerDown.y);\n          pointerDown = null;\n          if (moved > 8) return;\n        }\n        event.stopPropagation();\n        openNode(d);\n      });\n\n    svg.on("dblclick.zoom", null); // disable default d3 double-click zoom reset\n    svg.on("dblclick", (event) => {\n      event.preventDefault();\n      if (focus.parent) openNode(focus.parent, true);\n      else resetView();\n    });\n\n    document.getElementById("btn-back").addEventListener("click", () => {\n      if (focus.parent) openNode(focus.parent, true);\n    });\n    document.getElementById("btn-reset").addEventListener("click", () => resetView());\n\n    const searchInput = document.getElementById("viz-search");\n    const searchMeta = document.getElementById("search-meta");\n    let searchQuery = "";\n\n    function nodeDirectMatch(d, q) {\n      if (!q) return false;\n      if ((d.data.name || "").toLowerCase().includes(q)) return true;\n      return (d.data.tools || []).some((t) => String(t).toLowerCase().includes(q));\n    }\n\n    function lowestCommonAncestor(nodes) {\n      if (!nodes.length) return root;\n      let a = nodes[0];\n      for (let i = 1; i < nodes.length; i++) {\n        const path = new Set(nodes[i].ancestors());\n        while (a && !path.has(a)) a = a.parent;\n      }\n      return a || root;\n    }\n\n    function clearSearchVisual() {\n      node.classed("is-dim", false).classed("is-match", false);\n      label.classed("is-dim", false);\n      searchMeta.textContent = "";\n    }\n\n    function applySearch(rawQ, animate = true) {\n      const q = String(rawQ || "").trim().toLowerCase();\n      searchQuery = q;\n      if (!q) {\n        clearSearchVisual();\n        return;\n      }\n      const matches = root.descendants().filter((d) => d.depth > 0 && nodeDirectMatch(d, q));\n      const keep = new Set();\n      matches.forEach((d) => d.ancestors().forEach((a) => keep.add(a)));\n      node.classed("is-dim", (d) => !keep.has(d))\n          .classed("is-match", (d) => matches.includes(d));\n      label.classed("is-dim", (d) => !keep.has(d));\n      searchMeta.textContent = matches.length ? `${matches.length} hit${matches.length === 1 ? "" : "s"}` : "0 hits";\n\n      if (!matches.length) return;\n\n      // Prefer exact name, then concept (leaf) matches, then any\n      const preferred =\n        matches.find((d) => (d.data.name || "").toLowerCase() === q) ||\n        matches.find((d) => (d.data.name || "").toLowerCase().startsWith(q)) ||\n        matches.find((d) => !d.children && (d.data.name || "").toLowerCase().includes(q)) ||\n        matches.find((d) => !d.children) ||\n        matches[0];\n\n      selected = preferred;\n      renderDetail(preferred);\n      renderBreadcrumb(preferred);\n\n      const focusTarget = preferred.children ? preferred : (preferred.parent || preferred);\n      // If many scattered matches, zoom to LCA so the pack "moves" with the query\n      const target = matches.length === 1 ? focusTarget : lowestCommonAncestor(matches);\n      fitTo(target.depth === 0 && preferred.parent ? preferred.parent : target, animate);\n      updateLabels(d3.zoomTransform(svg.node()).k || 1);\n    }\n\n    let searchTimer = null;\n    searchInput.addEventListener("input", () => {\n      clearTimeout(searchTimer);\n      searchTimer = setTimeout(() => applySearch(searchInput.value, true), 90);\n    });\n    searchInput.addEventListener("keydown", (e) => {\n      if (e.key === "Escape") {\n        searchInput.value = "";\n        applySearch("", false);\n        resetView();\n      }\n    });\n\n    function fitTo(d, animate = true) {\n      focus = d;\n      const pad = 1.12;\n      const k = Math.min(width, height) / (d.r * 2 * pad);\n      const x = width / 2 - d.x * k;\n      const y = height / 2 - d.y * k;\n      const transform = d3.zoomIdentity.translate(x, y).scale(k);\n      const t = svg.transition().duration(animate ? 500 : 0);\n      t.call(zoomBehavior.transform, transform)\n        .on("end", () => updateLabels(d3.zoomTransform(svg.node()).k));\n      // also update immediately for duration 0 / first frame\n      updateLabels(k);\n      document.getElementById("btn-back").disabled = !focus.parent;\n    }\n\n    function openNode(d, forceFit = false) {\n      selected = d;\n      renderDetail(d);\n      renderBreadcrumb(d);\n      if (d.children) fitTo(d, true);\n      else if (forceFit && d.parent) fitTo(d.parent, true);\n      else if (!d.children && d.parent && focus !== d.parent) fitTo(d.parent, true);\n      // highlight selected\n      node.attr("stroke-width", (n) => (n === d ? 2.8 : 1.2))\n          .attr("stroke", (n) => (n === d ? "#1f4e79" : (n.children ? d3.color(n.color).darker(0.4) : "#8e9bab")));\n    }\n\n    function resetView() {\n      if (searchInput && searchInput.value) {\n        searchInput.value = "";\n        clearSearchVisual();\n        searchQuery = "";\n      }\n      openNode(root, true);\n      fitTo(root, true);\n    }\n\n    function wrapLabel(text, radiusPx) {\n      // Always prefer full readable names; wrap long phrases onto multiple lines.\n      const maxChars = Math.max(5, Math.floor(radiusPx / 11));\n      if (text.length <= maxChars) return [text];\n      const words = text.split(/\\s+/);\n      if (words.length === 1) return [text]; // never truncate single words like "Scale"\n      const lines = [];\n      let line = "";\n      for (const w of words) {\n        const next = line ? line + " " + w : w;\n        if (next.length > maxChars && line) {\n          lines.push(line);\n          line = w;\n        } else line = next;\n      }\n      if (line) lines.push(line);\n      return lines.slice(0, 4);\n    }\n\n    function updateLabels(k) {\n      const scale = k || 1;\n      label.each(function (d) {\n        const el = d3.select(this);\n        const isChildOfFocus = d.parent === focus;\n        const isSelectedLeaf = d === selected && !d.children;\n        const visible = isChildOfFocus || isSelectedLeaf;\n        if (!visible) {\n          el.style("display", "none");\n          return;\n        }\n        const rPx = d.r * scale;\n        if (rPx < 28) {\n          el.style("display", "none");\n          return;\n        }\n        const lines = wrapLabel(d.data.name, rPx).slice(0, 2);\n        const font = Math.max(7, Math.min(9.5, rPx / 11));\n        el.style("display", "block")\n          .style("font-size", font + "px")\n          .attr("x", d.x)\n          .attr("y", d.y)\n          .selectAll("tspan").remove();\n        el.selectAll("tspan")\n          .data(lines)\n          .join("tspan")\n          .attr("x", d.x)\n          .attr("dy", (_, i) => (i === 0 ? `${-((lines.length - 1) * 0.55)}em` : "1.15em"))\n          .text((t) => t);\n      });\n    }\n\n    function pathOf(d) {\n      return d.ancestors().reverse().map((n) => n.data.name);\n    }\n\n    function toolMeta(name) {\n      return TOOL_INFO[name] || {\n        source: "Geo-KTF registry",\n        blurb: "Representative geospatial tool or operation linked to this concept.",\n        relations: {},\n      };\n    }\n\n    function renderBreadcrumb(d) {\n      const parts = d.ancestors().reverse();\n      const el = document.getElementById("breadcrumb");\n      el.innerHTML = parts.map((n, i) => {\n        const name = n.data.name;\n        const short = name.length > 30 ? name.slice(0, 29) + "…" : name;\n        return `<button class="crumb-btn ${i === parts.length - 1 ? "font-semibold text-slate-900" : "text-slate-500"}">${escapeHtml(short)}</button>`;\n      }).join(\'<span class="text-slate-300 mx-0.5">/</span>\');\n      el.querySelectorAll("button").forEach((btn, i) => {\n        btn.addEventListener("click", () => openNode(parts[i], true));\n      });\n    }\n\n    function renderDetail(d) {\n      const data = d.data;\n      const tools = data.tools || [];\n      const children = d.children || [];\n      const path = pathOf(d).join(" › ");\n      let goalHtml = "";\n      if (data.goal_verb && data.goal) {\n        const sectionColor = d.color || COLORS[Math.max(0, d.depth === 1 ? d.parent.children.indexOf(d) : 0)] || "#e8eef4";\n        goalHtml = `\n          <div class="goal-banner" style="background:${sectionColor}">\n            <div class="goal-verb">${escapeHtml(data.goal_verb)}</div>\n            <p class="mt-2 text-[0.98rem] leading-6 text-slate-800">${escapeHtml(data.goal)}</p>\n          </div>`;\n      } else if (d.depth === 0) {\n        const pillars = (d.children || []).filter((c) => c.data.goal_verb);\n        if (pillars.length) {\n          goalHtml = `\n            <div class="mt-5">\n              <h3 class="text-xs font-semibold uppercase tracking-[0.14em] text-slate-500">Framework goals</h3>\n              <div class="goal-grid">\n                ${pillars.map((c, i) => `\n                  <button class="goal-item" data-child="${escapeHtml(c.data.name)}" style="background:${c.color || COLORS[i % COLORS.length]}">\n                    <div class="goal-verb">${escapeHtml(c.data.goal_verb)}</div>\n                    <div class="mt-1.5 text-sm font-semibold text-slate-900">${escapeHtml(c.data.name)}</div>\n                    <div class="mt-1 text-sm leading-5 text-slate-700">${escapeHtml(c.data.goal)}</div>\n                  </button>`).join("")}\n              </div>\n            </div>`;\n        }\n      }\n\n      // Root overview already shows Framework goals cards; skip duplicate Subtopics list there.\n      const childrenHtml = (children.length && d.depth > 0) ? `\n        <div class="mt-6">\n          <h3 class="text-xs font-semibold uppercase tracking-[0.14em] text-slate-500">Subtopics [${children.length}]</h3>\n          <ul class="mt-3 space-y-2">\n            ${children.map((c) => `\n              <li>\n                <button class="child-link text-left" data-child="${escapeHtml(c.data.name)}">${escapeHtml(c.data.name)}</button>\n                <span class="ml-2 text-xs text-slate-400">${countTools(c.data)} tools</span>\n              </li>`).join("")}\n          </ul>\n        </div>` : "";\n\n      const toolsHtml = tools.length ? `\n        <div class="mt-6">\n          <h3 class="text-xs font-semibold uppercase tracking-[0.14em] text-slate-500">Tools [${tools.length}]</h3>\n          <div class="mt-3 space-y-2.5">\n            ${tools.map((t) => {\n              const meta = toolMeta(t);\n              const text = (meta.relations && meta.relations[data.name]) || meta.blurb || "";\n              return `<div class="tool-card">\n                <div class="flex flex-wrap items-baseline justify-between gap-2">\n                  <div class="font-semibold text-slate-900">${escapeHtml(t)}</div>\n                  <div class="text-[11px] uppercase tracking-wide text-slate-500">${escapeHtml(meta.source)}</div>\n                </div>\n                <p class="tool-blurb">${escapeHtml(text)}</p>\n              </div>`;\n            }).join("")}\n          </div>\n        </div>` : "";\n\n      document.getElementById("detail").innerHTML = `\n        <h2 class="text-2xl font-semibold tracking-tight text-slate-900">${escapeHtml(data.name)}</h2>\n        <p class="mt-2 text-xs text-slate-400">${escapeHtml(path)}</p>\n        <p class="mt-4 text-[0.98rem] leading-7 text-slate-700">${escapeHtml(data.description || "")}</p>\n        ${goalHtml}\n        <div class="mt-5 grid grid-cols-2 gap-3">\n          <div class="rounded-2xl border border-slate-200 bg-slate-50 px-4 py-3">\n            <div class="text-xs uppercase tracking-wide text-slate-500">Concepts</div>\n            <div class="mt-1 text-xl font-semibold">${countLeaves(data)}</div>\n          </div>\n          <div class="rounded-2xl border border-slate-200 bg-slate-50 px-4 py-3">\n            <div class="text-xs uppercase tracking-wide text-slate-500">Tools</div>\n            <div class="mt-1 text-xl font-semibold">${countTools(data)}</div>\n          </div>\n        </div>\n        ${childrenHtml}\n        ${toolsHtml}\n      `;\n\n      document.querySelectorAll("[data-child]").forEach((btn) => {\n        btn.addEventListener("click", () => {\n          const child = children.find((c) => c.data.name === btn.getAttribute("data-child"));\n          if (child) openNode(child);\n        });\n      });\n    }\n\n    function escapeHtml(str) {\n      return String(str)\n        .replaceAll("&", "&amp;")\n        .replaceAll("<", "&lt;")\n        .replaceAll(">", "&gt;")\n        .replaceAll(\'"\', "&quot;");\n    }\n\n    window.addEventListener("resize", () => {\n      // keep current camera; only update svg box\n      resize();\n    });\n\n    selected = root;\n    focus = root;\n    fitTo(root, false);\n    renderDetail(root);\n    renderBreadcrumb(root);\n    updateLabels(d3.zoomTransform(svg.node()).k || 1);\n  </script>\n</body>\n</html>\n'

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
