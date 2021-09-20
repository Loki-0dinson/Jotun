# -*- coding: utf-8 -*-

"""
Project settings
"""

from os import environ
import logging

# Cogs
COGS = [
    'cogs.utils',
]

# ENVIRONMENT VARIABLES
DEBUG = environ.get('DEBUG') in 'True'
APP_ID = environ.get('APP_ID')
PUBLIC_KEY = environ.get('PUBLIC_KEY')
SECRET = environ.get('SECRET')
TOKEN = environ.get('TOKEN')
DB_NAME = environ.get('DB_NAME')

# LOGGING CONFIG
LOG_LEVEL = logging.DEBUG if DEBUG else logging.INFO
LOG_FORMAT = '{levelname}: AT {asctime} IN {filename} MODULE {module} >>> \
    {message}'
LOG_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

# CONSTANTS
LANG_OPTIONS={
    'ENGLISH': 'EN',
    'SPANISH': 'ES'
}

LANG = LANG_OPTIONS.get(environ.get('LANG'), 'EN')
