import folium 
import pandas as pd 


cities = pd.read_csv('worldcities.csv')

print(cities.head())

lat = list(cities['lat'])
lng = list(cities['lng'])
map = folium.Map(location = [40,-94], zoom_start = 5, tiles = "Mapbox Bright")

fg = folium.FeatureGroup(name = 'My Map')

fg.add_child(folium.Marker(location = [45.548611, -94.151944], popup = "Harvard of Central Minnesota", icon = folium.Icon(color = 'red')))
fg.add_child(folium.Marker(location = [44.928121, -93.3474], popup = "Kyle's Home", icon = folium.Icon(color = 'green')))

map.add_child(fg)

map.save("Map1.html")