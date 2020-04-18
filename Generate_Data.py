import json
import requests
import pandas as pd
#postgress password: onethrough8
# Api Key: 0cfbea9e43e0970262b7f589b8a44bfc
# Format the display so that all of the columns and rows are able to be shown:


# Adjust the display settings so that all of the contents of the rows/columns can be seen
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

#############################################################################################################################################

def get_city_api_calls():

    column_names = ['City_Name']
    # Create the empty dataframe that will hold the city names and the corresponding api calls
    city_api_calls = pd.DataFrame(data =['Chicago', 'New York', 'Los Angeles', 'Boston', 'Miami', 'Las Vegas', 'Houston'], columns=column_names)

    # Create the extra (empty) column that hill hold the api calls
    city_api_calls['API_Calls'] = "NAN"

    #print(city_api_calls.loc[1][1])
    # Add the api call for each individual city to its correct row in the dataframe
    city_api_calls.loc[0][1] = "http://api.openweathermap.org/data/2.5/forecast?q=chicago&appid=0cfbea9e43e0970262b7f589b8a44bfc&units=imperial"
    city_api_calls.loc[1][1] = "http://api.openweathermap.org/data/2.5/forecast?q=New+York&appid=0cfbea9e43e0970262b7f589b8a44bfc&units=imperial"
    city_api_calls.loc[2][1] = "http://api.openweathermap.org/data/2.5/forecast?q=los+angeles&appid=0cfbea9e43e0970262b7f589b8a44bfc&units=imperial"
    city_api_calls.loc[3][1] = "http://api.openweathermap.org/data/2.5/forecast?q=boston&appid=0cfbea9e43e0970262b7f589b8a44bfc&units=imperial"
    city_api_calls.loc[4][1] = "http://api.openweathermap.org/data/2.5/forecast?q=miami&appid=0cfbea9e43e0970262b7f589b8a44bfc&units=imperial"
    city_api_calls.loc[5][1] = "http://api.openweathermap.org/data/2.5/forecast?q=las+vegas&appid=0cfbea9e43e0970262b7f589b8a44bfc&units=imperial"
    city_api_calls.loc[6][1] = "http://api.openweathermap.org/data/2.5/forecast?q=houston&appid=0cfbea9e43e0970262b7f589b8a44bfc&units=imperial"

    #print(city_api_calls)

    # Assign variables that will hold the api call for each city
    chicago_api_call = city_api_calls.loc[0][1]
    new_york_api_call = city_api_calls.loc[1][1]
    los_angeles_api_call = city_api_calls.loc[2][1]
    boston_api_call = city_api_calls.loc[3][1]
    miami_api_call = city_api_calls.loc[4][1]
    las_vegas_api_call = city_api_calls.loc[5][1]
    houston_api_call = city_api_calls.loc[6][1]

    # return the dataframe so that the api calls can be used by other functions
    return city_api_calls
get_city_api_calls()
#############################################################################################################################################

# This function will loop through city_api_calls and call the api's
def get_city_api_responses():
    #print('\n')
    # Call get_city_api_calls to get the list of api calls
    city_api_calls = get_city_api_calls()
    #print('**City API Calls:')
    #print(city_api_calls)

    # Create a column name
    column = ['City']
    # Create a dataframe that will hold the api response for each city
    city_api_responses = pd.DataFrame(data=['Chicago', 'New York', 'Los Angeles', 'Boston', 'Miami', 'Las Vegas', 'Houston'], columns=column)
    # Add an extra column that will hold the api response
    city_api_responses['Api_Response'] = "NAN"
    #print(city_api_responses)

    # Establish a counter to help iterate through the rows
    counter = 0
    # Loop though the 'API_Call' column in city_api_calls, call the api, and store the response in a dataframe
    for x in city_api_calls.iterrows():
        # call the api
        call_api = requests.get(city_api_calls.loc[counter][1])
        # Store the response as json
        response_json = call_api.json()
        # add the response to its corresponding city/row in the dataframe
        city_api_responses.loc[counter][1] = response_json
        # iterate to the next row
        counter = counter + 1

    #print("**City API Responses")
    #print(city_api_responses)

    # Return the api responses so that they can be called by other functions
    return city_api_responses
get_city_api_responses()
#############################################################################################################################################
# Create a dataframe that will hold the city name, date, and the temperature for each city
def get_city_names():
    #print('\n')
    name_column = ['City_Name']
    master_city_data = pd.DataFrame(data=['Chicago', 'New York', 'Los Angeles', 'Boston', 'Miami', 'Las Vegas', 'Houston'], columns=name_column)

    #print(master_city_data)
    return  master_city_data
get_city_names()
#############################################################################################################################################
# This function will get the date information from the api responses
def get_city_date():
    # Call city_api_responses so that we can get the api responses and we can extract the date of of them
    city_api_responses = get_city_api_responses()
    #print(city_api_responses)

    #print('\n')
    # Create a column name to hold the city names
    name_column = ['City_name']
    # Create a dataframe that will store the date gotten from the api responses for each city
    store_city_dates = pd.DataFrame(columns=name_column, data=['Chicago', 'New York', 'Los Angeles', 'Boston', 'Miami', 'Las Vegas', 'Houston'])
    # Create a column that will hold the date info
    store_city_dates['Date'] = 'NAN'
    #print(city_dates)

    # Create a counter that will help iterate over the rows
    counter = 0
    # Create a loop that will go through each api call for each city and extract the date information (stored in 'dt-txt')
    for x in city_api_responses.iterrows():
        # Get the api response of the specific city
        response_json = city_api_responses.loc[counter][1]
        # Look at the list embedded called 'list', it contains the date information
        response_json_list = response_json['list'][1]
        # Get the city date from the embedded list called 'dt_txt'
        city_date = response_json_list['dt_txt']
        # Store the city date information in the dataframe called sotre_city_dates
        store_city_dates.loc[counter][1] = city_date
        #
        counter = counter + 1

    #print(store_city_dates)

    # Store the date information for later use
    return store_city_dates

get_city_date()
#############################################################################################################################################

def get_city_temp():
    # Call city_api_responses to get the api responses
    city_api_responses = get_city_api_responses()

    #print('\n')
    # Create a column name that will hold the city names
    column_name = ['City_Name']
    # Create a dataframe that will hold all of the temperature data for each city
    store_city_temps = pd.DataFrame(columns=column_name, data=['Chicago', 'New York', 'Los Angeles', 'Boston', 'Miami', 'Las Vegas', 'Houston'])
    # Create a column that will store the temperature information
    store_city_temps['Temp'] = 'NAN'
    #print(store_city_temps)

    #print('\n')
    # Create a counter that will iterate through each row
    counter = 0
    # Create a loop that will gor through the api responses and extract the temperautre information for each city
    for x in city_api_responses.iterrows():
        # Get the api response
        response_json = city_api_responses.loc[counter][1]
        # Get access to the list called 'list' in the api response
        response_json_list = response_json['list'][0]
        # Get access to the list 'main', which stores the temperature information
        response_json_list_main = response_json_list['main']
        # Get the temperature data in main from 'temp' and store it in a variable
        city_temp = response_json_list_main['temp']
        # Store the temperauture for each city in its corresponding row in the dataframe
        store_city_temps.loc[counter][1] = city_temp
        # Iterate the counter
        counter = counter + 1

    #print(store_city_temps)

    # Return the dataframe so that it can be used later
    return store_city_temps
get_city_temp()
#############################################################################################################################################
# Store the city name, date and temperature information for each city in a single dataframe
def main():
    city_api_responces = get_city_api_responses()
    # Get the city names (the variable with the city names will be called 'master_city_data' because the date and temp data will be added on to it)
    master_city_data = get_city_names()
    # Get the city dates
    city_dates = get_city_date()
    # Get the city temps
    city_temps = get_city_temp()

    #print(city_api_responces)
    # Print out the separate date abd temperature information
    #print('\n**City Dates:\n', city_dates, '\n\n**City Temperature:\n', city_temps, sep="")

    # Add the column containing the date information to the master_city_data
    master_city_data['Date'] = city_dates['Date']

    # Add the column containing the temperature information to the master_city_data
    master_city_data['Temp'] = city_temps['Temp']

    #print('\n**All City Data:\n', master_city_data, sep="")

    # Return master_city_data for future use
    return master_city_data
main()

