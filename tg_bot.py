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
        self.job = 'Нет работы'
        self.salary = 0

    def gain_experience(self, exp):
        while exp >= self.score:
            self.level_up()
        self.experience += exp

    def give_money(self, m):
        self.money += m

    def level_up(self):
        self.level += 1
        self.score *= 2

    def new_job(self, comp, sal):
        self.job = comp
        self.salary = sal

    def learn_skill(self, skill_name):
        if skill_name not in self.skills:
            self.skills[skill_name] = 1
        elif self.skills[skill_name] < 5:
            self.skills[skill_name] += 1

    def add_career_achievement(self, achievement):
        self.career_achievements.append(achievement)

    def get_level(self):
        return self.level

    def get_job(self):
        return self.job

    def get_salary(self):
        return self.salary

    def get_player_info(self):
        player_info = f"Имя игрока: {self.name}\nДеньги: {self.money}\nУровень: {self.level}\nОпыт: {self.experience}\n"
        player_info += "Навыки:\n"
        for skill, level in self.skills.items():
            player_info += f"- {skill}: {level}\n"
        player_info += f'Место роботы: {self.job}\n'
        player_info += "Достижения в карьере:\n"
        for achievement in self.career_achievements:
            player_info += f"- {achievement}\n"
        return player_info


with open('C:/Users/Admin/Desktop/tg_token.txt', encoding="UTF-8") as file_in:
    API_TOKEN = file_in.read().strip()

bot = telebot.TeleBot(API_TOKEN)


# Клавиатура для выбора действия
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup.row('Работать', 'Устроится на работу')
markup.row('Покупка оборудования', 'Изучение новых технологий')
markup.row('Статус', 'Развитие карьеры')
markup.row('Достижения')

markup_jobs = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup_jobs.row('NeuroCodex', 'VirtuoSphere')
markup_jobs.row('DigitalFusion', 'CyberSpires')
markup_jobs.row('HyperTech', 'Solutions')
markup_jobs.row('InnovaTechnosis')

company = {'NeuroCodex': [1, 150], 'VirtuoSphere': [3, 200], 'DigitalFusion': [5, 350],
           'CyberSpires': [8, 500], 'HyperTech': [8, 500], 'Solutions': [15, 900], 'InnovaTechnosis': [20, 1500]}


@bot.message_handler(commands=['start'])
def start(message):
    user = Player(message.from_user.first_name)
    bot.send_message(message.chat.id,
                     f"Привет, {message.from_user.first_name}! Добро пожаловать в игру Code tycoon!\n"
                     "Выберите действие:",
                     reply_markup=markup)
    bot.register_next_step_handler(message, select_action, user)


@bot.message_handler(commands=['site'])
def site(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="GitHub",
                                            url="https://github.com/Radzon/practical-work/blob/main/tg_bot.py")
    keyboard.add(url_button)
    bot.send_message(message.chat.id, "Исходный код", reply_markup=keyboard)


def select_action(message, user):
    text = message.text
    if text == 'Работать':
        if user.get_job() == 'Нет работы':
            bot.send_message(message.chat.id, "Вы вы еще не устроились на работу")
        else:
            bot.send_message(message.chat.id, f"Вы заработали:\n{user.get_salary()} доларов\n100 опыта")
    elif text == 'Устроится на работу':
        bot.send_message(message.chat.id, "Выберите, в какую компанию хотите устроиться:"
                                          "\nNeuroCodex - Минимальный уровень: 1 | Зарплата: 150$"
                                          "\nVirtuoSphere - Минимальный уровень: 3 | Зарплата: 200$"
                                          "\nDigitalFusion - Минимальный уровень: 5 | Зарплата: 350$"
                                          "\nCyberSpires - Минимальный уровень: 8 | Зарплата: 500$"
                                          "\nHyperTech - Минимальный уровень: 10 | Зарплата: 750$"
                                          "\nSolutions - Минимальный уровень: 15 | Зарплата: 900$"
                                          "\nInnovaTechnosis - Минимальный уровень: 20 | Зарплата: 1500$",
                         reply_markup=markup_jobs)
        bot.register_next_step_handler(message, select_job, user)
    elif text == 'Статус':
        bot.send_message(message.chat.id, user.get_player_info())
    bot.register_next_step_handler(message, select_action, user)


def select_job(message, user):
    if company[message.text][0] <= user.get_level():
        user.new_job(message.text, company[message.text][1])
        text = 'Вы устроились на работу'
    else:
        text = 'Ваш уровень слишком мал'
    bot.send_message(message.chat.id, text, reply_markup=markup)
    bot.register_next_step_handler(message, select_action, user)


def work_on_job():
    pass


def select_technology(message):
    pass


bot.polling()
