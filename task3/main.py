# Реалізувати структуру повного бінарного дерева
# числових елементів та функцію prettyPrint для
# виведення цього дерева у консоль таким чином, як зображено на рисунку:
#     ____8_
#    /      \
#   4_       10
#  /  \     /  \
# 2    6   9    11
#     / \
#    5   7
import random
class Tree:

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def insert(self, data):
        if self.data is None:
            self.data = data
            return

        if data is not None:
            if data > self.data:
                if self.right is not None:
                    self.right.insert(data)
                else:
                    self.right = Tree(data)
            if data < self.data:
                if self.left is not None:
                    self.left.insert(data)
                else:
                    self.left = Tree(data)

    def pretty_print(self):
        lines, *_ = self._create_print()
        for line in lines:
            print(line)

    def _create_print(self):
        if self.right is None and self.left is None:
            line = str(self.data)
            return [line], len(line), 1, len(line) // 2

        if self.right is None:
            lines, l, h, m = self.left._create_print()
            s = str(self.data)
            u = len(s)
            first_line = (m + 1) * ' ' + (l - m - 1) * '_' + s
            second_line = m * ' ' + '/' + (l - m - 1 + u) * ' '
            rest_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + rest_lines, l + u, h + 2, l + u // 2

        if self.left is None:
            lines, l, h, m = self.right._create_print()
            s = str(self.data)
            u = len(s)
            first_line = s + (m - 1) * '_' + (l - m + 1) * ' '
            second_line = (u + m - 1) * ' ' + '\\' + (l - m) * ' '
            rest_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + rest_lines, u + l, h + 2, u // 2

        left, ll, hl, ml = self.left._create_print()
        right, lr, hr, mr = self.right._create_print()
        s = str(self.data)
        u = len(s)

        if (ll - ml - 2 + u + mr) == 0:
            first_line = (ml + 1) * ' ' + (ll - ml - 1) * '_' + s + (mr - 1) * '_' + (lr - mr) * ' '
            second_line = ml * ' ' + '/' + u * ' ' + '\\' + (lr - 1) * ' '
        else:
            first_line = (ml + 1) * ' ' + (ll - ml - 1) * '_' + s + (mr - 1) * '_' + (lr - mr + 1) * ' '
            second_line = ml * ' ' + '/' + (ll - ml - 2 + u + mr) * ' ' + '\\' + (lr - mr) * ' '

        if hl < hr:
            left += [ll * ' '] * (hr - hl)
        elif hr < hl:
            right += [lr * ' '] * (hl - hr)
        res_lines = []
        for i in range(len(left)):
            res_lines.append(left[i] + u * ' ' + right[i])
        return [first_line, second_line] + res_lines, ll + lr + u, max(hl, hr) + 2, ll + u // 2



d = Tree()
d.insert(14)
d.insert(8)
d.insert(6)
d.insert(5)
d.insert(9)
d.insert(11)
d.insert(10)
d.insert(2)
d.insert(3)
d.insert(1)

# com = ""
# while com != "exit":
#     com = input("enter command: ")
#
#     if com == "exit":
#         break
#
#     elif com == "print":
#         d.pretty_print()
#
#     elif com.isdigit():
#         data = int(com)
#         d.insert(data)
#
#     else:
#         print("error. command doesn't exist")

# for i in range(10):
#     d.insert(round((random.uniform(0, 10)), 0))


# d.insert(8)
# d.insert(4)
# d.insert(2)
# d.insert(6)
# d.insert(5)
# d.insert(7)
# d.insert(10)
# d.insert(9)
# d.insert(11)
d.pretty_print()
