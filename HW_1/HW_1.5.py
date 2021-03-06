# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек,
# или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки
# (соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы
# и определите прибыль фирмы в расчете на одного сотрудника.

# Запрос на ввод выручки и издержки
earnings = int(input('Введите пожалуйста общую выручку: '))
costs = int(input('Введите пожалуйста общие издержки: '))

# считаем профит и рентабельность, так же прибыль в рассчете на одного работника, если есть профит,
# иначе сообщаем об убытках
if earnings > costs:
    profit = earnings - costs
    print(f'Круто. У вас {profit} прибыли')
    cost_effective = profit/costs
    number_of_workers = int(input('Введити пожалуйста количество работников: '))
    print(f'Прибыль в рассчете на одного сотрудника {profit / number_of_workers}')
elif earnings == costs:
    print('Ваши издержки и выручка равны, для профита вам нужно увеличить выручку')
else:
    print(f'Вы несете убытки. Вы в убытке на {earnings - costs}. Вам нужно, что то поменять в бизнесе.')
