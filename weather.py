# ===========
# weather.py 
# ===========
from urllib.request import urlopen
import json
def get_weather(city):
    sock = urlopen("http://api.openweathermap.org/data/2.5/weather?q=" +
        city + "&appid=885d3d78c62593e838a0429992a15300")
    result = sock.read()
    sock.close()
    weather = json.loads(result)
    return weather["main"]["temp"] -273.15
def postal_lookup(postal_code):
    sock = urlopen("http://api.postcodes.io/postcodes/" + postal_code)
    result = sock.read()
    sock.close()
    details = json.loads(result)
    return (details["result"]["latitude"], details["result"]["longitude"])
if __name__ == "__main__":
    degrees = get_weather("OSLO")
    print("Weather in Oslo is %.2f degrees Celsius" % degrees)
    location = postal_lookup("B323PP")
    print(location)

