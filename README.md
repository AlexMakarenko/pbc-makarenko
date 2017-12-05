*author: Alexander Makarenko*

# Python Boot Camp

## Day 1

### *fibonacci.py*
To get fibonacci sequence run function fibonacci_sequence(n), where n is a size of sequence. Out is a list of numbers.

### *numbers.py* 
To get pairs of numbers from 1 to 10 which sum is 10 run get_pairs_of_numbers(). Out is a set of pairs.

### *Vagrantfile*
Is a config for virtual machine `ubuntu/trusty64`.
* To up virtual machine you need to have vagrant == latest version, and VirtualBox <= 5.1 version.
* Run `vagrant up` in terminal.
* To connect to virtual machine use `ssh vagrant@192.168.33.10`, password is `vagrant`

## Day 2

### *Virtual environment*

Before running this project you need to set up a virtual environment. 
You need to have a latest python version. 
Then you can just run bash script from file `setup_virtualenv.sh` using command `sh setup_virtualenv.sh`
If you want to do it manually, follow these steps:
* `python3 -m venv venv` To create a virtual environment
* `source venv/bin/activate` to activate virtual environment
* `pip install -r requirements.txt` to install packages from requirements.txt

### *Unit tests*

To run unit tests you need to have already set up virtual environment.
* for fibonacci tests run `pytest test_fibonacci.py`
* for numbers tests run `pytest test_numbers.py`