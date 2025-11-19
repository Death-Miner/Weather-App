# Weather-Apo
Weather App - Python GUI Desktop Application A simple yet powerful Python desktop weather application that provides real-time weather forecasts and current conditions for any city worldwide. Built with Tkinter, this app offers an intuitive and modern user interface for checking weather information instantly.
# Weather App - Python GUI

A modern, user-friendly desktop weather application built with Python and Tkinter that provides real-time weather forecasts and current conditions for any city in the world.

## Features

- 🌡️ **Real-time Weather Data** - Current temperature, humidity, wind speed, and weather conditions
- 📅 **7-Day Forecast** - Daily high/low temperatures, weather conditions, and precipitation
- 🔍 **City Search** - Search weather for any city worldwide
- 🎨 **Modern GUI** - Dark-themed, clean, and professional interface
- ⚡ **Fast & Responsive** - Non-blocking weather fetching with threading
- 🆓 **Free API** - Uses Open-Meteo API (no API key required)
- 🖥️ **Cross-Platform** - Works on Windows, macOS, and Linux

## Screenshots

[Add screenshots of your app here]

## Requirements

- Python 3.6+
- requests
- pillow

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/weather-app-python.git
cd weather-app-python
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install requests pillow
```

### 3. Run the application
```bash
python weather_app_gui.py
```

## Usage

1. **Launch the app** by running the Python script
2. **Enter a city name** in the search box (e.g., "London", "New York", "Tokyo")
3. **Press Enter** or click the **Search** button
4. **View the results:**
   - Current weather with temperature and conditions
   - Humidity and wind speed information
   - 7-day forecast with daily details
5. **Search again** for different cities anytime

## How It Works

### API Integration
- **Geocoding API** - Converts city names to geographic coordinates
- **Weather API** - Fetches weather data using coordinates
- **Service** - Open-Meteo (free, no authentication required)

### Architecture
- **Threading** - Weather data fetching runs in background threads to keep GUI responsive
- **Error Handling** - Comprehensive error messages for invalid cities or connection issues
- **Real-time Updates** - Fresh data fetched on each search

## Project Structure
```
weather-app-python/
├── weather_app_gui.py      # Main application file
├── requirements.txt        # Project dependencies
└── README.md              # This file
```

## Code Overview

### Main Classes

**WeatherApp** - Main application class that handles:
- UI setup and management
- API communication
- Weather data display
- User interactions

### Key Methods

- `get_coordinates()` - Fetches latitude/longitude for a city
- `get_weather()` - Retrieves weather data from API
- `display_current_weather()` - Shows current conditions
- `display_forecast()` - Displays 7-day forecast
- `search_weather()` - Handles user search requests

## Technology Stack

- **Language** - Python 3
- **GUI Framework** - Tkinter
- **HTTP Client** - Requests
- **Image Processing** - Pillow (PIL)
- **API** - Open-Meteo Weather API

## Configuration

The app uses default colors and settings:
- Background Color: `#1e3a8a` (Dark Blue)
- Accent Color: `#fbbf24` (Yellow)
- Window Size: 900x700 pixels

You can customize these in the `WeatherApp.__init__()` method.

## Troubleshooting

### "City not found" error
- Check spelling of city name
- Try with a major city first
- Ensure internet connection is active

### App freezes
- This shouldn't happen due to threading
- If it does, wait a few seconds for API response
- Check your internet connection

### Missing dependencies
```bash
pip install --upgrade requests pillow
```

## API Information

This app uses the **Open-Meteo API** - a free weather API requiring no authentication.

- **Website** - https://open-meteo.com/
- **Documentation** - https://open-meteo.com/en/docs
- **Rate Limit** - Generous free tier (no API key required)

## Future Enhancements

- [ ] Save favorite cities
- [ ] Temperature unit toggle (Celsius/Fahrenheit)
- [ ] Weather alerts and notifications
- [ ] Historical weather data
- [ ] Export weather data to CSV
- [ ] Weather charts and graphs
- [ ] Hourly forecast
- [ ] Multiple language support

## Contributing

Contributions are welcome! Feel free to:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

Created as a Python learning project for college coursework.

## Support

If you encounter any issues or have questions:
1. Check the Troubleshooting section
2. Review the code comments
3. Open an issue on GitHub

## Disclaimer

This app relies on the Open-Meteo API for weather data. The accuracy depends on the API's data sources. Always verify important weather information from official meteorological services.

---

## Quick Start
```bash
# Clone the repo
git clone https://github.com/yourusername/weather-app-python.git

# Install dependencies
pip install -r requirements.txt

# Run the app
python weather_app_gui.py
```

That's it! Start checking weather for any city.

---

**Enjoy using Weather App! 🌤️**
```

---

Also create a `requirements.txt` file with:
```
requests==2.31.0
pillow==10.0.0
