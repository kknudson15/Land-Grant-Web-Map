'''
Geo Location map for different sets of data
Created by Kyle Knudson 
This program creates a web-based mapping for two sets of data and generates
separate layers for each of these data sets.  The map displays the set of 
land grant colleges in the United States and the populations of the countries of 
the world. The populations are broken down by groups of populations.
'''

#libraries needed to create web map and process data
import folium 
import pandas as pd 
import webbrowser
import os

def color_producer(name):
    '''
    This funcion returns the color of the markers for the map
    inputs: string name of college
    Ouputs: returns color of the marker to be used.
    '''
    if name == "Microsoft Headquarters":
        return 'blue'
    elif name == 'Harvard of Central Minnesota':
        return 'red'
    else:
        return 'green'

'''
Data collection
'''
colleges = pd.read_csv('landgrantcolleges.csv')

name = list(colleges['instnm'])
lat = list(colleges['LATITUDE (HD2017)'])
lng = list(colleges['LONGITUD (HD2017)'])


'''
Creation of the map
'''
#Uses folium to create the base layer of the web map
map = folium.Map(location = [40,-94], zoom_start = 5, tiles = "Mapbox Bright")

#Creates feature groups that elements can be added to
fg = folium.FeatureGroup(name = 'Land Based Colleges')
fgp = folium.FeatureGroup(name = 'Populations of the World')

#iterates throught the data and adds markers to the feature group
for lt, ln, nm in zip (lat, lng, name):
    fg.add_child(folium.Marker(location = [lt,ln], popup = f'{nm}', icon = folium.Icon(color = color_producer(nm))))

#Adds polygon data to the map to distinguish populations of different countries
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding = 'utf-8-sig').read(),
style_function = lambda x: {'fillColor': 'green' if x['properties']['POP2005']<1000000 
else 'yellow' if 1000000 <= x['properties']['POP2005'] < 100000000 
else 'orange' if 100000000 <= x['properties']['POP2005'] < 150000000
else 'red' }))

#Adds the feature groups to the map object
map.add_child(fg)
map.add_child(fgp)
#adds layer control so that the feature groups can be turned on/off
map.add_child(folium.LayerControl())
#Saves the map
map.save("Map1.html")

webbrowser.open('file://' + os.path.realpath('Map1.html'))