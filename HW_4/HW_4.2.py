# Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

# если элемент списка не стоит на первом месте, и если предыдущий элемент меньше то записываем в новый список
new_list = [el for el in my_list if my_list.index(el) != 0 if el > my_list[my_list.index(el) - 1]]

# вывод
print(f'Исходный список: {my_list}')
print(f'Новый список: {new_list}')
