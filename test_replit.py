# If you don't have python running on your machine, you can partially play along here:
#
#   https://repl.it/languages/python3
#
# But this doesn't work very well. It's python3 rather
# than python2, and I could only barely get the `unittest`
# module to work, so you may be better off with just simple
# asserts than writing proper unit tests...


import unittest

def isitanemail(e):
    return '@' in e


class TestCaseBlah(unittest.TestCase):
    def test_blah(self):
        self.assertTrue(False)

        
suite = unittest.TestLoader().loadTestsFromTestCase(TestCaseBlah)
testResult = unittest.TextTestRunner(verbosity=2).run(suite)
print(testResult)

