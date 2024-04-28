import sqlite3
import ETL_Logger

def load_weather_data(transformed_data):
    try:
        # Create connection to SQLite DB
        conn = sqlite3.connect('Weather_Data.db')
        cursor = conn.cursor()

        # Converting the timestamp to string data type for writing into the database
        transformed_data['Timestamp'] = transformed_data['Timestamp'].astype(str)

        # Create Weather Table if not present with the specified columns and data types
        cursor.execute('''CREATE TABLE IF NOT EXISTS Weather (
                            City TEXT,
                            Population INTEGER,
                            Latitude REAL, 
                            Longitude REAL,
                            Timestamp TEXT,
                            "Temperature (Celsius)" REAL,
                            Humidity INTEGER,
                            WindSpeed REAL,
                            "Daily Average Temperature" REAL,
                            Description TEXT
                        )''')

        # Iterate over rows and write data to Weather table
        for index, row in transformed_data.iterrows():
            cursor.execute('''INSERT INTO Weather
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                            (row['City'], row['Population'], row['Latitude'], row['Longitude'], row['Timestamp'], 
                             row['Temperature (Celsius)'], row['Humidity (%)'], row['Wind Speed (m/s)'], 
                             row['Daily Average Temperature'], row['Description']))

        conn.commit()
        conn.close()
        ETL_Logger.log("Info", "Data loaded to the database successfully.")
        print("\nThe ETL Process has been completed successfully!\n")

    except sqlite3.Error as e:
        ETL_Logger.log("Error", f"SQLite error occurred: {e}")
