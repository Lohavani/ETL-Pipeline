import json
import Extract
import Transform
import Load
import ETL_Logger

# Reading config file
# Config file used to handle sensitive data and predefined parameters
params = json.load(open('ETL_Params.json'))

def main():
    # Calling ETL Pipeline
    # This file can be invoked through a cron file for scheduled run at specific intervals
    extracted_data = Extract.extract_weather_data(params)

    # Checking if data returned by Extract process is empty or not
    if (not extracted_data.empty) :
        transformed_data = Transform.transform_weather_data(extracted_data)
        Load.load_weather_data(transformed_data)
    else:
        ETL_Logger.log("Error", "No data returned from Extract process")

if __name__ == '__main__':
    main()