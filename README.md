# Python-OOP

## Implements uber-ui

Python program that validated user signup input data using Object Oriented Programming 

## Installation 
- Clone the repository 

## Tools
- Python3.6
- Auto pep8 for vscode
- Pylint for linting also can be installed with vscode
```
 You need Python3+ no inbuild modules where imported
```

## Demo
- Uncomment the script at the end of the signup.py module and then run the it.
```
$ python signup.py
```

## How to use

- Create an object of the `Signup` class in `signup.py`
- Then pass in the parameters `firstname, lastname, countrycode, phone, email, password`
```
 SIGNUP = Signup("julius", "mubajje", 256, 758572829,
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
$ py -m unittest -v
```
or (But not tested)
```
$ python3 -m unittest -v
```
