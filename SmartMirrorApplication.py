import requests
import datetime
from Tkinter import *

geo_url = 'http://api.ipstack.com/check?access_key=dde7fcd3d5c26804500b409423f037d9&format=1'
geo_json = requests.get(geo_url).json()
latitude = geo_json['latitude']
longitude = geo_json['longitude']

window = Tk()
window.configure(background="black", cursor="none")
window.attributes("-fullscreen", True)
window.bind("<Escape>", lambda e: window.quit())

api_address = 'https://openweathermap.org/data/2.5/weather?lat='
api_address += str(latitude)
api_address += '&lon='
api_address += str(longitude)
api_address += '&appid=b6907d289e10d714a6e88b30761fae22'
json_data = requests.get(api_address).json()
print(json_data)
MainWeather = json_data['weather'][0]["main"]
WeatherDescription = json_data['weather'][0]['description']
CityName = json_data['name']
Temperature = json_data['main']['temp']
High = json_data['main']['temp_max']
Low = json_data['main']['temp_min']
Temperature *= (9/5)
Temperature += 32
TempStr = str(int(Temperature))
High *= (9/5)
High += 32
Low *= (9/5)
Low += 32

TempLbl = Label(window, text = TempStr)
TempLbl.configure(bg="black", fg="white", font=("Times New Roman", 72))
TempLbl.place(x=10, y=15, width=100, height=100)

lbl = Label(window, text=MainWeather+'\n'+WeatherDescription+'\n'+CityName)
lbl.configure(bg="black", fg="white", font=("Times New Roman", 16))
lbl.place(x=10, y=125, width=100, height=70)

clock = Label(window)
clock.configure(bg="black", fg="white", font=("Denmark", 44))
clock.place(x=1100, y=25, width=300, height=60)


def tick():
    current_dt = datetime.datetime.now()
    clock.configure(text=current_dt.strftime("%I:%M %p"))
    clock.after(200, tick)


tick()
window.mainloop()
