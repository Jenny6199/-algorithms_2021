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


def time_counter(func):
    """ Подсчитывает время выполнения функции"""
    import time

    def my_wrapper():
        """ Функция-обертка."""
        decor = '-'*20
        print(decor, 'Начало', decor)
        start = time.time()
        random_list = func()
        # print(f'Документация фуцнкции: \n{func.__doc__}\n', decor)
        print(random_list)
        end = time.time()
        result = end - start
        print(f'Время выполнения функции {func} - {result} c.')
        print('-'*20, 'Конец ', '-'*20)
        return random_list

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
    import random as rd
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
    import random as rd

    result_dict = {}
    for ID in range(1, length+1):
        result_dict[ID] = rd.randint(boarder_1, boarder_2)
    return result_dict


def get_descriptive_output():
    my_dict = random_int_dict()
    for key, values in my_dict.items():
        print(key, values, sep=':')
