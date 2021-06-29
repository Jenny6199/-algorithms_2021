import random as rd

"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Подсказка:
Базовый случай здесь - угадали число или закончились попытки

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""
import random as rd


def generate_aim():
    """ Генерация случайного числа."""
    aim = rd.randint(1, 100)
    return aim


def user_input():
    """ Ввод значения пользователем."""
    user_digit = int(input(' Введите целое чило и нажмите Enter: '))
    return user_digit


def merge(ui, gi):
    """ Сравнение значений случайного числа и выбора пользователя."""
    return True if ui == gi else False


def counter(user_try=0):
    """Подсчитывает количество попыток пользователя."""
    user_try += 1
    return user_try


def no_aim():
    """ Вывод если число не угадано."""
    print(' На этот раз Вас постигла неудача :(')
    if user_input() < generate_aim():
        print(' Загаданное число больше.')
    else:
        print(' Загаданное число меньше.')


def get_aim():
    """ Вывод если чило угадано."""
    print('Поздравляю! Вы угадали!')

"""
Домашнее задание к уроку №2 Алгоритмы и структуры данных на Python
Студент: Максим Сапунов. Jenny6199@yandex.ru 09.06.2021
"""


class GuessNumber:
    """ Игра - угадай число"""

    def __init__(self):
        """ Конструктор класса. """
        self.attempt = 10  # Количество попыток.
        self.number = rd.randint(1, 100)  # Генерация случайного числа.
        self.users_variant = []  # Данные введенные пользователем.
        self.result = False  # Флаг результата
        print('\033[032mПопробуйте отгадать случайное число от 1 до 100:\033[0m')  # Приветственное сообщение.

    def get_descriptive_input(self):
        """ Обеспечивает аккуратный ввод данных пользователем и обработку ошибок ввода."""
        print(f'У вас осталось попыток:  {self.attempt}.')
        while True:
            try:
                user_digit = int(input('Введите целое число и нажмите Enter: '))
                self.users_variant.append(user_digit)
                return user_digit
            except ValueError:
                print('\033[031m Ошибка ввода! Попробуйте еще раз.\033[0m')

    def comparison(self):
        """
        Обеспечивает сравнение данных введенных пользователем с загаданным числом.
        Возвращает True - если число угадано, иначе False и выводит информационное сообщение

        """
        data = self.get_descriptive_input()
        self.attempt -= 1
        if data > self.number:
            print(' Загаданное число меньше введенного.')
            return False
        elif data < self.number:
            print(' Загаданное число больше введенного.')
            return False
        else:
            return True

    def win(self):
        """ Флаг победы и сброс попыток"""
        self.result = True
        self.attempt = 0

    def game_over(self):
        """ Вывод сообщения и данных при завершении игры."""
        print(f'\033[032m Игра окончена.\033[0m\nБыло загадано число {self.number}.\nВаши попытки:', end=' ')
        for el in self.users_variant:
            print(el, end=' ')
        if self.result:
            print(' \033[034m\n Поздравляю! Вы выйграли!\033[0m')
        else:
            print('\nВы не смогли угадать число.\nНадеюсь, Вам обязательно повезет в следующий раз.\nУдачи!')

    def run_play(self):
        """Запуск игры"""
        if self.attempt == 0:
            self.game_over()
        else:
            if self.comparison():
                self.win()
            self.run_play()  # Рекурсивный вызов функции согласно учебному заданию.


if __name__ == '__main__':
    v1 = GuessNumber()
    v1.run_play()
