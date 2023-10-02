import googlemaps
gmaps = googlemaps.Client(key='AIzaSyAaG7C4O6cCscvdKtYWJqqxXmo6XAhej5w')

liveloc = gmaps.geolocate()
latlng = liveloc['location']
print(latlng)

