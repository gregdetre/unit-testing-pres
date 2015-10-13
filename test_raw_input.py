# USAGE:
# $ nose2 test_raw_input

from isitanemail import isitanemail

def test_isitanemail_ask():
	e = 'x@example.com'
	print 'Returned for %s:' % e, isitanemail(e)
	assert raw_input('Ok? ') == 'y'
        
