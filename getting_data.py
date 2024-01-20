import requests
import json

# college_name = input("Enter college name: ")

# Define the API endpoint URL
url = "https://api.data.gov/ed/collegescorecard/v1/schools.json"
params = {
    # 'school.degrees_awarded.predominant': '3',
    # 'school.ownership': '1',
    # 'school.name': f'{collesage_name}',
    # '_fields': 'id,school.name,student.size,latest.cost.tuition.in_state,latest.cost.tuition.out_of_state,location.lat,location.lon',
    '_fields': 'school.state',
    'api_key': 'aOIU3LYrzoO4z7Kaa3vqkp3UMS1to4KglDbdKyT0',
    'page': 0
}

for i in range(328):
    params['page'] = i


    #the GET request to the API
    response = requests.get(url, params=params)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:

        data = response.json()
        print(data)
        # Make the data type to string
        current_data = json.dumps(data)

    else:
        # Handle the case where the request was
        print("API request failed with status code:", response.status_code)
        print("API response content:", response.text)
    
    # # Write out the text document    
    # file_path = r'./output.txt'
    # with open(file_path, 'a') as f:
    #         f.write("Data:\n") 
    #         f.write(current_data)
