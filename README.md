# How to make the most of unit testing 

Presentation by [Greg Detre](http://blog.gregdetre.co.uk/) on unit testing in Python at [Tampa Bay Python meetup](http://www.meetup.com/python-178/events/225328442/) on 13th October 2015.

see:

- [presentation - FirstWave - python - 151013.pdf](https://github.com/gregdetre/unit-testing-pres/blob/master/presentation%20-%20FirstWave%20-%20python%20-%20151013.pdf)


## Join the Google Hangout

http://bit.ly/1GELH73
(requires Google Hangouts app & Google account)


## Setup

    cd ~/dev/
    git clone git@github.com:gregdetre/unit-testing-pres.git
    cd unit-testing-pres
    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt

Or, if you have trouble, just [download the tarball](https://github.com/gregdetre/unit-testing-pres/archive/master.zip).


## Running the tests

Create `test_template0.py`:

    def test_blah():
        assert True

Then run:

    $ nose2 test_template0

Or if you weren't able to install `nose2`, add these lines to the end of `test_template0.py`:

    if __name__ == '__main__':
        unittest.main()

And run:

    $ python test_template0.py


## Next steps

Have a look in `test_template1.py` and `test_template2.py` for further examples and usage instructions.
