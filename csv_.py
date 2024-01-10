import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

# Read CSV data
data = pd.read_csv('global_mining_area_per_country_v1.csv')

# Convert to GeoDataFrame (assuming 'latitude' and 'longitude' columns)
geometry = [Point(xy) for xy in zip(data['longitude'], data['latitude'])]
crs = {'init': 'epsg:4326'}  # Assuming WGS84 coordinate system
gdf = gpd.GeoDataFrame(data, crs=crs, geometry=geometry)

# Save as GeoJSON
gdf.to_file("mining_areas.geojson", driver='GeoJSON')
