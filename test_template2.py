import unittest

# USAGE:
# $ nose2 test_template2
# $ python test_template2.py


class MyTestCase(unittest.TestCase):
    x = 100
    
    def test_equal(self):
        self.assertEqual(self.x, 100)

    def test_notequal(self):
        self.assertNotEqual(self.x, 200)

    def test_true(self):
        self.assertTrue(self.x)

    def test_false(self):
        self.assertFalse(0)

    def test_raises(self):
        with self.assertRaises(ZeroDivisionError):
            1 / 0

    
if __name__ == '__main__':
    unittest.main()

