import folium
import webbrowser as wb

harita = folium.Map(location=[30.550718,-97.8075392],zoom_start=10, min_zoom=0, max_zoom=100)



folium.Marker(location=[30.550718,-97.8075392],tooltip="Home",popup="My House 512-293-7094").add_to(harita)
folium.Marker(location=[30.5285267,-97.9448106],tooltip="Target",popup="Target 512-456-2933").add_to(harita)
folium.Marker(location=[30.4451569,-97.7869468],tooltip="Main Event",popup="Main Event 512-401-0000").add_to(harita)
folium.Marker(location=[30.3818034,-97.6894034],tooltip="Peace Bakery",popup="Peace Bakery 512-386-1152").add_to(harita)
folium.Marker(location=[30.5669626,-97.8211152],tooltip="Wiley Middle School",popup="Wiley Middle School 512-570-3600").add_to(harita)
harita.save("aliharita.html")
wb.open("aliharita.html")