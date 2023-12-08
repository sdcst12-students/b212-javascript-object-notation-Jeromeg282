from urllib.parse import urlparse, parse_qs
import requests
import json
import tkinter as tk

latitude = 49.2827
longitude = -123.1207
api_url = f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m&timezone=America%2FLos_Angeles'

def get_weather_data():
    try:
        response = requests.get(api_url)
        
        if response.status_code == 200:
            data = json.loads(response.text)
            result_label.config(text=f"Weather forecast for Vancouver:\n")  
            hourly_data = data.get('hourly', {})
            
            if hourly_data:
                time = hourly_data.get('time', [])
                temperatures = hourly_data.get('temperature_2m', [])
                
                if len(time) == len(temperatures):
                    weather_data = {}  
                    current_day = None
                    
                    for i in range(len(time)):
                        day, formatted_time = time[i].split("T")
                        if day not in weather_data:
                            weather_data[day] = []
                            current_day = day
                        weather_data[current_day].append(f"Time: {formatted_time}, Temperature: {temperatures[i]}Â°C")
                    

                    for day, data in weather_data.items():
                        day_button = tk.Button(window, text=f"Day {day}", command=lambda d=day: display_weather_data(d, weather_data))
                        day_button.pack()