from isitanemail import isitanemail

# USAGE:
# $ nose2 test_legal
# $ nose2 test_legal.test_legal_basic


def test_legal_basic():
    assert isitanemail('ab@cd.com')



