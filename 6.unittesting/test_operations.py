import unittest
import operations

class TestOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(operations.add(10,5),15)
        self.assertEqual(operations.add(-1,1),0)
        self.assertEqual(operations.add(-1,-1),-2)

    def test_subtract(self):
        self.assertEqual(operations.subtract(10,5),5)
        self.assertEqual(operations.subtract(-1,1),-2)
        self.assertEqual(operations.subtract(-1,-1),0)

    def test_multiply(self):
        self.assertEqual(operations.multiply(10,5),50)
        self.assertEqual(operations.multiply(-1,1),-1)
        self.assertEqual(operations.multiply(-1,-1),1)
    
    def test_divide(self):
        self.assertEqual(operations.divide(10,5),2)
        self.assertEqual(operations.divide(-1,1),-1)
        self.assertEqual(operations.divide(-1,-1),1)
        self.assertEqual(operations.divide(5,2),2.5)

if __name__ == '__main__':
    unittest.main()