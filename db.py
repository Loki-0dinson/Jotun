# -*- coding: utf-8 -*-

"""
Database class for the bot.
"""

import logging
from typing import List

from core.settings import DB_NAME, LOG_LEVEL, LOG_FORMAT, LOG_DATE_FORMAT

from sqlite3 import OperationalError # pylint: disable=E0611
import aiosqlite


logger = logging.getLogger(__name__)
logger.setLevel(LOG_LEVEL)
formatter = logging.Formatter(
    fmt=LOG_FORMAT, datefmt=LOG_DATE_FORMAT, style='{')
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger.addHandler(handler)


class DB:
    """
    Represents a sqlite3 database instance

    The `DB` class is used to implement some level of persistence, the database
    name can be modified with the `DB_NAME`

    WARNING: Some methods may be suceptible to SQL Injection, the methods of
    this class should never accept user input directly without doing some clean
    up first
    """

    @classmethod
    async def select(cls, columns: List[str], table: str):
        """
        Selects columns from a database
        """
        columns = ",".join(columns)
        async with aiosqlite.connect(DB_NAME) as cursor:
            logger.info('Selecting from database %s: %s', table, columns)
            async with cursor.execute(f'SELECT {columns} FROM {table}') as _cursor:
                return _cursor

    @classmethod
    async def select_where(cls, columns: List[str], table: str, where: str):
        """
        Selects columns from a database where the values match the `where`
        expression
        """
        columns = ",".join(columns)
        async with aiosqlite.connect(DB_NAME) as cursor:
            logger.info('Selecting from database %s: %s', table, columns)
            async with cursor.execute(
                    f'SELECT {columns} FROM {table} WHERE {where}') as _cursor:
                return _cursor

    @classmethod
    async def insert(cls, into_table: str, columns: List[str], values: List[str]):
        """Insert values into a table"""
        columns = ",".join(columns)
        values = ",".join(values)
        async with aiosqlite.connect(DB_NAME) as cursor:
            logger.info(
                'Inserting into database %s values %s', into_table, values)
            await cursor.execute(
                f'INSERT INTO {into_table} ({columns}) VALUES ({values})')
            await cursor.commit()

    @classmethod
    async def _create(cls, table: str, columns: List[str]):
        """Creates a table with the given columns"""
        columns = ",".join(columns)
        async with aiosqlite.connect(DB_NAME) as cursor:
            logger.info('Creating database table: %s', table)
            await cursor.execute(f'CREATE TABLE {table} ({columns})')


    @classmethod
    async def setup(cls):
        """Checks if a database exists and if it has the basic configuration"""
        try:
            pass

        except OperationalError:
            pass
