import requests

API_KEY="85530246bdf881cd950b5edf5307074c"
BASE_URL="http://api.openweathermap.org/data/2.5/weather"

city=input("Enter a city name:",)
request_url=f"{BASE_URL}?appid={API_KEY}&q={city}"

response=requests.get(request_url)

if response.status_code==200:
    data=response.json()
    weather=data["weather"][0]["description"]
    temparature=round(data["main"]["temp"]-273.15,2)
    print("Weather",weather)
    print("Temparature",temparature,"celsius")

else:
    print("an error occured")