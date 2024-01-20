import requests
import json
<<<<<<< HEAD:data/getting_data.py
from dotenv import load_dotenv
import os
=======
import logging
>>>>>>> 1470e6981198bf7344feba76a151fb447f2569bc:getting_data.py

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

college_name = input("Enter college name: ")
school_name = []
tuition_in_state = []
tuition_out_of_state = []
latitude = []
longitude = []

load_dotenv()
api_key = os.environ.get("GOV_API")

# Define the API endpoint URL
url = "https://api.data.gov/ed/collegescorecard/v1/schools.json"
params = {
    # 'school.degrees_awarded.predominant': '3',
    # 'school.ownership': '1',
    # 'school.name': f'{collesage_name}',
    '_fields': 'id,school.name,student.size,school.state,latest.cost.tuition.in_state,latest.cost.tuition.out_of_state,location.lat,location.lon,school.ownership,school.degrees_awarded.highest',
    'api_key': api_key,
    'page': 0,
    'per_page': 100,
}
#the GET request to the API
response = requests.get(url, params=params)

# Check if the request was successful (status code 200)
if response.status_code == 200:
##########################
###send this to the db ###
##########################
        
    data = response.json()
    # Make the data type to string
    parsed_data = json.dumps(data)
    parsed_data = json.loads(parsed_data)
    #how many universities will there be?
    x = len(parsed_data[:]['school.name'])
    for i in range(x):
        school_name.append(parsed_data['results'][i]['school.name'])
        tuition_in_state.append(parsed_data['results'][i]['latest.cost.tuition.in_state'])
        tuition_out_of_state.append(parsed_data['results'][i]['latest.cost.tuition.out_of_state'])
        latitude.append(parsed_data['results'][i]['location.lat'])
        longitude.append(parsed_data['results'][i]['location.lon'])

    # the GET request to the API
    response = requests.get(url, params=params)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:

        data = response.json()
        # print(data)
        # Make the data type to string
        current_data = json.dumps(data)

    else:
        # Handle the case where the request was
        print("API request failed with status code:", response.status_code)
        print("API response content:", response.text)

    # Write out the text document
    file_path = r'./output.txt'
    with open(file_path, 'a') as f:
        f.write(current_data)
        f.write('\n')

    if current_data == None:
        break
