# Python-OOP

[![Build Status](https://travis-ci.org/crytos/level-up.svg?branch=python-oop-ci)](https://travis-ci.org/crytos/level-up)
[![Coverage Status](https://coveralls.io/repos/github/crytos/level-up/badge.svg?branch=python-oop-ci)](https://coveralls.io/github/crytos/level-up?branch=python-oop-ci)

## Implements uber-ui

Python program that validated user signup input data using Object Oriented Programming

## Installation

- Clone the repository
- Install packages

```
$ pip install requirements.txt
```

### Tools

- Python3.6
- `Autopep8` for vscode
- `Pylint` for linting also can be installed with vscode
- coveralls
- coverage
- nose

```
 You need Python3+
```

## Demo

- Uncomment the script at the end of the signup.py module and then run the it.

```
$ python signup.py
```

## How to use

- Create an object of the `Signup` class in `signup.py`
- Then pass in the parameters `firstname, lastname, countrycode, phone, email, password`
  for example:

```
 SIGNUP = Signup("julius", "mubajje", 256, 700572829,
               'jay@gmail.com', 'secret@123')
```

- Then on that object, call the message variable and print the output

```
MESSAGE = SIGNUP.message
print(MESSAGE)
```

- It should display a dictionary with keys, `err`and `msg`
- If there is an error, err will be true with the corressponding messege "msg" or otherwise

## Running Tests

- Tests are in `test_main.py`
- Test are run using python inbuilt unittesting module `unittest`

```
$ nosetests
```
