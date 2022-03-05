import requests
from tkinter import *
import math

ciudad = input("Por favor dígame el nombre de la ciudad: ")
city_name = f"{ciudad},CO"
api_key = "api_key_from_open_weather_provided"




def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    response = requests.get(url).json()

    
    temp = response['main']['temp']
    tempC = temp - 273.15

    humidity = response['main']['humidity']

    country = response['sys']['country']
    lugar = response['name']


    print (f"{lugar}, {country}\n\n" 
    "Temperatura: {0:.2f}".format(tempC), "°C\n"
    f"Humedad: {humidity}%")



get_weather(api_key, city_name)