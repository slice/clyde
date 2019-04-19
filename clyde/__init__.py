# encoding: utf-8

__all__ = ['register']
__title__ = 'clyde'
__version__ = '0.0.0'

from . import checker


def register(linter):
    for checker_name in checker.__all__:
        Checker = getattr(checker, checker_name)
        linter.register_checker(Checker(linter))
