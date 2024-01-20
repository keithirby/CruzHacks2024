from flask import Flask, render_template
from pymongo import MongoClient
from dotenv import load_dotenv
import os
from models.college_model import College

app = Flask(__name__)

# Set up MongoDB URI from environment variable
load_dotenv()
mongo_uri = os.environ.get("DB_URL")

client = MongoClient(mongo_uri)
db = client['morphius']

db_colleges = db['colleges']

# Check if the connection to MongoDB is successful
if db_colleges != None:
    print("Connected to MongoDB")
else:
    print("Failed to connect to MongoDB")


@app.route('/')
def index():
    # Fetch data from MongoDB using the data model
    colleges = db_colleges.find()
    items = [College(id=college['id'],
                     school_name=college['school.name'],
                     student_size=college['student.size'],
                     state=college['school.state'],
                     tuition_in_state=college['latest.cost.tuition.in_state'],
                     tuition_out_of_state=college['latest.cost.tuition.out_of_state'],
                     latitude=college['location.lat'],
                     longitude=college['location.lon'],
                     school_type=college['school.ownership'],
                     #  degree_length=college['latest.academics.progdram_reporter.program']
                     )
             for college in colleges]
    return render_template('index.html', colleges=items)


if __name__ == "__main__":
    app.run(debug=True)
