# ml
Notes I keep on Machine Learning.

## Installation
Although optional, the use of a python version managment tool and a virtual environment managment tool is highly 
recommended, to make sure that different projects can use different Python and libraries versions without interference.
In this project we use `pyenv`. Feel free to use whatever you like!

Install `pyenv` with `brew`:
```bash
brew install pyenv
```

Install Python with `pyenv`
```bash
pyenv install 3.12.7
```

Create a virtual environment with `pyenv`:
```bash
pyenv virtualenv 3.12.7 ml
```

Set `ml` as the local default virtual environment:
```bash
pyenv local ml
```

Upgrade `pip`:
```bash
pip install --upgrade pip
```

Install dependencies:
```bash
pip install -r requirements.txt
```