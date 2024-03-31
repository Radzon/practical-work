import telebot
from telebot import types


class Player:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.money = 0
        self.experience = 0
        self.skills = {}
        self.career_achievements = []
        self.score = 100

    def gain_experience(self, exp):
        while exp >= self.score:
            self.level_up()
        self.experience += exp

    def give_money(self, m):
        self.money += m

    def level_up(self):
        self.level += 1
        self.score *= 2

    def learn_skill(self, skill_name):
        if skill_name not in self.skills:
            self.skills[skill_name] = 1
        elif self.skills[skill_name] < 5:
            self.skills[skill_name] += 1

    def add_career_achievement(self, achievement):
        self.career_achievements.append(achievement)

    def get_player_info(self):
        player_info = f"Имя игрока: {self.name}\nДеньги: {self.money}\nУровень: {self.level}\nОпыт: {self.experience}\n"
        player_info += "Навыки:\n"
        for skill, level in self.skills.items():
            player_info += f"- {skill}: {level}\n"
        player_info += "Достижения в карьере:\n"
        for achievement in self.career_achievements:
            player_info += f"- {achievement}\n"
        return player_info


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
