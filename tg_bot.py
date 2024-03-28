import telebot

# токен скрыл на всякий случай
with open('C:/Users/Admin/Desktop/tg_token.txt', encoding="UTF-8") as file_in:
    token = file_in.read()
API_TOKEN = token

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def main(massage):
    bot.send_message(massage.chat.id, 'Привет это мой первый бот')


bot.polling()
