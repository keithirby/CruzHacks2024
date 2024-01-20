# Purpose: This python file is a script to find database entries that are lacking latitude and longitude
# but have tutiton costs to increase the number of possible entries to our heat map.


# Libraries for grabbing API key(s)
import os
from dotenv import load_dotenv
#Library for finding the lat and long
from geopy.geocoders import GoogleV3
# Library for reading the data folder
import json



def grab_API_KEY():
    # Load the .env file
    load_dotenv()

    # Grab the Google API key
    GOOGLE_KEY = os.getenv('GOOGLE_API')

    # Return the key
    return GOOGLE_KEY


# Grabbing the Google API Key and making it a global variable to reduce calls to grab_API_KEY
KEY = grab_API_KEY()


def find_coordinates(address):
    geolocator = GoogleV3(KEY)
    # Try getting the coordinates from a address
    try:
        # Finding location using geocode
        location = geolocator.geocode(address)
        if location:
            # If found grab the latitude and longitude
            latitude = round(location.latitude, 6)
            longitude = round(location.longitude, 6)
            return latitude, longitude
        else:
            # If not found return None
            return None
    except Exception as e:
        # If an error, return None as well
        print(f"Error: {e}")
        return None


def read_json():
    file_path = 'data/null_location.txt'

    try:
        with open(file_path, 'r') as file:
            data = json.load(file)

            for entry in data:
                school_name = entry.get('school.name')
                if school_name:
                    entry['location.lat'] = 1
                    entry['location.lon'] = 1
                    print(f"Updated location for {school_name}")
                else:
                    print("School name not found in JSON entry.")

        # Write the updated data back to the file
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=2)
        
        print("Location values updated and saved to the file.")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
    except Exception as e:
        print(f"Error: {e}")


read_json()

#Sources
# thank you Jake Witcher for the .env help! https://dev.to/jakewitcher/using-env-files-for-environment-variables-in-python-applications-55a1