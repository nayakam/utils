# import ujson
import sys

print(sys.version)
print(sys.version_info)

import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key="AIzaSyB_nfdLf7APO8_gYwmjQdv5jubDELqAdw0")


def get_directions(origin, destination, travelMode):
    directions_result = gmaps.directions(origin,
                                         destination,
                                         mode=travelMode,
                                         departure_time=now)
    print("directions_result: TravelMode:", travelMode, ", Result: ", directions_result)
    return directions_result


def distance_matrix(origin, destination, travelMode):
    directions_result = gmaps.distance_matrix(origin,
                                              destination,
                                              mode=travelMode,
                                              departure_time=now)
    print("distance_matrix: TravelMode:", travelMode, ", Result: ", directions_result)
    print("distance_matrix: TravelMode:", travelMode, ", Result: ",(((directions_result['rows'])[0])['elements'])[0]['distance'])
    return directions_result


print("gmaps", gmaps)
# Geocoding an address
# geocode_result = gmaps.geocode("1600 Amphitheatre Parkway, Mountain View, CA")
geocode_result = gmaps.geocode("68 Burelli St, Wollongong NSW 2500")
print("geocode_result", geocode_result)
# Look up an address with reverse geocoding
# reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))
# -34.4261401, 150.8953097
reverse_geocode_result = gmaps.reverse_geocode((-34.4261401, 150.8953097))
print("reverse_geocode_result", reverse_geocode_result)
# Request directions via public transit
now = datetime.now()
print("now", now)
travelMode = "transit"
origin = "Sydney Town Hall"
destination = "Wollongong, NSW"
travelMode = "transit"
directions_result = get_directions(origin, destination, travelMode)
# ujson.loads(directions_result)
# print(directions_result.bounds)
distance_matrix_result = distance_matrix(origin, destination, travelMode)
#print("isinstance  ", isinstance(distance_matrix_result, (dict)))
#print(distance_matrix_result['rows'])
#print("isinstance  ", isinstance(distance_matrix_result['rows'], (list)))
#print((distance_matrix_result['rows'])[0])
#print("isinstance  ", isinstance(((distance_matrix_result['rows'])[0]), (dict)))
print(((distance_matrix_result['rows'])[0])['elements'])
#print("isinstance  ", isinstance((((distance_matrix_result['rows'])[0])['elements']), (list)))
print((((distance_matrix_result['rows'])[0])['elements'])[0]['distance'])
# print(distance_matrix_result['duration'])
# j = json.loads(str(distance_matrix_result))
# print(j['rows'])

travelMode = "transit"
get_directions(origin, destination, travelMode)
distance_matrix(origin, destination, travelMode)

travelMode = "driving"
get_directions(origin, destination, travelMode)
distance_matrix(origin, destination, travelMode)

travelMode = "walking"
get_directions(origin, destination, travelMode)
distance_matrix(origin, destination, travelMode)

travelMode = "bicycling"
get_directions(origin, destination, travelMode)
distance_matrix(origin, destination, travelMode)
