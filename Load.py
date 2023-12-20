import sqlite3
import Logs

def load_weather_data(transformed_data):
    try:
        # Create connection to SQLite DB
        conn = sqlite3.connect('C:\\Users\\lose3\\OneDrive - NHS\\Python codes\\ETL\\Weather_Data.db')
        cursor = conn.cursor()
        print("Hii")

        # Create Weather Table if not present with the specified columns and data types
        cursor.execute('''CREATE TABLE IF NOT EXISTS Weather (
                            City TEXT,
                            Population REAL,
                            Latitude REAL, 
                            Longitude REAL,
                            Timestamp INTEGER,
                            Temperature (Celsius) REAL,
                            Humidity INTEGER,
                            WindSpeed REAL,
                            Description TEXT
                        )''')
        print("Hello")

        # Iterate over rows and write data to Weather table
        for row in transformed_data:
            print(row['City'])
            cursor.execute('''INSERT INTO Weather
                            VALUES (?, ?, ?, ?, ?)''',
                            (row['City'], row['Population'], row['Latitude'], row['Longitude'], row['Temperature (Celsius)'], row['Timestamp'], 
                            row['Humidity (%)'], row['Wind Speed (m/s)'], row['Description']))

        conn.commit()
        conn.close()
        print("Successful")
        Logs.log("Info", "Data loaded to the database successfully.")

    except sqlite3.Error as e:
        Logs.log("Error", f"SQLite error occurred: {e}")
