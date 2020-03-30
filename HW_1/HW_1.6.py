# Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
# Программа должна принимать значения параметров a и b и  выводить одно натуральное число — номер дня.

# запрос на ввод a и b
first_day_km = int(input('Введите сколько пробежал спортсмен в первый ден: '))
target_km = int(input('Введите сколько на какой результат должен выйти спортсмен: '))

# счетчик для дней
i = 1

# цикл для подсчета сколько дней понадобиться для достижения цели
while first_day_km < target_km:
    first_day_km = first_day_km + ((first_day_km / 100) * 10)
    i += 1

# вывод результата
print(f'на {i}-й день спортсмен достиг результата — не менее {int(first_day_km)} км')
