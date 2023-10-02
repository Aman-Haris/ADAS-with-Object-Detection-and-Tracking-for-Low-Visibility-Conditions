import googlemaps
gmaps = googlemaps.Client(key='AIzaSyAaG7C4O6cCscvdKtYWJqqxXmo6XAhej5w')


start = {'lat': 12.9564672, 'lng': 77.594624}
end = 'Royal Meenakshi Mall'
directions = gmaps.directions(start, end, mode='driving', units='metric',  optimize_waypoints=True) 

print(directions)
