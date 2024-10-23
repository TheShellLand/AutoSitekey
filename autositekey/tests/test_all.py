import unittest

from autositekey import _ALL_CLASSES
from autositekey import AutoSiteKeyClient


class MyTestCase(unittest.TestCase):
    def test_tests(self):
        for CLASS in _ALL_CLASSES:
            if CLASS.__name__ == 'MwejobsHK':
                pass


if __name__ == '__main__':
    unittest.main()
