import folium 

map = folium.Map(location = [40,-94], zoom_start = 5, tiles = "Mapbox Bright")
map.add_child(folium.Marker(location = [45.548611, -94.151944], popup = "Harvard of Central Minnesota", icon = folium.Icon(color = 'red')))
map.add_child(folium.Marker(location = [44.928121, -93.3474], popup = "Kyle's Home", icon = folium.Icon(color = 'green')))


map.save("Map1.html")