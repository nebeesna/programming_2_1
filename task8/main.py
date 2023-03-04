# Завдання 8: (6 балів)
import numpy as np


class Matrix:
    def __init__(self, arr=None):
        if arr is not None:
            self.data = arr
            if arr.size > 0:
                self.height = self.data.shape[0]
                self.width = self.data.shape[1]
            else:
                self.height = 0
                self.width = 0
        if arr is None:
            print('enter matrix:')
            st = input()
            row = [float(i) for i in st.split()]
            height = 1
            length = len(row)
            main_len = len(row)
            res = np.empty((0, main_len))
            res = np.append(res, np.array([row]), axis=0)
            row.clear()
            while True:
                st = input()
                if st != '/':
                    row = [float(i) for i in st.split()]
                    length = len(row)
                    if length == main_len:
                        res = np.append(res, np.array([row]), axis=0)
                        height += 1
                    else:
                        self.data = np.empty((0, 0))
                        self.height = 0
                        self.width = 0
                        print("Matrix size error")
                        return
                else:
                    break

            self.data = res
            self.height = height
            self.width = main_len

    def __str__(self):
        st = ''
        for i in range(self.height):
            for j in range(self.width):
                st += f"{self.data[i][j]: < 10.4f}"
            st += "\n"
        return st

    def __add__(self, other):
        return Matrix(self.data + other.data)

    def __sub__(self, other):
        return Matrix(self.data - other.data)

    def __mul__(self, other):
        if type(other) == Matrix and (self.height == other.width or self.width == other.width):
            return Matrix(self.data @ other.data)
        else:
            return Matrix(self.data * other)

    def __rmul__(self, other):
        if type(other) == Matrix and (self.height == other.width or self.width == other.width):
            return Matrix(self.data @ other.data)
        else:
            return Matrix(self.data * other)

    def __iter__(self):
        self.iterable = iter(self.data)
        self.row = iter(next(self.iterable))
        return self

    def __next__(self):
        i = 0
        self.current = next(self.row)
        if self.current == self.data[i][self.width - 1]:
            self.row = iter(next(self.iterable))
            i += 1
        return self.current

    def transpose(self):
        self.data = self.data.transpose()
        self.height = self.data.shape[0]
        self.width = self.data.shape[1]
        return self.data

    def inverse(self):
        if self.data.shape[0] == self.data.shape[1]:
            return Matrix(np.linalg.inv(self.data))

    def solve(self, b):
        return np.linalg.solve(self.data, b)

    def own_vector(self):
        return np.linalg.eig(self.data)

    def norm(self):
        return np.linalg.norm(self.data)

    def generator(self):
        arr = self.data
        rows = arr.shape[0]
        cols = arr.shape[1]
        i = 0
        j = 0
        left = 0
        right = 0
        top = 0
        down = 0
        for it in range(arr.size):
            yield arr[i][j]
            if i == left and j < cols - right - 1:
                j += 1
            elif j == cols - right - 1 and i < rows - down - 1:
                i += 1
            elif i == rows - down - 1 and j > left:
                j -= 1
            else:
                i -= 1
            if i == top + 1 and j == left and left != cols - right - 1:
                top += 1
                right += 1
                down += 1
                left += 1




print("""1 - Add matrixes
2 - Sub matrixes
3 - Mul matrixes
4 - Transpose matrix
5 - Inverse matrix
6 - Solve line equations
7 - Own value
8 - Matrix norm
9 - Iterator
10 - Generator
X - Stop""")
while True:
    command = input("Enter command: ")
    if command == "1":
        a = Matrix()
        b = Matrix()
        print(a + b)
    elif command == "2":
        a = Matrix()
        b = Matrix()
        print(a - b)
    elif command == "3":
        a = Matrix()
        b = Matrix()
        print(a * b)
    elif command == "4":
        a = Matrix()
        b = a.transpose()
        print(b)
    elif command == "5":
        a = Matrix()
        b = a.inverse()
        print(b)
        print(a * b)
    elif command == "6":
        a = Matrix()
        b = input("Enter vector b:\n").split()
        for i in range(len(b)):
            b[i] = float(b[i])
        b = np.array(b)
        print(a.solve(b))
    elif command == "7":
        a = Matrix()
        print("Own value:\n", a.own_vector()[0])
        print("Own vectors:")
        for i in a.own_vector()[1]:
            print(f"({', '.join(list(map(str, i)))})")
    elif command == "8":
        a = Matrix()
        print(a.norm())
    elif command == "9":
        a = Matrix()
        for it in a:
            print(it)
    elif command == "10":
        a = Matrix()
        g = a.generator()
        print(a)
        for it in g:
            print(it)
    elif command == "X":
        break
    else:
        print("Choose existing commands!")

