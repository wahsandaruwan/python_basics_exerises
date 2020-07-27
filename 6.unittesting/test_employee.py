import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

    def test_email(self):
        emp1 = Employee('Himal', 'Sandaruwan', 50000)
        emp2 = Employee('Kasun', 'Silva', 60000)

        self.assertEqual(emp1.email(),'Himal.Sandaruwan@email.com')
        self.assertEqual(emp2.email(),'Kasun.Silva@email.com')

        emp1.fname = 'Chamal'
        emp2.fname = "Dasun"

        self.assertEqual(emp1.email(),'Chamal.Sandaruwan@email.com')
        self.assertEqual(emp2.email(),'Dasun.Silva@email.com')

    def test_apply_raise(self):
        emp1 = Employee('Himal', 'Sandaruwan', 50000)
        emp2 = Employee('Kasun', 'Silva', 60000)

        emp1.apply_raise()
        emp2.apply_raise()

        self.assertEqual(emp1.payment, 52500)
        self.assertEqual(emp2.payment, 63000)

if __name__ == '__main__':
    unittest.main()