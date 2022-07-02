import requests
import datetime
from api import token_bot, token_weather
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token=token_bot)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Напишите название города и я дам сводку погоды!")


@dp.message_handler()
async def get_weather(message: types.Message):

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
            f'https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={token_weather}&units=metric&lang={"ru"}'

        )
        data = r.json()



        name = data['name']
        weather_temp = data['main']['temp']

        weather_description = data["weather"][0]["main"]
        if weather_description in smile_code:
            descr = smile_code[weather_description]
        else:
            descr = "Посмотрите в окно"

        weather_humidity = data['main']['humidity']
        weather_pressure = data['main']['pressure']
        weather_speed = data['wind']['speed']
        sunrise = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset = datetime.datetime.fromtimestamp(data['sys']['sunset'])
        daylight = datetime.datetime.fromtimestamp(data['sys']['sunset']) - datetime.datetime.fromtimestamp(
            data['sys']['sunrise'])

        await message.reply(
            f' ***{datetime.datetime.now().strftime("%Y-%m-%d %H:%M") }***\n'
            f' Погода в городе: {name} {descr}\n Температура: {weather_temp}°\n Dлажность: {weather_humidity}%\n Давление:'
            f' {weather_pressure} мм.рт.ст \n Скорость ветра: {weather_speed}\n Рассвет: {sunrise} 🌅 \n Закат: {sunset} 🌇 \n '
            f'Продолжительность дня: {daylight}  '
        )

    except:
        await message.reply("\U00002620 Проверьте название города \U00002620")


if __name__ == "__main__":
    executor.start_polling(dp)
