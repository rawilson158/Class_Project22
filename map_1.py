import folium
import requests
import os

# Create map object
m = folium.Map(location=[40.682097, -73.896606], zoom_start=12) 


# Global Tooltip
tooltip = 'Click For More Info'

# To create a custom icon, if needed
'''
logoIcon = folium.features.CustomIcon('logo.png', icon_size=(50, 50))

folium.Marker([40.705691, -73.996358], 
               popup="<strong>Name of logo goes here</strong>",
               tooltip=tooltip,
               icon=logoIcon)).add_to(m)                            
'''

# Geojson Data
overlay = os.path.join('data', 'overlay.json')

# Create Markers
folium.Marker([40.682097, -73.896606], 
               popup="<strong>Brooklyn, New York (B'Way Junc.)</strong>",
               tooltip=tooltip).add_to(m),
folium.Marker([40.693664, -73.992071], 
               popup="<strong>Osborne Association - Support Center</strong>",
               tooltip=tooltip,
               icon=folium.Icon(icon='cloud')).add_to(m),
folium.Marker([40.67546, -73.89706], 
               popup="<strong>Women's Prison Assoc. - Support Center</strong>",
               tooltip=tooltip,
               icon=folium.Icon(color='purple')).add_to(m)
folium.Marker([40.659026, -73.950207], 
               popup="<strong>LGBTQ - Health Services</strong>",
               tooltip=tooltip,
               icon=folium.Icon(color='purple')).add_to(m),
folium.Marker([40.66624, -73.957349], 
               popup="<strong>Medgar Evers College</strong>",
               tooltip=tooltip,
               icon=folium.Icon(icon='cloud')).add_to(m),
folium.Marker([40.656583, -73.94471], 
               popup="<strong>Healthfirst - Health Insurance</strong>",
               tooltip=tooltip,
               icon=folium.Icon(color='green', icon='leaf')).add_to(m)                            

# Create Circle marker
folium.CircleMarker(
location=[40.673234, -73.951072],
radius=75,
popup="Crown Heights/ Bedford-Stuyvesant",
color='#428bca',
fill=True,
fill_color='#428bca'    
).add_to(m)


# Geojson overlay
# folium.GeoJson(overlay, name='brooklyn').add_to(m)

# Generate Map
m.save('map.html')

m

# Brooklyn, NY (Myrtle Ave & Wyckoff Ave) -- 40.987384, -73.156735
# Osborne Association -- 	40.693664	-73.992071
# Women's Prison Assocation --	40.67546	-73.89706
# Workforce1 Career Center - Downtown Brooklyn --	40.679434	-73936198
# America Works --	40.705691	-73.996358
# Medgar Evers College --	40.66624	-73.957349
# Kingsborough Community College --	40.578349	-73.934465
# Community Health Network --	40.659026	-73.950207

# Use Icon Libraries to make changes to the icon styling
