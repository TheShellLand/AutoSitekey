import unittest

from autositekey import _ALL_CLASSES
from autositekey import AutoSiteKeyClient


class MyTestCase(unittest.TestCase):
    def test(self):
        for test in _ALL_CLASSES:
            test
            pass


if __name__ == '__main__':
    unittest.main()
