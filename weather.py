# weather-bot
import requests # This library 'talks' to the internet

# Configuration
API_KEY = "7947fca397fe58e3b992b1939b40bb50"
CITY = "London" # Change this to your city!

def get_weather():
    url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
    response = requests.get(url).json()
    
    temp = response['main']['temp']
    desc = response['weather'][0]['description']
    
    report = f"### Current Weather in {CITY}: {temp}°C, {desc}"
    
    with open("README.md", "w") as f:
        f.write(f"# 🌦️ My Live Weather Dashboard\n\n{report}\n\n*Last updated automatically by GitHub Actions*")

if __name__ == "__main__":
    get_weather()
