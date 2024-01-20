import requests
import json

# college_name = input("Enter college name: ")

# Define the API endpoint URL
url = "https://api.data.gov/ed/collegescorecard/v1/schools.json"
params = {
    'school.degrees_awarded.predominant': '2,3',
    'school.ownership': '1,2',
    # 'school.name': f'{college_name}',
    'school.state_fips': '6',
    'per_page':'720', # adjusts query size
    '_fields': 'school.name,latest.cost.tuition.in_state,latest.cost.tuition.out_of_state,location.lat,location.lon',
    'api_key': 'aOIU3LYrzoO4z7Kaa3vqkp3UMS1to4KglDbdKyT0'
}
#the GET request to the API
response = requests.get(url, params=params)

# Check if the request was successful (status code 200)
data =""
if response.status_code == 200:

    data = response.json()
    # print(data)
    # Make the data type to string
    current_data = json.dumps(data, indent=2)
 
    # Write out the text document
    file_path = 'output.json'
    with open(file_path, 'w') as f:
        f.write(current_data)
else:
    # Handle the case where the request was
    print("API request failed with status code:", response.status_code)
    print("API response content:", response.text)

