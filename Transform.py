import pandas as pd
import Logs

def kelvin_to_celsius(data):
    return data - 273.15

def transform_weather_data(extracted_data):
    # Check for data anomalies
    extracted_data.info()
    print(extracted_data.isna().sum())
    print(extracted_data.describe())
    # Since there are no null values, there is no handling required. 

    # Convert timestamp to time and date in standard format
    extracted_data['Timestamp'] = pd.to_datetime(extracted_data['Timestamp'], unit='s')

    # Convert temperature from Kelvin and Celsius
    # cnvert to lambda function
    #extracted_data  = extracted_data.assign(extracted_data['Temperature (Kelvin)'] = lambda x: kelvin_to_celsius(extracted_data))
    #??
    for i, row in extracted_data.iterrows():
        row['Temperature (Kelvin)'] = kelvin_to_celsius(row['Temperature (Kelvin)'])
    extracted_data = extracted_data.rename(columns={"Temperature (Kelvin)": "Temperature (Celsius)"})

    # Aggregating each city's data to find average daily temperature
    extracted_data['Daily Average Temperature'] = extracted_data.groupby('City')['Temperature (Celsius)'].transform('mean')
    Logs.log("Info", "Transform process completed successfully.")
    print(extracted_data.head)