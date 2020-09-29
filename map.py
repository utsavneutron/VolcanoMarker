import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])


def color_change(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 2000:
        return 'orange'
    elif 2000 <= elevation < 3000:
        return 'pink'

    else:
        return 'red'


map = folium.Map(location=[38.58, -84], zoom_start=8)

fg = folium.FeatureGroup(name="Volcano")


for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.Marker(location=[lt, ln],
                               popup=str(el)+"m", icon=folium.Icon(color=color_change(el))))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(
    data=(open('world.json', 'r', encoding='utf-8-sig').read())))


map.add_child(fg)
map.add_child(fgp)

map.add_child(folium.LayerControl())
map.save("map1.html")
