# -*- coding: utf-8 -*-

"""
Project settings
"""

from os import environ
from logging import DEBUG as L_DEBUG, INFO as L_INFO

# Cogs
COGS = [
    'cogs.administration',
    'cogs.utilities',
]

# ENVIRONMENT VARIABLES
DEBUG = environ.get('DEBUG') in 'True'
APP_ID = environ.get('APP_ID')
PUBLIC_KEY = environ.get('PUBLIC_KEY')
SECRET = environ.get('SECRET')
TOKEN = environ.get('TOKEN')
DB_NAME = environ.get('DB_NAME')

# LOGGING CONFIG
LOG_LEVEL = L_DEBUG if DEBUG else L_INFO
LOG_FORMAT = '{levelname}: AT {asctime} IN {filename} MODULE {module} >>> \
    {message}'
LOG_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

# CONSTANTS
LANG_OPTIONS={
    'ENGLISH': 'EN',
    'SPANISH': 'ES'
}

LANG = LANG_OPTIONS.get(environ.get('LANG'), 'EN')

# DEFAULT COLORS
COLOR_ERROR   = 15882328 # red
COLOR_INFO    = 5793266 # blue
COLOR_SUCCESS = 6615640 # green
COLOR_WARNING = 16770605  # yellow