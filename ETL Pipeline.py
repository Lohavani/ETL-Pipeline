import json
import Extract
import Transform
import Load
import File_Logger

# Reading config file
params = json.load(open('ETL_Params.json'))

def main():
    # Calling ETL Pipeline
    extracted_data = Extract.extract_weather_data(params)
    print(extracted_data.shape[0])
    # Checking if data returned by Extract process is empty or not
    if (not extracted_data.empty) :
        transformed_data = Transform.transform_weather_data(extracted_data)
        Load.load_weather_data(transformed_data)
    else:
        File_Logger.log("Error", "No data returned from Extract process")

main()