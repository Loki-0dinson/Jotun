import concurrent.futures
from typing import Any, Iterable, TypeVar


# Things that need instantiantion or set up go here
_executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)

# Custom types
logger_T = TypeVar('logging.Logger')


def loginfo(logger: logger_T, msg: str, *args: Iterable[Any]) -> None:
    """Logs a message with log level INFO
    
    Args:
        logger: a logging instance
        msg: message to be logged

    """
    _executor.submit(logger.info, msg, *args)


def logwarn(logger: logger_T, msg: str, *args: Iterable[Any]) -> None:
    """Logs a message with log level WARNING"""
    _executor.submit(logger.warning, msg, *args)


def logerror(logger: logger_T, msg: str, *args: Iterable[Any]) -> None:
    """Logs a message with log level ERROR"""
    _executor.submit(logger.error, msg, *args)


def logcritical(logger: logger_T, msg: str, *args: Iterable[Any]) -> None:
    """Logs a message with log level CRITICAL"""
    _executor.submit(logger.critical, msg, *args)
