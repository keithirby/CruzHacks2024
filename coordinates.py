# Libraries for grabbing API key(s)
import os
from dotenv import load_dotenv
#Library for finding the lat and long
from geopy.geocoders import GoogleV3


def grab_key():
    # Load the .env file
    load_dotenv()

    # Grab the Google API key
    GOOGLE_KEY = os.getenv('GOOGLE_API')

    # Return the key
    return GOOGLE_KEY


def find_coordinates(KEY, address):
    geolocator = GoogleV3(api_key=KEY)
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


def main():
    KEY = grab_key()

    coordinates = find_coordinates(KEY, "Clarks Summit University")

    print(coordinates)

main()
