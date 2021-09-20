import aiosqlite
from typing import List, TypeVar


_T = TypeVar('_T')

class DB:
    @classmethod
    async def select(cls: _T, columns: List[str], table: str) -> aiosqlite.Cursor: ...
    @classmethod
    async def selectWhere(cls: _T, columns: List[str], table: str, where: str) -> aiosqlite.Cursor: ...
    @classmethod
    async def insert(cls: _T, into_table: str, columns: List[str], values: List[str]) -> None: ...
    @classmethod
    async def _create(cls: _T, table: str, columns: List[str]) -> None: ...
    @classmethod
    async def setup(cls: _T) -> None: ...
