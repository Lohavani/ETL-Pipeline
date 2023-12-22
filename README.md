# ETL-Pipeline

This repository contains the code to run an ETL Pipeline to fetch weather data from OpenWeatherMap API, process it, and load it to an SQLite database. 

## Repository structure -
* ETL_Pipeline.py - Main file to run the ETL process
* ETL_Params.json - Contains the parameters required and sensitive data
* Extract.py, Load.py, Transform.py - Modules of the ETL pipeline
* ETL_Logger.py - File that handles the logging part of the pipeline
* ETL_Logs.log - Contains the log output from the pipeline
* Unit_Testing.py - Testing file 

## Steps to run the file -
* Run the main ETL_Pipeline file. This imports the Extract, Transform and Load modules written in separate files to manage the readability and reusability of the code.
* After the ETL Pipeline is run, the terminal shows data validation output from the Transform module. Upon successfully running the pipeline, the terminal shows output that the process has been completed.
* The ETL_Logs file contains the logs from each module and can be analyzed for monitoring and performance metrics.
* After the ETL pipeline has run, a Weather_Data.db file will be created in the same folder as the codebase. This file can be opened using SQLite Viewer in Visual Studio to see the Weather table. It should have 9 columns and 200 records for a single run of this pipeline.
* Testing - The Unit_Testing file should be run separately to check the temperature conversion function which is part of the Transform module. The terminal output shows OK when the tests have been run successfully. If there is any error, it will be shown in the terminal output. 

## Dependencies required -
* Python 3 version should be installed on the system.
* Visual Studio code to view the code and make changes.
* Libraries used by the code - pandas, json, unittest, urllib, sqlite3. If these are not present, run the pip command to install these libraries.
    pip install "dependency-name"
* To view the SQLite DB, install the SQLite Viewer Extension in Visual Studio Code.
