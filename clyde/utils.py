# encoding: utf-8

__all__ = ['ClydeChecker']

from pylint.checkers import BaseChecker
from pylint.interfaces import IAstroidChecker


class ClydeChecker(BaseChecker):
    __implements__ = IAstroidChecker
