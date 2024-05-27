import unittest
import asyncio

from autositekey.client import AutoSiteKeyClient


class MyTestCase(unittest.TestCase):
    def test_something(self):
        c = AutoSiteKeyClient()
        asyncio.run(c.run(headless=False))
        self.assertTrue(asyncio.run(c.get('https://1.1.1.1')))


if __name__ == '__main__':
    unittest.main()
