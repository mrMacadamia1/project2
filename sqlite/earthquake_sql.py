import requests
import sqlite3

def save_earthquakes(place_magnitude_list):
	conn = sqlite3.connect("earthquakes_db.db")
	cursor = conn.cursor()
	cursor.execute("CREATE TABLE earthquakes (place TEXT, magnitude REAL")
	cursor,executemany("INSERT INTO earthquakes VALUES (?, ?)", place_magnitude_list)
	conn.commit()
	conn.close()


url = 'http://earthquake.usgs.gov/fdsnws/event/1/query?'

start_time = input('enter the start time')
end_time = input('enter the end time')
latitude = input('enter the latitude')
longitude = input('enter the longitude')
max_radius_km = input('enter the max radius in km')
min_magnitude = input('enter the min magnitude')

response = requests.get(url, headers = {'Accept':'application/json'}, params = {
	'format':'gepjson',
	'starttime':start_time,
	'endtime':end_time,
	'latitude':latitude,
	'longitude':longitude,
	'maxradiuskm':max_radius_km,
	'minmagnitude':min_magnitude

	})

data = response.json()
earthquake_list = data['features']
place_magnitude_list = []
count=0
for earthquake in  earthquake_list:
	count+=1
	# print(f"{count}. Place: {earthquake['properties']['place']}. Magnitude: {earthquake['properties']['mag']}.")
	place_magnitude_list.append((earthquake['properties']['place'],earthquake['properties']['mag']))

save_earthquakes(place_magnitude_list)