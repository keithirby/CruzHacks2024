import folium
from folium.plugins import HeatMap
from branca.colormap import linear
# import getting_data
from flask import Flask, render_template
from pymongo import MongoClient
from dotenv import load_dotenv
import os
from app.models.college_model import College

app = Flask(__name__)

# Set up MongoDB URI from environment variable
load_dotenv()
mongo_uri = os.environ.get("DB_URL")

client = MongoClient(mongo_uri)
db = client['morphius']

db_colleges = db['colleges']
colleges = db_colleges.find()

items = [College(id=college['id'],
                 school_name=college['school.name'],
                 student_size=college['student.size'],
                 state=college['school.state'],
                 tuition_in_state=college['latest.cost.tuition.in_state'],
                 tuition_out_of_state=college['latest.cost.tuition.out_of_state'],
                 latitude=college['location.lat'],
                 longitude=college['location.lon'],
                 school_type=college['school.ownership'],
                 degree_length=college['school.degrees_awarded.highest']
                 )
         for college in colleges]

# # Example data from the API responsea
# latitude = getting_data.latitude  # Example latitudes
# longitude = getting_data.longitude  # Example longitudes
# # Replace with the actual tuition data
# tuition_in_state = getting_data.tuition_in_state

# Create a folium map centered around the US
us_map = folium.Map(location=[37.7749, -95.4194], zoom_start=4)

# Create HeatMap data using the latitude, longitude, and tuition data
# heat_data = list(zip(items.latitude, items.longitude,
#                  items.tuition_in_state))
heat_data = [(c.latitude, c.longitude, c.tuition_in_state) for c in items]

# Create a colormap based on tuition values
# Adjust scale based on your data
colormap = linear.YlOrRd_04.scale(
    0, max(max([c.tuition_in_state for c in items]), 1))

# Add HeatMap layer
HeatMap(heat_data, radius=50, blur=50, gradient={
        0.4: 'yellow', 0.65: 'orange', 1: 'red'}).add_to(us_map)

# Display the map
us_map.save('colored_heatmap_geojson.html')
