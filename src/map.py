from geojson import dumps
import geojson as g

import parse
from parse import parse, MY_FILE

import parse as p 

def create_map(data_file):
  # Define type of GeoJSON we're creating
  geo_map = {"type":"FeatureCollection"}

  # Define empty list to collect each point to graph
  item_list = []

  # Iterate over our data to create GeoJSON document.
  # We're using enumerate() so we get the line, as well
  # the index, which is the line number.
  for index, line in enumerate(data_file):

    # Skip any 0 coords as this will throw off our map
    if line['X'] == "0" or line['Y'] == "0":
      continue
    
    # Setup a new dictionary for each iteration
    data = {}
    
    # Assign line itesm to appropriate GeoJSON fields
    data['type']       = 'Feature'
    data['id']         = index
    data['properties'] = {
                          'title':line['Category'],
                          'description':line['Description'],
                          'date':line['Date']
                        }
    data['geometry'] = {'type':'Point',
                        'coordinates':(line['X'],line['Y'])}
    # Add data dictionary to our item list
    item_list.append(data)

  # For each point in our item_list, we add the point to our
  # dictionary. setdefault creates a key called 'features' that
  # has a value type of an empty list. With each iteration,
  # we are appending our point to that list.
  for point in item_list:
    geo_map.setdefault('features',[]).append(point)

  # Now that all data is parsed in GeoJSON write to a file 
  # so we can upload it to gist.github.com
  with open('file_sf.geojson','w') as f:
    f.write(g.dumps(geo_map))

def main():
  data = p.parse(p.MY_FILE,',')
  return create_map(data)

if __name__ == "__main__":
  main()




