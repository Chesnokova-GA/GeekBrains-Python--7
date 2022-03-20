"Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),"
"который должен принимать данные (список списков) для формирования матрицы."
"Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы."
"Примеры матриц: см. в методичке."
"Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде."
"Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц)."
"Результатом сложения должна быть новая матрица."
"Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы "
"складываем с первым элементом первой строки второй матрицы и т.д."

class Matrix:
    value: list

    def __init__(self, value: list):
        self.value = value

    def __add__(self, other: 'Matrix'):
        try:
            rows_count = len(self.value)
            items_count = len(self.value[0])

            new_value = [
                [
                    self.value[row][indx] + other.value[row][indx]
                    for indx in range(items_count)
                ]
                for row in range(rows_count)
            ]

            return Matrix(new_value)
        except IndexError:
            print("Ошибка: размер матриц не совпадает")
            exit(1)

    def __str__(self):
        return "\n".join(
            str(row).strip('[]').replace(',', '')
            for row in self.value
        )


matrix_1 = Matrix([
    [1, 2, 3],
    [11, 22, 33],
])

matrix_2 = Matrix([
    [1, 3, 2],
    [100, 111, 10],
])

matrix_result = matrix_1 + matrix_2

print(matrix_result)