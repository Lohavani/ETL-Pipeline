import pandas as pd
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
import json
import ETL_Logger

def extract_weather_data(params):
    API_Key = params['API_Key']
    df_weather = pd.DataFrame()
    
    try: 
        # using urllib library as requests library had ssl error
        # Using predefined list of cities from config file
        for city in params['cities'] :
            url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_Key}'  
            response = urlopen(url)
            body = response.read()

            data = json.loads(body)

            # Looping through index from 0 to number of timestamps returned per city (default 5 days and 3 hour intervals, so cnt = 40) 
            index = 0
            for index in range(0,data['cnt']): 
                dict_temp = {
                    'City': city,
                    'Population' : data['city']['population'],
                    'Latitude' : data['city']['coord']['lat'],
                    'Longitude' : data['city']['coord']['lon'],
                    'Timestamp' : data['list'][index]['dt'],
                    'Temperature (Kelvin)': data['list'][index]['main']['temp'],
                    'Humidity (%)': data['list'][index]['main']['humidity'],
                    'Wind Speed (m/s)': data['list'][index]['wind']['speed'],
                    'Description': data['list'][index]['weather'][0]['description']
                    }
                
                # Converting dictionary object to dataframe and appending each city's data to final dataframe
                df_temp = pd.DataFrame([dict_temp])
                df_weather = pd.concat([df_weather, df_temp])

        ETL_Logger.log("Info", "Extract process completed successfully.")
                    
    except HTTPError as e:
        ETL_Logger.log("Error", f"Exception HTTPError : {e.code} {e.reason}")

    except URLError as e:
        ETL_Logger.log("Error", f"Exception URLError : {e.reason}")

    return df_weather