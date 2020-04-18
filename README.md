# Database_Pipeline
1) Use Python to call the OpenWeatherMap API (an API that stores weather data across the U.S) and store it in JSON. (I am calling 7 APIs for 7 different U.S cities)

2) Use Python to create a connection to an postgresql database.
3) Use Python to upload the data aquired from the api response to the database. 


*File Descriptions:
Generate_Data.py:
This Python file calls the OpenWeatheMap API, stores the responses as JSON, extracts specific data (city name, date, and temperature) and stores it all in a data frame. 

pipeline_to_database.py:
This python file establishes a connection to the postgresql database. It also takes the data frame created in Generate_data.py, and inserts the elements to a table in the database.

