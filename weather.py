import requests, json
response = requests.get("http://api.openweathermap.org/data/2.5/weather?q=Lahore,pk&units=metric&appid=1168fedf3708f978364bc3e35b520e83")
x = response.json()

print("The Temprature of Lahore is: " + str(x["main"]["temp"]) + " C")

print("The Humidity of Lahore is: "+str(x["main"]["humidity"])+" %")