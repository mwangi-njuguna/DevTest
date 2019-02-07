import unittest
from question1 import isPrime,Memoize


class TestIsPrimeFunction(unittest.TestCase):

    def test_should_return_false_for_negative_number(self):
        self.assertFalse(isPrime(-3))

    def test_should_return_false_for_all_even_except_two(self):
        self.assertFalse(isPrime(600))
        self.assertTrue(isPrime(2))
        self.assertNotEqual(isPrime(2), isPrime(1000000000))

    def test_should_throw_type_error_if_arg_is_none(self):
        self.assertRaises(TypeError, isPrime(None))
    
    def test_should_throw_exception_if_number_is_not_integer(self):
        self.assertRaises(TypeError, isPrime(9.9999))

class TestMemoize(unittest.TestCase):

    def setUp(self):
        self.mem = Memoize(isPrime)

    def test_class_memoize_should_memoize(self):
        self.mem(3)
        self.assertDictEqual(self.mem.memoize, {(3,): True})

    def test_memoize_should_not_mutate_result(self):
        self.assertEqual(self.mem(2), isPrime(2))

    def test_memoize_should_not_mutate_function(self):
        self.assertIs(self.mem(3), isPrime(3))


if __name__ == "__main__":
    unittest.main()
