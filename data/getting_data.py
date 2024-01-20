import requests
import json
from dotenv import load_dotenv
import os

# college_name = input("Enter college name: ")

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

for i in range(328):
    params['page'] = i

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
