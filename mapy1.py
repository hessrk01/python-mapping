
import folium
import pandas

data = pandas.read_csv("Volcanoes_USA.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000<= elevation < 3000:
        return 'orange'
    else:
        return 'red'

map=folium.Map(location=[38,-99], zoom_start=4, tiles="Mapbox Bright")
fg = folium.FeatureGroup(name="MyMap")

for lt, ln, el in zip(lat, lon, elev):
    popup = folium.Popup(str(el)+ " ft.", parse_html=True)
    fg.add_child(folium.CircleMarker(location=[lt, ln], popup=popup, color='grey', fill_opacity=0.7, fill=True,fill_color=color_producer(el)))


fg.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'yellow' if x['properties']['POP2005'] < 10000000
else  'orange' if 10000000 <= x['properties']['POP2005'] < 20000000
else 'red' if 1000000000 <= x['properties']['POP2005']
else 'green'}))
#fg.add_child(folium.GeoJson(data=(open('uscounties.json', 'r', errors='ignore').read())))

map.add_child(fg)
map.save("Map1a.html")
