# ml-tutorial
Notes I keep on Machine Learning.

## Installation
Install pyenv-virtualenv through brew:
```bash
brew install pyenv-virtualenv
```

Install python through pyenv:
```bash
pyenv install 3.12.6
```

Create a virtual environment through pyenv-virtualenv:
```bash
pyenv virtualenv 3.12.6 ml-tutorial
```

Set ml-tutorial as the local default virtualenv:
```bash
pyenv local ml-tutorial
```

Upgrade pip:
```bash
pip install --upgrade pip
```

Install dependencies:
```bash
pip install -r requirements.txt
```