import psycopg2
from Generate_Data import *
#############################################################################################################################################

def get_connection():
    # Create connection to the database
    connection = psycopg2.connect(host="localhost", database="test_weather", user="postgres", password="onethrough8")

    # Print PostgreSQL Connection properties
    print('\nDatabase Connection info: ',connection.get_dsn_parameters(),"\n", sep="")

    return connection
get_connection()
#############################################################################################################################################

def insert_into_postgresql():

    # Call get_connection() to get database connection
    connection = get_connection()

    # Create a cursor so to execute queries
    cursor = connection.cursor()

    # Get the dataframe with the temperature data from Generate_Data.py
    master_city_date = main()
    print(master_city_date)

    # From here we need to read in each row of master_city_data and insert it into the database
    # cursor.execute("INSERT INTO public.weather_api_log VALUES (%s, %s, %s)", (city_name, city_date, city_temp))
    # connection.commit()
    # connection.close()

    # A counter to iterate through the rows of master_city_data
    counter_row = 0
    # A counter to iterate through the columns of master_city_data
    counter_col = 0
    # This loop goes through every row of master_city_date and inserts the element into the table in the database
    for x in master_city_date.iterrows():
        cursor.execute("INSERT INTO public.weather_api_log VALUES (%s, %s, %s)", (master_city_date.loc[counter_row][counter_col], master_city_date.loc[counter_row][counter_col+1], master_city_date.loc[counter_row][counter_col+2]))
        connection.commit()
        counter_row = counter_row + 1
        counter_col = 0

    # Close the connection
    connection.close()


insert_into_postgresql()


