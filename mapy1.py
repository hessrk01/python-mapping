
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


map.add_child(fg)
map.save("Map1a.html")
