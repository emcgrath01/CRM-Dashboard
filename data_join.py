
import pandas as pd
import geopandas as gpd
# Load GeoJSON file into a GeoDataFrame
geojson_data = gpd.read_file('.venv/templates/custom.geo.json')

# Load CSV file into a DataFrame
csv_data = pd.read_csv('.venv/templates/global_mining_area_per_country_v1.csv')

# Merge the GeoDataFrame with the DataFrame based on a common column (e.g., ISO3_CODE)
merged_data = geojson_data.merge(csv_data, how='left', left_on='sov_a3', right_on='ISO3_CODE')

# Display the merged data (geometry + attributes)
print(merged_data.head())

# Save the merged data as a new GeoJSON file
merged_data.to_file(".venv/templates/merged_data.geojson", driver='GeoJSON')
