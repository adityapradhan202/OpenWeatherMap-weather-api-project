import requests as req

def kelvin_celsius(temp):
    temp = temp - 273.15
    return temp

def give_weather(lat, long, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&appid={api_key}"
    response = req.get(url).json()

    temp = kelvin_celsius(response['main']['temp'])
    feels_like = kelvin_celsius(response['main']['feels_like'])
    max_temp = kelvin_celsius(response['main']['temp_max'])
    min_temp = kelvin_celsius(response['main']['temp_min'])

    humidity = response['main']['humidity']
    weather_description = response['weather'][0]['description']

    temp = round(temp, 2)
    feels_like = round(feels_like, 2)
    max_temp = round(max_temp, 2)
    min_temp = round(min_temp, 2)
    
    print(f"Temperature: {temp} degree celsius")
    print(f"Temperature feels like: {feels_like} degree celsius")
    print(f"Max temperature: {max_temp} degree celsius")
    print(f"Min temperature: {min_temp} degree celsius")
    print(f"Humidity: {humidity}")
    print(f"Weather description: {weather_description}")
    
# Lattitude and longitude of BHOPAL, MADHYA PRADESH
lat = 23.259933
long = 77.412613

f = open("api_key.txt", "r")
api_key = f.read()

if __name__ == "__main__":

    print("For testing purpose only!")
    print("\nData fetched from the API:")
    give_weather(lat, long, api_key)



