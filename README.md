## Welcome to Jotun bot - ᛃᛟᛏᚢᚾ ᛒᛟᛏ

Jotun is a discord bot that currently is a WIP

## Installation
```bash
# Clone the repo
$ git clone https://github.com/Loki-0dinson/Jotun.git
$ cd ./Jotun
```

Then create a `.env` file, and replace the values as follow:
```bash
DEBUG="True" # Anything other than "True" will be set this to False
APP_ID="YOUR_DISCORD_APP_ID"
PUBLIC_KEY="YOUR_DISCORD_APP_PUBLIC_KEY"
SECRET="YOUR_DISCORD_APP_SECRET"
TOKEN="YOUR_DISCORD_APP_TOKEN"
DB_NAME="NAME_OF_THE_LOCAL_SQLite3_DB" # Any name is ok, the SQLite3 database file will be created using this name 
```

[OPTIONAL] If you are on a Debian-based distribution you may want to install these `discord.py` dependencies:
```bash
$ apt install libffi-dev libnacl-dev python3-dev
```

Now we install pipenv which we will use to create a virtual environment
```bash
# Install pipenv
$ python3 -m pip install pipenv

# Install Pipfile dependencies and activate virtual environment
$ pipenv install && pipenv shell

# Run the bot
$ python main.py
```
⚠ WARNING ⚠ By default, `python 3.9` will be used, if you want to use a diferent version just modify the `Pipfile` or
specify it to `pipenv` with the `--python` flag (must be 3.6 or above, you can check your version with `python3 --version`)

# Requirements
| Name  | Version | Package | Dev-Package |
| ------------- |:-------------:|:-------------:|:-------------:|
| discord.py    | 1.7.3 | ✅ |  |
| aiosqlite     | 0.17.0 | ✅ |  |
| autopep8      | * |  | ✅ |
| icecream      | * |  | ✅ |
