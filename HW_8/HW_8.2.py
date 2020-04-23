# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа
# должна корректно обработать эту ситуацию и не завершиться с ошибкой.


class MyDivisionZero(Exception):
    def __index__(self, my_err):
        self.my_err = my_err


try:
    a = int(input('Введите делимое: '))
    b = int(input('Введите делитель: '))
    if b == 0:
        raise MyDivisionZero('Делить на ноль нельзя!')
    print(a/b)
except MyDivisionZero:
    print('делитель равен 0')