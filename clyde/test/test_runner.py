# encoding: utf-8

import os
import sys
from pathlib import Path

import pylint

# Import the internal module-based testing mechanisms from pylint.
# We use these internal mechanisms to test the checkers.
sys.path.append(os.path.join(os.path.dirname(pylint.__file__), 'test'))
import test_functional


class LintModuleTest(test_functional.LintModuleTest):
    def __init__(self, test_file):
        super().__init__(test_file)
        self._linter.load_plugin_modules(['clyde'])


def _test_module(path):
    test = LintModuleTest(test_functional.FunctionalTestFile(str(path.parent), path.name))
    test.setUp()
    test._runTest()


def test_everything():
    for path in (Path(__file__).parent / 'input').glob('*.py'):
        _test_module(path)
