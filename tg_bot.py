import telebot
from telebot import types


with open('C:/Users/Admin/Desktop/tg_token.txt', encoding="UTF-8") as file_in:
    API_TOKEN = file_in.read().strip()

bot = telebot.TeleBot(API_TOKEN)

SELECT_ACTION, SELECT_JOB, SELECT_TECHNOLOGY, MAIN_MENU = range(4)

# Клавиатура для выбора действия
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup.row('Устройство на работу', 'Изучение новых технологий')
markup.row('Покупка оборудования', 'Работа над проектами')
markup.row('Участие в событиях', 'Развитие карьеры')
markup.row('Достижения')


# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,
                     f"Привет, {message.from_user.first_name}! Добро пожаловать в игру Code tycoon!\n"
                     "Выберите действие:",
                     reply_markup=markup)
    bot.register_next_step_handler(message, select_action)


# Обработчик действий
def select_action(message):
    text = message.text
    if text == 'Устройство на работу':
        bot.send_message(message.chat.id, "Выберите, в какую компанию хотите устроиться:",
                         reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, select_job)
    elif text == 'Изучение новых технологий':
        bot.send_message(message.chat.id, "Выберите технологию, которую хотите изучить:")
        bot.register_next_step_handler(message, select_technology)
    # Другие действия обрабатываются аналогично


def main():
    bot.polling()


if __name__ == '__main__':
    main()
