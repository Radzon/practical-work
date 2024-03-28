import telebot
from random import *
import json
import requests
films = []

# токен скрыл на всякий случай
with open('C:/Users/Admin/Desktop/tg_token.txt', encoding="UTF-8") as file_in:
    token = file_in.read()
API_TOKEN = token
a = 'библиотека'
