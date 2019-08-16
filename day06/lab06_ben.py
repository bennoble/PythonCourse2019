# TODO: write code to answer the following questions: 
# 1) which of these embassies is closest to the White House in meters? 
# how far is it, and what is the address?
# 2) if I wanted to hold a morning meeting there, which cafe would you suggest?
# 3) if I wanted to hold an evening meeting there, which bar would you suggest? 


# Preamble
import imp
imported_items = imp.load_source('goog', '/Users/bennoble/Dropbox/Ben/Keys/start_google.py')
gmaps = imported_items.client

# Starting addresses
whitehouse = '1600 Pennsylvania Avenue, Washington, DC'

embassies = [[38.917228,-77.0522365], 
	[38.9076502, -77.0370427], 
	[38.916944, -77.048739] ]


def closest(list_of_emb):
  emb = []
# For the coordinates in the list...
  for i in range(len(list_of_emb)):
# Convert embassy list entries to lat/lng dict
    embassy = {}
    embassy['lat'] = embassies[i][0]
    embassy['lng'] = embassies[i][1]
# Determinehe distance, split on the number, and convert string number to float
    dist = gmaps.distance_matrix(whitehouse, embassy)
    num_dist = float(dist['rows'][0]['elements'][0]['distance']['text'].split(' ')[0])
# Append the float to a list    
    emb.append(num_dist)
# Find the min of all embassy distances
  close = min(emb)
# Inform the user of the lat/lng, index, and distance of the closest embassy
  print('The closest embassy is %s, which is index %d of your list. The distance is %.02f km' 
        % (list_of_emb[(emb.index(close))], (emb.index(close)), emb[emb.index(close)]))
# Take the closest embassy and reverse lookup
  close_emb = {}
  close_emb['lat'] = list_of_emb[(emb.index(close))][0]
  close_emb['lng'] = list_of_emb[(emb.index(close))][1]
  close_loc = gmaps.reverse_geocode(close_emb)
# Print the address
  print("""
      %s %s
      %s, %s %s
      """ % 
      (close_loc[0]['address_components'][0]['short_name'], 
       close_loc[0]['address_components'][1]['short_name'],
       close_loc[0]['address_components'][3]['short_name'],
       close_loc[0]['address_components'][4]['short_name'],
       close_loc[0]['address_components'][6]['short_name']))
  return close_emb
 
out = closest(embassies)
out

def nearby(lat, long, rad, type_str):
# Lookup the places nearby as specified by user
  place = gmaps.places_nearby(location = (lat, long), radius = rad, type = type_str)
  venues = []
  name = []
# find the names and ratings for each place in the lookup
  for i in range(len(place)):
    name.append(place['results'][i]['name'])
    venues.append(place['results'][i]['rating'])
# Print out the name and rating of the top rated venue
  #print('%s: %s' % (max(venues), name[venues.index(max(venues))]))
# Reverse lookup the best venue
  address = gmaps.reverse_geocode(place['results'][venues.index(max(venues))]['geometry']['location'])
# Print the venue address and relevant info
  print("""
      %s,
      %s %s
      %s, %s %s
      Rated: %s
      Price Level: %s
      """ % 
      (name[venues.index(max(venues))],
       address[0]['address_components'][0]['short_name'], 
       address[0]['address_components'][1]['short_name'],
       address[0]['address_components'][3]['short_name'],
       address[0]['address_components'][4]['short_name'],
       address[0]['address_components'][6]['short_name'],
       max(venues),
       place['results'][venues.index(max(venues))]['price_level']))
  
nearby(38.9076502, -77.0370427, 1000, 'bar')  

