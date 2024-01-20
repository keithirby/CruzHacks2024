import requests
import json
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

college_name = input("Enter college name: ")
school_name = []
tuition_in_state = []
tuition_out_of_state = []
latitude = []
longitude = []

# Define the API endpoint URL
url = "https://api.data.gov/ed/collegescorecard/v1/schools.json"
params = {
    'school.degrees_awarded.predominant': '3',
    #'school.ownership': '1',
    'school.name': f'{college_name}',
    '_fields': 'id,school.name,latest.cost.tuition.in_state,latest.cost.tuition.out_of_state,location.lat,location.lon',
    'api_key': 'aOIU3LYrzoO4z7Kaa3vqkp3UMS1to4KglDbdKyT0'
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

else:
    # Handle the case where the request was
    print("API request failed with status code:", response.status_code)
    print("API response content:", response.text)

print(f"School Name: {school_name}")
print(f"Tuition (In-State): {tuition_in_state}")
print(f"Tuition (Out-of-State): {tuition_out_of_state}")
print(f"Latitude: {latitude}")
print(f"Longitude: {longitude}")