import folium
import requests
import os

# Create map object
m = folium.Map(location=[40.682097, -73.896606], zoom_start=12, control_scale=True) 


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
overlay = os.path.join('C:/Users/Robert Wilson/Documents/Class_Project22/map_data', 'overlay.json')

# Create Markers
folium.Marker([40.811911, -73.920396], 
               popup="<strong>Abraham House - Transitional Housing</strong>",
               tooltip=tooltip).add_to(m),
folium.Marker([40.76, -73.94], 
               popup="<strong>Hour Children - Communal Housing for Women & Children</strong>",
               tooltip=tooltip).add_to(m),               
folium.Marker([40.828331, -73.951329], 
               popup="<strong>Fortune Society - Permanent/ Scatter-Site</strong>",
               tooltip=tooltip,
               icon=folium.Icon(icon='cloud')).add_to(m),
folium.Marker([40.788622, -73.945634], 
               popup="<strong>DOE Fund - Single Apts & Dorms</strong>",
               tooltip=tooltip,
               icon=folium.Icon(color='purple')).add_to(m)
folium.Marker([40.659026, -73.95021], 
               popup="<strong>LGBTQ - Health Services</strong>",
               tooltip=tooltip,
               icon=folium.Icon(color='purple')).add_to(m),
folium.Marker([40.796534, -73.9313], 
               popup="<strong>Acacia Network - Short-term housing for wormen</strong>",
               tooltip=tooltip,
               icon=folium.Icon(icon='cloud')).add_to(m),
folium.Marker([40.689352, -73.983035], 
               popup="<strong>Workforce1 Career Center - Downtown Brooklyn</strong>",
               tooltip=tooltip).add_to(m), 
folium.Marker([40.685738, -73.97355], 
               popup="<strong>Brooklyn Tech. HS - Primary Edu</strong>",
               tooltip=tooltip).add_to(m),                  
folium.Marker([40.705132, -74.009258], 
               popup="<strong>Fullstack Academy Inc - Software Coding</strong>",
               tooltip=tooltip,
               icon=folium.Icon(color='purple')).add_to(m)                             
folium.Marker([40.656583, -73.94471], 
               popup="<strong>Healthfirst - Health Insurance</strong>",
               tooltip=tooltip,
               icon=folium.Icon(color='green', icon='leaf')).add_to(m)           
                 

# Create Circle marker
# folium.CircleMarker(
# location=[40.673234, -73.951072],
# radius=75,
# popup="Crown Heights/ Bedford-Stuyvesant",
# color='#428bca',
# fill=True,
# fill_color='#428bca'    
# ).add_to(m)


# Geojson overlay
folium.GeoJson(overlay, name='New York City').add_to(m)

# Generate Map
m.save('map.html')

m

# Use Icon Libraries to make changes to the icon styling
