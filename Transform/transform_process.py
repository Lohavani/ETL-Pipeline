import pandas as pd
import ETL_Logger

def kelvin_to_celsius(extracted_data):
    if isinstance(extracted_data, pd.DataFrame) :
        return extracted_data['Temperature (Kelvin)'] - 273.15
    if int(extracted_data)==extracted_data :
        return extracted_data - 273.15

def transform_weather_data(extracted_data):
    # Check for data anomalies
    # Data Validation
    print("\nChecking the extracted data information - ")
    extracted_data.info()
    print("\n\nChecking if extracted data has N/A values - ")
    print(extracted_data.isna().sum())
    print("\n\nDescribing the extracted data - ")
    print(extracted_data.describe())
    # Since there are no null values as can be seen in the output, there is no handling required. 

    # Convert timestamp to time and date in standard format
    extracted_data['Timestamp'] = pd.to_datetime(extracted_data['Timestamp'], unit='s')

    # Convert temperature from Kelvin and Celsius
    extracted_data['Temperature (Kelvin)'] = kelvin_to_celsius(extracted_data)
    extracted_data = extracted_data.rename(columns={"Temperature (Kelvin)": "Temperature (Celsius)"})

    # Round the 'Temperature (Celsius)' column to 2 decimal places
    extracted_data['Temperature (Celsius)'] = extracted_data['Temperature (Celsius)'].round(2)

    # Aggregating each city's data to find average daily temperature
    extracted_data['Daily Average Temperature'] = extracted_data.groupby('City')['Temperature (Celsius)'].transform('mean')

    # Round the 'Daily Average Temperature' column to 2 decimal places
    extracted_data['Daily Average Temperature'] = extracted_data['Daily Average Temperature'].round(2)

    ETL_Logger.log("Info", "Transform process completed successfully.")

    return extracted_data