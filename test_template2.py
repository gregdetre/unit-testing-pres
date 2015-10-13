import unittest

# USAGE:
# $ nose2 test_template2
# $ python test_template2.py
# $ nose2 test_template2.TestCaseOk
# $ nose2 test_template2.TestCaseProblems
# $ nose2 test_template2.TestCaseGotchas -v
# $ nose2 test_template2.TestCaseWithSetUpTearDown

y = 0


class TestCaseOk(unittest.TestCase):
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


class TestCaseProblems(unittest.TestCase):

    def test_fails(self):
        self.assertTrue(False)

    def test_error(self):
        1/0
        
    def test_doesnt_raise(self):
        with self.assertRaises(ZeroDivisionError):
            1 / 1


class TestCaseGotchas(unittest.TestCase):

    def test_nothing(self):
        2+2 == 5 # will pass, because nothing really got tested

    def gets_ignored(self):
        # ignored, because the test runners look for functions called 'test*'
        1/0

    # I *think* it's undefined which of these get run
    def test_duplicate_name(self):
        self.assertTrue(False)
    def test_duplicate_name(self):
        self.assertTrue(True)


class TestCaseWithSetUpTearDown(unittest.TestCase):
    x = 0
    
    def setUp(self):
        # gets run just before each test function in this class
        self.x += 1
        global y
        y += 1
        print 'in the setup, now x =', self.x, ', y =', y
    
    def tearDown(self):
        # gets run just after each test function in this class
        print 'in the tearDown'

    def test1(self):
        self.assertEqual(self.x, 1)
        self.assertEqual(y, 1)

    def test2(self):
        self.assertEqual(self.x, 1)
        self.assertEqual(y, 2)
    

# if you include this section, you can run with 'python test_template2.py'
if __name__ == '__main__':
    unittest.main()

