# Interactive-Map
Opens the map of the place you want to see along with the current weather pop-up

### by Mehak Puri

This project creates various maps in accordance to the location we enter, opens the map in any browser and tells us the current weather of that place as a pop-up. 

## Required Libraries and Dependencies

Python 2.x is required to run this project. The Python executable should be in
your default path, which the Python installer should have set.
In this we are using a python package called *folium*. Folium is a wrapper around leaflet.js which makes beautiful interactive maps that you can view in any browser. Some other libraries including webbrowser, os, requests, json, geopy.geocoders etc would also have to be included.
 We’ll use pip to install the libraries not installed already; using your terminal (linux/osx) or command prompt (windows) type
 
 ```
  pip install --upgrade folium
 ```
 
 Also, we use *openweathermap* service for the current weather data. It is an API with JSON. To use this current weather data API, one   must need the API key.
 **Note**: User need to create an account on openweathermap.org then only can use the APIs.

## How to Run Project

Download the project zip file to you computer and unzip the file. Or clone this
repository to your desktop.

Open the text-based interface for your operating system (e.g. the terminal
window in Linux, the command prompt in Windows).

Navigate to the project directory and type in the following command:

```bash
python entertainment_center.py
```

Your default browser should launch a new tab displaying the movie trailer website.

## Extra Credit Description

* I have added the storyline of the movie to the website.

## Miscellaneous

This README document is based on a template by SteveWooding in this
Udacity forum [post](https://github.com/SteveWooding/movie-website/blob/master/README.md).
