import tkinter as tk
from tkinter import ttk, messagebox
import requests
import threading
from datetime import datetime
from PIL import Image, ImageTk
from io import BytesIO

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather App")
        self.root.geometry("900x700")
        self.root.config(bg="#1e3a8a")
        
     
        self.bg_color = "#1e3a8a"
        self.fg_color = "white"
        self.accent_color = "#fbbf24"
        
        self.setup_ui()
    
    def setup_ui(self):
        """Setup the user interface"""
  
        main_frame = tk.Frame(self.root, bg=self.bg_color)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        
        title_label = tk.Label(
            main_frame,
            text="Weather App",
            font=("Arial", 28, "bold"),
            bg=self.bg_color,
            fg=self.fg_color
        )
        title_label.pack(pady=10)
        
        # Search frame
        search_frame = tk.Frame(main_frame, bg=self.bg_color)
        search_frame.pack(fill=tk.X, pady=10)
        
        self.city_entry = tk.Entry(
            search_frame,
            font=("Arial", 12),
            width=40,
            relief=tk.FLAT,
            bd=2
        )
        self.city_entry.pack(side=tk.LEFT, padx=5)
        self.city_entry.bind('<Return>', lambda e: self.search_weather())
        
        search_btn = tk.Button(
            search_frame,
            text="Search",
            font=("Arial", 12, "bold"),
            bg=self.accent_color,
            fg="black",
            relief=tk.FLAT,
            cursor="hand2",
            command=self.search_weather
        )
        search_btn.pack(side=tk.LEFT, padx=5)
        
        # Current weather frame
        self.weather_frame = tk.Frame(main_frame, bg="#0f172a", relief=tk.RAISED, bd=1)
        self.weather_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # Forecast frame
        self.forecast_frame = tk.Frame(main_frame, bg=self.bg_color)
        self.forecast_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # Status label
        self.status_label = tk.Label(
            main_frame,
            text="Enter a city name and click Search",
            font=("Arial", 10),
            bg=self.bg_color,
            fg="#bfdbfe"
        )
        self.status_label.pack(pady=5)
    
    def get_coordinates(self, city_name):
        """Fetch coordinates for a city"""
        try:
            url = "https://geocoding-api.open-meteo.com/v1/search"
            params = {
                "name": city_name,
                "count": 1,
                "language": "en",
                "format": "json"
            }
            response = requests.get(url, params=params)
            data = response.json()
            
            if "results" in data and len(data["results"]) > 0:
                result = data["results"][0]
                return {
                    "lat": result["latitude"],
                    "lon": result["longitude"],
                    "name": result["name"],
                    "country": result.get("country", "")
                }
            return None
        except Exception as e:
            messagebox.showerror("Error", f"Failed to get coordinates: {str(e)}")
            return None
    
    def get_weather(self, lat, lon):
        """Fetch weather data"""
        try:
            url = "https://api.open-meteo.com/v1/forecast"
            params = {
                "latitude": lat,
                "longitude": lon,
                "current": "temperature_2m,relative_humidity_2m,weather_code,wind_speed_10m",
                "daily": "weather_code,temperature_2m_max,temperature_2m_min,precipitation_sum",
                "timezone": "auto"
            }
            response = requests.get(url, params=params)
            return response.json()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to get weather: {str(e)}")
            return None
    
    def get_weather_description(self, code):
        """Convert weather code to description"""
        codes = {
            0: "Clear sky", 1: "Mainly clear", 2: "Partly cloudy", 3: "Overcast",
            45: "Foggy", 51: "Light drizzle", 53: "Moderate drizzle", 55: "Dense drizzle",
            61: "Slight rain", 63: "Moderate rain", 65: "Heavy rain",
            71: "Slight snow", 73: "Moderate snow", 75: "Heavy snow",
            80: "Rain showers", 81: "Moderate showers", 82: "Violent showers",
            95: "Thunderstorm", 96: "Thunderstorm + hail", 99: "Thunderstorm + heavy hail"
        }
        return codes.get(code, "Unknown")
    
    def display_current_weather(self, location, current):
        """Display current weather"""
        # Clear previous content
        for widget in self.weather_frame.winfo_children():
            widget.destroy()
        
        # Location
        loc_label = tk.Label(
            self.weather_frame,
            text=f"{location['name']}, {location['country']}",
            font=("Arial", 18, "bold"),
            bg="#0f172a",
            fg=self.accent_color
        )
        loc_label.pack(pady=10)
        
        # Temperature and condition
        info_frame = tk.Frame(self.weather_frame, bg="#0f172a")
        info_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        temp_label = tk.Label(
            info_frame,
            text=f"{current['temperature_2m']}°C",
            font=("Arial", 48, "bold"),
            bg="#0f172a",
            fg=self.fg_color
        )
        temp_label.pack()
        
        condition_label = tk.Label(
            info_frame,
            text=self.get_weather_description(current['weather_code']),
            font=("Arial", 14),
            bg="#0f172a",
            fg="#bfdbfe"
        )
        condition_label.pack()
        
        # Details
        details_frame = tk.Frame(self.weather_frame, bg="#0f172a")
        details_frame.pack(fill=tk.X, padx=20, pady=10)
        
        # Humidity
        humidity_box = tk.Frame(details_frame, bg="#1e3a8a", relief=tk.RAISED, bd=1)
        humidity_box.pack(side=tk.LEFT, padx=10, fill=tk.BOTH, expand=True)
        
        tk.Label(humidity_box, text="Humidity", font=("Arial", 10), bg="#1e3a8a", fg="#bfdbfe").pack()
        tk.Label(humidity_box, text=f"{current['relative_humidity_2m']}%", font=("Arial", 14, "bold"), bg="#1e3a8a", fg=self.fg_color).pack()
        
        # Wind Speed
        wind_box = tk.Frame(details_frame, bg="#1e3a8a", relief=tk.RAISED, bd=1)
        wind_box.pack(side=tk.LEFT, padx=10, fill=tk.BOTH, expand=True)
        
        tk.Label(wind_box, text="Wind Speed", font=("Arial", 10), bg="#1e3a8a", fg="#bfdbfe").pack()
        tk.Label(wind_box, text=f"{current['wind_speed_10m']} km/h", font=("Arial", 14, "bold"), bg="#1e3a8a", fg=self.fg_color).pack()
    
    def display_forecast(self, daily):
        """Display 7-day forecast"""
        # Clear previous content
        for widget in self.forecast_frame.winfo_children():
            widget.destroy()
        
        # Title
        title_label = tk.Label(
            self.forecast_frame,
            text="7-Day Forecast",
            font=("Arial", 14, "bold"),
            bg=self.bg_color,
            fg=self.fg_color
        )
        title_label.pack(pady=5)
        
        # Forecast items
        forecast_container = tk.Frame(self.forecast_frame, bg=self.bg_color)
        forecast_container.pack(fill=tk.BOTH, expand=True)
        
        for i in range(len(daily["time"])):
            date = daily["time"][i]
            max_temp = daily["temperature_2m_max"][i]
            min_temp = daily["temperature_2m_min"][i]
            condition = self.get_weather_description(daily["weather_code"][i])
            precip = daily["precipitation_sum"][i]
            
            # Day box
            day_box = tk.Frame(forecast_container, bg="#0f172a", relief=tk.RAISED, bd=1)
            day_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
            
            # Date
            date_obj = datetime.strptime(date, "%Y-%m-%d")
            date_label = tk.Label(
                day_box,
                text=date_obj.strftime("%a\n%m/%d"),
                font=("Arial", 9, "bold"),
                bg="#0f172a",
                fg="#bfdbfe"
            )
            date_label.pack(pady=5)
            
            # Condition
            cond_label = tk.Label(
                day_box,
                text=condition,
                font=("Arial", 8),
                bg="#0f172a",
                fg=self.fg_color,
                wraplength=60
            )
            cond_label.pack(pady=3)
            
            # Temperatures
            temp_label = tk.Label(
                day_box,
                text=f"↑{max_temp}° ↓{min_temp}°",
                font=("Arial", 9, "bold"),
                bg="#0f172a",
                fg=self.accent_color
            )
            temp_label.pack()
            
            # Precipitation
            precip_label = tk.Label(
                day_box,
                text=f"💧 {precip}mm",
                font=("Arial", 8),
                bg="#0f172a",
                fg="#bfdbfe"
            )
            precip_label.pack(pady=3)
    
    def search_weather(self):
        """Search for weather"""
        city = self.city_entry.get().strip()
        
        if not city:
            messagebox.showwarning("Input Error", "Please enter a city name")
            return
        
        self.status_label.config(text="Fetching weather data...")
        self.root.update()
        
        # Run in thread to prevent freezing
        thread = threading.Thread(target=self.fetch_and_display, args=(city,))
        thread.daemon = True
        thread.start()
    
    def fetch_and_display(self, city):
        """Fetch weather and display results"""
        try:
            # Get coordinates
            location = self.get_coordinates(city)
            if not location:
                messagebox.showerror("Error", f"City '{city}' not found")
                self.status_label.config(text="City not found. Try again.")
                return
            
            # Get weather
            weather_data = self.get_weather(location["lat"], location["lon"])
            if not weather_data:
                messagebox.showerror("Error", "Could not fetch weather data")
                self.status_label.config(text="Failed to fetch weather data")
                return
            
            # Display results
            self.display_current_weather(location, weather_data["current"])
            self.display_forecast(weather_data["daily"])
            
            self.status_label.config(text=f"Weather for {location['name']}, {location['country']}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            self.status_label.config(text="An error occurred")

def main():
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()

if __name__ == "__main__":

    main()
