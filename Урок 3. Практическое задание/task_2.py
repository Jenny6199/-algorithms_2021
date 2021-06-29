"""
Студент Максим Сапунов Jenny6199@yandex.ru

Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш.

Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль

Обязательно усложните задачу! Добавьте сохранение хеша в файле и получение его из файла.
А если вы знаете как через Python работать с БД, привяжите к заданию БД и сохраняйте хеши там.
"""
import hashlib
import json


class Registration:
    """ Модель регистрации в системе"""

    users_db = {}
    _salt = 'Cassiopeia'
    work_file = 'shadow.txt'

    def __init__(self):
        self.salt = Registration._salt

    def save_data(self):
        """
        Функция принимает словарь с базой данных и записывает его в файл
        :return: info - сообщение о результате сохранения данных в файл
        """
        try:
            with open(self.work_file, 'w', encoding='UTF-8') as f_obj:
                json.dump(self.users_db, f_obj)
                message = '\nУспех! Все данные сохранены в файл.'
        except IOError:
            message = 'Внимание!\nПроизошла ошибка ввода-вывода! Данные не сохранены!'
        finally:
            f_obj.close()
        print(message)
        return message

    def log_in(self):
        """ Функция запрашивает логин, пароль, возращает хэш."""
        login = input('Введите логин: ')
        password = input('Ведите пароль: ')
        hash_info = hashlib.sha256(password.encode() + login.encode() + self.salt.encode()).hexdigest()
        self.users_db[login] = hash_info

    def check_password(self):
        """ Функция проверяет соответствие логина и пароля."""
        with open(self.work_file, 'r', encoding='UTF-8') as f_obj:
            self.users_db = json.load(f_obj)
        login = input('Введите логин: ')
        if login in self.users_db.keys():
            password = input('Ведите пароль: ')
            check_result = hashlib.sha256(password.encode() + login.encode() + self.salt.encode()).hexdigest()
            print(check_result)
            if check_result == self.users_db[login]:
                print('Доступ разрешен!')
            else:
                print('Неверное сочетание логина и пароля!')
        else:
            print('Необходима регистрация.')

    def show_db(self):
        for key, value in self.users_db.items():
            print(key, value, sep=' : ')


def start():
    """Тестовый запуск"""
    v1 = Registration()         # Создаем объект класса
    v1.log_in()
    v1.log_in()         # Заполнение словаря данных
    v1.save_data()      # Сохраняю словарь с данными в json файл.
    v1.check_password()
    v1.check_password()     # Проверка пароля с обновлением данных в объекте.
    v1.show_db()            # Вывод данных на экран.


if __name__ == '__main__':
    start()


# Результат работы программы:
# Введите логин: maksim
# Ведите пароль: 123
# Введите логин: oleg
# Ведите пароль: 456

# Успех! Все данные сохранены в файл.
# Введите логин: maks
# Необходима регистрация.
# Введите логин: oleg
# Ведите пароль: 456
# ed136caac6b7fd8ec00d4d2034b86831600d2b696c61763c002c3fb068c4601b
# Доступ разрешен!
# maksim : 2cbf801e8c3de55b2272e1808207e3b8a20264c2aae3a438c1688a73fe6ffb02
# oleg : ed136caac6b7fd8ec00d4d2034b86831600d2b696c61763c002c3fb068c4601b

# Process finished with exit code 0
