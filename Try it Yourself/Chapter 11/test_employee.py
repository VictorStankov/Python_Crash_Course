import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee = Employee('john', 'johnson', 1000)

    def test_default_raise(self):
        self.assertEqual(self.employee.give_raise(), 6000)

    def test_specific_raise(self):
        self.assertEqual(self.employee.give_raise(6000), 7000)


if __name__ == '__main__':
    unittest.main()
