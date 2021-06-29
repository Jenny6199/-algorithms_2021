"""
Задание 1.

Реализуйте свои пользовательские функции, в которых реализуйте:

a) заполнение списка и словаря,
   сделайте замеры и сделайте выводы, что выполняется быстрее и почему
b) выполните набор операций и со списком, и со словарем,
   сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: если вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!

Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
"""
import random as rd
import timeit
import time


# Вариант 1
def time_counter(func):
    """ Подсчитывает время выполнения функции"""
    def my_wrapper():
        """ Функция-обертка."""
        decor = '-'*20
        print(decor, f'Тестируется функция: {func.__name__}', decor)
        start = time.time()
        rand_list = func()
        # print(f'Документация фуцнкции: \n{func.__doc__}\n', decor)
        print(rand_list)
        end = time.time()
        result = end - start
        print(f'Время выполнения функции {func.__name__} - {result} c.')
        print('-'*20, 'Конец ', '-'*20)
        return rand_list
    return my_wrapper()


@time_counter
def random_int_list(length=10, boarder_1=1, boarder_2=100):
    """
    Функция создает список и заполняет его случайными целыми числами в указанном диапазоне.
    :param - length:int - длина списка
    :param - boarder_1:int - начальная граница выборки
    :param - boarder_2:int - конечная граница выборки
    :return - result_list:list - список со случайными целыми числами
    """
    result_list = [rd.randint(boarder_1, boarder_2) for _ in range(length)]
    return result_list


@time_counter
def random_int_dict(length=10, boarder_1=1, boarder_2=100):
    """
    :param length:int - длина словаря 
    :param boarder_1:int - начальная граница выборки 
    :param boarder_2:int - конечная граница выборки
    :return: - result_dict:dict - словарь со случайными значениями
    """
    result_dict = {}
    for ID in range(1, length+1):
        result_dict[ID] = rd.randint(boarder_1, boarder_2)
    return result_dict


def get_descriptive_output():
    my_dict = random_int_dict()
    for key, values in my_dict.items():
        print(key, values, sep=':')


# Второй вариант
def analyzer(func):
    """Тестирующая функция"""
    def wrapper():
        """Вспомогательная функция-обертка"""
        print(f'Время выполнения функции {func.__name__} составило: ',
              timeit.timeit(stmt="random_list()", globals=globals(), number=1000))
    return wrapper()


def random_list(length=10, min_boarder=0, max_boarder=100):
    """
    Фунция создает список заполненный случайными значениями,
    добавлен блок обработки ошибок принимаемых значений -
    в случае выявления возвращаются значения по умолчанию.
    :param - length - длина списка, по умолчанию 10,
    :param - min_boarder - нижняя граница значений элементов списка, по умолчанию 0,
    :param - max_boarder - верхяя граница значений элементов списка, по умолчанию 100.
    :return - array - список заполненный случайными значениями.
    """
    try:
        length, min_boarder, max_boarder = round(length), round(min_boarder), round(max_boarder)
    except TypeError:
        length, min_boarder, max_boarder = 10, 0, 100
    return [rd.randint(min_boarder, max_boarder) for _ in range(length)]


analyzer(random_list)
