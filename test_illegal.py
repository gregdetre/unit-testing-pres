from isitanemail import isitanemail

# USAGE:
# $ nose2 test_illegal
# $ nose2 test_illegal.test_illegal_no_tld


def test_illegal_no_tld():
    assert not isitanemail('ab@cd')
    

