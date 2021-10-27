import geocoder, folium

g = geocoder.ip("103.85.207.139")

myAddress = g.latlng
my_map1 = folium.Map(location=myAddress, zoom_start=15)

my_map1.save("my_map.html")
