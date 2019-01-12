import folium
import webbrowser, os
import requests, json
from geopy.geocoders import Nominatim
from folium import IFrame

api_key = "299780d5b33271a65a85a57e4ee273b5"
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# Nominatim is a tool to search data using map by name or address
geolocator = Nominatim(user_agent="specify_your_app_name_here",timeout=3)
loc = input("enter the place you want to find?")

complete_url = base_url + "appid=" + api_key + "&q=" + loc

# get method of requests module and return response object
response = requests.get(complete_url)

# json method of response object to convert json format data into python format data
x = response.json()

# x contains list of nested dictionaries
if(x["cod"]!="404"):
    y = x["main"]
    current_temp = str(format(y["temp"]-273.15,'0.2f'))
    current_humidity = str(y["humidity"])
    z = x["weather"]
    descrptn = str(z[0]["description"])


    location = geolocator.geocode(loc)
    lat = location.latitude
    long = location.longitude

    # popup text placed in iframe
    text = "CURRENT WEATHER <br> City Name: " +loc +"<br> Temperature(in celsius): " + current_temp +"<br> Humidity(in percentage): " + current_humidity + "<br> Weather Description: " + descrptn
    text_final = text
    iframe = folium.IFrame(text_final, width = 300, height = 100)
    popup = folium.Popup(iframe,max_width=3000)

    # creating map with the given location
    folium_map = folium.Map(location=[lat,long],
                            zoom_start=7)
    marker = folium.Marker(location=[lat,long],popup = popup)
    marker.add_to(folium_map)

    folium_map.save("this_map.html")


    webbrowser.open('file://' + os.path.realpath('this_map.html'))
else:
    print("Place not found")
