import unittest
from scrappier.browser import Browser
import os

class TestDriver(unittest.TestCase):

    def test_resize_method(self):

        browser = Browser()
        browser.resize(1400, 1000)
        self.assertEqual(1400, browser.width())

    def test_snapshot(self):

        browser = Browser()
        browser.visit("https://github.com/public-apis/public-apis")
        browser.screenshot("images/test.png")
        self.assertTrue( os.path.isfile("images/test.png") )

    def test_count(self):

        browser = Browser()
        browser.visit("https://github.com/public-apis/public-apis")
        count = browser.where_class_name("Box-row--focus-gray").get().count()

        self.assertEqual(7, count)

if __name__ == '__main__':
    unittest.main()