"""
Студент: Максим Сапунов Jenny6199@yandex.ru


Задание 3.
Определить количество различных (уникальных) подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените вычисление хешей для подстрок с помощью хеш-функций и множества
Можно воспользоваться ф-цией hash() (см. материалы к уроку)

Пример:
рара - 6 уникальных подстрок

рар
ра
ар
ара
р
а
"""
import hashlib


def use_hash_set(text):
    """
    Функция принимает строку и подсчитывает количество подстрок используя хэш-функцию
    :param - text - текстовая строка
    :return - int - количество подстрок.
    """
    hash_set = set()
    for position in range(len(text)):
        for position_2 in range(position + 1, len(text) + 1):
            hash_set.add(hashlib.md5(text[position:position_2].encode()).hexdigest())
    return len(hash_set)


def use_hash_dict(text):
    """
    Функция принимает строку и разбивает ее на подстроки сохраняя их в словарь.
    :param - text - текстовая строка
    :return - int - количество доступных вариантов подстрок для данной строки
    """
    # Вариант реализации через словарь, при совпадении подстрок они будут перезаписаны в одно и то же значение
    # ключа и таким образом мы также как и с множеством получаем желаемый результат.
    hash_dict = {}
    for smb in range(len(text)):
        for smb2 in range(smb+1, len(text) + 1):
            hash_dict[text[smb:smb2]] = hashlib.sha256(text[smb:smb2].encode()).hexdigest()
    return len(hash_dict)


string = 'fallout'
print(f'Количество уникальных подстрок для строки {string} составляет {use_hash_set(string)}.')
print(f'Количество уникальных подстрок для строки {string} составляет {use_hash_dict(string)}.')
