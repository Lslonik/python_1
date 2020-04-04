# Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

# Запрос чисел для возведение числа x на y
first_number = input('Введите число которое нужно возвести в степень: ')
second_number = input('Введите спетень в которую нужно возвести число: ')


# первый способ
def my_func(x, y):
    """
    :param x: число котороую нужно возвести в степень
    :param y: степень
    :return: возвращает результат возведения в степень, если ввели не числа возвращает ошибку
    """
    try:
        return int(x) ** int(y)
    except ValueError:
        return 'Нужно ввести только числа!'


print('\nПервый способ:')
print(f'Ваше число {first_number} в степени {second_number} : {my_func(first_number, second_number)}\n')


# второй способ
def my_func_second(x, y):
    """
    функция возведения чисел через цикл for i in range(), если ввели степень 0, то цикл не выполняется
    и сразу возвращается result
    :param x: число котороую нужно возвести в степень
    :param y: степень
    :return: функция возвращает результат возведения в степень, если ввели не числа возвращает ошибку
    """
    try:
        x = int(x)
        y = int(y)
        result = 1
        for i in range(y):
            result = result * x
        return result
    except ValueError:
        return 'Нужно ввести только числа!'


print('Второй способ:')
print(f'Ваше число {first_number} в степени {second_number} : {my_func_second(first_number, second_number)}')