# Libraries for grabbing API key(s)
import os
from dotenv import load_dotenv


def grab_key():
    # Load the .env file
    load_dotenv()

    # Grab the Google API key
    GOOGLE_KEY = os.getenv('GOOGLE_API')

    # Return the key
    return GOOGLE_KEY
