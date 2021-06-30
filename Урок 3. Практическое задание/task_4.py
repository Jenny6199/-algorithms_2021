"""
Студент: Максим Сапунов Jenny6199@yandex.ru

Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносить ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации.

Задание творческое. Здесь нет жестких требований к выполнению.
"""
import hashlib


class WebCash:
    """Модель кэширования вэб-страниц"""

    __salt = 'sunlight'

    def __init__(self):
        """ Конструктор класса"""
        self.salt = WebCash.__salt
        self.current_cash = []
        self.test_hash = 0

    def update_table(self):
        """ Функция загружает данные из файла."""
        with open('web_cash.txt', 'r', encoding='UTF-8') as file_obj:
            self.current_cash = file_obj.read()
        print('Данные кэша успешно обновлены.')

    def load_table(self):
        """ Функция осуществляет сохранение данных в файл."""
        with open('web_cash.txt', 'a', encoding='UTF-8') as file_obj:
            file_obj.writelines('\n')
            file_obj.writelines(str(self.test_hash))
        print('Страница была успешно добавлена в кэш.')

    def url_cash(self, url: str):
        """ Функция принимает строку, хеширует ее и сравнивает с имеющимися данными"""
        self.test_hash = hashlib.sha256(url.encode() + self.salt.encode()).hexdigest()
        if self.test_hash in self.current_cash:
            print('Страница присутствует в кэше.')
        else:
            self.load_table()
            self.update_table()

    def show_cash(self):
        print(self.current_cash)


v1 = WebCash()
v1.update_table()
v1.url_cash('gb.ru')
v1.url_cash('www.yandex.ru')
v1.url_cash('github.com')
v1.url_cash('google.com')
v1.show_cash()
