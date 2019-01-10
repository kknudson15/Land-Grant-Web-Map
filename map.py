import folium 
import pandas as pd 


colleges = pd.read_csv('landgrantcolleges.csv')

print(colleges.head())

name = list(colleges['instnm'])
lat = list(colleges['LATITUDE (HD2017)'])
lng = list(colleges['LONGITUD (HD2017)'])
map = folium.Map(location = [40,-94], zoom_start = 5, tiles = "Mapbox Bright")

fg = folium.FeatureGroup(name = 'My Map')

for lt, ln, nm in zip (lat, lng, name):
    fg.add_child(folium.Marker(location = [lt,ln], popup = f'{nm}', icon = folium.Icon(color = 'blue')))

fg.add_child(folium.Marker(location = [45.548611, -94.151944], popup = "Harvard of Central Minnesota", icon = folium.Icon(color = 'red')))
fg.add_child(folium.Marker(location = [44.928121, -93.3474], popup = "Kyle's Home", icon = folium.Icon(color = 'green')))

map.add_child(fg)

map.save("Map1.html")