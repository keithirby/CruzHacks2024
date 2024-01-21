# CruzHacks2024 **tuitionshock.us**

# Group Members
* Airi Kokuryo
* Dallas Meyer
* Eunice Hong
* Keith Irby
 

# Summary of **[tuitionshock.us](http://tuitionshock.us)**

Our hack, **[tuitionshock.us](http://tuitionshock.us)**, is a heatmap of the cost for community colleges and universities in the United States. 

Our goal was to show the disparity between a 2-year education and a 4-year education while also highlighting the privilege of access to higher education in more expensive cities and states. We added the following filtering options to our heatmap to help highlight cost differences:

1. Degree length
    * 4-year 
    * 2-year
    * Both 

2. School type
    * Private
    * Public
    * Both

3. Tuition type
    * In-state 
    * Out-of-state

In addition to this, we also added a list feature that can sort the schools by their costs in a descending and ascending order.

## Disclaimer

The dataset we used was provided by the U.S goverment college scorecard online tool (linked below). As is the nature of a heatmap schools without a definite address or failed to report their cost of attendance to the U.S goverment are **NOT** included in the list or as locations on the map.

link: [collegescorecard.ed.gov](collegescorecard.ed.gov)


# How was data collected? 

The data collected was pulled from the *U.S Department of Education College Scorecard* database. We collected this data using the *Open Data Maker HTTP API*, which allowed us to use HTTP queries for JSON formatted packets based on a variety of fields. Some examples of fields are a specific school, state schools only, or degree level rewarded.  

[Open Data Maker HTTP API](https://github.com/RTICWDT/open-data-maker/blob/master/API.md)

[College Scorecard API Guide](https://collegescorecard.ed.gov/data/documentation/)

# Tech Stack

Server: Flask 🚀
Database: MongoDB Atlas 📊
Frontend: HTML + CSS + JavaScript 🌐



