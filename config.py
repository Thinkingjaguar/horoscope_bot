import os
from aiogram import Bot
import dotenv

dotenv.load_dotenv()
ADMINS = os.environ.get('ADMINS').split(', ')
TOKEN = os.environ.get('TOKEN')
ARIES = os.environ.get('ARIES').split(', ')
bot = Bot(token=TOKEN)
symbols = {'aries': 'Овен',
           'taurus': 'Телец',
           'gemini': 'Близнецы',
           'cancer': 'Рак',
           'leo': 'Лев',
           'virgo': 'Дева',
           'libra': 'Весы',
           'scorpio': 'Скорпион',
           'sagittarius': 'Стрелец',
           'capricorn': 'Козерог',
           'aquaris': 'Водолей',
           'pisces': 'Рыбы'}
