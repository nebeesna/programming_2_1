import unittest


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


class TreeTest(unittest.TestCase):
    def test_init(self):
        t = Tree()
        self.assertEqual(t.data, None)

    def test_insert(self):
        t = Tree()
        t.insert(3)
        self.assertEqual(t.data, 3)

    def test_multi_insert(self):
        t = Tree()
        t.insert(3)
        t.insert(5)
        t.insert(1)
        self.assertEqual(t.left.data, 1)
        self.assertEqual(t.right.data, 5)

    def test_pretty_print(self):
        t = Tree()
        t.insert(3)
        t.insert(5)
        t.insert(1)
        res = [' 3 ', '/ \\', '1 5']
        lines, *_ = t._create_print()
        self.assertEqual(lines, res)

    def test_create_print(self):
        t = Tree()
        t.insert(3)
        t.insert(5)
        t.insert(1)
        print("\ntest_create_print")
        t.pretty_print()
        *_, w, h, m = t._create_print()
        self.assertEqual((w, h, m), (3, 3, 1))

    def test_only_left_child(self):
        t = Tree()
        t.insert(14)
        t.insert(8)
        t.insert(6)
        t.insert(5)
        t.insert(3)
        t.insert(2)
        lines, w, h, m = t._create_print()
        print("\ntest_only_left_child")
        for line in lines:
            print(line)
        self.assertEqual((w, h, m), (7, 11, 6))

    def test_only_right_child(self):
        t = Tree()
        t.insert(1)
        t.insert(3)
        t.insert(5)
        t.insert(8)
        t.insert(12)
        lines, w, h, m = t._create_print()
        print("\ntest_only_right_child")
        for line in lines:
            print(line)
        self.assertEqual((w, h, m), (6, 9, 0))

    def test_two_children(self):
        t = Tree()
        t.insert(8)
        t.insert(4)
        t.insert(2)
        t.insert(6)
        t.insert(5)
        t.insert(7)
        t.insert(10)
        t.insert(9)
        t.insert(11)
        lines, w, h, m = t._create_print()
        print("\ntest_two_children")
        for line in lines:
            print(line)
        self.assertEqual((w, h, m), (11, 7, 5))


unittest.main()

