import requests
from pyspark.sql import SparkSession
from pyspark.sql import Row

# Initialize Spark session
spark = SparkSession.builder.appName("WeatherAPI").getOrCreate()

# Read the API key from the file
try:
    with open('api_key.txt', 'r') as file:
        api_key = file.read().strip()
except FileNotFoundError:
    print("Error: The file 'api_key.txt' was not found.")
    exit()

# Define the base URL and city
base_url = "https://api.openweathermap.org/data/2.5/weather?"
city = "Ahmedabad"

# Construct the full URL
url = base_url + "appid=" + api_key + "&q=" + city

# Make the API request
response = requests.get(url)
data = response.json()

# Print the JSON response
print(data)

# Prepare data for DataFrame
temp_data = {
    'city': data['name'],
    'country': data['sys']['country'],
    'lon': data['coord']['lon'],
    'lat': data['coord']['lat'],
    'weather_main': data['weather'][0]['main'],
    'temp': data['main']['temp'],
    'pressure': data['main']['pressure'],
    'humidity': data['main']['humidity'],
    'wind_speed': data['wind']['speed']
}
 
temp_df = spark.createDataFrame([temp_data])
temp_df.write.mode('append').option('header', True).csv('openweathermap_temp_data')
print("CSV file has been created")