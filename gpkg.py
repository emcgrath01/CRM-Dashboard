import geopandas as gpd

# Read the GPKG file
gdf = gpd.read_file('.venv/templates/global_mining_polygons_v1.gpkg')

# Convert to GeoJSON
gdf.to_file('.venv/templates/output.geojson', driver='GeoJSON')


import geopandas as gpd

# Read the GeoPackage file containing point data
point_data = gpd.read_file('.venv/templates/validation_points_v1.gpkg')

# Convert to GeoJSON format
point_data.to_file('.venv/templates/points_output.geojson', driver='GeoJSON')
