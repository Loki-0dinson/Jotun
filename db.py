# -*- coding: utf-8 -*-

"""
Database class for the bot.
"""

import logging
from sqlite3 import OperationalError
from typing import List

import aiosqlite

from core.settings import DB_NAME, LANG, LOG_LEVEL, LOG_FORMAT, LOG_DATE_FORMAT
from core.utils import loginfo, logwarn, logcritical


logger = logging.getLogger(__name__)
logger.setLevel(LOG_LEVEL)
formatter = logging.Formatter(
    fmt=LOG_FORMAT, datefmt=LOG_DATE_FORMAT, style='{')
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger.addHandler(handler)


class DB:
    """Represents a sqlite3 database instance

    The `DB` class is used to implement some level of persistence, the database
    name can be modified with the `DB_NAME`

    WARNING: Some methods may be suceptible to SQL Injection, the methods of
    this class should never accept user input directly without doing some clean
    up first 
    
    """
    
    @classmethod
    async def select(cls, columns: List[str], table: str) -> aiosqlite.Cursor:
        """
        Selects columns from a database
        """
        columns = ",".join(columns)
        async with aiosqlite.connect(DB_NAME) as db:
            loginfo(logger, f'Selecting from database {table}: {columns}')
            async with db.execute(f'SELECT {columns} FROM {table}') as cursor:
                return cursor
    
    @classmethod
    async def selectWhere(cls, columns: List[str], table: str, where: str) -> aiosqlite.Cursor:
        """
        Selects columns from a database where the values match the `where`
        expression
        """
        columns = ",".join(columns)
        async with aiosqlite.connect(DB_NAME) as db:
            loginfo(logger, f'Selecting from database {table}: {columns}')
            async with db.execute(f'SELECT {columns} FROM {table} WHERE {where}') as cursor:
                return cursor

    @classmethod
    async def insert(cls, into_table: str, columns: List[str], values: List[str]) -> None:
        """Insert values into a table"""
        columns = ",".join(columns)
        values = ",".join(values)
        async with aiosqlite.connect(DB_NAME) as db:
            loginfo(logger, f'Inserting into database {into_table} values {values}')
            await db.execute(f'INSERT INTO {into_table} ({columns}) VALUES ({values})')
            await db.commit()
    
    @classmethod
    async def _create(cls, table: str, columns: List[str]) -> None:
        """Creates a table with the given columns"""
        columns = ",".join(columns)
        async with aiosqlite.connect(DB_NAME) as db:
            loginfo(logger, f'Creating database table: {table}')
            await db.execute(f'CREATE TABLE {table} ({columns})')


    @classmethod
    async def setup(cls) -> None:
        """Checks if a database exists and if it has the basic configuration"""
        try:
            pass

        except OperationalError:
            pass
