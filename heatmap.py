import folium
from folium.plugins import HeatMap
from branca.colormap import linear
import getting_data
# Example data from the API responsea
latitude = getting_data.latitude # Example latitudes
longitude = getting_data.longitude  # Example longitudes
tuition_in_state = getting_data.tuition_in_state  # Replace with the actual tuition data

# Create a folium map centered around the US
us_map = folium.Map(location=[37.7749, -95.4194], zoom_start=4)

# Create HeatMap data using the latitude, longitude, and tuition data
heat_data = list(zip(latitude, longitude, tuition_in_state))

# Create a colormap based on tuition values
colormap = linear.YlOrRd_04.scale(0, max(max(tuition_in_state), 1))  # Adjust scale based on your data

# Add HeatMap layer
HeatMap(heat_data, radius=50, blur=50, gradient={0.4: 'yellow', 0.65: 'orange', 1: 'red'}).add_to(us_map)

# Display the map
us_map.save('colored_heatmap_geojson.html')
