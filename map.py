import folium 

map = folium.Map(location = [45,-94], zoom_start = 10, tiles = "Mapbox Bright")


map.save("Map1.html")