# Geo-KTF — Geospatial Knowledge to Tool Framework

> Generated for external review. Category blurbs: 2–3 sentences (what / why / common tools). Tool blurbs: 3 sentences (what+source / does+benefit / expected output).

## Purpose of the framework

Geo-KTF (Geospatial Knowledge to Tool) organises geospatial practice into six pillars that follow a practical path: Understand foundations (Basic Geospatial Knowledge), Act with operations (Analytical Capabilities), Apply reusable workflows (Workflow), Ensure quality (Validation), Deliver outputs (Output), and Enable the work with software and data providers (Provider Registry). Concepts are kept separate from tools, so one idea can map to several equivalent implementations across QGIS, GDAL, PostGIS, Python, and related stacks. That separation makes it easier to learn what to do before choosing software, compare options fairly, and move from theory to executable practice.

### Design intent

- Separate **knowledge concepts** from **software tools**.
- Six pillars: Understand → Act → Apply → Ensure → Deliver → Enable.
- One concept can map to several equivalent tools.
- Duplicate leaf names across pillars were removed (Spatial Statistics & Spatial Interpolation kept only under Analytical Capabilities; Accuracy Assessment only under Validation; Terrain Analysis only under Basic Geospatial Knowledge).

### The six pillars

- **Understand — Basic Geospatial Knowledge**: Foundations: data models, CRS, relationships, quality ideas, and core analysis concepts.
- **Act — Analytical Capabilities**: Operations: the software-independent steps used to process, analyse, and map spatial data.
- **Apply — Workflow**: Workflows: repeatable chains of operations for common real-world geospatial tasks.
- **Ensure — Validation**: Quality: checks that data, CRS, geometry, and results are valid and trustworthy.
- **Deliver — Output**: Outputs: tables, files, maps, reports, APIs, and other products for sharing and decisions.
- **Enable — Provider Registry**: Providers: libraries, platforms, catalogues, and data sources that power the analysis stack.

## Full category tree with definitions

### Understand: Basic Geospatial Knowledge

- **Relationship**
  - **Overlay** (11 tools)
    - Overlay is the set of geometric operations that cut, merge, or reshape features by how they share space (buffer, clip, intersection, union, difference, dissolve). Use it when you need new geometries that answer “where do these layers interact?” Common tools include Buffer, Clip, Intersection, Union, Difference, Dissolve, and geopandas.overlay().
    - Tools: `Buffer`, `Clip`, `Intersection`, `Difference`, `Union`, `Dissolve`, `Split with lines`, `Line intersections`, `geopandas.overlay()`, `ST_Buffer`, `ST_Intersection`
  - **Adjacency** (5 tools)
    - Adjacency describes whether features touch or share a boundary without one containing the other. Use it to find neighbours, shared borders, or topology between adjacent polygons and lines. Common tools include ST_Touches, ST_Overlaps, ST_Crosses, and Extract by location.
    - Tools: `ST_Touches`, `ST_Overlaps`, `ST_Crosses`, `Line intersections`, `Extract by location`
  - **Containment** (5 tools)
    - Containment is the inside/outside relationship between features (contains, within, clip-to-boundary). Use it for points-in-polygons, zoning checks, and coverage tests. Common tools include ST_Contains, ST_Within, Clip, and Extract by location.
    - Tools: `ST_Contains`, `ST_Within`, `Extract by location`, `geopandas.sjoin()`, `Clip`
  - **Distance** (6 tools)
    - Distance measures how far features are from each other in coordinate or ground units. Use it for proximity, nearest-neighbour, and neighbourhood definitions that are metric rather than purely topological. Common tools include Distance Matrix, Distance to nearest hub, ST_Distance, ST_DWithin, and Join attributes by nearest.
    - Tools: `Distance Matrix`, `Distance to nearest hub`, `Join attributes by nearest`, `ST_Distance`, `ST_DWithin`, `geopandas.sjoin_nearest()`
  - **Connectivity** (5 tools)
    - Connectivity asks whether places are linked by a traversable network path, not just by straight-line nearness. Use it for routing, service reach, and corridor questions on roads or other graphs. Common tools include pgr_dijkstra, pgr_aStar, pgr_drivingDistance, and openrouteservice directions.
    - Tools: `pgr_dijkstra`, `pgr_aStar`, `pgr_KSP`, `pgr_drivingDistance`, `openrouteservice directions`
  - **Scale** (7 tools)
    - Scale is about how much detail a dataset keeps and at what resolution phenomena are represented. Use it when generalising maps, choosing cell size, or building multi-resolution pyramids so analysis matches the question. Common tools include Simplify, Generalize, Create grid, gdaladdo, and gdalbuildvrt.
    - Tools: `Simplify`, `Generalize`, `Create grid`, `Generate points (pixel centroids) inside polygons`, `gdaladdo`, `gdalbuildvrt`, `gdal_retile`
  - **Uncertainty** (3 tools)
    - Uncertainty means locations or values are not known exactly and may vary randomly or vaguely. Use it when sampling, testing sensitivity, or avoiding false certainty in maps. Common tools include Random points in extent, Random points in polygons, and Random selection.
    - Tools: `Random points in extent`, `Random points in polygons`, `Random selection`
- **Data Models**
  - **Vector** (7 tools)
    - Vector data stores discrete features as points, lines, or polygons with attributes. Use it for crisp boundaries, networks of features, and rich tabular properties. Common tools include ogrinfo, ogr2ogr, and GeoPandas read/write functions.
    - Tools: `ogrinfo`, `ogr2ogr`, `geopandas.read_file()`, `geopandas.read_postgis()`, `geopandas.to_file()`, `geopandas.to_parquet()`, `geopandas.to_postgis()`
  - **Raster** (7 tools)
    - Raster data stores values on a regular grid of cells (imagery, elevation, land cover). Use it for continuous fields and pixel-based analysis. Common tools include gdalinfo, gdal_translate, gdalwarp, gdalbuildvrt, and rasterio.open().
    - Tools: `gdalinfo`, `gdal_translate`, `gdalwarp`, `gdalbuildvrt`, `gdal_merge`, `rasterio.open()`, `rasterio.merge.merge()`
  - **Point Cloud** (7 tools)
    - A point cloud is a dense set of 3D points, often from LiDAR or photogrammetry. Use it to capture fine surface structure before deriving DEMs or meshes. Common tools include PDAL pipeline stages such as readers.las, filters, and writers.
    - Tools: `PDAL pipeline`, `readers.las`, `filters.crop`, `filters.range`, `filters.reprojection`, `writers.las`, `writers.gdal`
  - **Mesh** (5 tools)
    - A mesh represents surfaces as connected faces and edges, often for 3D visualisation or simulation. Use it when terrain or urban surfaces are more complex than a simple DEM grid. Common tools include Mesh Calculator and mesh export tools in QGIS.
    - Tools: `Mesh Calculator`, `Export mesh edges`, `Export mesh faces`, `Export mesh on grid`, `QGIS 3D Map View`
  - **TIN** (2 tools)
    - A TIN (triangulated irregular network) models a surface from irregular points connected as triangles. Use it to interpolate terrain or other fields while keeping sample locations. Common tools include TIN Interpolation and Delaunay triangulation.
    - Tools: `TIN Interpolation`, `Delaunay triangulation`
  - **DEM** (8 tools)
    - A DEM (digital elevation model) is a raster of ground (or surface) height. Use it as the base for slope, aspect, hydrology, viewsheds, and hillshade. Common tools include gdaldem derivatives, gdal_contour, and gdal_viewshed.
    - Tools: `gdaldem hillshade`, `gdaldem slope`, `gdaldem aspect`, `gdaldem roughness`, `gdaldem TRI`, `gdaldem TPI`, `gdal_contour`, `gdal_viewshed`
  - **Network** (8 tools)
    - A network is a graph of nodes and edges with costs such as length or travel time. Use it when movement follows roads or pipes rather than straight lines. Common tools include pgRouting functions such as pgr_dijkstra and pgr_drivingDistance.
    - Tools: `pgr_dijkstra`, `pgr_aStar`, `pgr_drivingDistance`, `pgr_dijkstraVia`, `pgr_KSP`, `pgr_dijkstraCostMatrix`, `pgr_dijkstraNear`, `pgr_dijkstraNearCost`
  - **Temporal Data** (5 tools)
    - Temporal data attaches times or date ranges to geographic observations so change can be tracked. Use it for multi-date imagery, event histories, and trend analysis. Common tools include gdalbuildvrt for time stacks, GeoParquet, and time-aware vector reads.
    - Tools: `gdalbuildvrt`, `gdal_translate`, `ogr2ogr`, `geopandas.read_file()`, `GeoParquet`
  - **Hex Grid** (4 tools)
    - A hex grid divides space into regular hexagonal cells for aggregation and comparison. Use it to summarise points or rates with less directional bias than square grids. Common tools include Create grid plus spatial joins such as geopandas.sjoin() or ST_Intersects.
    - Tools: `Create grid`, `geopandas.sjoin()`, `ST_Intersects`, `Join attributes by location`
  - **Trajectory** (5 tools)
    - A trajectory is an ordered path of locations through time for a moving object. Use it for mobility, GPS tracks, and route behaviour analysis. Common tools include MovingPandas and network routing functions that reconstruct travel paths.
    - Tools: `Shortest Path`, `pgr_dijkstra`, `pgr_dijkstraVia`, `pgr_aStar`, `openrouteservice directions`
  - **3D** (4 tools)
    - 3D geospatial models add height or full volumetric structure beyond flat maps. Use them for buildings, terrain scenes, and height-aware planning. Common tools include QGIS 3D Map View and mesh export utilities.
    - Tools: `QGIS 3D Map View`, `Export mesh faces`, `Export mesh edges`, `Mesh Calculator`
  - **Spatial Indexing** (3 tools)
    - Spatial indexing organises geometries so searches and joins do not scan every feature. Use it to keep large spatial queries fast in databases. Common tools include CREATE INDEX USING GIST, ST_GeoHash, and PostGIS.
    - Tools: `CREATE INDEX USING GIST`, `ST_GeoHash`, `PostGIS`
  - **Array Database** (3 tools)
    - Array databases store rasters and data cubes as multi-dimensional arrays rather than only as files or geometry rows. Use them for large time–space–band volumes and scientific slicing. Common tools include TileDB, xarray.open_dataset(), and GeoParquet for related columnar workflows.
    - Tools: `TileDB`, `xarray.open_dataset()`, `GeoParquet`
  - **Knowledge Graph** (3 tools)
    - A spatial knowledge graph links places and concepts as typed relationships that can be queried semantically. Use it when meaning and links matter as much as coordinates. Common tools include GeoSPARQL, RDFLib, and Apache Jena.
    - Tools: `GeoSPARQL`, `RDFLib`, `Apache Jena`
- **Coordinate Reference Systems**
  - **Geographic** (6 tools)
    - A geographic CRS locates positions on the Earth ellipsoid (latitude/longitude); a projected CRS maps them to a plane. Use the right type so distance, area, and alignment stay meaningful. Common tools include pyproj.CRS, geopandas.to_crs(), ST_Transform, and gdalwarp.
    - Tools: `pyproj.CRS`, `pyproj.Transformer`, `geopandas.to_crs()`, `ST_Transform`, `gdalwarp`, `projinfo`
  - **Datums** (5 tools)
    - A datum is the reference frame that defines where coordinates sit relative to the Earth. Use correct datum transformations to avoid metre- to tens-of-metre shifts between layers. Common tools include pyproj.Transformer, ST_Transform, gdalwarp, and projinfo.
    - Tools: `pyproj.CRS`, `pyproj.Transformer`, `ST_Transform`, `gdalwarp`, `projinfo`
  - **Vertical CRS** (7 tools)
    - A vertical CRS defines how heights and depths are referenced (ellipsoid, geoid, or local). Use it when elevation must be consistent for engineering, flood, or 3D work. Common tools include pyproj.CRS, projinfo, gdalinfo, and ST_Transform where vertical operations are supported.
    - Tools: `pyproj.CRS`, `pyproj.Transformer`, `projinfo`, `gdalinfo`, `ogrinfo`, `ST_Transform`, `gdalwarp`
  - **Units** (8 tools)
    - CRS units are the linear or angular units of coordinates (degrees, metres, feet). Use them consciously so buffers and lengths are not computed in degrees by mistake. Common tools include pyproj.CRS, projinfo, ST_Length, and ST_Area.
    - Tools: `pyproj.CRS`, `projinfo`, `gdalinfo`, `ogrinfo`, `geopandas.to_crs()`, `ST_Transform`, `ST_Length`, `ST_Area`
  - **Common CRS Errors** (9 tools)
    - Common CRS errors include missing CRS tags, wrong axis order, wrong datum, and confusing assign vs reproject. Fix them early to prevent silent misalignment and bad measurements. Common tools include Assign projection, Reproject Layer, geopandas.set_crs()/to_crs(), and pyproj.Transformer(always_xy=True).
    - Tools: `pyproj.Transformer(always_xy=True)`, `geopandas.set_crs()`, `geopandas.to_crs()`, `ST_SetSRID`, `ST_Transform`, `Assign projection`, `Reproject Layer`, `gdalwarp`, `projinfo`
- **Data Quality**
  - **Metadata** (5 tools)
    - Metadata is descriptive information about a dataset (what it is, CRS, extent, how it was made). Use it to judge fitness for purpose before analysis. Common tools include gdalinfo, ogrinfo, rio info, and dataset openers that surface schema and CRS.
    - Tools: `gdalinfo`, `ogrinfo`, `rio info`, `geopandas.read_file()`, `rasterio.open()`
  - **Lineage** (4 tools)
    - Lineage is the processing history of how a dataset or result was produced. Use it for reproducibility, auditing, and teaching. Common tools include QGIS Processing History, Processing Log, qgis_process, and Model Designer.
    - Tools: `QGIS Processing History`, `QGIS Processing Log`, `qgis_process`, `QGIS Model Designer`
  - **Precision** (7 tools)
    - Precision is how finely locations and values are represented (resolution, decimals, generalisation)—not whether they are correct. Use appropriate precision to balance detail, file size, and meaningful differences. Common tools include gdalinfo, Simplify, Generalize, Create grid, gdaladdo, and Snap geometries to grid.
    - Tools: `gdalinfo`, `Simplify`, `Generalize`, `gdal_translate`, `Create grid`, `gdaladdo`, `Snap geometries to grid`
  - **Validity** (5 tools)
    - Geometric validity means features obey structural rules needed for overlays and databases. Use validity checks to stop silent failures before analysis. Common tools include Check Geometries, Fix Geometries, ST_IsValid, and the QGIS Geometry Checker.
    - Tools: `QGIS Geometry Checker Plugin`, `Check Geometries`, `Fix Geometries`, `ST_IsValid`, `ST_IsValidDetail`
  - **Standards** (4 tools)
    - Standards define shared ways to describe and exchange geospatial information (especially metadata). Use them so data can be discovered and reused across organisations. Common tools and specs include ISO 19115, FGDC CSDGM, GeoNetwork, and pygeometa.
    - Tools: `GeoNetwork`, `ISO 19115`, `FGDC CSDGM`, `pygeometa`
  - **Uncertainty Modeling** (4 tools)
    - Uncertainty modeling represents error, vagueness, or random variation instead of treating every value as exact. Use it when decisions need confidence ranges or soft thresholds. Common tools include Fuzzy Overlay, Monte Carlo simulation, and random sampling tools.
    - Tools: `Fuzzy Overlay`, `Monte Carlo simulation`, `Random selection`, `Random points in extent`
- **Spatial Analysis**
  - **Vector Analysis** (15 tools)
    - Vector analysis is the family of geometry and attribute operations on points, lines, and polygons. Use it for overlays, buffers, dissolves, joins, and proximity on discrete features. Common tools include Buffer, Clip, Intersection, Dissolve, and spatial joins.
    - Tools: `Buffer`, `Clip`, `Intersection`, `Difference`, `Union`, `Dissolve`, `Centroids`, `Convex hull`, `Voronoi polygons`, `Split with lines`, `Line intersections`, `Join attributes by nearest`, `Extract by location`, `Distance Matrix`, `Distance to nearest hub`
  - **Raster Analysis** (8 tools)
    - Raster analysis applies map algebra, resampling, proximity, and related operations on grids. Use it for indices, reclassification, distance surfaces, and areal transfers to new zones. Common tools include Raster Calculator, gdal_calc, gdal_proximity, and tobler.area_interpolate().
    - Tools: `Raster Calculator`, `gdal_calc`, `gdal_proximity`, `gdal_fillnodata`, `gdal_polygonize`, `gdalwarp`, `gdal_translate`, `tobler.area_interpolate()`
  - **Terrain Analysis** (8 tools)
    - Terrain analysis derives landform metrics from elevation (slope, aspect, ruggedness, viewshed, contours). Use it for hazard, ecology, engineering, and landscape characterisation. Common tools include gdaldem slope/aspect/hillshade/TRI/TPI, gdal_contour, and gdal_viewshed.
    - Tools: `gdaldem slope`, `gdaldem aspect`, `gdaldem hillshade`, `gdaldem roughness`, `gdaldem TRI`, `gdaldem TPI`, `gdal_contour`, `gdal_viewshed`
  - **Network Analysis** (9 tools)
    - Network analysis solves path, cost, and catchment problems on connected graphs. Use it for logistics, emergency response, and service planning on roads or similar networks. Common tools include Shortest Path, Service Area, pgr_dijkstra, and openrouteservice directions.
    - Tools: `pgr_dijkstra`, `pgr_aStar`, `pgr_drivingDistance`, `pgr_dijkstraVia`, `pgr_KSP`, `pgr_dijkstraCostMatrix`, `Shortest Path`, `Service Area`, `openrouteservice directions`

### Act: Analytical Capabilities

- **Data Inspection** (6 tools)
  - Data inspection is checking structure, CRS, extent, schema, and content before analysis. Use it to catch bad inputs early and avoid wasted runs. Common tools include gdalinfo, ogrinfo, GeoPandas readers, rasterio.open(), and PDAL pipeline.
  - Tools: `gdalinfo`, `ogrinfo`, `geopandas.read_file()`, `geopandas.read_postgis()`, `rasterio.open()`, `PDAL pipeline`
- **Data Acquisition** (7 tools)
  - Data acquisition is capturing or collecting new geospatial observations in the field or from imagery and VGI. Use it when you need fresh, georeferenced primary data. Common tools include QField, ODK Collect, Georeferencer, GPSBabel, OpenDroneMap, iD Editor, and JOSM.
  - Tools: `QField`, `ODK Collect`, `Georeferencer`, `GPSBabel`, `OpenDroneMap`, `iD Editor`, `JOSM`
- **Data Conversion** (7 tools)
  - Data conversion transforms formats, encodings, and storage targets while trying to preserve meaning. Use it to move data between desktop, database, and cloud ecosystems. Common tools include ogr2ogr, gdal_translate, gdalwarp, gdalbuildvrt, and GeoPandas writers.
  - Tools: `ogr2ogr`, `gdal_translate`, `gdalwarp`, `gdalbuildvrt`, `geopandas.to_file()`, `geopandas.to_parquet()`, `geopandas.to_postgis()`
- **CRS Management** (8 tools)
  - CRS management assigns, inspects, and reprojects coordinate reference systems. Use it so layers align and measurements stay valid. Common tools include pyproj, GeoPandas CRS methods, ST_Transform, Assign projection, and gdalwarp.
  - Tools: `pyproj.CRS`, `pyproj.Transformer`, `projinfo`, `ST_Transform`, `geopandas.to_crs()`, `geopandas.set_crs()`, `Assign projection`, `gdalwarp`
- **Vector Processing** (11 tools)
  - Vector processing runs geometry and attribute operations that reshape vector layers. Use it as the day-to-day geoprocessing toolbox for overlays and edits. Common tools include Buffer, Clip, Intersection, Dissolve, Merge, Simplify, and nearest joins.
  - Tools: `Buffer`, `Clip`, `Intersection`, `Difference`, `Union`, `Dissolve`, `Merge Vector Layers`, `Multipart to Singleparts`, `Split Vector Layer`, `Join attributes by nearest`, `Simplify`
- **Raster Processing** (10 tools)
  - Raster processing covers resampling, algebra, mosaics, proximity, and raster–vector conversion. Use it to prepare imagery and surfaces for modelling and maps. Common tools include Raster Calculator, gdal_calc, gdal_translate, gdalwarp, and gdal_polygonize.
  - Tools: `Raster Calculator`, `gdal_calc`, `gdal_translate`, `gdalwarp`, `gdal_proximity`, `gdal_fillnodata`, `gdal_polygonize`, `gdal_contour`, `gdalbuildvrt`, `gdal_merge`
- **Database Processing** (8 tools)
  - Database processing reads, writes, and computes spatial data inside a spatial database. Use it for scalable analysis close to stored data with indexes. Common tools include PostGIS ST_ functions, DuckDB ST_Read, and GeoPandas PostGIS I/O.
  - Tools: `ST_Buffer`, `ST_Intersects`, `ST_DWithin`, `ST_Transform`, `ST_IsValid`, `geopandas.read_postgis()`, `geopandas.to_postgis()`, `DuckDB ST_Read`
- **Spatial SQL** (8 tools)
  - Spatial SQL expresses spatial filters and overlays as declarative queries. Use it for reproducible, set-based analysis on large tables. Common tools include ST_Intersects, ST_Contains, ST_Buffer, ST_DWithin, ST_Intersection, and ST_Transform.
  - Tools: `ST_Intersects`, `ST_Contains`, `ST_Within`, `ST_Buffer`, `ST_DWithin`, `ST_Intersection`, `ST_Distance`, `ST_Transform`
- **Geocoding** (4 tools)
  - Geocoding converts place names or addresses to coordinates (and reverse geocoding does the opposite). Use it to put tabular records on the map. Common tools include Nominatim, openrouteservice geocoding, Google Geocoding API, and ArcGIS Geocoding Service.
  - Tools: `openrouteservice geocoding`, `Nominatim`, `Google Geocoding API`, `ArcGIS Geocoding Service`
- **Routing** (5 tools)
  - Routing computes paths, costs, and turn-by-turn directions on a transportation network. Use it when travel follows roads rather than straight lines. Common tools include Shortest Path, pgr_dijkstra, pgr_aStar, pgr_KSP, and openrouteservice directions.
  - Tools: `Shortest Path`, `pgr_dijkstra`, `pgr_aStar`, `pgr_KSP`, `openrouteservice directions`
- **Accessibility** (5 tools)
  - Accessibility measures how reachable places are under time, distance, or impedance limits. Use it for equity, service coverage, and catchment planning. Common tools include Service Area, openrouteservice isochrones/matrices, Distance Matrix, and pgr_drivingDistance.
  - Tools: `Service Area`, `Distance Matrix`, `openrouteservice isochrones`, `openrouteservice matrices`, `pgr_drivingDistance`
- **Location-Allocation** (5 tools)
  - Location-allocation chooses facility sites and assigns demand to them to cut travel cost or raise coverage. Use it for siting schools, clinics, warehouses, and similar facilities. Common tools include v.net.alloc, OD matrices, Service Area, Distance Matrix, and ortools.routing.
  - Tools: `v.net.alloc`, `OD Matrix from Layers as Lines (m:n)`, `Distance Matrix`, `ortools.routing`, `Service Area`
- **Remote Sensing** (18 tools)
  - Remote sensing processes Earth observation imagery into analysis-ready layers and thematic maps. Use it for land cover, change, and feature extraction from satellites or drones. Common tools include GDAL/Rasterio/OTB utilities, OpenDroneMap, classifiers, and confusion-matrix tools.
  - Tools: `gdal_translate`, `gdalwarp`, `gdalbuildvrt`, `gdal_calc`, `rasterio.mask.mask()`, `OTB BandMath`, `OTB ComputeImagesStatistics`, `OpenDroneMap`, `Structure from Motion`, `PDAL pipeline`, `writers.gdal`, `OTB TrainImagesClassifier`, `OTB KMeansClassification`, `Segment Anything Model (SAM)`, `OTB ComputeConfusionMatrix`, `scikit-learn.metrics`, `Extract by location`, `Random points in polygons`
- **Spatial Statistics** (6 tools)
  - Spatial statistics quantify pattern, clustering, autocorrelation, and density in geographic data. Use it to test whether observed patterns are structured or likely random. Common tools include esda.Moran, Moran_Local, Geary, GetisOrd, libpysal.weights, and Heatmap (KDE).
  - Tools: `esda.Moran`, `esda.Moran_Local`, `esda.Geary`, `esda.GetisOrd`, `libpysal.weights`, `Heatmap (Kernel Density Estimation)`
- **Spatial Regression** (5 tools)
  - Spatial regression models relationships while accounting for spatial dependence or local variation. Use it when ordinary regression residuals are spatially autocorrelated or effects change across space. Common tools include spreg.OLS, ML_Lag, ML_Error, mgwr.GWR, and libpysal.weights.
  - Tools: `mgwr.GWR`, `spreg.OLS`, `spreg.ML_Lag`, `spreg.ML_Error`, `libpysal.weights`
- **Point Pattern Analysis** (5 tools)
  - Point pattern analysis describes whether events cluster, disperse, or look random in space. Use it for crime, disease, retail, or any event-dot map beyond a simple heatmap. Common tools include pointpats.PointPattern, centrography, Heatmap (KDE), and DBSCAN.
  - Tools: `pointpats.PointPattern`, `pointpats.centrography`, `Heatmap (Kernel Density Estimation)`, `DBSCAN clustering`, `Random points in extent`
- **Multi-Criteria Evaluation** (5 tools)
  - Multi-criteria evaluation (MCE) combines weighted criteria layers to rank or select suitable places. Use it for suitability and site screening with several factors. Common tools include Weighted Overlay, Fuzzy Overlay, Reclassify by table, and raster calculators.
  - Tools: `Weighted Overlay`, `Fuzzy Overlay`, `Reclassify by table`, `Raster Calculator`, `gdal_calc`
- **Spatial Interpolation** (6 tools)
  - Spatial interpolation predicts values at unsampled locations to build a continuous surface. Use it to map sparse measurements such as temperature, pollution, or elevation samples. Common tools include IDW, TIN, multilevel B-spline, thin-plate spline, gdal_grid, and PyKrige.
  - Tools: `IDW Interpolation`, `TIN Interpolation`, `gdal_grid`, `PyKrige`, `Multilevel B-Spline Interpolation`, `Thin plate spline`
- **Clustering** (8 tools)
  - Clustering groups observations by location and/or attributes into similar sets. Use it to find natural groupings without drawing boundaries by hand. Common tools include DBSCAN, K-means, HDBSCAN, scikit-learn clusterers, and PostGIS ST_Cluster* functions.
  - Tools: `DBSCAN clustering`, `K-means clustering`, `scikit-learn DBSCAN`, `scikit-learn KMeans`, `HDBSCAN`, `ST_ClusterDBSCAN`, `ST_ClusterKMeans`, `ST_ClusterWithin`
- **Cartography** (10 tools)
  - Cartography designs how spatial information is seen through symbols, colour, labels, themes, and layout. Use it to communicate patterns clearly without misleading readers. Common tools include QGIS Style Manager, symbol/label tools, graduated/categorized renderers, Print Layout, contours, and hillshade.
  - Tools: `QGIS Style Manager`, `QGIS Symbol Selector`, `QGIS Label settings`, `QGIS Print Layout`, `graduated renderer`, `categorized renderer`, `gdaldem hillshade`, `Contour`, `gdal_contour`, `QGIS 3D Map View`
- **Space-Time Analysis** (5 tools)
  - Space-time analysis studies how locations, attributes, or movements change through time. Use it for dynamics, animation, and multi-date comparison. Common tools include MovingPandas, QGIS Temporal Controller, GeoParquet, and multi-date VRT stacks.
  - Tools: `MovingPandas`, `QGIS Temporal Controller`, `GeoParquet`, `gdalbuildvrt`, `openrouteservice directions`
- **Trajectory Analysis** (6 tools)
  - Trajectory analysis studies ordered movement paths and travel behaviour. Use it for GPS tracks, fleet routes, and path comparison. Common tools include MovingPandas, Shortest Path, and pgRouting/openrouteservice path tools.
  - Tools: `Shortest Path`, `pgr_dijkstra`, `pgr_aStar`, `pgr_dijkstraVia`, `openrouteservice directions`, `MovingPandas`
- **Geocomputation** (4 tools)
  - Geocomputation uses simulation and iterative models (agents, cellular automata, visual models) for spatial processes. Use it when static GIS overlays cannot capture evolving behaviour. Common tools include mesa, NetLogo, Cellular Automata concepts, and QGIS Model Designer.
  - Tools: `mesa`, `NetLogo`, `Cellular Automata`, `QGIS Model Designer`

### Apply: Workflow

- **Site Selection** (7 tools)
  - Site selection is a workflow that combines spatial criteria to shortlist candidate locations. Use it for facilities or interventions that must meet several geographic rules. Common tools include Buffer, Clip, Intersection, and Weighted Overlay.
  - Tools: `Buffer`, `Clip`, `Intersection`, `Extract by location`, `Raster Calculator`, `Weighted Overlay`, `Dissolve`
- **Suitability Analysis** (6 tools)
  - Suitability analysis scores places against weighted criteria so alternatives can be ranked. Use it to turn policy or expert weights into a comparable map. Common tools include Raster Calculator, Weighted Overlay, Fuzzy Overlay, and Model Designer.
  - Tools: `Raster Calculator`, `gdal_calc`, `Weighted Overlay`, `Fuzzy Overlay`, `QGIS Model Designer`, `Reclassify by table`
- **Catchment Analysis** (3 tools)
  - Catchment analysis delineates the area served by a facility or contributing to a downstream point. Use it for service areas and watershed-style reasoning. Common tools include Service Area, pgr_drivingDistance, and openrouteservice isochrones.
  - Tools: `Service Area`, `pgr_drivingDistance`, `openrouteservice isochrones`
- **Accessibility Analysis** (5 tools)
  - Accessibility analysis evaluates how easily people or goods reach destinations under travel constraints. Use it for equity and coverage studies. Common tools include Service Area, Distance Matrix, and openrouteservice isochrones/matrices.
  - Tools: `Service Area`, `Distance Matrix`, `openrouteservice matrices`, `openrouteservice isochrones`, `pgr_drivingDistance`
- **Demographic Enrichment** (8 tools)
  - Demographic enrichment attaches population or socioeconomic attributes to spatial features. Use it when analysis needs census-like context not stored on the geometry. Common tools include Join attributes by location, geopandas.sjoin(), ST_Contains, and ST_Intersects.
  - Tools: `geopandas.sjoin()`, `geopandas.sjoin_nearest()`, `Join attributes by location`, `Join attributes by nearest`, `Extract by location`, `ST_Intersects`, `ST_Contains`, `ST_Within`
- **Hazard Assessment** (7 tools)
  - Hazard assessment maps exposure and susceptibility using terrain and thematic overlays. Use it for screening and preparedness communication. Common tools include gdaldem slope/aspect, Intersection, Clip, and Buffer.
  - Tools: `gdaldem slope`, `gdaldem aspect`, `gdaldem hillshade`, `Raster Calculator`, `gdal_proximity`, `Buffer`, `Intersection`
- **Environmental Assessment** (7 tools)
  - Environmental assessment evaluates conditions and impacts with buffers, proximity, overlays, and raster criteria. Use it for screening sensitivity and constraints. Common tools include Buffer, Clip, Intersection, gdal_proximity, and raster calculators.
  - Tools: `Buffer`, `Clip`, `Intersection`, `Raster Calculator`, `gdal_proximity`, `gdal_calc`, `gdal_fillnodata`
- **Infrastructure Planning** (7 tools)
  - Infrastructure planning uses networks, catchments, and proximity to site facilities and corridors. Use it when cost, access, and spatial suitability must be balanced. Common tools include Shortest Path, Service Area, Distance Matrix, Buffer, and routing engines.
  - Tools: `Shortest Path`, `Service Area`, `Distance Matrix`, `Buffer`, `ST_DWithin`, `pgr_dijkstra`, `openrouteservice directions`
- **Change Detection** (6 tools)
  - Change detection compares multi-temporal datasets to find where and how landscapes changed. Use it for monitoring land cover, urban growth, or disturbance. Common tools include gdalwarp, gdal_translate, gdal_calc, BandMath, and gdalbuildvrt.
  - Tools: `gdalwarp`, `gdal_translate`, `gdal_calc`, `Raster Calculator`, `OTB BandMath`, `gdalbuildvrt`
- **Hydrological Analysis** (6 tools)
  - Hydrological analysis models surface drainage from filled DEMs through flow and watersheds. Use it for flood, watershed, and drainage design studies. Common tools include Fill sinks, Flow direction, Flow accumulation, Watershed, and Channel network.
  - Tools: `Fill sinks`, `Flow direction`, `Flow accumulation`, `Watershed`, `Channel network`, `Strahler order`
- **Visibility Analysis** (2 tools)
  - Visibility analysis finds what can be seen from observer points given terrain occlusion. Use it for towers, scenic assessment, and security line-of-sight. Common tools include Viewshed and gdal_viewshed.
  - Tools: `Viewshed`, `gdal_viewshed`
- **Remote Sensing Classification** (6 tools)
  - Remote sensing classification assigns thematic classes to pixels or objects from imagery. Use it to produce land-cover or similar maps from EO data. Common tools include OTB TrainImagesClassifier, KMeansClassification, SAM, and BandMath.
  - Tools: `OTB TrainImagesClassifier`, `OTB KMeansClassification`, `OTB BandMath`, `OTB ComputeImagesStatistics`, `gdal_calc`, `Segment Anything Model (SAM)`
- **Urban Growth Analysis** (8 tools)
  - Urban growth analysis tracks expansion and intensification of development over time. Use it for planning insight from multi-date imagery and pattern metrics. Common tools include gdalwarp, gdal_calc, Heatmap (KDE), and spatial statistics tools.
  - Tools: `Raster Calculator`, `gdal_calc`, `OTB BandMath`, `Heatmap (Kernel Density Estimation)`, `DBSCAN clustering`, `gdalwarp`, `gdalbuildvrt`, `Intersection`

### Ensure: Validation

- **Geometry Validation** (6 tools)
  - Geometry validation detects and repairs invalid vector geometries. Use it before overlays, joins, or database loads. Common tools include Check Geometries, Fix Geometries, ST_IsValid, and Shapely is_valid.
  - Tools: `Check Geometries`, `Fix Geometries`, `QGIS Geometry Checker`, `ST_IsValid`, `ST_IsValidDetail`, `geometry.is_valid (Shapely)`
- **CRS Validation** (12 tools)
  - CRS validation confirms that coordinate systems are assigned and transformed correctly. Use it to prevent alignment and measurement errors. Common tools include pyproj, projinfo, Reproject Layer, Assign projection, and gdalinfo/ogrinfo.
  - Tools: `pyproj.CRS`, `pyproj.Transformer`, `pyproj.Transformer(always_xy=True)`, `projinfo`, `ST_Transform`, `geopandas.to_crs()`, `geopandas.set_crs()`, `gdalwarp`, `gdalinfo`, `ogrinfo`, `Reproject Layer`, `Assign projection`
- **Metadata Validation** (4 tools)
  - Metadata validation checks whether descriptive information is complete and consistent with the data. Use it before publishing or handing datasets to others. Common tools include gdalinfo, ogrinfo, rio info, and GeoPandas readers.
  - Tools: `gdalinfo`, `ogrinfo`, `rio info`, `geopandas.read_file()`
- **Schema Validation** (4 tools)
  - Schema validation checks fields, types, and table structure before joins or loads. Use it to stop automation and database failures from mismatched attributes. Common tools include ogrinfo, GeoPandas readers, and Refactor Fields.
  - Tools: `ogrinfo`, `geopandas.read_file()`, `geopandas.read_postgis()`, `Refactor Fields`
- **Topology Validation** (6 tools)
  - Topology validation checks relationships between features (gaps, overlaps, shared borders), not only single-geometry validity. Use it before overlays and network building. Common tools include ST_Touches/Overlaps/Crosses, Extract by location, and Check Geometries.
  - Tools: `ST_Touches`, `ST_Overlaps`, `ST_Crosses`, `Extract by location`, `Delete Duplicate Geometries`, `Check Geometries`
- **Statistical Validation** (5 tools)
  - Statistical validation uses spatial statistics to test whether patterns are structured or consistent with expectations. Use it as a quality gate for claims about clustering or dependence. Common tools include esda Moran/Geary/GetisOrd and libpysal.weights.
  - Tools: `esda.Moran`, `esda.Moran_Local`, `esda.Geary`, `esda.GetisOrd`, `libpysal.weights`
- **Accuracy Assessment** (4 tools)
  - Accuracy assessment compares classified or predicted maps with reference samples. Use it to report how close results are to truth (distinct from precision/resolution). Common tools include OTB ComputeConfusionMatrix, scikit-learn.metrics, Extract by location, and Random points in polygons.
  - Tools: `OTB ComputeConfusionMatrix`, `scikit-learn.metrics`, `Extract by location`, `Random points in polygons`
- **Result Validation** (5 tools)
  - Result validation audits outputs against methods, parameters, and processing history. Use it before publishing or handing results to another analyst. Common tools include QGIS Processing History/Log, qgis_process, and field statistics reports.
  - Tools: `QGIS Processing History`, `QGIS Processing Log`, `qgis_process`, `Basic Statistics for Fields`, `Field Statistics`

### Deliver: Output

- **Tables** (6 tools)
  - Tables are tabular exports of attributes and summaries. Use them for spreadsheets, statistics, and non-map review. Common tools include GeoPandas writers, ogr2ogr, and field statistics tools.
  - Tools: `geopandas.to_file()`, `geopandas.to_parquet()`, `geopandas.to_postgis()`, `ogr2ogr`, `Basic Statistics for Fields`, `Field Statistics`
- **GIS Files** (8 tools)
  - GIS files package geometries, attributes, and georeferencing for exchange between systems. Use them as the portable handoff between analysis and reuse. Common tools include ogr2ogr, gdal_translate/warp/buildvrt/merge, and GeoPandas file writers.
  - Tools: `ogr2ogr`, `gdal_translate`, `gdalwarp`, `gdalbuildvrt`, `gdal_merge`, `gdal_retile`, `geopandas.to_file()`, `geopandas.to_parquet()`
- **Reports** (2 tools)
  - Reports combine narrative, figures, and methods for stakeholders. Use them when a map alone is not enough explanation. Common tools include QGIS Reports and QGIS Print Layout.
  - Tools: `QGIS Reports`, `QGIS Print Layout`
- **Story Maps** (3 tools)
  - Story maps present maps, text, and media in a guided narrative sequence. Use them for outreach, teaching, and explained spatial stories. Common tools include ArcGIS StoryMaps, QGIS Print Layout, and MapLibre GL JS.
  - Tools: `ArcGIS StoryMaps`, `QGIS Print Layout`, `MapLibre GL JS`
- **Dashboards** (5 tools)
  - Dashboards are interactive operational views of spatial results. Use them for monitoring and exploration beyond static maps. Common tools include QGIS Server, GeoServer, Leaflet, MapLibre GL JS, and OpenLayers.
  - Tools: `QGIS Server`, `MapLibre GL JS`, `Leaflet`, `OpenLayers`, `GeoServer`
- **APIs** (9 tools)
  - APIs expose spatial data and processing programmatically. Use them to integrate GIS results into other applications. Common tools and services include QGIS Server, GeoServer, PostGIS, DuckDB Spatial, and routing/geocoding APIs.
  - Tools: `QGIS Server`, `GeoServer`, `PostGIS`, `DuckDB Spatial`, `openrouteservice`, `OSRM`, `Nominatim`, `Google Geocoding API`, `ArcGIS Geocoding Service`

### Enable: Provider Registry

- **Geospatial Libraries** (16 tools)
  - Geospatial libraries are the software engines behind many GIS operations (I/O, geometry, raster, routing). Use this registry to see which stack implements a capability. Common entries include GDAL/OGR, GeoPandas, PostGIS, PDAL, PySAL, and routing libraries.
  - Tools: `GDAL / OGR`, `GeoPandas`, `Shapely`, `Rasterio`, `Fiona`, `PyProj`, `PDAL`, `PySAL`, `OTB (Orfeo ToolBox)`, `DuckDB Spatial`, `PostGIS`, `Apache Sedona`, `OSRM`, `pgRouting`, `openrouteservice`, `Valhalla`
- **Cloud** (6 tools)
  - Cloud providers and formats support scalable storage and compute for large spatial data. Use them when desktop machines are not enough. Common entries include AWS, Google Earth Engine, ArcGIS Online, COG, GeoParquet, and Apache Sedona.
  - Tools: `Apache Sedona`, `GeoParquet`, `Cloud Optimized GeoTIFF (COG)`, `AWS`, `Google Earth Engine`, `ArcGIS Online`
- **SDI / Catalogs** (5 tools)
  - SDI and catalogs make datasets discoverable through metadata search and standard access. Use them to find and publish organisational or open data. Common entries include GeoNetwork, CKAN, STAC, pystac, and Planetary Computer.
  - Tools: `GeoNetwork`, `CKAN`, `STAC`, `pystac`, `Microsoft Planetary Computer`
- **Notebooks** (3 tools)
  - Notebooks are literate computing environments mixing code, text, and figures. Use them for reproducible teaching and analysis workflows. Common entries include Jupyter Notebook, Google Colab, and ArcGIS Notebooks.
  - Tools: `Jupyter Notebook`, `Google Colab`, `ArcGIS Notebooks`
- **Development** (5 tools)
  - Development covers languages and automation used to build GIS scripts and apps. Use them to move beyond one-off GUI clicks. Common entries include Python for GIS, R for GIS, JavaScript for GIS, Model Designer, and qgis_process.
  - Tools: `Python for GIS`, `R for GIS`, `JavaScript for GIS`, `QGIS Model Designer`, `qgis_process`
- **Basemap** (6 tools)
  - Basemap providers supply reference geography and open contextual layers. Use them as background or boundary inputs for analysis and maps. Common entries include OpenStreetMap, Google Maps, Overture Maps, Natural Earth, and open data APIs.
  - Tools: `OpenStreetMap`, `Google Maps`, `Overture Maps`, `Natural Earth`, `Microsoft Planetary Computer`, `Government Open Data APIs`
- **Web Mapping** (5 tools)
  - Web mapping providers are clients and servers for interactive online maps. Use them to publish results beyond desktop GIS. Common entries include MapLibre GL JS, Leaflet, OpenLayers, GeoServer, and QGIS Server.
  - Tools: `MapLibre GL JS`, `OpenLayers`, `Leaflet`, `GeoServer`, `QGIS Server`
- **AI** (5 tools)
  - AI providers are machine-learning frameworks and models applied to geospatial tasks. Use them for prediction, classification, and image segmentation. Common entries include scikit-learn, XGBoost, PyTorch, TensorFlow, and Segment Anything (SAM).
  - Tools: `scikit-learn`, `XGBoost`, `PyTorch`, `TensorFlow`, `Segment Anything Model (SAM)`

## Tool catalogue (255 tools in tree)

### `Apache Jena`
- Source: Apache Software Foundation
- Categories: Geo-KTF › Basic Geospatial Knowledge › Data Models › Knowledge Graph
- Definition: Apache Jena is an Apache Java framework for RDF and SPARQL. It stores and queries linked-data graphs at larger scale than lightweight Python tooling. Expected output: SPARQL results from a Jena dataset/store.

### `Apache Sedona`
- Source: Apache Sedona
- Categories: Geo-KTF › Provider Registry › Geospatial Libraries; Geo-KTF › Provider Registry › Cloud
- Definition: Apache Sedona is a spatial computing layer for Apache Spark/Flink. It runs distributed spatial SQL and joins when data exceeds one machine. Expected output: distributed spatial query results/DataFrames.

### `ArcGIS Geocoding Service`
- Source: Esri ArcGIS
- Categories: Geo-KTF › Analytical Capabilities › Geocoding; Geo-KTF › Output › APIs
- Definition: ArcGIS Geocoding Service is Esri’s geocoding REST API. It supports single and batch geocoding plus reverse geocoding with match scores. Expected output: candidate locations and addresses (token required).

### `ArcGIS Notebooks`
- Source: Esri
- Categories: Geo-KTF › Provider Registry › Notebooks
- Definition: ArcGIS Notebooks are Jupyter notebooks hosted in ArcGIS Online/Enterprise. They combine ArcGIS Python APIs with literate documentation for reproducible GIS workflows. Expected output: executed notebooks and derived layers/files.

### `ArcGIS Online`
- Source: Esri
- Categories: Geo-KTF › Provider Registry › Cloud
- Definition: ArcGIS Online is Esri’s cloud GIS platform. It hosts layers, web maps, apps, and analysis for organisational sharing. Expected output: hosted services, web maps, and shared content items.

### `ArcGIS StoryMaps`
- Source: Esri
- Categories: Geo-KTF › Output › Story Maps
- Definition: ArcGIS StoryMaps is Esri’s narrative mapping product. It guides readers through maps, text, and media as a spatial story for outreach and teaching. Expected output: a published story URL.

### `Assign projection`
- Source: QGIS Processing
- Categories: Geo-KTF › Basic Geospatial Knowledge › Coordinate Reference Systems › Common CRS Errors; Geo-KTF › Analytical Capabilities › CRS Management; Geo-KTF › Validation › CRS Validation
- Definition: Assign projection is a QGIS Processing CRS tool. It writes a CRS definition without changing coordinates—use when the tag is missing or wrong. Expected output: the same coordinates with updated CRS metadata.

### `AWS`
- Source: Amazon Web Services
- Categories: Geo-KTF › Provider Registry › Cloud
- Definition: AWS (Amazon Web Services) is a major cloud infrastructure provider. It hosts COGs/GeoParquet on S3 and runs compute for large geospatial pipelines. Expected output: stored datasets and processed results in cloud services.

### `Basic Statistics for Fields`
- Source: QGIS Processing
- Categories: Geo-KTF › Validation › Result Validation; Geo-KTF › Output › Tables
- Definition: Basic Statistics for Fields is a QGIS Processing summary tool. It computes count, min, max, mean, median, and related stats for one attribute as a quick data audit. Expected output: an HTML/text report plus numeric statistic outputs.

### `Buffer`
- Source: QGIS / ArcGIS Processing
- Categories: Geo-KTF › Basic Geospatial Knowledge › Relationship › Overlay; Geo-KTF › Basic Geospatial Knowledge › Spatial Analysis › Vector Analysis; Geo-KTF › Analytical Capabilities › Vector Processing; Geo-KTF › Workflow › Site Selection; Geo-KTF › Workflow › Hazard Assessment; Geo-KTF › Workflow › Environmental Assessment; Geo-KTF › Workflow › Infrastructure Planning
- Definition: Buffer is a core geoprocessing tool in QGIS and ArcGIS. It builds polygons around features at a fixed or attribute-based distance so you can model proximity and setbacks in projected units. Expected output: a polygon layer of buffer zones (optionally dissolved).

### `categorized renderer`
- Source: QGIS
- Categories: Geo-KTF › Analytical Capabilities › Cartography
- Definition: A categorized renderer is a QGIS thematic mapping mode. It assigns a distinct symbol to each unique attribute value for qualitative maps. Expected output: a categorical map appearance with a class legend.

### `Cellular Automata`
- Source: Geocomputation method
- Categories: Geo-KTF › Analytical Capabilities › Geocomputation
- Definition: Cellular automata are a geocomputation modelling style used in research tools and NetLogo/Mesa models. They update each cell from local neighbourhood rules over time to simulate processes like urban growth or fire spread. Expected output: a sequence of grid states or a final simulated landscape raster.

### `Centroids`
- Source: QGIS Processing
- Categories: Geo-KTF › Basic Geospatial Knowledge › Spatial Analysis › Vector Analysis
- Definition: Centroids is a QGIS Processing algorithm. It places one point at the geometric centre of each feature (with an option to force points inside), which helps labelling and distance work. Expected output: a point layer with original attributes.

### `Channel network`
- Source: QGIS / SAGA
- Categories: Geo-KTF › Workflow › Hydrological Analysis
- Definition: Channel network is a SAGA-based stream extraction tool in QGIS Processing. It traces channels where accumulation exceeds a threshold on a conditioned DEM. Expected output: stream rasters and/or vector channel lines.

### `Check Geometries`
- Source: QGIS Processing
- Categories: Geo-KTF › Basic Geospatial Knowledge › Data Quality › Validity; Geo-KTF › Validation › Geometry Validation; Geo-KTF › Validation › Topology Validation
- Definition: Check Geometries is part of the QGIS Geometry Checker toolset. It tests selected validity/topology rules and reports failures without auto-fixing everything. Expected output: valid/invalid feature sets plus an error point layer with messages.

### `CKAN`
- Source: Open Knowledge Foundation / CKAN
- Categories: Geo-KTF › Provider Registry › SDI / Catalogs
- Definition: CKAN is open-source data portal software. With spatial extensions it supports dataset catalogues and bounding-box search for government open data. Expected output: a public data catalogue with dataset pages/APIs.

### `Clip`
- Source: QGIS / ArcGIS Processing
- Categories: Geo-KTF › Basic Geospatial Knowledge › Relationship › Overlay; Geo-KTF › Basic Geospatial Knowledge › Relationship › Containment; Geo-KTF › Basic Geospatial Knowledge › Spatial Analysis › Vector Analysis; Geo-KTF › Analytical Capabilities › Vector Processing; Geo-KTF › Workflow › Site Selection; Geo-KTF › Workflow › Environmental Assessment
- Definition: Clip is a standard overlay tool in QGIS and ArcGIS. It cuts an input layer to overlay polygon boundaries and keeps only the inside parts, without bringing overlay attributes. Expected output: a clipped layer of the same geometry type as the input.

### `Cloud Optimized GeoTIFF (COG)`
- Source: OGC / GDAL ecosystem
- Categories: Geo-KTF › Provider Registry › Cloud
- Definition: Cloud Optimized GeoTIFF (COG) is an OGC/community GeoTIFF profile. It enables HTTP range reads of tiles/overviews so apps fetch only needed bytes. Expected output: a COG file readable efficiently from object storage.

### `Contour`
- Source: QGIS / GDAL
- Categories: Geo-KTF › Analytical Capabilities › Cartography
- Definition: Contour is a QGIS tool built on GDAL contouring. It draws isolines of equal value from a raster band (usually elevation) for readable terrain maps. Expected output: a line (or polygon) vector layer of contours with level attributes.

### `Convex hull`
- Source: QGIS Processing
- Categories: Geo-KTF › Basic Geospatial Knowledge › Spatial Analysis › Vector Analysis
- Definition: Convex hull is a QGIS Processing geometry tool. It builds the smallest convex polygon enclosing each geometry, like a rubber band around the shape. Expected output: a polygon layer of hulls (rough extents, ignoring concavities).

### `Create grid`
- Source: QGIS Processing
- Categories: Geo-KTF › Basic Geospatial Knowledge › Relationship › Scale; Geo-KTF › Basic Geospatial Knowledge › Data Models › Hex Grid; Geo-KTF › Basic Geospatial Knowledge › Data Quality › Precision
- Definition: Create grid is a QGIS Processing tool. It builds a regular vector lattice over an extent for sampling or aggregation frames. Expected output: a polygon (or line) grid layer in a chosen CRS.

### `CREATE INDEX USING GIST`
- Source: PostgreSQL / PostGIS
- Categories: Geo-KTF › Basic Geospatial Knowledge › Data Models › Spatial Indexing
- Definition: CREATE INDEX USING GIST is PostgreSQL/PostGIS SQL for spatial indexes. It accelerates bounding-box filters behind most ST_ predicates on large tables. Expected output: a GiST index on a geometry/geography column.

### `DBSCAN clustering`
- Source: QGIS / scikit-learn
- Categories: Geo-KTF › Analytical Capabilities › Point Pattern Analysis; Geo-KTF › Analytical Capabilities › Clustering; Geo-KTF › Workflow › Urban Growth Analysis
- Definition: DBSCAN clustering is a QGIS Processing density-clustering tool. It groups nearby points and labels sparse points as noise without choosing the number of clusters in advance. Expected output: a layer with cluster ID attributes (and noise labels).

### `Delaunay triangulation`
- Source: QGIS Processing
- Categories: Geo-KTF › Basic Geospatial Knowledge › Data Models › TIN
- Definition: Delaunay triangulation is a QGIS Processing triangulation tool. It connects points into non-overlapping triangles used to build TINs and related surfaces. Expected output: a triangular mesh/polygon layer of Delaunay faces.

### `Delete Duplicate Geometries`
- Source: QGIS Processing
- Categories: Geo-KTF › Validation › Topology Validation
- Definition: Delete Duplicate Geometries is a QGIS Processing cleanup tool. It collapses features with identical geometries to a single feature to remove digitising duplicates. Expected output: a deduplicated layer.

### `Difference`
- Source: QGIS / ArcGIS Processing
- Categories: Geo-KTF › Basic Geospatial Knowledge › Relationship › Overlay; Geo-KTF › Basic Geospatial Knowledge › Spatial Analysis › Vector Analysis; Geo-KTF › Analytical Capabilities › Vector Processing
- Definition: Difference (Erase) is an overlay tool in QGIS/ArcGIS Processing. It removes parts of the input covered by an overlay layer, which is useful for exclusion zones. Expected output: the input geometry minus the overlay areas.

### `Dissolve`
- Source: QGIS / ArcGIS Processing
- Categories: Geo-KTF › Basic Geospatial Knowledge › Relationship › Overlay; Geo-KTF › Basic Geospatial Knowledge › Spatial Analysis › Vector Analysis; Geo-KTF › Analytical Capabilities › Vector Processing; Geo-KTF › Workflow › Site Selection
- Definition: Dissolve is a vector aggregation tool in QGIS/ArcGIS. It merges features into larger ones, optionally grouped by attributes, removing shared boundaries within groups. Expected output: fewer multipart or single dissolved features with aggregated geometry.

### `Distance Matrix`
- Source: QGIS Processing
- Categories: Geo-KTF › Basic Geospatial Knowledge › Relationship › Distance; Geo-KTF › Basic Geospatial Knowledge › Spatial Analysis › Vector Analysis; Geo-KTF › Analytical Capabilities › Accessibility; Geo-KTF › Analytical Capabilities › Location-Allocation; Geo-KTF › Workflow › Accessibility Analysis; Geo-KTF › Workflow › Infrastructure Planning
- Definition: Distance Matrix is a QGIS Processing tool for point-to-point distances. It measures straight-line distances between two point layers (not road-network travel time) and can summarise nearest targets. Expected output: a distance table, matrix, or summary statistics in CRS units.

### `Distance to nearest hub`
- Source: QGIS Processing
- Categories: Geo-KTF › Basic Geospatial Knowledge › Relationship › Distance; Geo-KTF › Basic Geospatial Knowledge › Spatial Analysis › Vector Analysis
- Definition: Distance to nearest hub is a QGIS Processing proximity tool. It finds each feature’s closest hub and records hub identity and distance, optionally as connecting lines. Expected output: points or lines with HubName/HubDist-style fields.

### `DuckDB Spatial`
- Source: DuckDB
- Categories: Geo-KTF › Output › APIs; Geo-KTF › Provider Registry › Geospatial Libraries
- Definition: DuckDB Spatial is the spatial extension for DuckDB. It adds geometry types and ST_ functions for fast in-process spatial SQL on local/Parquet data. Expected output: query results and spatial tables/files.

### `DuckDB ST_Read`
- Source: DuckDB Spatial
- Categories: Geo-KTF › Analytical Capabilities › Database Processing
- Definition: DuckDB ST_Read is a DuckDB Spatial table function. It reads vector files through GDAL/OGR directly into SQL without a separate import step. Expected output: a queryable table with geometry.

### `esda.Geary`
- Source: PySAL ESDA
- Categories: Geo-KTF › Analytical Capabilities › Spatial Statistics; Geo-KTF › Validation › Statistical Validation
- Definition: esda.Geary is a PySAL ESDA class for Geary’s C. It measures global spatial autocorrelation as a complement to Moran’s I. Expected output: Geary’s C statistic with inference.

### `esda.GetisOrd`
- Source: PySAL ESDA
- Categories: Geo-KTF › Analytical Capabilities › Spatial Statistics; Geo-KTF › Validation › Statistical Validation
- Definition: esda.GetisOrd is a PySAL ESDA hotspot tool. It computes Getis-Ord statistics to locate concentrations of high or low values. Expected output: Gi/Gi* scores for hotspot mapping.

### `esda.Moran`
- Source: PySAL ESDA
- Categories: Geo-KTF › Analytical Capabilities › Spatial Statistics; Geo-KTF › Validation › Statistical Validation
- Definition: esda.Moran is a PySAL ESDA class for Moran’s I. It measures global spatial autocorrelation to test whether similar values cluster. Expected output: Moran’s I statistic with inference (e.g., p-value).

### `esda.Moran_Local`
- Source: PySAL ESDA
- Categories: Geo-KTF › Analytical Capabilities › Spatial Statistics; Geo-KTF › Validation › Statistical Validation
- Definition: esda.Moran_Local is a PySAL ESDA LISA tool. It finds local clusters and spatial outliers (high-high, low-low, etc.) for mapping. Expected output: local Moran indicators and cluster classifications.

### `Export mesh edges`
- Source: QGIS Mesh tools
- Categories: Geo-KTF › Basic Geospatial Knowledge › Data Models › Mesh; Geo-KTF › Basic Geospatial Knowledge › Data Models › 3D
- Definition: Export mesh edges is a QGIS mesh conversion tool. It turns mesh edges into ordinary vector lines for use outside mesh formats. Expected output: a line vector layer of mesh edges.

### `Export mesh faces`
- Source: QGIS Mesh tools
- Categories: Geo-KTF › Basic Geospatial Knowledge › Data Models › Mesh; Geo-KTF › Basic Geospatial Knowledge › Data Models › 3D
- Definition: Export mesh faces is a QGIS mesh conversion tool. It turns mesh faces into polygons, optionally with sampled dataset values. Expected output: a polygon vector layer of faces.

### `Export mesh on grid`
- Source: QGIS Mesh tools
- Categories: Geo-KTF › Basic Geospatial Knowledge › Data Models › Mesh
- Definition: Export mesh on grid is a QGIS mesh sampling tool. It samples mesh values onto a regular point grid that is easier to rasterise or join. Expected output: a point grid layer with sampled values.

### `Extract by location`
- Source: QGIS Processing
- Categories: Geo-KTF › Basic Geospatial Knowledge › Relationship › Adjacency; Geo-KTF › Basic Geospatial Knowledge › Relationship › Containment; Geo-KTF › Basic Geospatial Knowledge › Spatial Analysis › Vector Analysis; Geo-KTF › Analytical Capabilities › Remote Sensing; Geo-KTF › Workflow › Site Selection; Geo-KTF › Workflow › Demographic Enrichment; Geo-KTF › Validation › Topology Validation; Geo-KTF › Validation › Accuracy Assessment
- Definition: Extract by location is a QGIS Processing selection tool. It keeps input features that satisfy a spatial relationship with another layer, without cutting geometries. Expected output: a subset layer of matching features.

### `FGDC CSDGM`
- Source: FGDC
- Categories: Geo-KTF › Basic Geospatial Knowledge › Data Quality › Standards
- Definition: FGDC CSDGM is the classic U.S. federal geospatial metadata content standard. It structures identification, quality, spatial reference, entities, and distribution sections for catalogues. Expected output: CSDGM metadata records.

### `Field Statistics`
- Source: QGIS Processing
- Categories: Geo-KTF › Validation › Result Validation; Geo-KTF › Output › Tables
- Definition: Field Statistics is a QGIS summary tool for attribute columns. It calculates descriptive statistics to check distributions before modelling or mapping. Expected output: numeric summaries and a readable report.

### `Fill sinks`
- Source: QGIS Hydrology
- Categories: Geo-KTF › Workflow › Hydrological Analysis
- Definition: Fill sinks is a hydrological preprocessing tool in QGIS/SAGA/GRASS workflows. It removes DEM depressions that trap flow so drainage algorithms can run consistently. Expected output: a hydrologically conditioned DEM.

### `filters.crop`
- Source: PDAL
- Categories: Geo-KTF › Basic Geospatial Knowledge › Data Models › Point Cloud
- Definition: filters.crop is a PDAL filter stage. It crops points to a box or polygon to keep only an area of interest. Expected output: a reduced point view.

### `filters.range`
- Source: PDAL
- Categories: Geo-KTF › Basic Geospatial Knowledge › Data Models › Point Cloud
- Definition: filters.range is a PDAL filter stage. It keeps points whose dimension values fall in specified ranges (class, return, intensity, …). Expected output: a filtered point view.

### `filters.reprojection`
- Source: PDAL
- Categories: Geo-KTF › Basic Geospatial Knowledge › Data Models › Point Cloud
- Definition: filters.reprojection is a PDAL filter stage. It reprojects point coordinates to another CRS inside the pipeline. Expected output: points in the target CRS.

### `Fiona`
- Source: Python (Toblerity)
- Categories: Geo-KTF › Provider Registry › Geospatial Libraries
- Definition: Fiona is a Python OGR wrapper for vector I/O. It reads/writes GIS files with a simple dict-based interface as a lower-level companion to GeoPandas. Expected output: Python feature records or written vector files.

### `Fix Geometries`
- Source: QGIS Processing
- Categories: Geo-KTF › Basic Geospatial Knowledge › Data Quality › Validity; Geo-KTF › Validation › Geometry Validation
- Definition: Fix Geometries is a QGIS Processing repair tool. It attempts to make invalid geometries valid so overlays and databases do not fail. Expected output: a repaired layer (inspect remaining errors afterward).

### `Flow accumulation`
- Source: QGIS Hydrology
- Categories: Geo-KTF › Workflow › Hydrological Analysis
- Definition: Flow accumulation is a hydrological tool in QGIS/SAGA/GRASS toolboxes. It counts how much upslope area drains through each cell, highlighting likely channels. Expected output: an accumulation raster (proxy catchment area).

### `Flow direction`
- Source: QGIS Hydrology
- Categories: Geo-KTF › Workflow › Hydrological Analysis
- Definition: Flow direction is a hydrological tool in QGIS/SAGA/GRASS toolboxes. It records the downhill neighbour for each DEM cell as the basis for accumulation and streams. Expected output: a flow-direction raster.

### `Fuzzy Overlay`
- Source: QGIS Processing
- Categories: Geo-KTF › Basic Geospatial Knowledge › Data Quality › Uncertainty Modeling; Geo-KTF › Analytical Capabilities › Multi-Criteria Evaluation; Geo-KTF › Workflow › Suitability Analysis
- Definition: Fuzzy Overlay is a soft multi-criteria combination tool (ArcGIS/QGIS fuzzy workflows). It combines membership rasters (0–1) when thresholds are vague, unlike crisp weighted classes. Expected output: a continuous suitability/membership raster.

### `GDAL / OGR`
- Source: OSGeo
- Categories: Geo-KTF › Provider Registry › Geospatial Libraries
- Definition: GDAL/OGR is the OSGeo translator library and utilities for rasters (GDAL) and vectors (OGR). It underpins most GIS I/O and conversion across QGIS, PostGIS loaders, and Python tools. Expected output: converted datasets and metadata via its CLI/API.

### `gdal_calc`
- Source: GDAL
- Categories: Geo-KTF › Basic Geospatial Knowledge › Spatial Analysis › Raster Analysis; Geo-KTF › Analytical Capabilities › Raster Processing; Geo-KTF › Analytical Capabilities › Remote Sensing; Geo-KTF › Analytical Capabilities › Multi-Criteria Evaluation; Geo-KTF › Workflow › Suitability Analysis; Geo-KTF › Workflow › Environmental Assessment; Geo-KTF › Workflow › Change Detection; Geo-KTF › Workflow › Remote Sensing Classification; Geo-KTF › Workflow › Urban Growth Analysis
- Definition: gdal_calc is GDAL’s NumPy raster calculator. It evaluates band expressions (A, B, C, …) for indices, masks, and change detection in scripts. Expected output: a computed raster.

### `gdal_contour`
- Source: GDAL
- Categories: Geo-KTF › Basic Geospatial Knowledge › Data Models › DEM; Geo-KTF › Basic Geospatial Knowledge › Spatial Analysis › Terrain Analysis; Geo-KTF › Analytical Capabilities › Raster Processing; Geo-KTF › Analytical Capabilities › Cartography
- Definition: gdal_contour is a GDAL contouring utility. It extracts isolines (or filled contour polygons) from a raster band with chosen intervals or levels. Expected output: a contour vector dataset.

### `gdal_fillnodata`
- Source: GDAL
- Categories: Geo-KTF › Basic Geospatial Knowledge › Spatial Analysis › Raster Analysis; Geo-KTF › Analytical Capabilities › Raster Processing; Geo-KTF › Workflow › Environmental Assessment
- Definition: gdal_fillnodata is a GDAL gap-filling utility. It interpolates into nodata holes from surrounding valid cells as cleanup before analysis. Expected output: a raster with filled gaps.

### `gdal_grid`
- Source: GDAL
- Categories: Geo-KTF › Analytical Capabilities › Spatial Interpolation
- Definition: gdal_grid is a GDAL interpolator. It grids scattered points to a raster using IDW, nearest, average, and related algorithms. Expected output: an interpolated raster surface.

### `gdal_merge`
- Source: GDAL
- Categories: Geo-KTF › Basic Geospatial Knowledge › Data Models › Raster; Geo-KTF › Analytical Capabilities › Raster Processing; Geo-KTF › Output › GIS Files
- Definition: gdal_merge is a GDAL mosaic utility. It merges rasters into one file when a simple same-CRS mosaic is enough. Expected output: a single mosaicked raster.

### `gdal_polygonize`
- Source: GDAL
- Categories: Geo-KTF › Basic Geospatial Knowledge › Spatial Analysis › Raster Analysis; Geo-KTF › Analytical Capabilities › Raster Processing
- Definition: gdal_polygonize is a GDAL raster-to-vector utility. It converts regions of equal cell value into polygons for GIS overlay work. Expected output: a polygon vector layer.

### `gdal_proximity`
- Source: GDAL
- Categories: Geo-KTF › Basic Geospatial Knowledge › Spatial Analysis › Raster Analysis; Geo-KTF › Analytical Capabilities › Raster Processing; Geo-KTF › Workflow › Hazard Assessment; Geo-KTF › Workflow › Environmental Assessment
- Definition: gdal_proximity is a GDAL distance utility. It measures each cell’s distance to the nearest target cell for exposure and accessibility-style surfaces. Expected output: a proximity distance raster.

### `gdal_retile`
- Source: GDAL
- Categories: Geo-KTF › Basic Geospatial Knowledge › Relationship › Scale; Geo-KTF › Output › GIS Files
- Definition: gdal_retile is a GDAL tiling utility. It cuts rasters into tiles for web mapping or distributed processing. Expected output: a set of tiled raster files.

### `gdal_translate`
- Source: GDAL
- Categories: Geo-KTF › Basic Geospatial Knowledge › Data Models › Raster; Geo-KTF › Basic Geospatial Knowledge › Data Models › Temporal Data; Geo-KTF › Basic Geospatial Knowledge › Data Quality › Precision; Geo-KTF › Basic Geospatial Knowledge › Spatial Analysis › Raster Analysis; Geo-KTF › Analytical Capabilities › Data Conversion; Geo-KTF › Analytical Capabilities › Raster Processing; Geo-KTF › Analytical Capabilities › Remote Sensing; Geo-KTF › Workflow › Change Detection; Geo-KTF › Output › GIS Files
- Definition: gdal_translate is a GDAL raster conversion utility. It changes format, bands, data type, and can write Cloud Optimized GeoTIFF efficiently. Expected output: a converted raster file.

### `gdal_viewshed`
- Source: GDAL
- Categories: Geo-KTF › Basic Geospatial Knowledge › Data Models › DEM; Geo-KTF › Basic Geospatial Knowledge › Spatial Analysis › Terrain Analysis; Geo-KTF › Workflow › Visibility Analysis
- Definition: gdal_viewshed is a GDAL visibility utility. It computes DEM viewsheds from observer points for siting and line-of-sight studies. Expected output: a visibility raster.

### `gdaladdo`
- Source: GDAL
- Categories: Geo-KTF › Basic Geospatial Knowledge › Relationship › Scale; Geo-KTF › Basic Geospatial Knowledge › Data Quality › Precision
- Definition: gdaladdo is a GDAL overview builder. It adds pyramid levels so rasters display faster at small scales without changing full resolution. Expected output: the raster file with internal/external overviews.

### `gdalbuildvrt`
- Source: GDAL
- Categories: Geo-KTF › Basic Geospatial Knowledge › Relationship › Scale; Geo-KTF › Basic Geospatial Knowledge › Data Models › Raster; Geo-KTF › Basic Geospatial Knowledge › Data Models › Temporal Data; Geo-KTF › Analytical Capabilities › Data Conversion; Geo-KTF › Analytical Capabilities › Raster Processing; Geo-KTF › Analytical Capabilities › Remote Sensing; Geo-KTF › Analytical Capabilities › Space-Time Analysis; Geo-KTF › Workflow › Change Detection; Geo-KTF › Workflow › Urban Growth Analysis; Geo-KTF › Output › GIS Files
- Definition: gdalbuildvrt is a GDAL virtual mosaic utility. It references many rasters as one virtual dataset without copying pixels, ideal for large mosaics or time stacks. Expected output: a .vrt virtual raster.

### `gdaldem aspect`
- Source: GDAL
- Categories: Geo-KTF › Basic Geospatial Knowledge › Data Models › DEM; Geo-KTF › Basic Geospatial Knowledge › Spatial Analysis › Terrain Analysis; Geo-KTF › Workflow › Hazard Assessment
- Definition: gdaldem aspect is a GDAL DEM derivative mode. It computes downhill-facing direction for solar, ecology, and snow applications. Expected output: an aspect raster (degrees).

### `gdaldem hillshade`
- Source: GDAL
- Categories: Geo-KTF › Basic Geospatial Knowledge › Data Models › DEM; Geo-KTF › Basic Geospatial Knowledge › Spatial Analysis › Terrain Analysis; Geo-KTF › Analytical Capabilities › Cartography; Geo-KTF › Workflow › Hazard Assessment
- Definition: gdaldem hillshade is a GDAL DEM visualisation mode. It creates shaded relief so terrain form is easy to read on maps. Expected output: a hillshade raster.

### `gdaldem roughness`
- Source: GDAL
- Categories: Geo-KTF › Basic Geospatial Knowledge › Data Models › DEM; Geo-KTF › Basic Geospatial Knowledge › Spatial Analysis › Terrain Analysis
- Definition: gdaldem roughness is a GDAL DEM morphometric mode. It measures local elevation irregularity for landform characterisation. Expected output: a roughness raster.

### `gdaldem slope`
- Source: GDAL
- Categories: Geo-KTF › Basic Geospatial Knowledge › Data Models › DEM; Geo-KTF › Basic Geospatial Knowledge › Spatial Analysis › Terrain Analysis; Geo-KTF › Workflow › Hazard Assessment
- Definition: gdaldem slope is a GDAL DEM derivative mode. It computes steepness in degrees or percent for hazard and engineering analyses. Expected output: a slope raster.

### `gdaldem TPI`
- Source: GDAL
- Categories: Geo-KTF › Basic Geospatial Knowledge › Data Models › DEM; Geo-KTF › Basic Geospatial Knowledge › Spatial Analysis › Terrain Analysis
- Definition: gdaldem TPI is a GDAL Topographic Position Index mode. It shows whether cells sit above or below their neighbourhood mean (ridges vs valleys). Expected output: a TPI raster.

### `gdaldem TRI`
- Source: GDAL
- Categories: Geo-KTF › Basic Geospatial Knowledge › Data Models › DEM; Geo-KTF › Basic Geospatial Knowledge › Spatial Analysis › Terrain Analysis
- Definition: gdaldem TRI is a GDAL Terrain Ruggedness Index mode. It summarises neighbourhood elevation variation as a ruggedness metric. Expected output: a TRI raster.

### `gdalinfo`
- Source: GDAL
- Categories: Geo-KTF › Basic Geospatial Knowledge › Data Models › Raster; Geo-KTF › Basic Geospatial Knowledge › Coordinate Reference Systems › Vertical CRS; Geo-KTF › Basic Geospatial Knowledge › Coordinate Reference Systems › Units; Geo-KTF › Basic Geospatial Knowledge › Data Quality › Metadata; Geo-KTF › Basic Geospatial Knowledge › Data Quality › Precision; Geo-KTF › Analytical Capabilities › Data Inspection; Geo-KTF › Validation › CRS Validation; Geo-KTF › Validation › Metadata Validation
- Definition: gdalinfo is a GDAL command-line utility. It prints raster metadata so you can verify size, CRS, bands, and nodata before processing. Expected output: a text report of dataset metadata.

### `gdalwarp`
- Source: GDAL
- Categories: Geo-KTF › Basic Geospatial Knowledge › Data Models › Raster; Geo-KTF › Basic Geospatial Knowledge › Coordinate Reference Systems › Geographic; Geo-KTF › Basic Geospatial Knowledge › Coordinate Reference Systems › Datums; Geo-KTF › Basic Geospatial Knowledge › Coordinate Reference Systems › Vertical CRS; Geo-KTF › Basic Geospatial Knowledge › Coordinate Reference Systems › Common CRS Errors; Geo-KTF › Basic Geospatial Knowledge › Spatial Analysis › Raster Analysis; Geo-KTF › Analytical Capabilities › Data Conversion; Geo-KTF › Analytical Capabilities › CRS Management; Geo-KTF › Analytical Capabilities › Raster Processing; Geo-KTF › Analytical Capabilities › Remote Sensing; Geo-KTF › Workflow › Change Detection; Geo-KTF › Workflow › Urban Growth Analysis; Geo-KTF › Validation › CRS Validation; Geo-KTF › Output › GIS Files
- Definition: gdalwarp is a GDAL warping utility. It reprojects, resamples, clips, and mosaics rasters so layers share a common grid/CRS. Expected output: a warped/mosaicked raster.

### `Generalize`
- Source: QGIS Processing
- Categories: Geo-KTF › Basic Geospatial Knowledge › Relationship › Scale; Geo-KTF › Basic Geospatial Knowledge › Data Quality › Precision
- Definition: Generalize is a QGIS/GRASS-style simplification tool exposed in Processing. It reduces shape detail while keeping recognisable form for small-scale maps. Expected output: generalised line/polygon geometries.

### `Generate points (pixel centroids) inside polygons`
- Source: QGIS Processing
- Categories: Geo-KTF › Basic Geospatial Knowledge › Relationship › Scale
- Definition: This QGIS Processing tool creates sample points from raster pixels inside polygons. It places a point at each pixel centroid that falls inside a polygon, aligning samples to an image grid. Expected output: a point layer of pixel centres.

### `geometry.is_valid (Shapely)`
- Source: Shapely
- Categories: Geo-KTF › Validation › Geometry Validation
- Definition: geometry.is_valid is a Shapely geometry property. It reports whether a geometry is topologically valid under GEOS rules before overlays or DB loads. Expected output: True/False (per geometry).

### `GeoNetwork`
- Source: OSGeo / GeoNetwork
- Categories: Geo-KTF › Basic Geospatial Knowledge › Data Quality › Standards; Geo-KTF › Provider Registry › SDI / Catalogs
- Definition: GeoNetwork is an OSGeo catalogue application. It publishes and searches ISO-style geospatial metadata as the discovery face of an SDI. Expected output: searchable catalogue records linking to data/services.

### `GeoPandas`
- Source: Python geospatial stack
- Categories: Geo-KTF › Provider Registry › Geospatial Libraries
- Definition: GeoPandas is a Python library that adds a geometry column to pandas. It makes vector GIS operations feel like dataframe analysis with overlays, joins, and CRS tools. Expected output: GeoDataFrames and exported GIS files/tables.

### `geopandas.overlay()`
- Source: GeoPandas
- Categories: Geo-KTF › Basic Geospatial Knowledge › Relationship › Overlay
- Definition: geopandas.overlay() is a GeoPandas overlay API. It runs intersection/union/difference/identity/symmetric_difference between polygon layers in Python. Expected output: an overlaid GeoDataFrame.

### `geopandas.read_file()`
- Source: GeoPandas
- Categories: Geo-KTF › Basic Geospatial Knowledge › Data Models › Vector; Geo-KTF › Basic Geospatial Knowledge › Data Models › Temporal Data; Geo-KTF › Basic Geospatial Knowledge › Data Quality › Metadata; Geo-KTF › Analytical Capabilities › Data Inspection; Geo-KTF › Validation › Metadata Validation; Geo-KTF › Validation › Schema Validation
- Definition: geopandas.read_file() is a GeoPandas I/O function. It loads vector files (GeoPackage, Shapefile, GeoJSON, …) into a GeoDataFrame via OGR. Expected output: a GeoDataFrame in memory.

### `geopandas.read_postgis()`
- Source: GeoPandas
- Categories: Geo-KTF › Basic Geospatial Knowledge › Data Models › Vector; Geo-KTF › Analytical Capabilities › Data Inspection; Geo-KTF › Analytical Capabilities › Database Processing; Geo-KTF › Validation › Schema Validation
- Definition: geopandas.read_postgis() is a GeoPandas database reader. It runs SQL against PostGIS and returns geometries as a GeoDataFrame for Python analysis. Expected output: a GeoDataFrame from the query.

### `geopandas.set_crs()`
- Source: GeoPandas
- Categories: Geo-KTF › Basic Geospatial Knowledge › Coordinate Reference Systems › Common CRS Errors; Geo-KTF › Analytical Capabilities › CRS Management; Geo-KTF › Validation › CRS Validation
- Definition: geopandas.set_crs() is a GeoPandas CRS tagging method. It assigns CRS metadata without transforming coordinates when the tag was missing. Expected output: the same coordinates with CRS set.

### `geopandas.sjoin()`
- Source: GeoPandas
- Categories: Geo-KTF › Basic Geospatial Knowledge › Relationship › Containment; Geo-KTF › Basic Geospatial Knowledge › Data Models › Hex Grid; Geo-KTF › Workflow › Demographic Enrichment
- Definition: geopandas.sjoin() is a GeoPandas spatial join. It joins two GeoDataFrames by predicates such as intersects or within to transfer attributes by location. Expected output: a joined GeoDataFrame.

### `geopandas.sjoin_nearest()`
- Source: GeoPandas
- Categories: Geo-KTF › Basic Geospatial Knowledge › Relationship › Distance; Geo-KTF › Workflow › Demographic Enrichment
- Definition: geopandas.sjoin_nearest() is a GeoPandas nearest join. It matches each geometry to the closest feature in another frame, optionally with a max distance. Expected output: a GeoDataFrame with nearest attributes/distance.

### `geopandas.to_crs()`
- Source: GeoPandas
- Categories: Geo-KTF › Basic Geospatial Knowledge › Coordinate Reference Systems › Geographic; Geo-KTF › Basic Geospatial Knowledge › Coordinate Reference Systems › Units; Geo-KTF › Basic Geospatial Knowledge › Coordinate Reference Systems › Common CRS Errors; Geo-KTF › Analytical Capabilities › CRS Management; Geo-KTF › Validation › CRS Validation
- Definition: geopandas.to_crs() is a GeoPandas reprojection method. It transforms geometries to a target CRS so distance/area work is valid. Expected output: a reprojected GeoDataFrame.

### `geopandas.to_file()`
- Source: GeoPandas
- Categories: Geo-KTF › Basic Geospatial Knowledge › Data Models › Vector; Geo-KTF › Analytical Capabilities › Data Conversion; Geo-KTF › Output › Tables; Geo-KTF › Output › GIS Files
- Definition: geopandas.to_file() is a GeoPandas writer. It exports a GeoDataFrame to common vector formats through OGR. Expected output: a GIS file on disk.

### `geopandas.to_parquet()`
- Source: GeoPandas
- Categories: Geo-KTF › Basic Geospatial Knowledge › Data Models › Vector; Geo-KTF › Analytical Capabilities › Data Conversion; Geo-KTF › Output › Tables; Geo-KTF › Output › GIS Files
- Definition: geopandas.to_parquet() is a GeoPandas writer for GeoParquet. It stores vectors in columnar Parquet with geometry/CRS metadata for analytics and cloud use. Expected output: a GeoParquet file.

### `geopandas.to_postgis()`
- Source: GeoPandas
- Categories: Geo-KTF › Basic Geospatial Knowledge › Data Models › Vector; Geo-KTF › Analytical Capabilities › Data Conversion; Geo-KTF › Analytical Capabilities › Database Processing; Geo-KTF › Output › Tables
- Definition: geopandas.to_postgis() is a GeoPandas database writer. It loads a GeoDataFrame into a PostGIS table over SQLAlchemy. Expected output: a PostGIS table.

### `GeoParquet`
- Source: Open geospatial format
- Categories: Geo-KTF › Basic Geospatial Knowledge › Data Models › Temporal Data; Geo-KTF › Basic Geospatial Knowledge › Data Models › Array Database; Geo-KTF › Analytical Capabilities › Space-Time Analysis; Geo-KTF › Provider Registry › Cloud
- Definition: GeoParquet is a Parquet-based vector format with geometry/CRS metadata. It supports fast columnar analytics and cloud data-lake workflows for features. Expected output: GeoParquet files queryable by analytics engines.

### `Georeferencer`
- Source: QGIS
- Categories: Geo-KTF › Analytical Capabilities › Data Acquisition
- Definition: Georeferencer is a QGIS tool for registering images to a map CRS. It uses ground control points and a chosen transformation so scanned maps or unreferenced imagery align to real coordinates. Expected output: a georeferenced raster (with GCPs/world file) plus residual diagnostics.

### `GeoServer`
- Source: OSGeo
- Categories: Geo-KTF › Output › Dashboards; Geo-KTF › Output › APIs; Geo-KTF › Provider Registry › Web Mapping
- Definition: GeoServer is an OSGeo Java map server. It publishes PostGIS/files as WMS/WMTS/WFS/WCS for interoperable web access. Expected output: OGC web services and rendered map images/features.

### `GeoSPARQL`
- Source: OGC
- Categories: Geo-KTF › Basic Geospatial Knowledge › Data Models › Knowledge Graph
- Definition: GeoSPARQL is an OGC standard extending SPARQL/RDF with geometry and spatial filters. It enables semantic queries that also use intersects/within-style tests. Expected output: SPARQL result sets over spatial RDF data.

### `Google Colab`
- Source: Google
- Categories: Geo-KTF › Provider Registry › Notebooks
- Definition: Google Colab is Google’s browser-hosted Jupyter environment. It provides free/paid runtimes (optional GPU) for teaching and prototyping geospatial Python. Expected output: executed notebooks and saved artifacts (e.g., to Drive).

### `Google Earth Engine`
- Source: Google
- Categories: Geo-KTF › Provider Registry › Cloud
- Definition: Google Earth Engine is Google’s planetary EO cloud platform. It runs parallel JS/Python analysis on a huge imagery catalogue without hosting the archive locally. Expected output: computed images/tables exported to Drive/Cloud Storage.

### `Google Geocoding API`
- Source: Google Maps Platform
- Categories: Geo-KTF › Analytical Capabilities › Geocoding; Geo-KTF › Output › APIs
- Definition: Google Geocoding API is Google’s address geocoding web service. It converts addresses to coordinates and reverse-geocodes points under Google’s key and terms. Expected output: JSON geocoding results with locations.

### `Google Maps`
- Source: Google Maps Platform
- Categories: Geo-KTF › Provider Registry › Basemap
- Definition: Google Maps is Google’s mapping platform. It provides basemap tiles and related location APIs under Google keys/quotas. Expected output: map tiles and API location responses.

### `Government Open Data APIs`
- Source: Public agencies
- Categories: Geo-KTF › Provider Registry › Basemap
- Definition: Government Open Data APIs are public-sector catalogue/API endpoints (CKAN, ArcGIS Hub, OGC API, etc.). They publish authoritative boundaries and thematic open data for reuse. Expected output: downloadable datasets or API feature responses.

### `GPSBabel`
- Source: GPSBabel project
- Categories: Geo-KTF › Analytical Capabilities › Data Acquisition
- Definition: GPSBabel is an open GNSS format converter. It converts waypoints/tracks/routes among many device and GIS formats and can filter tracks. Expected output: converted GPS files (e.g., GPX/KML).

### `graduated renderer`
- Source: QGIS
- Categories: Geo-KTF › Analytical Capabilities › Cartography
- Definition: A graduated renderer is a QGIS thematic mapping mode. It classifies a numeric field into ranges and colours (or sizes) each class for choropleth-style maps. Expected output: a classified thematic map appearance with a legend.

### `HDBSCAN`
- Source: hdbscan / scikit-learn-contrib
- Categories: Geo-KTF › Analytical Capabilities › Clustering
- Definition: HDBSCAN is a hierarchical density-clustering library/algorithm. It finds stable clusters without fixing K and can label noise when density varies. Expected output: cluster labels (and probabilities/noise flags).

### `Heatmap (Kernel Density Estimation)`
- Source: QGIS / spatial stats
- Categories: Geo-KTF › Analytical Capabilities › Spatial Statistics; Geo-KTF › Analytical Capabilities › Point Pattern Analysis; Geo-KTF › Workflow › Urban Growth Analysis
- Definition: Heatmap (KDE) is a QGIS Processing density tool. It turns points into a smooth density raster so event intensity is easy to see (it does not assign cluster IDs). Expected output: a continuous density raster.

### `iD Editor`
- Source: OpenStreetMap / Mapbox
- Categories: Geo-KTF › Analytical Capabilities › Data Acquisition
- Definition: iD Editor is the default browser editor for OpenStreetMap. It lets contributors draw and tag features quickly with imagery backgrounds. Expected output: OSM changesets uploaded to the OSM database.

### `IDW Interpolation`
- Source: QGIS Processing
- Categories: Geo-KTF › Analytical Capabilities › Spatial Interpolation
- Definition: IDW Interpolation is a QGIS Processing interpolator (also common elsewhere). It predicts unsampled values as a distance-weighted average of nearby points—fast and simple, without kriging variance. Expected output: a continuous interpolated raster surface.

### `Intersection`
- Source: QGIS / ArcGIS Processing
- Categories: Geo-KTF › Basic Geospatial Knowledge › Relationship › Overlay; Geo-KTF › Basic Geospatial Knowledge › Spatial Analysis › Vector Analysis; Geo-KTF › Analytical Capabilities › Vector Processing; Geo-KTF › Workflow › Site Selection; Geo-KTF › Workflow › Hazard Assessment; Geo-KTF › Workflow › Environmental Assessment; Geo-KTF › Workflow › Urban Growth Analysis
- Definition: Intersection is a classic overlay operation in desktop GIS toolboxes. It keeps only the geometric overlap between two layers and combines attributes from both, answering where A and B coincide. Expected output: a new layer of overlapping pieces with joined attributes.

### `ISO 19115`
- Source: ISO / TC 211
- Categories: Geo-KTF › Basic Geospatial Knowledge › Data Quality › Standards
- Definition: ISO 19115 is an ISO/TC 211 metadata standard for geographic information. It defines how to describe datasets/services (title, extent, CRS, lineage, constraints) for discovery. Expected output: standards-compliant metadata records (often ISO 19139 XML).

### `JavaScript for GIS`
- Source: Web GIS languages
- Categories: Geo-KTF › Provider Registry › Development
- Definition: JavaScript for GIS refers to web-mapping languages/libraries (Leaflet, MapLibre, OpenLayers). It builds interactive browser maps and custom map UIs outside desktop GIS. Expected output: web map applications in the browser.

### `Join attributes by location`
- Source: QGIS Processing
- Categories: Geo-KTF › Basic Geospatial Knowledge › Data Models › Hex Grid; Geo-KTF › Workflow › Demographic Enrichment
- Definition: Join attributes by location is a QGIS Processing spatial join. It appends attributes from another layer based on a spatial relationship such as intersects or within. Expected output: an attribute-enriched layer (one-to-one or one-to-many depending on settings).

### `Join attributes by nearest`
- Source: QGIS Processing
- Categories: Geo-KTF › Basic Geospatial Knowledge › Relationship › Distance; Geo-KTF › Basic Geospatial Knowledge › Spatial Analysis › Vector Analysis; Geo-KTF › Analytical Capabilities › Vector Processing; Geo-KTF › Workflow › Demographic Enrichment
- Definition: Join attributes by nearest is a QGIS Processing spatial join. It copies attributes from the closest feature in another layer and can record distance, without needing overlap. Expected output: the input layer enriched with nearest-neighbour fields (and optional distance).

### `JOSM`
- Source: OpenStreetMap
- Categories: Geo-KTF › Analytical Capabilities › Data Acquisition
- Definition: JOSM is a desktop Java OpenStreetMap editor. It supports advanced validation, presets, and bulk edits beyond the browser iD editor. Expected output: OSM changesets uploaded via the OSM API.

### `Jupyter Notebook`
- Source: Project Jupyter
- Categories: Geo-KTF › Provider Registry › Notebooks
- Definition: Jupyter Notebook (JupyterLab) is Project Jupyter’s literate computing interface. It mixes code, narrative, and figures for reproducible geospatial analysis. Expected output: .ipynb notebooks and exported HTML/Markdown reports.

### `K-means clustering`
- Source: scikit-learn / QGIS
- Categories: Geo-KTF › Analytical Capabilities › Clustering
- Definition: K-means clustering is a QGIS Processing partitioning tool. It assigns features to a fixed number of groups by similarity when you already know how many clusters you want. Expected output: features labelled with cluster IDs 0…K-1.

### `Leaflet`
- Source: Leaflet.js
- Categories: Geo-KTF › Output › Dashboards; Geo-KTF › Provider Registry › Web Mapping
- Definition: Leaflet is a lightweight open-source JavaScript map library. It makes interactive tiled maps with markers and GeoJSON with a small API and many plugins. Expected output: an interactive web map in the browser.

### `libpysal.weights`
- Source: PySAL
- Categories: Geo-KTF › Analytical Capabilities › Spatial Statistics; Geo-KTF › Analytical Capabilities › Spatial Regression; Geo-KTF › Validation › Statistical Validation
- Definition: libpysal.weights is a PySAL module for spatial weights. It defines neighbour relationships (contiguity, distance, knn) required by most spatial stats and regressions. Expected output: a spatial weights object/matrix.

### `Line intersections`
- Source: QGIS Processing
- Categories: Geo-KTF › Basic Geospatial Knowledge › Relationship › Overlay; Geo-KTF › Basic Geospatial Knowledge › Relationship › Adjacency; Geo-KTF › Basic Geospatial Knowledge › Spatial Analysis › Vector Analysis
- Definition: Line intersections is a QGIS Processing tool. It creates points where lines from two layers cross, useful for junctions and conflict detection. Expected output: a point layer at crossing locations.

### `MapLibre GL JS`
- Source: MapLibre
- Categories: Geo-KTF › Output › Story Maps; Geo-KTF › Output › Dashboards; Geo-KTF › Provider Registry › Web Mapping
- Definition: MapLibre GL JS is an open-source WebGL vector-tile map library. It renders smooth, style-driven interactive maps from vector tiles and GeoJSON. Expected output: an interactive styled web map.

### `Merge Vector Layers`
- Source: QGIS Processing
- Categories: Geo-KTF › Analytical Capabilities › Vector Processing
- Definition: Merge Vector Layers is a QGIS Processing tool. It stacks multiple layers of the same geometry type into one dataset for combined analysis. Expected output: a single vector layer (schema differences may introduce nulls).

### `mesa`
- Source: Project Mesa
- Categories: Geo-KTF › Analytical Capabilities › Geocomputation
- Definition: mesa is a Python framework for agent-based modelling (Project Mesa). It lets agents interact on grids or continuous spaces under scheduled rules to simulate spatial processes. Expected output: simulation runs with agent/grid states, often viewed in a browser dashboard.

### `Mesh Calculator`
- Source: QGIS Mesh tools
- Categories: Geo-KTF › Basic Geospatial Knowledge › Data Models › Mesh; Geo-KTF › Basic Geospatial Knowledge › Data Models › 3D
- Definition: Mesh Calculator is a QGIS mesh analysis tool. It evaluates expressions on mesh datasets to derive new quantities for visualisation or export. Expected output: computed mesh dataset values.

### `mgwr.GWR`
- Source: PySAL mgwr
- Categories: Geo-KTF › Analytical Capabilities › Spatial Regression
- Definition: mgwr.GWR is Geographically Weighted Regression in the PySAL mgwr package. It fits local regressions whose coefficients vary across space to reveal non-stationarity. Expected output: local coefficient surfaces and local fit diagnostics.

### `Microsoft Planetary Computer`
- Source: Microsoft
- Categories: Geo-KTF › Provider Registry › SDI / Catalogs; Geo-KTF › Provider Registry › Basemap
- Definition: Microsoft Planetary Computer is Microsoft’s planetary EO data platform. It exposes large public imagery archives through STAC-style access for scalable analysis. Expected output: discoverable assets and analysis-ready data access.

### `Monte Carlo simulation`
- Source: Uncertainty / simulation method
- Categories: Geo-KTF › Basic Geospatial Knowledge › Data Quality › Uncertainty Modeling
- Definition: Monte Carlo simulation is an uncertainty method used in GIS workflows (not one single vendor button). It reruns a model many times with random input variation to show a range of outcomes instead of one brittle map. Expected output: an ensemble of results and summary statistics/confidence surfaces.

### `MovingPandas`
- Source: MovingPandas / PySAL ecosystem
- Categories: Geo-KTF › Analytical Capabilities › Space-Time Analysis; Geo-KTF › Analytical Capabilities › Trajectory Analysis
- Definition: MovingPandas is a Python trajectory library in the PySAL ecosystem. It analyses GPS tracks with splitting, generalisation, speed, stops, and path metrics on GeoPandas. Expected output: trajectory objects, derived attributes, and plots/exports.

### `Multilevel B-Spline Interpolation`
- Source: QGIS / SAGA
- Categories: Geo-KTF › Analytical Capabilities › Spatial Interpolation
- Definition: Multilevel B-Spline Interpolation is a SAGA algorithm available in QGIS Processing. It fits a hierarchy of smooth B-spline surfaces to scattered points, often smoother than IDW. Expected output: a smooth interpolated raster grid.

### `Multipart to Singleparts`
- Source: QGIS Processing
- Categories: Geo-KTF › Analytical Capabilities › Vector Processing
- Definition: Multipart to Singleparts is a QGIS Processing tool. It splits multipart geometries into separate single-part features when each part must be handled alone. Expected output: a layer with one feature per part.

### `Natural Earth`
- Source: Natural Earth
- Categories: Geo-KTF › Provider Registry › Basemap
- Definition: Natural Earth is a public-domain cartographic dataset collection. It provides clean cultural/physical layers at multiple scales for atlas-style basemaps. Expected output: ready-to-use vector/raster basemap layers.

### `NetLogo`
- Source: Northwestern University / CCL
- Categories: Geo-KTF › Analytical Capabilities › Geocomputation
- Definition: NetLogo is a widely taught agent-based modelling environment from Northwestern’s CCL. It uses a simple language and visual world so agents and patches follow rules you write, optionally linked to GIS data. Expected output: simulated spatial scenarios and plots/exports from the model world.

### `Nominatim`
- Source: OpenStreetMap / OSMF
- Categories: Geo-KTF › Analytical Capabilities › Geocoding; Geo-KTF › Output › APIs
- Definition: Nominatim is the OpenStreetMap search/geocoding service. It converts place names/addresses to coordinates and reverse-geocodes points (respect usage policy for bulk jobs). Expected output: geocoding result places with coordinates.

### `OD Matrix from Layers as Lines (m:n)`
- Source: QGIS Processing
- Categories: Geo-KTF › Analytical Capabilities › Location-Allocation
- Definition: OD Matrix from Layers as Lines (m:n) is a QGIS Processing tool. It draws straight lines from every origin to every destination as a simple OD geometry scaffold. Expected output: a line layer of origin–destination links (Euclidean, not network paths).

### `ODK Collect`
- Source: ODK / Get ODK
- Categories: Geo-KTF › Analytical Capabilities › Data Acquisition
- Definition: ODK Collect is an Android form-based survey app (ODK). It captures GPS, photos, and structured answers with skip logic for field campaigns. Expected output: submitted survey records (often geotagged tables).

### `ogr2ogr`
- Source: GDAL/OGR
- Categories: Geo-KTF › Basic Geospatial Knowledge › Data Models › Vector; Geo-KTF › Basic Geospatial Knowledge › Data Models › Temporal Data; Geo-KTF › Analytical Capabilities › Data Conversion; Geo-KTF › Output › Tables; Geo-KTF › Output › GIS Files
- Definition: ogr2ogr is the main GDAL/OGR vector conversion utility. It converts formats and can reproject, clip, and SQL-filter during ETL between systems. Expected output: a new vector file or database layer.

### `ogrinfo`
- Source: GDAL/OGR
- Categories: Geo-KTF › Basic Geospatial Knowledge › Data Models › Vector; Geo-KTF › Basic Geospatial Knowledge › Coordinate Reference Systems › Vertical CRS; Geo-KTF › Basic Geospatial Knowledge › Coordinate Reference Systems › Units; Geo-KTF › Basic Geospatial Knowledge › Data Quality › Metadata; Geo-KTF › Analytical Capabilities › Data Inspection; Geo-KTF › Validation › CRS Validation; Geo-KTF › Validation › Metadata Validation; Geo-KTF › Validation › Schema Validation
- Definition: ogrinfo is a GDAL/OGR command-line utility. It prints vector dataset layers, CRS, schema, and feature counts without modifying files. Expected output: a text report of vector metadata.

### `OpenDroneMap`
- Source: OpenDroneMap
- Categories: Geo-KTF › Analytical Capabilities › Data Acquisition; Geo-KTF › Analytical Capabilities › Remote Sensing
- Definition: OpenDroneMap is an open photogrammetry pipeline. It turns overlapping drone/aerial photos into orthomosaics, point clouds, DEMs, and meshes. Expected output: orthophoto, point cloud, DEM/DSM, and related products.

### `OpenLayers`
- Source: OSGeo
- Categories: Geo-KTF › Output › Dashboards; Geo-KTF › Provider Registry › Web Mapping
- Definition: OpenLayers is a full-featured open-source JavaScript mapping library. It supports many OGC services and on-the-fly reprojection for standards-heavy apps. Expected output: an interactive web map with rich layer types.

### `openrouteservice`
- Source: HeiGIT / openrouteservice
- Categories: Geo-KTF › Output › APIs; Geo-KTF › Provider Registry › Geospatial Libraries
- Definition: openrouteservice is an open routing/location API stack (HeiGIT) on OpenStreetMap. It provides directions, isochrones, matrices, and geocoding via HTTP for apps that need OSM-based mobility. Expected output: JSON routing/accessibility/geocoding responses.

### `openrouteservice directions`
- Source: openrouteservice
- Categories: Geo-KTF › Basic Geospatial Knowledge › Relationship › Connectivity; Geo-KTF › Basic Geospatial Knowledge › Data Models › Trajectory; Geo-KTF › Basic Geospatial Knowledge › Spatial Analysis › Network Analysis; Geo-KTF › Analytical Capabilities › Routing; Geo-KTF › Analytical Capabilities › Space-Time Analysis; Geo-KTF › Analytical Capabilities › Trajectory Analysis; Geo-KTF › Workflow › Infrastructure Planning
- Definition: openrouteservice directions is an ORS routing endpoint. It returns paths for travel profiles such as driving or walking with distance and duration. Expected output: route geometry plus travel metrics.

### `openrouteservice geocoding`
- Source: openrouteservice
- Categories: Geo-KTF › Analytical Capabilities › Geocoding
- Definition: openrouteservice geocoding is an ORS place-search endpoint (Pelias). It turns text into coordinates and reverse-geocodes points to addresses. Expected output: ranked geocoding candidate features.

### `openrouteservice isochrones`
- Source: openrouteservice
- Categories: Geo-KTF › Analytical Capabilities › Accessibility; Geo-KTF › Workflow › Catchment Analysis; Geo-KTF › Workflow › Accessibility Analysis
- Definition: openrouteservice isochrones is an ORS accessibility endpoint. It builds reachability polygons for time or distance limits around locations. Expected output: isochrone polygons (GeoJSON).

### `openrouteservice matrices`
- Source: openrouteservice
- Categories: Geo-KTF › Analytical Capabilities › Accessibility; Geo-KTF › Workflow › Accessibility Analysis
- Definition: openrouteservice matrices is an ORS travel-matrix endpoint. It returns duration/distance between many origins and destinations for location models. Expected output: a travel cost matrix.

### `OpenStreetMap`
- Source: OpenStreetMap community
- Categories: Geo-KTF › Provider Registry › Basemap
- Definition: OpenStreetMap is a collaborative world map database and community project. It provides open basemap data feeding routing, geocoding, and thematic extracts. Expected output: map data/tiles and downloadable OSM extracts.

### `ortools.routing`
- Source: Google OR-Tools
- Categories: Geo-KTF › Analytical Capabilities › Location-Allocation
- Definition: ortools.routing is Google OR-Tools’ vehicle routing solver API. It optimises tours and assignments with capacities and time windows using a cost matrix from GIS. Expected output: optimised routes/assignments and objective costs.

### `OSRM`
- Source: Project OSRM
- Categories: Geo-KTF › Output › APIs; Geo-KTF › Provider Registry › Geospatial Libraries
- Definition: OSRM (Open Source Routing Machine) is a high-speed OSM routing engine. It powers custom routing services when you need very fast directions on self-hosted data. Expected output: route geometries and travel times via its API.

### `OTB (Orfeo ToolBox)`
- Source: CNES / Orfeo
- Categories: Geo-KTF › Provider Registry › Geospatial Libraries
- Definition: OTB (Orfeo ToolBox) is an open remote-sensing toolbox (CNES/OSGeo). It provides applications for preprocessing, classification, and accuracy assessment of EO imagery. Expected output: processed images, class maps, and metric reports.

### `OTB BandMath`
- Source: Orfeo ToolBox
- Categories: Geo-KTF › Analytical Capabilities › Remote Sensing; Geo-KTF › Workflow › Change Detection; Geo-KTF › Workflow › Remote Sensing Classification; Geo-KTF › Workflow › Urban Growth Analysis
- Definition: OTB BandMath is an Orfeo ToolBox application. It applies per-pixel math across bands for indices and thresholds in RS pipelines. Expected output: a computed image band/file.

### `OTB ComputeConfusionMatrix`
- Source: Orfeo ToolBox
- Categories: Geo-KTF › Analytical Capabilities › Remote Sensing; Geo-KTF › Validation › Accuracy Assessment
- Definition: OTB ComputeConfusionMatrix is an Orfeo ToolBox accuracy app. It compares a classified map with reference labels and reports confusion-matrix metrics. Expected output: a confusion matrix CSV plus precision/recall/F-score measures.

### `OTB ComputeImagesStatistics`
- Source: Orfeo ToolBox
- Categories: Geo-KTF › Analytical Capabilities › Remote Sensing; Geo-KTF › Workflow › Remote Sensing Classification
- Definition: OTB ComputeImagesStatistics is an Orfeo ToolBox application. It computes band statistics used to normalise or prepare imagery for classification. Expected output: image statistics files/reports.

### `OTB KMeansClassification`
- Source: Orfeo ToolBox
- Categories: Geo-KTF › Analytical Capabilities › Remote Sensing; Geo-KTF › Workflow › Remote Sensing Classification
- Definition: OTB KMeansClassification is an Orfeo ToolBox unsupervised classifier. It groups pixels into spectral clusters without training labels (clusters still need interpretation). Expected output: a clustered classification image.

### `OTB TrainImagesClassifier`
- Source: Orfeo ToolBox
- Categories: Geo-KTF › Analytical Capabilities › Remote Sensing; Geo-KTF › Workflow › Remote Sensing Classification
- Definition: OTB TrainImagesClassifier is an Orfeo ToolBox supervised classification app. It trains classifiers (e.g., RF/SVM) from imagery and labelled samples then classifies pixels. Expected output: a trained model and/or classified image.

### `Overture Maps`
- Source: Overture Maps Foundation
- Categories: Geo-KTF › Provider Registry › Basemap
- Definition: Overture Maps is an open map data project. It releases globally consistent themes (buildings, places, transportation, …) for modern basemaps. Expected output: downloadable open map theme datasets.

### `PDAL`
- Source: PDAL project
- Categories: Geo-KTF › Provider Registry › Geospatial Libraries
- Definition: PDAL is the Point Data Abstraction Library. It processes LiDAR and other point clouds through JSON pipelines of readers, filters, and writers. Expected output: filtered clouds and derived products (LAS/LAZ/rasters).

### `PDAL pipeline`
- Source: PDAL
- Categories: Geo-KTF › Basic Geospatial Knowledge › Data Models › Point Cloud; Geo-KTF › Analytical Capabilities › Data Inspection; Geo-KTF › Analytical Capabilities › Remote Sensing
- Definition: PDAL pipeline is PDAL’s JSON workflow (and CLI runner). It chains read → filter → write stages for reproducible point-cloud processing. Expected output: written point-cloud or raster products from the pipeline.

### `pgr_aStar`
- Source: pgRouting
- Categories: Geo-KTF › Basic Geospatial Knowledge › Relationship › Connectivity; Geo-KTF › Basic Geospatial Knowledge › Data Models › Network; Geo-KTF › Basic Geospatial Knowledge › Data Models › Trajectory; Geo-KTF › Basic Geospatial Knowledge › Spatial Analysis › Network Analysis; Geo-KTF › Analytical Capabilities › Routing; Geo-KTF › Analytical Capabilities › Trajectory Analysis
- Definition: pgr_aStar is a pgRouting shortest-path function. It finds least-cost paths with a geometric heuristic that usually explores fewer nodes than plain Dijkstra. Expected output: a least-cost path result set.

### `pgr_dijkstra`
- Source: pgRouting
- Categories: Geo-KTF › Basic Geospatial Knowledge › Relationship › Connectivity; Geo-KTF › Basic Geospatial Knowledge › Data Models › Network; Geo-KTF › Basic Geospatial Knowledge › Data Models › Trajectory; Geo-KTF › Basic Geospatial Knowledge › Spatial Analysis › Network Analysis; Geo-KTF › Analytical Capabilities › Routing; Geo-KTF › Analytical Capabilities › Trajectory Analysis; Geo-KTF › Workflow › Infrastructure Planning
- Definition: pgr_dijkstra is a pgRouting shortest-path function. It finds least-cost routes on a network using Dijkstra, supporting one-to-one and many variants. Expected output: ordered path rows with node/edge/cost/aggregate cost.

### `pgr_dijkstraCostMatrix`
- Source: pgRouting
- Categories: Geo-KTF › Basic Geospatial Knowledge › Data Models › Network; Geo-KTF › Basic Geospatial Knowledge › Spatial Analysis › Network Analysis
- Definition: pgr_dijkstraCostMatrix is a pgRouting cost-matrix function. It computes least-cost travel between many vertex pairs without returning full geometries. Expected output: a cost matrix table.

### `pgr_dijkstraNear`
- Source: pgRouting
- Categories: Geo-KTF › Basic Geospatial Knowledge › Data Models › Network
- Definition: pgr_dijkstraNear is a pgRouting nearest-destination function. It finds the path to the cheapest destination among candidates (nearest facility on the network). Expected output: path rows to the nearest target.

### `pgr_dijkstraNearCost`
- Source: pgRouting
- Categories: Geo-KTF › Basic Geospatial Knowledge › Data Models › Network
- Definition: pgr_dijkstraNearCost is a pgRouting nearest-cost function. It returns only the cost to the nearest destination when you need scores rather than mapped paths. Expected output: nearest-destination cost values.

### `pgr_dijkstraVia`
- Source: pgRouting
- Categories: Geo-KTF › Basic Geospatial Knowledge › Data Models › Network; Geo-KTF › Basic Geospatial Knowledge › Data Models › Trajectory; Geo-KTF › Basic Geospatial Knowledge › Spatial Analysis › Network Analysis; Geo-KTF › Analytical Capabilities › Trajectory Analysis
- Definition: pgr_dijkstraVia is a pgRouting via-route function. It chains Dijkstra legs through an ordered list of stops for fixed itineraries. Expected output: a concatenated path across waypoints.

### `pgr_drivingDistance`
- Source: pgRouting
- Categories: Geo-KTF › Basic Geospatial Knowledge › Relationship › Connectivity; Geo-KTF › Basic Geospatial Knowledge › Data Models › Network; Geo-KTF › Basic Geospatial Knowledge › Spatial Analysis › Network Analysis; Geo-KTF › Analytical Capabilities › Accessibility; Geo-KTF › Workflow › Catchment Analysis; Geo-KTF › Workflow › Accessibility Analysis
- Definition: pgr_drivingDistance is a pgRouting catchment function. It finds all nodes reachable within a cost limit from start vertices for service-area style questions. Expected output: reachable nodes with aggregate costs.

### `pgr_KSP`
- Source: pgRouting
- Categories: Geo-KTF › Basic Geospatial Knowledge › Relationship › Connectivity; Geo-KTF › Basic Geospatial Knowledge › Data Models › Network; Geo-KTF › Basic Geospatial Knowledge › Spatial Analysis › Network Analysis; Geo-KTF › Analytical Capabilities › Routing
- Definition: pgr_KSP is a pgRouting K-shortest-path function (Yen). It returns several alternative routes ordered by cost when backups are needed. Expected output: K alternative path result sets.

### `pgRouting`
- Source: pgRouting project
- Categories: Geo-KTF › Provider Registry › Geospatial Libraries
- Definition: pgRouting is a PostgreSQL/PostGIS network analysis extension. It runs shortest path, driving distance, and related graph algorithms on edge tables. Expected output: path/cost result tables.

### `pointpats.centrography`
- Source: PySAL pointpats
- Categories: Geo-KTF › Analytical Capabilities › Point Pattern Analysis
- Definition: pointpats.centrography is a PySAL pointpats summary module. It computes mean/median centres, standard distance, and standard deviational ellipses for point sets. Expected output: centrography statistics and optional ellipse geometry.

### `pointpats.PointPattern`
- Source: PySAL pointpats
- Categories: Geo-KTF › Analytical Capabilities › Point Pattern Analysis
- Definition: pointpats.PointPattern is a PySAL pointpats data structure. It stores event coordinates for intensity and distance-based point pattern analysis. Expected output: a PointPattern object for further summaries/tests.

### `PostGIS`
- Source: PostGIS / OSGeo
- Categories: Geo-KTF › Basic Geospatial Knowledge › Data Models › Spatial Indexing; Geo-KTF › Output › APIs; Geo-KTF › Provider Registry › Geospatial Libraries
- Definition: PostGIS is the spatial extension for PostgreSQL (OSGeo). It adds geometry/geography types, spatial indexes, and hundreds of ST_ functions for storage and analysis. Expected output: spatial tables and query result sets.

### `projinfo`
- Source: PROJ
- Categories: Geo-KTF › Basic Geospatial Knowledge › Coordinate Reference Systems › Geographic; Geo-KTF › Basic Geospatial Knowledge › Coordinate Reference Systems › Datums; Geo-KTF › Basic Geospatial Knowledge › Coordinate Reference Systems › Vertical CRS; Geo-KTF › Basic Geospatial Knowledge › Coordinate Reference Systems › Units; Geo-KTF › Basic Geospatial Knowledge › Coordinate Reference Systems › Common CRS Errors; Geo-KTF › Analytical Capabilities › CRS Management; Geo-KTF › Validation › CRS Validation
- Definition: projinfo is a PROJ command-line inspection tool. It prints CRS and coordinate-operation details to verify EPSG codes and transform paths. Expected output: a text report of CRS/operation info.

### `pygeometa`
- Source: Geopython / pygeometa
- Categories: Geo-KTF › Basic Geospatial Knowledge › Data Quality › Standards
- Definition: pygeometa is a Geopython metadata generator. It creates standards-based metadata (e.g., ISO 19139) from simple YAML/dict records. Expected output: metadata XML/records for catalogues.

### `PyKrige`
- Source: Python
- Categories: Geo-KTF › Analytical Capabilities › Spatial Interpolation
- Definition: PyKrige is a Python kriging library. It performs geostatistical interpolation with variogram modelling and uncertainty estimates beyond simple IDW. Expected output: interpolated surfaces plus variance/uncertainty grids.

### `PyProj`
- Source: Python (pyproj)
- Categories: Geo-KTF › Provider Registry › Geospatial Libraries
- Definition: PyProj is the Python interface to PROJ. It defines CRSs and transforms coordinates accurately across datums. Expected output: CRS objects and transformed coordinates.

### `pyproj.CRS`
- Source: PyProj
- Categories: Geo-KTF › Basic Geospatial Knowledge › Coordinate Reference Systems › Geographic; Geo-KTF › Basic Geospatial Knowledge › Coordinate Reference Systems › Datums; Geo-KTF › Basic Geospatial Knowledge › Coordinate Reference Systems › Vertical CRS; Geo-KTF › Basic Geospatial Knowledge › Coordinate Reference Systems › Units; Geo-KTF › Analytical Capabilities › CRS Management; Geo-KTF › Validation › CRS Validation
- Definition: pyproj.CRS is a PyProj class for CRS definitions. It builds CRS objects from EPSG/WKT/PROJ so you can inspect axes, units, and datums. Expected output: a CRS object/metadata.

### `pyproj.Transformer`
- Source: PyProj
- Categories: Geo-KTF › Basic Geospatial Knowledge › Coordinate Reference Systems › Geographic; Geo-KTF › Basic Geospatial Knowledge › Coordinate Reference Systems › Datums; Geo-KTF › Basic Geospatial Knowledge › Coordinate Reference Systems › Vertical CRS; Geo-KTF › Analytical Capabilities › CRS Management; Geo-KTF › Validation › CRS Validation
- Definition: pyproj.Transformer is a PyProj coordinate transformer. It converts coordinates between CRSs efficiently when created once and reused. Expected output: transformed coordinate arrays.

### `pyproj.Transformer(always_xy=True)`
- Source: PyProj
- Categories: Geo-KTF › Basic Geospatial Knowledge › Coordinate Reference Systems › Common CRS Errors; Geo-KTF › Validation › CRS Validation
- Definition: pyproj.Transformer(always_xy=True) is a PyProj transformer mode. It forces easting/northing (or lon/lat) order to avoid axis-order bugs in some EPSG codes. Expected output: coordinates in consistent xy order.

### `PySAL`
- Source: Python Spatial Analysis Library
- Categories: Geo-KTF › Provider Registry › Geospatial Libraries
- Definition: PySAL is the Python Spatial Analysis Library ecosystem. It provides weights, spatial stats, regression, point patterns, and related modules for scientific GIS. Expected output: statistical objects, maps of indicators, and model results.

### `pystac`
- Source: STAC project
- Categories: Geo-KTF › Provider Registry › SDI / Catalogs
- Definition: pystac is a Python library for STAC. It reads, writes, and walks STAC catalogues for building or consuming cloud EO catalogs. Expected output: STAC objects in Python / written catalog files.

### `Python for GIS`
- Source: Python geospatial ecosystem
- Categories: Geo-KTF › Provider Registry › Development
- Definition: Python for GIS refers to the Python geospatial ecosystem (GeoPandas, Rasterio, PySAL, etc.). It automates analysis and pipelines beyond click-based GUI work. Expected output: scripts/notebooks producing GIS files, maps, and statistics.

### `PyTorch`
- Source: Meta / Linux Foundation
- Categories: Geo-KTF › Provider Registry › AI
- Definition: PyTorch is a deep-learning framework. It trains neural networks on imagery and geospatial tensors with flexible Python APIs. Expected output: trained models and inference tensors/maps.

### `QField`
- Source: OPENGIS.ch / QField
- Categories: Geo-KTF › Analytical Capabilities › Data Acquisition
- Definition: QField is a mobile field app for QGIS projects (OPENGIS.ch). It supports offline viewing/editing with GPS capture and sync back to desktop/cloud. Expected output: updated project layers/features from the field.

### `QGIS 3D Map View`
- Source: QGIS
- Categories: Geo-KTF › Basic Geospatial Knowledge › Data Models › Mesh; Geo-KTF › Basic Geospatial Knowledge › Data Models › 3D; Geo-KTF › Analytical Capabilities › Cartography
- Definition: QGIS 3D Map View is the QGIS three-dimensional scene viewer. It shows terrain and extruded/modelled features for immersive exploration beyond 2D. Expected output: an interactive 3D view (exportable frames/animations depending on setup).

### `QGIS Geometry Checker`
- Source: QGIS Plugin
- Categories: Geo-KTF › Validation › Geometry Validation
- Definition: QGIS Geometry Checker refers to QGIS geometry validation tooling (plugin/Processing). It finds structural and topological problems before overlays or publishing. Expected output: diagnostic error features and messages.

### `QGIS Geometry Checker Plugin`
- Source: QGIS Plugin
- Categories: Geo-KTF › Basic Geospatial Knowledge › Data Quality › Validity
- Definition: The Geometry Checker Plugin is a QGIS interactive validation add-on. It helps find and review geometry/topology problems with a guided interface. Expected output: error reports and optional fixes applied in the project.

### `QGIS Label settings`
- Source: QGIS
- Categories: Geo-KTF › Analytical Capabilities › Cartography
- Definition: QGIS Label settings control feature labelling in QGIS. They manage fonts, placement, filters, and buffers so text remains readable. Expected output: labelled map features on canvas/layout.

### `QGIS Model Designer`
- Source: QGIS Processing
- Categories: Geo-KTF › Basic Geospatial Knowledge › Data Quality › Lineage; Geo-KTF › Analytical Capabilities › Geocomputation; Geo-KTF › Workflow › Suitability Analysis; Geo-KTF › Provider Registry › Development
- Definition: QGIS Model Designer is the visual workflow builder in QGIS. It chains Processing algorithms into reusable models for repeatable multi-step analysis. Expected output: a saved model that can run batch jobs with defined outputs.

### `QGIS Print Layout`
- Source: QGIS
- Categories: Geo-KTF › Analytical Capabilities › Cartography; Geo-KTF › Output › Reports; Geo-KTF › Output › Story Maps
- Definition: QGIS Print Layout is QGIS’s map-composition environment. It arranges map frames, legends, scale bars, and text for publication-quality pages or atlases. Expected output: PDF/SVG/image exports (optionally multi-page Atlas).

### `QGIS Processing History`
- Source: QGIS
- Categories: Geo-KTF › Basic Geospatial Knowledge › Data Quality › Lineage; Geo-KTF › Validation › Result Validation
- Definition: QGIS Processing History records algorithms you have run. It stores parameters so you can reproduce or re-run earlier steps. Expected output: a browsable history list and re-runnable commands.

### `QGIS Processing Log`
- Source: QGIS
- Categories: Geo-KTF › Basic Geospatial Knowledge › Data Quality › Lineage; Geo-KTF › Validation › Result Validation
- Definition: QGIS Processing Log shows messages from Processing runs. It surfaces errors and warnings when algorithms fail or need diagnosis. Expected output: timestamped log text for troubleshooting.

### `QGIS Reports`
- Source: QGIS
- Categories: Geo-KTF › Output › Reports
- Definition: QGIS Reports builds structured multi-page report outputs from a project. It combines maps and attribute-driven sections for stakeholder documents. Expected output: a paginated report export.

### `QGIS Server`
- Source: QGIS
- Categories: Geo-KTF › Output › Dashboards; Geo-KTF › Output › APIs; Geo-KTF › Provider Registry › Web Mapping
- Definition: QGIS Server is the QGIS map server component. It publishes QGIS projects as OGC web services using desktop styling. Expected output: WMS/WFS (and related) web map services.

### `QGIS Style Manager`
- Source: QGIS
- Categories: Geo-KTF › Analytical Capabilities › Cartography
- Definition: QGIS Style Manager is the QGIS cartography style library. It stores and reuses symbols and styles so maps stay visually consistent across projects. Expected output: saved styles applied to layers.

### `QGIS Symbol Selector`
- Source: QGIS
- Categories: Geo-KTF › Analytical Capabilities › Cartography
- Definition: QGIS Symbol Selector is the QGIS dialog for designing feature symbols. It controls mark layers, colours, sizes, and patterns for points, lines, and polygons. Expected output: a configured symbol rendered on the map canvas.

### `QGIS Temporal Controller`
- Source: QGIS
- Categories: Geo-KTF › Analytical Capabilities › Space-Time Analysis
- Definition: QGIS Temporal Controller is the time filter/animation tool in QGIS. It steps through time so only matching features or frames display, aiding space-time exploration. Expected output: a time-filtered canvas view or animation sequence.

### `qgis_process`
- Source: QGIS
- Categories: Geo-KTF › Basic Geospatial Knowledge › Data Quality › Lineage; Geo-KTF › Validation › Result Validation; Geo-KTF › Provider Registry › Development
- Definition: qgis_process is the QGIS command-line Processing runner. It executes the same algorithms as the GUI without opening the desktop app, which helps automation. Expected output: algorithm result files written to specified paths.

### `R for GIS`
- Source: R spatial ecosystem
- Categories: Geo-KTF › Provider Registry › Development
- Definition: R for GIS refers to R spatial packages such as sf, terra, and spatstat. It combines spatial data structures with statistical modelling in one reproducible language. Expected output: spatial objects, models, and plots/reports.

### `Random points in extent`
- Source: QGIS Processing
- Categories: Geo-KTF › Basic Geospatial Knowledge › Relationship › Uncertainty; Geo-KTF › Basic Geospatial Knowledge › Data Quality › Uncertainty Modeling; Geo-KTF › Analytical Capabilities › Point Pattern Analysis
- Definition: Random points in extent is a QGIS Processing sampling tool. It scatters random points inside a rectangle for unbiased spatial sampling designs. Expected output: a point layer within the given extent.

### `Random points in polygons`
- Source: QGIS Processing
- Categories: Geo-KTF › Basic Geospatial Knowledge › Relationship › Uncertainty; Geo-KTF › Analytical Capabilities › Remote Sensing; Geo-KTF › Validation › Accuracy Assessment
- Definition: Random points in polygons is a QGIS Processing sampling tool. It creates randomly located points inside polygons for surveys or accuracy samples. Expected output: a point layer of random sample locations.

### `Random selection`
- Source: QGIS Processing
- Categories: Geo-KTF › Basic Geospatial Knowledge › Relationship › Uncertainty; Geo-KTF › Basic Geospatial Knowledge › Data Quality › Uncertainty Modeling
- Definition: Random selection is a QGIS Processing sampling tool. It picks a random subset of features by count or percentage for validation or experiments. Expected output: a selected subset (or new layer) of features.

### `Raster Calculator`
- Source: QGIS / ArcGIS
- Categories: Geo-KTF › Basic Geospatial Knowledge › Spatial Analysis › Raster Analysis; Geo-KTF › Analytical Capabilities › Raster Processing; Geo-KTF › Analytical Capabilities › Multi-Criteria Evaluation; Geo-KTF › Workflow › Site Selection; Geo-KTF › Workflow › Suitability Analysis; Geo-KTF › Workflow › Hazard Assessment; Geo-KTF › Workflow › Environmental Assessment; Geo-KTF › Workflow › Change Detection; Geo-KTF › Workflow › Urban Growth Analysis
- Definition: Raster Calculator is QGIS’s map-algebra tool. It evaluates expressions across raster layers/bands to build indices, masks, and suitability scores in the GUI. Expected output: a new raster of computed values.

### `Rasterio`
- Source: Python (Mapbox lineage)
- Categories: Geo-KTF › Provider Registry › Geospatial Libraries
- Definition: Rasterio is a Python library for geospatial rasters via GDAL. It reads/writes rasters as NumPy arrays with CRS and transform metadata for analysis. Expected output: arrays and raster files.

### `rasterio.mask.mask()`
- Source: Rasterio
- Categories: Geo-KTF › Analytical Capabilities › Remote Sensing
- Definition: rasterio.mask.mask() is a Rasterio AOI tool. It clips a raster to polygons and sets outside cells to nodata. Expected output: a masked array plus updated transform.

### `rasterio.merge.merge()`
- Source: Rasterio
- Categories: Geo-KTF › Basic Geospatial Knowledge › Data Models › Raster
- Definition: rasterio.merge.merge() is a Rasterio mosaic function. It mosaics multiple rasters into one array with a combined transform. Expected output: a mosaicked array and transform.

### `rasterio.open()`
- Source: Rasterio
- Categories: Geo-KTF › Basic Geospatial Knowledge › Data Models › Raster; Geo-KTF › Basic Geospatial Knowledge › Data Quality › Metadata; Geo-KTF › Analytical Capabilities › Data Inspection
- Definition: rasterio.open() is Rasterio’s dataset opener. It opens rasters for read/write in a context manager so handles close cleanly. Expected output: a dataset object yielding arrays/metadata.

### `RDFLib`
- Source: RDFLib
- Categories: Geo-KTF › Basic Geospatial Knowledge › Data Models › Knowledge Graph
- Definition: RDFLib is a Python RDF library. It parses and SPARQL-queries knowledge graphs, including GeoSPARQL data in scripts/notebooks. Expected output: RDF graphs and query results.

### `readers.las`
- Source: PDAL
- Categories: Geo-KTF › Basic Geospatial Knowledge › Data Models › Point Cloud
- Definition: readers.las is a PDAL reader stage. It loads LAS/LAZ points with dimensions such as XYZ, intensity, and classification into a pipeline. Expected output: an in-pipeline point view from LAS/LAZ.

### `Reclassify by table`
- Source: QGIS Processing
- Categories: Geo-KTF › Analytical Capabilities › Multi-Criteria Evaluation; Geo-KTF › Workflow › Suitability Analysis
- Definition: Reclassify by table is a QGIS Processing raster tool. It maps input value ranges to new classes using a reclassification table, preparing criteria for overlay. Expected output: a classified raster with discrete class values.

### `Refactor Fields`
- Source: QGIS Processing
- Categories: Geo-KTF › Validation › Schema Validation
- Definition: Refactor Fields is a QGIS Processing schema tool. It renames, retypes, reorders, and maps fields so tables match a target schema. Expected output: a layer with the revised attribute structure.

### `Reproject Layer`
- Source: QGIS Processing
- Categories: Geo-KTF › Basic Geospatial Knowledge › Coordinate Reference Systems › Common CRS Errors; Geo-KTF › Validation › CRS Validation
- Definition: Reproject Layer is a QGIS Processing CRS tool. It transforms coordinates into a target CRS (unlike Assign projection), which is required for meaningful metre distances. Expected output: a new layer in the target CRS.

### `rio info`
- Source: Rasterio CLI
- Categories: Geo-KTF › Basic Geospatial Knowledge › Data Quality › Metadata; Geo-KTF › Validation › Metadata Validation
- Definition: rio info is the Rasterio command-line metadata tool. It prints raster metadata as JSON for scripting and quick checks. Expected output: JSON metadata (CRS, transform, dtype, bounds).

### `scikit-learn`
- Source: scikit-learn
- Categories: Geo-KTF › Provider Registry › AI
- Definition: scikit-learn is a Python machine-learning library. It provides a consistent fit/predict API for classical classification, regression, and clustering on feature tables. Expected output: trained models and predictions.

### `scikit-learn DBSCAN`
- Source: scikit-learn
- Categories: Geo-KTF › Analytical Capabilities › Clustering
- Definition: scikit-learn DBSCAN is scikit-learn’s density clustering estimator. It groups dense regions and labels noise using eps and min_samples (feed coordinates for spatial use). Expected output: cluster labels per sample.

### `scikit-learn KMeans`
- Source: scikit-learn
- Categories: Geo-KTF › Analytical Capabilities › Clustering
- Definition: scikit-learn KMeans is scikit-learn’s K-means estimator. It partitions samples into a fixed number of clusters quickly when K is known. Expected output: cluster labels and centroids.

### `scikit-learn.metrics`
- Source: scikit-learn
- Categories: Geo-KTF › Analytical Capabilities › Remote Sensing; Geo-KTF › Validation › Accuracy Assessment
- Definition: scikit-learn.metrics is the metrics module of scikit-learn. It computes confusion matrices, accuracy, precision, recall, F1, and kappa for predicted vs reference labels. Expected output: numeric scores and confusion matrices.

### `Segment Anything Model (SAM)`
- Source: Meta AI
- Categories: Geo-KTF › Analytical Capabilities › Remote Sensing; Geo-KTF › Workflow › Remote Sensing Classification; Geo-KTF › Provider Registry › AI
- Definition: Segment Anything Model (SAM) is a foundation vision model (Meta) used in geospatial pipelines. It segments objects from prompts with fewer hand labels, helping extract features from imagery. Expected output: segmentation masks (then georeferenced into GIS layers).

### `Service Area`
- Source: QGIS / network analysis
- Categories: Geo-KTF › Basic Geospatial Knowledge › Spatial Analysis › Network Analysis; Geo-KTF › Analytical Capabilities › Accessibility; Geo-KTF › Analytical Capabilities › Location-Allocation; Geo-KTF › Workflow › Catchment Analysis; Geo-KTF › Workflow › Accessibility Analysis; Geo-KTF › Workflow › Infrastructure Planning
- Definition: Service Area is a QGIS network analysis algorithm. It delineates how far you can travel from facilities within a cost limit on the network. Expected output: reachable polygons or boundary lines.

### `Shapely`
- Source: Python (Toblerity)
- Categories: Geo-KTF › Provider Registry › Geospatial Libraries
- Definition: Shapely is a Python geometry library backed by GEOS. It creates and analyses geometries (buffers, overlays, predicates, validity) used under GeoPandas. Expected output: geometry objects and boolean/metric results.

### `Shortest Path`
- Source: QGIS network analysis
- Categories: Geo-KTF › Basic Geospatial Knowledge › Data Models › Trajectory; Geo-KTF › Basic Geospatial Knowledge › Spatial Analysis › Network Analysis; Geo-KTF › Analytical Capabilities › Routing; Geo-KTF › Analytical Capabilities › Trajectory Analysis; Geo-KTF › Workflow › Infrastructure Planning
- Definition: Shortest Path is a QGIS network analysis algorithm. It finds a least-cost route on a network layer using length or another impedance field. Expected output: a path line (and cost) between chosen points.

### `Simplify`
- Source: QGIS Processing
- Categories: Geo-KTF › Basic Geospatial Knowledge › Relationship › Scale; Geo-KTF › Basic Geospatial Knowledge › Data Quality › Precision; Geo-KTF › Analytical Capabilities › Vector Processing
- Definition: Simplify is a QGIS Processing generalisation tool. It reduces vertices with a tolerance to speed drawing and remove unnecessary detail. Expected output: a simplified copy of the input geometries.

### `Snap geometries to grid`
- Source: QGIS Processing
- Categories: Geo-KTF › Basic Geospatial Knowledge › Data Quality › Precision
- Definition: Snap geometries to grid is a QGIS Processing precision tool. It moves vertices onto a coordinate grid to reduce slivers and micro-gaps when tolerance is set carefully. Expected output: geometries with snapped coordinates.

### `Split Vector Layer`
- Source: QGIS Processing
- Categories: Geo-KTF › Analytical Capabilities › Vector Processing
- Definition: Split Vector Layer is a QGIS Processing tool. It writes separate outputs for each unique value of a chosen attribute field. Expected output: multiple layers or files, one per class.

### `Split with lines`
- Source: QGIS Processing
- Categories: Geo-KTF › Basic Geospatial Knowledge › Relationship › Overlay; Geo-KTF › Basic Geospatial Knowledge › Spatial Analysis › Vector Analysis
- Definition: Split with lines is a QGIS Processing tool. It cuts polygons or lines wherever they cross a line layer, creating segments at intersections. Expected output: split features of the input geometry type.

### `spreg.ML_Error`
- Source: PySAL spreg
- Categories: Geo-KTF › Analytical Capabilities › Spatial Regression
- Definition: spreg.ML_Error is a PySAL spreg spatial error model. It models spatial dependence in residuals when omitted factors are spatially structured. Expected output: spatial error model coefficients and fit stats.

### `spreg.ML_Lag`
- Source: PySAL spreg
- Categories: Geo-KTF › Analytical Capabilities › Spatial Regression
- Definition: spreg.ML_Lag is a PySAL spreg spatial lag model. It models an outcome that depends on neighbouring outcomes (spillover) via maximum likelihood. Expected output: spatial lag model coefficients and fit stats.

### `spreg.OLS`
- Source: PySAL spreg
- Categories: Geo-KTF › Analytical Capabilities › Spatial Regression
- Definition: spreg.OLS is a PySAL spreg ordinary least squares estimator. It fits classical regression with optional spatial residual diagnostics before choosing spatial models. Expected output: regression coefficients and diagnostics.

### `ST_Area`
- Source: PostGIS
- Categories: Geo-KTF › Basic Geospatial Knowledge › Coordinate Reference Systems › Units
- Definition: ST_Area is a PostGIS measurement function. It returns polygon area in CRS units (prefer equal-area CRS for comparable planar areas). Expected output: numeric area values.

### `ST_Buffer`
- Source: PostGIS / Spatial SQL
- Categories: Geo-KTF › Basic Geospatial Knowledge › Relationship › Overlay; Geo-KTF › Analytical Capabilities › Database Processing; Geo-KTF › Analytical Capabilities › Spatial SQL
- Definition: ST_Buffer is a PostGIS buffering function. It expands or shrinks geometries by a distance in CRS units (use projected SRIDs for metres). Expected output: buffer geometries.

### `ST_ClusterDBSCAN`
- Source: PostGIS
- Categories: Geo-KTF › Analytical Capabilities › Clustering
- Definition: ST_ClusterDBSCAN is a PostGIS clustering window function. It assigns DBSCAN cluster IDs by distance and minimum points inside SQL. Expected output: rows labelled with cluster IDs.

### `ST_ClusterKMeans`
- Source: PostGIS
- Categories: Geo-KTF › Analytical Capabilities › Clustering
- Definition: ST_ClusterKMeans is a PostGIS clustering function. It assigns K-means cluster IDs to geometries on the server. Expected output: rows labelled with K cluster IDs.

### `ST_ClusterWithin`
- Source: PostGIS
- Categories: Geo-KTF › Analytical Capabilities › Clustering
- Definition: ST_ClusterWithin is a PostGIS clustering aggregate. It groups geometries that fall within a given distance of each other. Expected output: clustered geometry collections/groups.

### `ST_Contains`
- Source: PostGIS / Spatial SQL
- Categories: Geo-KTF › Basic Geospatial Knowledge › Relationship › Containment; Geo-KTF › Analytical Capabilities › Spatial SQL; Geo-KTF › Workflow › Demographic Enrichment
- Definition: ST_Contains is a PostGIS containment predicate. It tests whether one geometry completely contains another. Expected output: boolean (or filtered rows).

### `ST_Crosses`
- Source: PostGIS / Spatial SQL
- Categories: Geo-KTF › Basic Geospatial Knowledge › Relationship › Adjacency; Geo-KTF › Validation › Topology Validation
- Definition: ST_Crosses is a PostGIS topology predicate. It is true when geometries cross under OGC rules (e.g., a line crossing a polygon). Expected output: boolean (or filtered rows).

### `ST_Distance`
- Source: PostGIS / Spatial SQL
- Categories: Geo-KTF › Basic Geospatial Knowledge › Relationship › Distance; Geo-KTF › Analytical Capabilities › Spatial SQL
- Definition: ST_Distance is a PostGIS distance function. It returns the shortest distance between geometries in CRS units (spheroidal for geography). Expected output: numeric distances.

### `ST_DWithin`
- Source: PostGIS / Spatial SQL
- Categories: Geo-KTF › Basic Geospatial Knowledge › Relationship › Distance; Geo-KTF › Analytical Capabilities › Database Processing; Geo-KTF › Analytical Capabilities › Spatial SQL; Geo-KTF › Workflow › Infrastructure Planning
- Definition: ST_DWithin is a PostGIS proximity predicate. It tests whether geometries are within a distance without buffering just to filter. Expected output: boolean (or filtered rows).

### `ST_GeoHash`
- Source: PostGIS
- Categories: Geo-KTF › Basic Geospatial Knowledge › Data Models › Spatial Indexing
- Definition: ST_GeoHash is a PostGIS geohash function. It encodes geometries into geohash strings for hierarchical grid keys and coarse spatial grouping. Expected output: geohash text values.

### `ST_Intersection`
- Source: PostGIS / Spatial SQL
- Categories: Geo-KTF › Basic Geospatial Knowledge › Relationship › Overlay; Geo-KTF › Analytical Capabilities › Spatial SQL
- Definition: ST_Intersection is a PostGIS overlay function. It returns the shared geometry of two inputs. Expected output: intersection geometries.

### `ST_Intersects`
- Source: PostGIS / Spatial SQL
- Categories: Geo-KTF › Basic Geospatial Knowledge › Data Models › Hex Grid; Geo-KTF › Analytical Capabilities › Database Processing; Geo-KTF › Analytical Capabilities › Spatial SQL; Geo-KTF › Workflow › Demographic Enrichment
- Definition: ST_Intersects is a PostGIS spatial predicate. It tests whether geometries share any space and runs fast with a spatial index. Expected output: boolean (or filtered rows).

### `ST_IsValid`
- Source: PostGIS / Spatial SQL
- Categories: Geo-KTF › Basic Geospatial Knowledge › Data Quality › Validity; Geo-KTF › Analytical Capabilities › Database Processing; Geo-KTF › Validation › Geometry Validation
- Definition: ST_IsValid is a PostGIS validity function. It returns whether a geometry passes OGC validity rules. Expected output: boolean true/false.

### `ST_IsValidDetail`
- Source: PostGIS / Spatial SQL
- Categories: Geo-KTF › Basic Geospatial Knowledge › Data Quality › Validity; Geo-KTF › Validation › Geometry Validation
- Definition: ST_IsValidDetail is a PostGIS validity diagnostic. It explains why a geometry is invalid and where the problem is. Expected output: reason/location details for invalid geometries.

### `ST_Length`
- Source: PostGIS
- Categories: Geo-KTF › Basic Geospatial Knowledge › Coordinate Reference Systems › Units
- Definition: ST_Length is a PostGIS measurement function. It returns length of linestrings in CRS units (or spheroidal for geography). Expected output: numeric length values.

### `ST_Overlaps`
- Source: PostGIS / Spatial SQL
- Categories: Geo-KTF › Basic Geospatial Knowledge › Relationship › Adjacency; Geo-KTF › Validation › Topology Validation
- Definition: ST_Overlaps is a PostGIS topology predicate. It is true when geometries partly overlap without one containing the other. Expected output: boolean (or filtered rows).

### `ST_SetSRID`
- Source: PostGIS
- Categories: Geo-KTF › Basic Geospatial Knowledge › Coordinate Reference Systems › Common CRS Errors
- Definition: ST_SetSRID is a PostGIS CRS tagging function. It assigns an SRID without changing coordinates (like assign projection). Expected output: geometry with updated SRID metadata.

### `ST_Touches`
- Source: PostGIS / Spatial SQL
- Categories: Geo-KTF › Basic Geospatial Knowledge › Relationship › Adjacency; Geo-KTF › Validation › Topology Validation
- Definition: ST_Touches is a PostGIS adjacency predicate. It is true when geometries touch at boundaries but interiors do not intersect. Expected output: boolean (or filtered rows).

### `ST_Transform`
- Source: PostGIS / Spatial SQL
- Categories: Geo-KTF › Basic Geospatial Knowledge › Coordinate Reference Systems › Geographic; Geo-KTF › Basic Geospatial Knowledge › Coordinate Reference Systems › Datums; Geo-KTF › Basic Geospatial Knowledge › Coordinate Reference Systems › Vertical CRS; Geo-KTF › Basic Geospatial Knowledge › Coordinate Reference Systems › Units; Geo-KTF › Basic Geospatial Knowledge › Coordinate Reference Systems › Common CRS Errors; Geo-KTF › Analytical Capabilities › CRS Management; Geo-KTF › Analytical Capabilities › Database Processing; Geo-KTF › Analytical Capabilities › Spatial SQL; Geo-KTF › Validation › CRS Validation
- Definition: ST_Transform is a PostGIS reprojection function. It converts geometries to another SRID inside the database. Expected output: geometries in the target SRID.

### `ST_Within`
- Source: PostGIS / Spatial SQL
- Categories: Geo-KTF › Basic Geospatial Knowledge › Relationship › Containment; Geo-KTF › Analytical Capabilities › Spatial SQL; Geo-KTF › Workflow › Demographic Enrichment
- Definition: ST_Within is a PostGIS containment predicate. It tests whether a geometry lies entirely inside another. Expected output: boolean (or filtered rows).

### `STAC`
- Source: STAC community / OGC
- Categories: Geo-KTF › Provider Registry › SDI / Catalogs
- Definition: STAC (SpatioTemporal Asset Catalog) is a community/OGC-aligned JSON catalog spec. It makes cloud imagery and assets searchable by space, time, and properties. Expected output: STAC Catalog/Collection/Item JSON and search results.

### `Strahler order`
- Source: QGIS / SAGA
- Categories: Geo-KTF › Workflow › Hydrological Analysis
- Definition: Strahler order is a stream-ordering tool in hydrological toolboxes (SAGA/GRASS/QGIS). It classifies channel segments by hierarchical stream order for network morphology studies. Expected output: streams attributed with Strahler order values.

### `Structure from Motion`
- Source: Photogrammetry method
- Categories: Geo-KTF › Analytical Capabilities › Remote Sensing
- Definition: Structure from Motion (SfM) is a photogrammetry method implemented in tools such as OpenDroneMap. It recovers camera poses and 3D structure from overlapping photos before dense matching. Expected output: sparse/dense point clouds, meshes, DEMs, and orthomosaics (via a full SfM pipeline).

### `TensorFlow`
- Source: Google
- Categories: Geo-KTF › Provider Registry › AI
- Definition: TensorFlow is a deep-learning platform. It trains and deploys neural nets for EO and other geospatial learning tasks. Expected output: trained models and predictions.

### `Thin plate spline`
- Source: QGIS / GDAL georeferencing
- Categories: Geo-KTF › Analytical Capabilities › Spatial Interpolation
- Definition: Thin plate spline (TPS) is used in QGIS georeferencing and interpolation contexts. It bends a flexible surface through control points while keeping bending energy low, good for irregular GCPs or samples. Expected output: a warped georeferenced image or an interpolated surface.

### `TileDB`
- Source: TileDB
- Categories: Geo-KTF › Basic Geospatial Knowledge › Data Models › Array Database
- Definition: TileDB is an array database/storage engine. It stores dense/sparse multi-dimensional arrays (including geospatial cubes) on disk or cloud. Expected output: array slices and derived analytics outputs.

### `TIN Interpolation`
- Source: QGIS Processing
- Categories: Geo-KTF › Basic Geospatial Knowledge › Data Models › TIN; Geo-KTF › Analytical Capabilities › Spatial Interpolation
- Definition: TIN Interpolation is a QGIS Processing interpolator. It builds triangles from sample points and interpolates across faces, preserving sample locations well for terrain-like fields. Expected output: an interpolated raster (from the TIN).

### `tobler.area_interpolate()`
- Source: PySAL tobler
- Categories: Geo-KTF › Basic Geospatial Knowledge › Spatial Analysis › Raster Analysis
- Definition: tobler.area_interpolate() is a PySAL tobler areal interpolation function. It transfers polygon attributes to new zones by overlap area, handling extensive vs intensive values correctly. Expected output: a target-zone layer with interpolated attributes.

### `Union`
- Source: QGIS / ArcGIS Processing
- Categories: Geo-KTF › Basic Geospatial Knowledge › Relationship › Overlay; Geo-KTF › Basic Geospatial Knowledge › Spatial Analysis › Vector Analysis; Geo-KTF › Analytical Capabilities › Vector Processing
- Definition: Union is a polygon overlay tool in QGIS/ArcGIS. It keeps all pieces from both layers and combines attributes where they overlap, giving a full topological union. Expected output: a polygon layer covering the combined extent with overlap attributes filled where relevant.

### `v.net.alloc`
- Source: GRASS GIS
- Categories: Geo-KTF › Analytical Capabilities › Location-Allocation
- Definition: v.net.alloc is a GRASS GIS network allocation tool. It assigns network edges to the nearest facility centre by network cost for service partitions. Expected output: network edges labelled by allocated centre.

### `Valhalla`
- Source: Valhalla / Mapbox lineage
- Categories: Geo-KTF › Provider Registry › Geospatial Libraries
- Definition: Valhalla is an open-source routing engine with flexible costing models. It supports multiple travel modes for self-hosted directions as an alternative to OSRM/ORS. Expected output: routing API responses (paths and costs).

### `Viewshed`
- Source: QGIS / GDAL
- Categories: Geo-KTF › Workflow › Visibility Analysis
- Definition: Viewshed is a QGIS/terrain visibility tool. It computes which DEM cells are visible from observer points given terrain occlusion. Expected output: a visibility raster (and optional vectorised visible areas).

### `Voronoi polygons`
- Source: QGIS Processing
- Categories: Geo-KTF › Basic Geospatial Knowledge › Spatial Analysis › Vector Analysis
- Definition: Voronoi (Thiessen) polygons is a QGIS Processing tool. It partitions the plane so each polygon is closer to its seed point than to any other, useful for planar catchments. Expected output: a polygon layer of Voronoi cells around input points.

### `Watershed`
- Source: QGIS Hydrology
- Categories: Geo-KTF › Workflow › Hydrological Analysis
- Definition: Watershed is a hydrological delineation tool in QGIS/SAGA/GRASS workflows. It outlines drainage basins contributing to pour points or stream outlets. Expected output: watershed polygons or labelled basin rasters.

### `Weighted Overlay`
- Source: QGIS / ArcGIS
- Categories: Geo-KTF › Analytical Capabilities › Multi-Criteria Evaluation; Geo-KTF › Workflow › Site Selection; Geo-KTF › Workflow › Suitability Analysis
- Definition: Weighted Overlay is a multi-criteria raster combination method (ArcGIS-style; similar patterns in QGIS models). It combines reclassified criteria with weights to rank suitability in a transparent, repeatable way. Expected output: a scored suitability raster.

### `writers.gdal`
- Source: PDAL
- Categories: Geo-KTF › Basic Geospatial Knowledge › Data Models › Point Cloud; Geo-KTF › Analytical Capabilities › Remote Sensing
- Definition: writers.gdal is a PDAL writer stage. It interpolates points onto a raster grid via GDAL (e.g., DSM/DEM surfaces). Expected output: a raster surface from the cloud.

### `writers.las`
- Source: PDAL
- Categories: Geo-KTF › Basic Geospatial Knowledge › Data Models › Point Cloud
- Definition: writers.las is a PDAL writer stage. It writes LAS/LAZ output from a pipeline (choose compression for LAZ). Expected output: a LAS or LAZ file.

### `xarray.open_dataset()`
- Source: xarray
- Categories: Geo-KTF › Basic Geospatial Knowledge › Data Models › Array Database
- Definition: xarray.open_dataset() is an xarray I/O function. It opens NetCDF/Zarr-style labelled arrays with named coordinates for data-cube analysis. Expected output: an xarray Dataset.

### `XGBoost`
- Source: XGBoost project
- Categories: Geo-KTF › Provider Registry › AI
- Definition: XGBoost is a gradient-boosting machine-learning library. It builds strong tabular predictors often used with remote-sensing and spatial features. Expected output: trained models and predicted values/classes.

## Review checklist
1. Clear / easy / correct for each category and tool?
2. Any remaining duplicate concepts across pillars?
3. Category–tool membership mismatches?
4. Official tool behaviour vs blurb?