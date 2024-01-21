import folium 
from folium import plugins
from folium.plugins import HeatMap
from branca.colormap import linear
# import getting_data
from pymongo import MongoClient
from dotenv import load_dotenv
import os
from models.college_model import College
import logging 

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Create a logger
logger = logging.getLogger(__name__)

def add_html():
    sidebar_html = """
        <div style="position: fixed; z-index:3; top: 0; left: 0; width: 200px; height: 100%; background-color: #f5f5f5; padding: 10px;">
            <h2>Sidebar</h2>
            <p>Content goes here...</p>
            <ul>
                <li>Option 1</li>
                <li>Option 2</li>
                <li>Option 3</li>
            </ul>
        </div>

    """
    # Create an Html object with the sidebar content
    sidebar_html_obj = folium.Html(sidebar_html, script=True)

    # Create a Popup with the Html object
    popup = folium.Popup(sidebar_html_obj, max_width=300)
    return popup

def create_map():
    sidebar = add_html()   
    # Set up MongoDB URI from environment variable
    load_dotenv()
    mongo_uri = os.environ.get("DB_URL")
    client = MongoClient(mongo_uri)
    db = client['morphius']
    db_colleges = db['colleges']
    colleges = db_colleges.find()
    #data variables for colleges
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

    # Create a folium map centered around the US
    us_map = folium.Map(location=[37.7749, -95.4194], zoom_start=4)

    for c in items:
        if c.latitude == None or c.longitude == None:
            c.latitude = 0
            c.longitude = 0
        if c.tuition_out_of_state == None:
            c.tuition_out_of_state = 0
        if c.tuition_in_state == None:
            c.tuition_in_state = 0
                
    try:
        #create the maptype for each options
        #public in
        logger.debug("inside try")
        public_4yrs_in = [(c.latitude, c.longitude, c.tuition_in_state) for c in items if c.degree_length >= 3 and c.school_type == +1]        
        public_2yrs_in = [(c.latitude, c.longitude, c.tuition_in_state) for c in items if c.degree_length == 2 and c.school_type == +1]        
        public_in = [(c.latitude, c.longitude, c.tuition_in_state) for c in items if c.school_type == +1]

        #public out
        public_4yrs_out = [(c.latitude, c.longitude, c.tuition_out_of_state) for c in items if c.degree_length >= 3 and c.school_type == +1]        
        public_2yrs_out = [(c.latitude, c.longitude, c.tuition_out_of_state) for c in items if c.degree_length == 2 and c.school_type == +1]        
        public_out = [(c.latitude, c.longitude, c.tuition_out_of_state) for c in items if c.school_type == +1]

        #private
        private_4yrs = [(c.latitude, c.longitude, c.tuition_in_state) for c in items if c.degree_length >= 3 and c.school_type >= 2]        
        private_2yrs = [(c.latitude, c.longitude, c.tuition_in_state) for c in items if c.degree_length == 2 and c.school_type >= 2]        
        private = [(c.latitude, c.longitude, c.tuition_in_state) for c in items if c.school_type >= 2]

        #public and private
        all_in = [(c.latitude, c.longitude, c.tuition_in_state) for c in items]
        all_out = [(c.latitude, c.longitude, c.tuition_out_of_state) for c in items]
    except Exception as e:
        logger.debug("inside exception")
        # Code to handle other exceptions
        print(f"An error occurred: {e}")
    
    # Create a colormap based on tuition values. This is based on the out of state tuition
    colormap = linear.YlOrRd_04.scale(
        0, max(max([c.tuition_out_of_state for c in items]), 1))

    #decide maptype
    maptype = [public_in,public_4yrs_in,public_2yrs_in,public_out,public_4yrs_out,public_2yrs_out,all_in,all_out]
    mapname = ["public_in","public_4yrs_in","public_2yrs_in","public_out","public_4yrs_out","public_2yrs_out","all_in","all_out"]
    #where you make the heatmap
    for i in range(len(maptype)):
        logger.debug("inside for loop")
        HeatMap(maptype[i], radius=50, blur=50, gradient={
            0.4: 'green', 0.65: 'yellow', 1: 'red'}).add_to(us_map)
        us_map.get_root().add_child(sidebar)
        us_map.save(f'templates/{mapname[i]}.html')
        us_map = folium.Map(location=[37.7749, -95.4194], zoom_start=4)

def main():
    # Display the map
    logger.debug("inside main")
    create_map()
    
main()