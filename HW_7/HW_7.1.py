# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
#
# 31 22           3  5  32          3 5 8 3
# 37 43           2  4   6           8 3 7 1
# 51 86          -1  64 -8
#
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
# (двух матриц)
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
# первым элементом первой строки второй матрицы и т.д.


# матрицы для выполнения операций над ними
my_matrix_1 = [[3, 5, 32, 7], [2, 4, 6, -98], [-1, 64, -8, 77], [39, 6, 14, 2]]
my_matrix_2 = [[31, 3, 3, -8], [37, 2, 8, 100], [51, -1, -8, 23], [-37, -2, -8, -100]]


# класс Matrix, имеет атрибуты my_list_1 и result, операторы __add__ и __str__
class Matrix:
    def __init__(self, my_list_1):
        self.my_list_1 = my_list_1
        self.result = []

    def __add__(self, my_list_2):

        # хранят количество строк и столбцов
        row_my_list_1 = len(self.my_list_1)
        column_my_list_1_elem = len(self.my_list_1[0])
        row_my_list_2 = len(my_matrix_2)
        column_my_list_2_elem = len(my_matrix_2[0])

        # складываем две матрицы, если они имеет одинаковое количество строк и столбцов
        # иначе матрице result присваиваем None
        if row_my_list_1 == row_my_list_2 and column_my_list_1_elem == column_my_list_2_elem:

            # создаем матрицу, куда запищем результат операции. заполняем нулями
            for i in range(row_my_list_1):
                self.result.append([])
                for j in range(column_my_list_1_elem):
                    self.result[i].append(0)

            # выполняем операцию сложения, результат сохраняем в матрицу result
            for i in range(row_my_list_1):
                for j in range(column_my_list_1_elem):
                    self.result[i][j] = self.my_list_1[i][j] + my_list_2[i][j]
        else:
            print("Матрицы не равны")
            self.result = None

    def __str__(self):
        # если result не равно None, переводим наш список с матрицей в строковый вид
        # иначе возвращаем None
        if self.result is not None:
            return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.result]))
        else:
            return None


# Экземпляр класса
mat = Matrix(my_matrix_1)

# складываем две матрицы
mat + my_matrix_2

# вывод результата
print(f'Результат сложения двух матриц:\n{mat}')