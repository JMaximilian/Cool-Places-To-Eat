"""
This script fetches the two data sources for the restaurant info. 
Merges the two datasets. #Dumps them as JSON. 
And uploads them to the specified Algolio application.
"""

# Imports
import pandas as pd
# import requests
from algoliasearch.search_client import SearchClient

# Parameter
src_json_path = 'dataset/restaurants_list.json'
src_csv_path ='dataset/restaurants_info.csv'
dst_path_csv = 'dataset/merged_restaurants_info.csv'
dst_path_json = 'dataset/merged_restaurant_info.json'
index_name = 'Restaurant_Index'
# KEYS
application_id = '***APPLICATION_ID***'
api_key = '***API_KEY***'

# Get raw datasets
raw_csv_df = pd.read_csv(src_csv_path, sep=';')
raw_json_df = pd.read_json(src_json_path)

# Merge datasets
merged_df = raw_csv_df.merge(raw_json_df, how='left', on='objectID')
restaurant_lst = merged_df.to_dict('records')

# # Dump as JSON
# with open(dst_path_json, 'w') as pth:
#     json.dump(restaurant_lst , pth)

# Create Algolia Search Client
client = SearchClient.create(
    application_id,
    api_key
)

# Create Index
index = client.init_index(index_name)

# Upload Entries
index.save_objects(restaurant_lst, {
    'autoGenerateObjectIDIfNotExist': True
    })

