from isitanemail import isitanemail

# USAGE:
# $ nose2 test_legal
# $ nose2 test_legal.test_legal_basic
# $ python test_legal.py


def test_legal_basic():
    assert isitanemail('ab@de.com')



