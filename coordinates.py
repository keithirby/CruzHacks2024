# Purpose: This python file is a script to find database entries that are lacking latitude and longitude
# but have tutiton costs to increase the number of possible entries to our heat map.


# Libraries for grabbing API key(s)
import os
from dotenv import load_dotenv
#Library for finding the lat and long
from geopy.geocoders import GoogleV3



def grab_API_KEY():
    # Load the .env file
    load_dotenv()

    # Grab the Google API key
    GOOGLE_KEY = os.getenv('GOOGLE_API')

    # Return the key
    return GOOGLE_KEY


def grab_DB_URL():
    #load the .env file
    load_dotenv()

    # Grab the DB URL
    DB_URL = os.getenv("DB_URL")

    return DB_URL




# Grabbing the Google API Key and making it a global variable to reduce calls to grab_API_KEY
KEY = grab_API_KEY()

# Grabbing the DB URL and making it a global variable to reduce calls to grab_DB_URL
URL = grab_DB_URL()

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

def open_db()




#Sources
# thank you Jake Witcher for the .env help! https://dev.to/jakewitcher/using-env-files-for-environment-variables-in-python-applications-55a1