# Python Developer Recruitment Exercise 4 - Anton Kuksov

Create a Python script that interacts with a public weather API, fetches data for a specified city, and
displays it in a readable format.
Requirements:

### API Interaction
   - Use the OpenWeatherMap API, api.met.no or any similar weather API that provides
   current weather data for a city.
   - If the API requires an API key, the script should allow the key to be configured somehow.
### Functionality:
   1. The application should take a city name as input.
   2. Query the API for the current weather of the specified city.
   3. Parse and display the following weather information:
      - City name
      - Current temperature
      - Weather description (e.g., "clear sky," "rainy")
      - Humidity (if available)
      - Wind speed (if available)
   4. Display the temperature in both Celsius and Fahrenheit for user convenience.
### Optional:
- Allow users to request weather data for multiple cities at once.
- Cache API responses for recent city queries to avoid redundant API calls (simple inmemory caching is fine).

### Solution

I made it so that when we first enter the application, the weather data of the city that is set by default in the config is loaded. The default city can be changed on the settings page, and you can also configure the API key and save everything in the user session. The user also has a choice in which measurement system (metric or imperial) to request weather data.
To get to the main page, click on the "Weather app" in the top left corner

### Run

Run app.py in this directory to see an example of usage of the app.