# Телефонный справочник

Этот программный код представляет собой простой телефонный справочник, реализованный на Python. Он позволяет пользователю добавлять, просматривать, редактировать и удалять контакты, а также импортировать данные из файла.

## Описание функций

- **rules(text)**: Выводит список доступных команд.
- **err()**: Выводит сообщение об ошибке при вводе недопустимой команды.
- **stop()**: Останавливает выполнение программы, ожидая ввода от пользователя.
- **confirmation()**: Предлагает пользователю подтвердить продолжение операции.
- **reset()**: Сбрасывает данные контакта.
- **load_data(file_name)**: Загружает данные из файла JSON.
- **save_data(data)**: Сохраняет данные в файл JSON.
- **check_number()**: Проверяет формат введенного номера телефона.
- **conti_save(char, name)**: Сохраняет измененные данные контакта.
- **new_data()**: Создает новый контакт.
- **show_data(name, data)**: Выводит информацию о контакте.
- **view_all(name='')**: Просматривает все контакты или конкретный контакт.
- **edit_save(con)**: Сохраняет отредактированные данные.
- **edit_data()**: Редактирует или удаляет контакты.
- **main()**: Главная функция, управляющая всем процессом работы программы.

## Как использовать

1. Запустите программу.
2. Следуйте инструкциям в меню для выполнения нужных операций: просмотр, добавление, редактирование или удаление контактов.
3. Используйте опцию импорта для загрузки данных из файла JSON.
4. Пользуйтесь командой "завершение работы программы" для выхода из программы.

## Примечания

- Внимание: перед использованием убедитесь, что файл `phone_db.json` создан в той же директории, где находится программа, либо укажите путь к существующему файлу при импорте.
- Программа ожидает ввода данных в указанном формате, следуйте указаниям в тексте интерфейса программы.

## Зависимости

- Python 3.12
- Библиотека json

## Автор

Автор: Николаев Радмир Игоревич