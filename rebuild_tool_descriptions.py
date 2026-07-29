"""
Rebuild tool_catalog.py with accurate blurbs and per-category relation text.

Run:
    python3 rebuild_tool_descriptions.py
    python3 generate_geo_ktf_site.py
"""

from __future__ import annotations

import re
from collections import defaultdict
from pathlib import Path
from textwrap import dedent

from generate_geo_ktf_site import GEO_KTF_DATA
from tool_catalog import TOOL_INFO as OLD_INFO

# ---------------------------------------------------------------------------
# Category frames: what each leaf category is about (for relation sentences)
# ---------------------------------------------------------------------------
CATEGORY_FRAMES = {
    "Spatial relationships": "how features relate through containment, overlap, adjacency, and proximity",
    "Scale": "representation and processing of geography at different resolutions and levels of detail",
    "Uncertainty": "incomplete knowledge, measurement error, and communicating variability in spatial results",
    "Distance": "quantitative nearness, accessibility, and neighborhood definitions in space",
    "Vector": "the Vector data model—points, lines, and polygons with attributes",
    "Raster": "the Raster data model—values on a regular georeferenced grid",
    "Point Cloud": "the Point Cloud data model—dense 3D measurements such as LiDAR",
    "Mesh": "the Mesh data model—surfaces as connected faces and edges",
    "TIN": "the TIN data model—triangulated irregular networks from sample points",
    "DEM": "digital elevation models and terrain height surfaces",
    "Network": "the Network data model—graphs of nodes and costed edges for connectivity and routing",
    "Geographic": "geographic and projected CRS choices and transformations",
    "Datums": "horizontal (and related) datums and transformations between reference frames",
    "Vertical CRS": "vertical reference systems for heights and depths",
    "Units": "linear or angular units implied by a CRS definition",
    "Common CRS Errors": "typical CRS mistakes such as missing tags, wrong transforms, or axis-order confusion",
    "Metadata": "documenting what a dataset is, how it was produced, and how it should be used",
    "Lineage": "processing history that supports rerunning and auditing analyses",
    "Accuracy": "how close spatial measurements and locations are to true values",
    "Validity": "geometric validity rules required for reliable overlays and spatial SQL",
    "Vector Analysis": "geometric and attribute operations on points, lines, and polygons",
    "Raster Analysis": "map algebra, resampling, and neighborhood operations on grids",
    "Terrain Analysis": "landform metrics and surfaces derived from elevation data",
    "Network Analysis": "path, cost, and catchment problems on connected graphs",
    "Spatial Statistics": "pattern, clustering, autocorrelation, and density in geographic distributions",
    "Spatial Interpolation": "estimating continuous surfaces from discrete sample points",
    "Data Inspection": "inspecting structure, extent, CRS, and content before analysis",
    "Data Conversion": "transforming formats, encodings, and storage targets",
    "CRS Management": "assigning, inspecting, and reprojecting coordinate reference systems",
    "Vector Processing": "executable vector geoprocessing operators",
    "Raster Processing": "executable raster geoprocessing operators",
    "Database Processing": "spatial processing inside databases such as PostGIS or DuckDB",
    "Spatial SQL": "SQL geometry types, predicates, and spatial functions",
    "Geocoding": "converting between addresses/places and coordinates",
    "Routing": "computing paths, costs, and directions on transportation networks",
    "Accessibility": "measuring reachability by time, distance, or impedance",
    "Remote Sensing": "processing Earth observation imagery into analysis-ready products",
    "Spatial Clustering": "grouping observations by location and/or attributes",
    "Cartography": "visual encoding and map production for communication",
    "Site Selection": "combining criteria to identify candidate locations",
    "Suitability Analysis": "scoring locations against multi-criteria suitability models",
    "Catchment Analysis": "delineating areas served by facilities or outlets on a network",
    "Accessibility Analysis": "evaluating ease of reaching destinations",
    "Demographic Enrichment": "joining demographic or socioeconomic attributes by location",
    "Hazard Assessment": "screening exposure and terrain-related hazard conditions",
    "Environmental Assessment": "spatial overlays and indicators for environmental evaluation",
    "Infrastructure Planning": "siting and reachability analysis for infrastructure",
    "Land Use Analysis": "overlay and dissolve workflows for land-use change and composition",
    "Change Detection": "comparing multi-date layers to find what changed",
    "Hydrological Analysis": "flow direction, accumulation, sinks, and watershed delineation",
    "Visibility Analysis": "what can be seen from observer locations",
    "Remote Sensing Classification": "supervised or unsupervised labeling of imagery",
    "Urban Growth Analysis": "mapping and quantifying urban expansion patterns",
    "Geometry Validation": "detecting and repairing invalid geometries",
    "CRS Validation": "checking CRS metadata and reprojection correctness",
    "Metadata Validation": "verifying that metadata and inspection reports are complete",
    "Schema Validation": "checking attribute schemas, duplicates, and field structure",
    "Topology Validation": "checking topological rules between features",
    "Data Quality Assessment": "summarizing quality indicators from attributes and metadata",
    "Statistical Validation": "checking spatial statistical assumptions and patterns",
    "Result Validation": "auditing analytical outputs and processing trails",
    "Risk Detection": "flagging datasets or results that pose analysis risk",
    "Tables": "tabular exports of attributes and summaries for stakeholders",
    "GIS Files": "interoperable geospatial file deliverables",
    "Reports": "narrative and figure-based analysis reports",
    "Dashboards": "interactive operational views of spatial results",
    "APIs": "programmatic access to spatial data and services",
    "Geospatial Libraries": "software foundations that implement geospatial operations",
    "Cloud": "scalable cloud storage, formats, and compute for large spatial data",
    "Basemap": "reference basemaps and open geospatial data sources",
    "Web Mapping": "clients and servers for interactive web maps",
    "AI": "machine-learning frameworks applied to geospatial tasks",
}

# ---------------------------------------------------------------------------
# Accurate one-line capability for tools where auto-extract is weak / wrong
# ---------------------------------------------------------------------------
DOES_OVERRIDES = {
    "AWS": "provides cloud storage (S3) and scalable compute for hosting and analyzing large geospatial datasets, including COG and GeoParquet workflows",
    "Apache Sedona": "runs distributed spatial SQL and geometry analytics on Apache Spark at large scale",
    "Cloud Optimized GeoTIFF (COG)": "is a GeoTIFF layout optimized for HTTP range requests and efficient cloud streaming of rasters",
    "GeoParquet": "stores vector geometries in Parquet for columnar, cloud-friendly interchange",
    "OTB (Orfeo ToolBox)": "is an open-source remote sensing toolbox for image processing and classification",
    "OTB BandMath": "applies per-pixel mathematical expressions across image bands",
    "OTB ComputeImagesStatistics": "computes band-wise statistics needed for remote-sensing preprocessing",
    "OTB KMeansClassification": "performs unsupervised K-means classification of multispectral imagery",
    "OTB TrainImagesClassifier": "trains a supervised image classifier from labeled training samples",
    "PDAL": "is the Point Data Abstraction Library for reading, filtering, and writing point clouds",
    "PDAL pipeline": "chains PDAL readers, filters, and writers in a JSON workflow for LiDAR processing",
    "pdal pipeline": "chains PDAL readers, filters, and writers in a JSON workflow for LiDAR processing",
    "Fiona": "reads and writes vector formats through Python bindings to OGR",
    "GDAL / OGR": "is the core open-source library suite for raster (GDAL) and vector (OGR) geospatial I/O and transforms",
    "GeoPandas": "provides pandas-like GeoDataFrames for vector reading, writing, overlays, and joins",
    "Rasterio": "reads and writes rasters as NumPy arrays with affine/CRS metadata for scripted workflows",
    "Shapely": "provides geometric objects and predicates (buffer, intersection, validity) in Python",
    "PyProj": "exposes PROJ CRS definitions and coordinate transformations in Python",
    "PySAL": "implements spatial weights, spatial statistics, and related analytical components in Python",
    "ST_Buffer": "creates a distance buffer around geometries in PostGIS Spatial SQL",
    "ST_Contains": "tests whether one geometry fully contains another in PostGIS",
    "ST_Crosses": "tests whether geometries cross each other in PostGIS",
    "ST_DWithin": "tests whether geometries are within a specified distance in PostGIS",
    "ST_Distance": "returns the minimum distance between two geometries in PostGIS",
    "ST_Intersection": "returns the geometric intersection of two geometries in PostGIS",
    "ST_Intersects": "tests whether geometries intersect (including touch) in PostGIS",
    "ST_IsValid": "returns whether a geometry is topologically valid in PostGIS",
    "ST_IsValidDetail": "reports validity status and the location of invalidity in PostGIS",
    "ST_Overlaps": "tests whether geometries overlap in PostGIS",
    "ST_Touches": "tests whether geometries touch at boundary without overlapping interiors",
    "ST_Transform": "reprojects geometries between SRIDs/CRS definitions in PostGIS",
    "ST_Within": "tests whether a geometry lies entirely inside another in PostGIS",
    "gdal_calc": "evaluates band math expressions to create new rasters (indices, masks, conditionals)",
    "gdal_contour": "generates contour vectors from a raster elevation or continuous surface",
    "gdal_fillnodata": "interpolates across NoData gaps in a raster using neighboring valid cells",
    "gdal_grid": "creates a regular raster grid by interpolating from scattered points",
    "gdal_merge": "mosaics or stacks multiple rasters into one dataset",
    "gdal_polygonize": "converts connected regions of a raster into polygon features",
    "gdal_proximity": "computes distance from each cell to the nearest target cell value",
    "gdal_retile": "splits large rasters into tiled pyramids for scalable serving and processing",
    "gdal_translate": "converts rasters between formats/drivers, selects bands, and can assign georeferencing",
    "gdal_viewshed": "computes a viewshed raster from observer location(s) on a DEM",
    "gdaladdo": "builds overview (pyramid) levels for faster raster display and browsing",
    "gdalbuildvrt": "creates a virtual mosaic (VRT) that references tiles without rewriting them",
    "gdaldem TPI": "derives Topographic Position Index from a DEM",
    "gdaldem TRI": "derives Terrain Ruggedness Index from a DEM",
    "gdaldem aspect": "derives aspect (downslope direction) from a DEM",
    "gdaldem hillshade": "derives shaded relief from a DEM for visualization",
    "gdaldem roughness": "derives a roughness surface from a DEM",
    "gdaldem slope": "derives slope steepness from a DEM",
    "gdalinfo": "prints raster metadata: driver, CRS, geotransform, bands, NoData, and optional statistics",
    "gdalwarp": "reprojects, resamples, and clips rasters into a new georeferenced dataset",
    "ogr2ogr": "converts and transforms vector datasets between formats, including CRS and SQL filters",
    "ogrinfo": "prints vector layer metadata, fields, CRS, feature counts, and extents",
    "projinfo": "inspects CRS definitions and available PROJ transformation pipelines",
    "pyproj.CRS": "represents and inspects CRS objects from EPSG, WKT, PROJJSON, and authority codes",
    "pyproj.Transformer": "transforms coordinates between CRS definitions using PROJ pipelines",
    "pyproj.Transformer(always_xy=True)": "forces x/y (lon/lat) axis order to avoid common CRS axis-order errors",
    "geopandas.overlay()": "performs spatial overlays (intersection, union, difference, identity) between GeoDataFrames",
    "geopandas.read_file()": "reads vector files into a GeoDataFrame via Fiona/pyogrio",
    "geopandas.read_postgis()": "reads spatial SQL results from PostGIS into a GeoDataFrame",
    "geopandas.sjoin()": "joins GeoDataFrames using spatial predicates such as intersects or within",
    "geopandas.sjoin_nearest()": "joins each feature to its nearest neighbor with an optional distance limit",
    "geopandas.to_crs()": "reprojects a GeoDataFrame to a target CRS using pyproj",
    "geopandas.to_file()": "writes a GeoDataFrame to a geospatial file format",
    "geopandas.to_parquet()": "writes GeoParquet for cloud-efficient vector interchange",
    "geopandas.to_postgis()": "writes geometries and attributes into a PostGIS table",
    "rasterio.open()": "opens a raster dataset and exposes bands as arrays with CRS/transform metadata",
    "rasterio.mask.mask()": "clips a raster to polygon geometries, returning a masked array",
    "rasterio.features.rasterize()": "burns vector geometries into a raster grid",
    "rasterio.merge.merge()": "merges multiple raster datasets into one mosaic",
    "rio info": "prints Rasterio/GDAL-style metadata for a raster file from the command line",
    "geometry.is_valid": "reports whether a Shapely geometry passes validity rules",
    "geometry.is_valid (Shapely)": "reports whether a Shapely geometry passes validity rules",
    "esda.Moran": "computes Moran’s I for global spatial autocorrelation of an attribute",
    "esda.Moran_Local": "computes Local Moran’s I (LISA) to find local clusters and outliers",
    "esda.Geary": "computes Geary’s C statistic for global spatial autocorrelation",
    "esda.GetisOrd": "computes Getis-Ord statistics for hotspot and coldspot detection",
    "libpysal.weights": "constructs spatial weights matrices (contiguity, distance, kernel, etc.)",
    "filters.crop": "crops a point cloud to a spatial extent or polygon boundary",
    "filters.range": "keeps or removes points whose dimensions fall inside value ranges",
    "filters.reprojection": "reprojects point-cloud coordinates from one CRS to another",
    "readers.las": "reads LAS/LAZ point-cloud files into a PDAL pipeline",
    "writers.las": "writes point clouds to LAS/LAZ files",
    "writers.gdal": "writes point-cloud values onto a GDAL-supported raster grid",
    "pgr_dijkstra": "computes Dijkstra least-cost paths between nodes on a costed network graph in PostGIS/pgRouting",
    "pgr_aStar": "computes A* least-cost paths using a heuristic on a network graph",
    "pgr_KSP": "finds the K shortest paths between two nodes on a network",
    "pgr_dijkstraCostMatrix": "builds an all-pairs routing cost matrix using Dijkstra",
    "pgr_dijkstraNear": "finds nearest destinations from starting nodes by Dijkstra network cost",
    "pgr_dijkstraNearCost": "returns Dijkstra routing costs to nearby destinations",
    "pgr_dijkstraVia": "computes a path that visits a sequence of via vertices on a network",
    "pgr_drivingDistance": "computes the network catchment reachable within a cost (distance/time) limit",
    "pgRouting": "extends PostGIS with network routing and graph algorithms on edge tables",
    "openrouteservice": "provides open routing and accessibility services powered by OpenStreetMap",
    "openrouteservice directions": "returns turn-by-turn routing directions between locations",
    "openrouteservice geocoding": "geocodes and reverse-geocodes places and addresses",
    "openrouteservice isochrones": "creates travel-time or distance isochrone polygons from origins",
    "openrouteservice matrices": "computes origin–destination travel-time/distance matrices",
    "OSRM": "is a high-performance open-source routing engine based on OpenStreetMap",
    "Valhalla": "is an open-source routing engine for multimodal transportation graphs",
    "PostGIS": "adds geometry types, spatial indexes, and Spatial SQL to PostgreSQL",
    "DuckDB Spatial": "adds SQL geometry types and spatial functions to DuckDB",
    "DuckDB ST_Read": "reads geospatial files directly into DuckDB for SQL spatial analysis",
    "MapLibre GL JS": "renders interactive vector-tile maps in the browser with WebGL",
    "Leaflet": "builds interactive browser maps with a lightweight JavaScript API",
    "OpenLayers": "builds feature-rich interactive web mapping applications in JavaScript",
    "GeoServer": "publishes geospatial data through OGC web services (WMS/WFS/etc.)",
    "QGIS Server": "serves QGIS projects as OGC web map and feature services",
    "Microsoft Planetary Computer": "provides analysis-ready Earth observation datasets and cloud APIs",
    "Government Open Data APIs": "exposes agency open geospatial and administrative datasets via APIs",
    "OpenStreetMap": "is a collaborative worldwide basemap and open geospatial data project",
    "Overture Maps": "publishes open global map datasets for buildings, places, and transport",
    "Natural Earth": "provides public-domain cultural and physical basemap layers",
    "scikit-learn": "provides general-purpose machine-learning algorithms used in spatial workflows",
    "scikit-learn DBSCAN": "clusters nearby samples with DBSCAN for spatial pattern discovery",
    "XGBoost": "trains gradient-boosted trees often used for spatial predictive modeling",
    "PyTorch": "is a deep-learning framework commonly used for geospatial AI models",
    "TensorFlow": "is a deep-learning framework used for geospatial AI and perception models",
    "Segment Anything Model (SAM)": "segments objects in imagery and can support geospatial AI annotation workflows",
    "qgis_process": "runs QGIS Processing algorithms headlessly from the command line for reproducible pipelines",
    "ArcGIS Geocoding Service": "converts addresses and place names into coordinates through Esri’s cloud geocoding API",
    "Google Geocoding API": "geocodes addresses and reverse-geocodes coordinates through a web API",
    "Nominatim": "geocodes and reverse-geocodes places using an open-source service built on OpenStreetMap",
    "DBSCAN clustering": "groups nearby points with density-based clustering and flags noise points",
    "PyKrige": "performs kriging-based geostatistical interpolation in Python",
    "QGIS 3D Map View": "visualizes terrain, meshes, and 3D vector layers in an interactive 3D scene",
    "QGIS Geometry Checker": "checks vector layers against geometry and topology rules",
    "QGIS Geometry Checker Plugin": "checks vector layers against geometry and topology rules",
    "QGIS Model Designer": "builds reusable multi-step geoprocessing models visually",
    "QGIS Print Layout": "composes map pages, legends, scale bars, and print/PDF cartographic outputs",
    "QGIS Processing History": "records previously run Processing algorithms for audit and reuse",
    "QGIS Processing Log": "captures detailed runtime messages from Processing tools for debugging workflows",
    "QGIS Symbol Selector": "designs point, line, and polygon symbols and renderers",
    "Roughness": "measures elevation variability within a local neighborhood as a terrain metric",
    "TPI": "computes Topographic Position Index by comparing cell elevation to its neighborhood",
    "TRI": "computes Terrain Ruggedness Index from local elevation differences",
    "Heatmap (Kernel Density Estimation)": "estimates a continuous density surface from point occurrences using a kernel",
    "Heatmap / kernel density estimation": "estimates a continuous density surface from point occurrences using a kernel",
    "Kernel Density Estimation": "creates a smoothed density surface from point events using a kernel function",
    "IDW Interpolation": "interpolates a surface by inverse-distance weighting of nearby sample points",
    "TIN Interpolation": "interpolates a surface using a triangulated irregular network",
    "Delaunay triangulation": "builds a triangular mesh from point locations for TIN-style surfaces",
    "Hillshade": "renders shaded relief from a DEM using a simulated light source",
    "Aspect": "computes the downhill direction (aspect) of a terrain surface from elevation",
    "Slope": "computes slope steepness from a terrain surface",
    "Contour": "generates contour lines from a raster elevation or continuous surface",
    "Viewshed": "determines which areas are visible from one or more observer points",
    "QGIS Style Manager": "manages shared symbology, color ramps, and style libraries",
    "QGIS Label settings": "controls how feature labels are placed, styled, and prioritized on the map",
    "QGIS Reports": "generates multi-page atlas-style reports from layouts and project data",
    "Fiona": "reads and writes vector formats through Python bindings to OGR",
}


def extract_does(name: str, blurb: str) -> str:
    if name in DOES_OVERRIDES:
        return DOES_OVERRIDES[name]

    # New catalog format: "{name} {does}. It is documented under ..."
    m = re.match(rf"^{re.escape(name)}\s+(.+?)\.\s+It is documented under", blurb)
    if m:
        return m.group(1).strip()

    patterns = [
        r"characterizes its role as:\s*(.+?)\.\s",
        r"describes it as follows:\s*(.+?)\.\s+In practice",
        r"practice\.\s*(.+?)\.\s*Official documentation",
        r"In short:\s*(.+?)(?:\.|$)",
        r"Specifically:\s*(.+?)(?:\.|$)",
        r"Official OTB application docs describe it as:\s*(.+?)(?:\.|$)",
        r"Official PySAL documentation describes this component as:\s*(.+?)(?:\.|$)",
        r"Official GeoPandas documentation describes this API as one that\s*(.+?)(?:\.|$)",
        r"Official PROJ and pyproj documentation explain that it\s*(.+?)(?:\.|$)",
        r"as follows:\s*(.+?)\.\s",
    ]
    for pat in patterns:
        m = re.search(pat, blurb)
        if m:
            text = m.group(1).strip()
            text = re.sub(r"^(A |An |The )", "", text, flags=re.I)
            # Normalize leading capital for "does" phrase when needed
            if text[0].isupper() and not text.startswith(name):
                # keep as capability sentence fragment
                pass
            return text[0].lower() + text[1:] if text and text[0].isupper() and not text.startswith(("I ", "IDW", "A*", "K-", "SQL", "JSON", "HTTP", "OGC", "EPSG", "WKT", "CRS", "DEM", "TIN", "VRT", "LAS", "LAZ", "GDAL", "OGR", "PDAL", "PostGIS", "QGIS")) else text

    # Fallbacks for remaining awkward extracts — use first distinctive short sentence
    for sent in re.split(r"(?<=\.)\s+", blurb):
        if len(sent) < 40:
            continue
        if any(x in sent for x in ("Official documentation typically", "Responsible use includes", "Interoperability often", "Within the Geo Knowledge", "Within Geo-KTF", "In practice, the algorithm")):
            continue
        s = sent.strip().rstrip(".")
        s = re.sub(rf"^{re.escape(name)}\s+(is|are|provides|provided)\s+", "", s, flags=re.I)
        return s[0].lower() + s[1:] if s and s[0].isupper() else s
    return f"supports geospatial work related to {name}"


def to_does_phrase(text: str, name: str = "") -> str:
    text = text.strip().rstrip(".")
    if name:
        # Drop accidental leading tool-name duplicates from re-extraction
        for prefix in (name, name.lower(), name[0].lower() + name[1:] if name else ""):
            if prefix and text.lower().startswith(prefix.lower() + " "):
                text = text[len(prefix) :].lstrip(" :-")
                break
            if prefix and text.lower().startswith(prefix.lower()):
                # e.g. "Buffercreates" unlikely; keep
                pass
    text = text.strip()
    if not text:
        return "supports this geospatial capability"
    # Convert "Creates X" -> "creates X"
    if text[0].isupper() and not text.startswith(
        ("I ", "IDW", "A*", "K-", "SQL", "JSON", "HTTP", "OGC", "EPSG", "WKT", "CRS", "DEM", "TIN", "VRT", "LAS", "LAZ", "GDAL", "OGR", "PDAL", "PostGIS", "QGIS")
    ):
        text = text[0].lower() + text[1:]
    return text


def make_blurb(name: str, source: str, does: str, category: str | None = None) -> str:
    """One concise paragraph (~50–90 words): what the tool does, why it fits, source."""
    does = to_does_phrase(does, name)
    if does.startswith(
        ("is ", "are ", "provides ", "adds ", "extends ", "stores ", "runs ", "exposes ", "implements ", "renders ", "builds ", "publishes ")
    ):
        lead = f"{name} {does}."
    else:
        lead = f"{name} {does}."

    if category:
        frame = CATEGORY_FRAMES.get(category, f"{category} in Geo-KTF")
        bridge = (
            f" In {category}, which covers {frame}, "
            f"this tool is a representative way to carry out that work."
        )
    else:
        bridge = ""

    return f"{lead}{bridge} Documented under {source}; confirm CRS, units, and input validity before use."


def collect_tool_categories(root):
    mapping = defaultdict(set)

    def walk(node):
        if "tools" in node:
            for t in node["tools"]:
                mapping[t].add(node["name"])
        for c in node.get("children", []):
            walk(c)

    walk(root)
    return mapping


def rebuild():
    tool_cats = collect_tool_categories(GEO_KTF_DATA)
    new_info = {}

    for name in sorted(OLD_INFO):
        old = OLD_INFO[name]
        source = old["source"]
        does = to_does_phrase(extract_does(name, old["blurb"]), name)
        if name in DOES_OVERRIDES:
            does = to_does_phrase(DOES_OVERRIDES[name], name)
        # Fallback blurb (no category); per-category single paragraphs in relations
        blurb = make_blurb(name, source, does, category=None)
        relations = {
            cat: make_blurb(name, source, does, category=cat)
            for cat in sorted(tool_cats.get(name, []))
        }
        new_info[name] = {
            "source": source,
            "blurb": blurb,
            "relations": relations,
        }

    missing = [t for t in tool_cats if t not in new_info]
    if missing:
        raise SystemExit(f"Missing tools: {missing}")

    all_cats = {c for cats in tool_cats.values() for c in cats}
    missing_frames = sorted(c for c in all_cats if c not in CATEGORY_FRAMES)
    if missing_frames:
        raise SystemExit(f"Missing CATEGORY_FRAMES: {missing_frames}")

    out = Path(__file__).with_name("tool_catalog.py")
    lines = [
        '"""Tool catalog for Geo-KTF: source and concise per-category blurbs."""',
        "",
        "TOOL_INFO = {",
    ]
    for name in sorted(new_info):
        info = new_info[name]
        lines.append(f"    {name!r}: {{")
        lines.append(f"        'source': {info['source']!r},")
        lines.append(f"        'blurb': {info['blurb']!r},")
        lines.append("        'relations': {")
        for cat, rel in info["relations"].items():
            lines.append(f"            {cat!r}: {rel!r},")
        lines.append("        },")
        lines.append("    },")
    lines.append("}")
    lines.append("")
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")

    sample = new_info["Distance matrix"]
    print("Wrote", out)
    print("Tools:", len(new_info))
    print("Distance matrix / Distance:")
    print(" ", sample["relations"]["Distance"])
    print("words:", len(sample["relations"]["Distance"].split()))
    pgr = new_info["pgr_dijkstra"]["relations"]["Network"]
    print("pgr_dijkstra / Network:")
    print(" ", pgr)


if __name__ == "__main__":
    rebuild()
