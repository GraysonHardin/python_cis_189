import unittest


def fun(x):
    return x + 1


class MyTestCase(unittest.TestCase):
    def test(self):
        self.assertEqual(fun(3), 4)


if __name__ == '__main__':
    unittest.main()
