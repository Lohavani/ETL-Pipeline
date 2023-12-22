import sqlite3
import File_Logger

def load_weather_data(transformed_data):
    try:
        # Create connection to SQLite DB
        conn = sqlite3.connect('Weather_Data.db')
        cursor = conn.cursor()
        #print("Hii")

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
        #print("Hello")
        #print(transformed_data.head)
        # Iterate over rows and write data to Weather table
        for index, row in transformed_data.iterrows():
            # print(row['City'])
            cursor.execute('''INSERT INTO Weather
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                            (row['City'], row['Population'], row['Latitude'], row['Longitude'], row['Timestamp'], 
                             row['Temperature (Celsius)'], row['Humidity (%)'], row['Wind Speed (m/s)'], 
                             row['Daily Average Temperature'], row['Description']))

        conn.commit()
        conn.close()
        #print("Successful")
        File_Logger.log("Info", "Data loaded to the database successfully.")

    except sqlite3.Error as e:
        File_Logger.log("Error", f"SQLite error occurred: {e}")
