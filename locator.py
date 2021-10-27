import geocoder, folium

g = geocoder.ip("me")

myAddress = g.latlng
my_map1 = folium.Map(location=myAddress, zoom_start=15)

my_map1.save("my_ip_location.html")
