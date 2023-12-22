import unittest  # Import the unittest module for writing and running unit tests.
from unittest.mock import patch  # Import the patch function from unittest.mock module for mocking objects.
import Extract
import Transform
import Load

class TestETLIntegration(unittest.TestCase):  # Create a test class inheriting from unittest.TestCase.

    @patch('Extract.requests.get')  # Use the patch decorator to mock the requests.get method.
    def test_etl_flow(self, mock_get):  # Define a test method that will run the ETL flow test.

        # Mock API response with a dictionary representing weather data.
        mock_response = {'name': 'TestCity', 'main': {'temp': 290, 'humidity': 75}, 'wind': {'speed': 5}, 'weather': [{'description': 'Cloudy'}]}

        # Set the return values for the mocked requests.get method.
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response
        
        # Call the ETL functions: fetch_weather_data, transform_data, load_data_to_db.
        api_key = 'your_api_key'
        cities = ['TestCity']
        weather_data = fetch_weather_data(api_key, cities)  # Fetch weather data for 'TestCity'.
        transformed_data = transform_data(weather_data)  # Transform the fetched data.
        load_data_to_db(transformed_data, 'test_db.sqlite')  # Load transformed data into the database.

        # Assertions to check if data loaded correctly into the database.
        conn = sqlite3.connect('test_db.sqlite')  # Connect to the test database.
        cursor = conn.cursor()  # Create a cursor object to execute SQL queries.
        cursor.execute('''SELECT * FROM Weather WHERE City = ?''', ('TestCity',))  # Execute a query to select data for 'TestCity'.
        result = cursor.fetchone()  # Fetch the first row of the query result.
        conn.close()  # Close the database connection.

        # Assert statements to validate the fetched data matches the expected values.
        self.assertIsNotNone(result)  # Check if any data was fetched for 'TestCity'.
        self.assertEqual(result[0], 'TestCity')  # Check if the city name matches 'TestCity'.
        self.assertAlmostEqual(result[1], 16.85, places=2)  # Check if the temperature matches approximately 16.85°C.
        self.assertEqual(result[2], 75)  # Check if the humidity matches 75%.
        self.assertAlmostEqual(result[3], 5.0, places=1)  # Check if the wind speed matches approximately 5.0 m/s.
        self.assertEqual(result[4], 'Cloudy')  # Check if the weather description matches 'Cloudy'.

if __name__ == '__main__':
    unittest.main()  # Run the tests when the script is executed.
