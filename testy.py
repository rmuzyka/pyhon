import unittest
from regular_expressions import split_function


def fun(x):
    return x + 1


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test(self):
        self.assertEqual(fun(3), 4)

    def test_of_split(self):
        string_we_have = '1234567890AB'       #why for string_we_have = '1234567890AB1' test passed ??
        sep = ':'
        result = split_function(string_we_have,sep)

        string_we_want = '12:34:56:78:90:AB'

        self.assertEquals(result, string_we_want)


if __name__ == '__main__':
    unittest.main()
