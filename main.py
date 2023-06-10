import requests
import datetime
from api import token_weather
from pprint import pprint

def get_weather(city, token_weather):
    smile_code = {
        "clear": "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "Rain": "Дождь \U00002614",
        "Drizzle": "Дождь \U00002614",
        "Snow": "Снег \U0001F328",
        "Mist": "Туман \U0001F32B",
    }

    try:
        r = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={token_weather}&units=metric&lang={"ru"}'
        )
        data = r.json()
        pprint(data)

        name = data['name']
        weather_temp = data['main']['temp']
        weather_description = data["weather"][0]["main"]
        descr = smile_code.get(weather_description, "Посмотрите в окно")
        weather_humidity = data['main']['humidity']
        weather_pressure = data['main']['pressure']
        weather_speed = data['wind']['speed']
        sunrise = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset = datetime.datetime.fromtimestamp(data['sys']['sunset'])
        daylight = sunset - sunrise

        print(f'*** {datetime.datetime.now().strftime("%Y-%m-%d %H:%M")} ***')
        print(f'Погода в городе: {name}')
        print(f'Состояние погоды: {descr}')
        print(f'Температура: {weather_temp}°C')
        print(f'Влажность: {weather_humidity}%')
        print(f'Давление: {weather_pressure} мм.рт.ст')
        print(f'Скорость ветра: {weather_speed}')
        print(f'Рассвет: {sunrise} 🌅')
        print(f'Закат: {sunset} 🌇')
        print(f'Продолжительность дня: {daylight}')

    except Exception as ex:
        print(ex)
        print("Проверьте название города")

def main():
    city = input("Введите город: ")
    get_weather(city, token_weather)

if __name__ == "__main__":
    main()
