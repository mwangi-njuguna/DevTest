import unittest
from question2 import search


class TestSearchFunction(unittest.TestCase):

    def setUp(self):
        self.col1 = [0, 1, 2, 4]
        self.col2 = [9, 303, 4 ,120, 303]
        self.col3 = [-9, -920, -29, -93]

    def test_should_search_and_return_correct_index(self):
        self.assertEqual(search(self.col1, 3), None)
        self.assertTrue(search(self.col1, 2), 2)

    def test_should_return_correctly_for_negative_values(self):
        self.assertNotEqual(search(self.col3, -29), 3)
        self.assertTrue(search(self.col3, -29), 2)

    def test_should_return_first_index_of_value(self):
        self.assertNotEqual(search(self.col2, 303), 4)
        self.assertTrue(search(self.col2, 303), 1)

    def test_should_throw_index_error_if_value_not_found(self):
        self.assertRaises(IndexError, search(self.col1, 3))
    

if __name__ == "__main__":
    unittest.main()
