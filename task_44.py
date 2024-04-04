import random
import pandas as pd

# Создание DataFrame
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})


# Первый вариант
def first_var():
    data['robot'] = '0'
    data['human'] = '0'
    data.loc[data['whoAmI'] == 'robot', 'robot'] = 1
    data.loc[data['whoAmI'] == 'human', 'human'] = 1


# Второй вариант в одну с выводом в одну строку (Робот = 0 | Человек = 1)
def second_var():
    data.loc[data['whoAmI'] == 'robot', 'whoAmI'] = 0
    data.loc[data['whoAmI'] == 'human', 'whoAmI'] = 1


# Раскомментировать нужный способ и закомментировать не нужный
first_var()
# second_var()

print(data.head())


