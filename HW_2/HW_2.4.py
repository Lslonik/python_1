# Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

# счетчик для нумерации
counter = 1
# запрос на ввод строки из нескольких слов
your_str = input("Введите вашу строку из нескольких слов: ")
# разбираем строку на части используя разделитель, и получаем список
list_for_str = your_str.split(' ')

# печатаем элементы списка нумеруя каждый элемент, и сокращая элемент до 10 символов
for list_elem in list_for_str:
    if len(list_elem) > 10:
        list_elem = list_elem[:10]
    print(f'№ {counter}: {list_elem}')
    counter += 1
