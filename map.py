import folium 
import pandas as pd 


colleges = pd.read_csv('landgrantcolleges.csv')

print(colleges.head())

name = list(colleges['instnm'])
lat = list(colleges['LATITUDE (HD2017)'])
lng = list(colleges['LONGITUD (HD2017)'])

def color_producer(name):
    if name == "Kyle's Home":
        return 'blue'
    elif name == 'Harvard of Central Minnesota':
        return 'red'
    else:
        return 'green'
map = folium.Map(location = [40,-94], zoom_start = 5, tiles = "Mapbox Bright")

fg = folium.FeatureGroup(name = 'My Map')

for lt, ln, nm in zip (lat, lng, name):
    fg.add_child(folium.Marker(location = [lt,ln], popup = f'{nm}', icon = folium.Icon(color = color_producer(nm))))

fg.add_child(folium.GeoJson(data=open('world.json', 'r', encoding = 'utf-8-sig').read(),
style_function = lambda x: {'fillColor': 'green' if x['properties']['POP2005']<1000000 
else 'yellow' if 1000000 <= x['properties']['POP2005'] < 100000000 
else 'orange' if 100000000 <= x['properties']['POP2005'] < 150000000
else 'red' }))



map.add_child(fg)

map.save("Map1.html")