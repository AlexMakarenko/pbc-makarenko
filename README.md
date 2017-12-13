*author: Alexander Makarenko*

# Python Boot Camp

## Day 1

### *fibonacci_app.py*
To get fibonacci sequence run `get_fibonacci_sequence(n)`, where n is a size of sequence. Out is a list of numbers.

### *numbers_app.py* 
To get pairs of numbers from 1 to 10 which sum is 10 run `get_pairs_of_numbers()`. Out is a set of pairs.

### *Vagrantfile*
Is a config for virtual machine `ubuntu/trusty64`.
* To up virtual machine you need to have `vagrant == latest version`, and `VirtualBox <= 5.1 version`.
* Run `vagrant up` in terminal.
* To connect to virtual machine use `ssh vagrant@192.168.33.10`, password is `vagrant`

## Day 2

### *Virtual environment*

Before running this project you need to set up a virtual environment. 
You need to have python 2.7 version. 
Then you can just run bash script from file `setup_virtualenv.sh` using command `sh setup_virtualenv.sh`
If you want to do it manually, follow these steps:
* `python virtualenv venv` To create a virtual environment
* `source venv/bin/activate` to activate virtual environment
* `pip install -r requirements.txt` to install packages from requirements.txt

### *Unit tests*

To run unit tests you need to have already set up virtual environment.
* for fibonacci tests run `pytest test_fibonacci.py`
* for numbers tests run `pytest test_numbers.py`

## Day 3

### 1. *Structurize project*

Project's structure was changed due to dev conventions for python devs.

### 2. *Use 'parametrize'*

All unit tests became parametrized due to similar tests logic.

### 3. *Configure markers*

Also, tests were marked with pytest markers and now you can use:

* `pytest -v -m fib` To run tests for `fibonacci_app`.
* `pytest -v -m numbers` To run tests for `numbers_app`.

### 4. *Use CLI config for your tow programs*
```
#   for fibonacci_app
run `python app.py --app fib -l 7` Where 7 is a desired length of the fibonacci sequence.
Output will be: 0, 1, 1, 2, 3, 5, 8

#   for pairs_of_numbers
run `python app.py --app pairs -n 1 2 3 4 5 6 7 8 9` Where `1 2 3 4 5 6 7 8 9` are numbers needed to be parsed.
Output will be: (5, 5), (2, 8), (4, 6), (1, 9), (3, 7)
```
### 5. *Decorator*

Both apps are using decorator `@log` for printing information needed for debugging in format `get_pairs_of_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9)
`

## Day 5

Added fixture which installs Selenium grid on Vagrant box using Python, pytest and paramiko before running tests.
To check run: `pytest -s -v tests`.

## Day 6

Run `pytest pbc` to check selenium grid.

## Day 7

Added Selenium test for Grid.

## Day 8

Added Rest test for Selenium Grid. 
Added UI test for remote webdriver.
To run all tests use `pytest -s -v`