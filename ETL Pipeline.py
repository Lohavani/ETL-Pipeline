import json
import Extract
import Transform
import Load
import Logs

# Reading config file
params = json.load(open('C:\\Users\\lose3\\OneDrive - NHS\\Python codes\\ETL\\ETL_Params.json'))

def main():
    # Calling ETL Pipeline
    extracted_data = Extract.extract_weather_data(params)
    #print(extracted_data)
    # Checking if data returned by Etract process is empty or not
    if (not extracted_data.empty) :
        transformed_data = Transform.transform_weather_data(extracted_data)
        Load.load_weather_data(transformed_data)
    else:
        Logs.log("Error", "No data returned from Extract process")

main()