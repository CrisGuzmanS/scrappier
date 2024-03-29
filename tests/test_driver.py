import unittest
from scrappier import Browser
import os

class TestDriver(unittest.TestCase):

    # def test_resize_method(self):

    #     browser = Browser()
    #     browser.resize(1400, 1000)
    #     self.assertEqual(1400, browser.width())

    # def test_snapshot(self):

    #     browser = Browser()
    #     browser.visit("https://github.com/public-apis/public-apis")
    #     browser.screenshot("images/test.png")
    #     self.assertTrue( os.path.isfile("images/test.png") )

    # def test_count(self):

    #     browser = Browser()
    #     browser.visit("https://github.com/public-apis/public-apis")
    #     count = browser.where_class_name("Box-row--focus-gray").get().count()

    #     self.assertEqual(7, count)

    # def test_where_inner_text(self):
    #     browser = Browser()
    #     browser.visit("https://github.com/public-apis/public-apis")

    #     element = browser.where_inner_text("Add files via upload").first()

    #     self.assertEqual("Add files via upload", element.text())

    # def test_visit(self):

    #     url = "https://github.com/public-apis/public-apis"
        
    #     params = {
    #         'first':'firstvalue'
    #     }

    #     browser = Browser()
    #     browser.visit(url)

    #     self.assertEqual(url, browser.url())

    #     browser.visit(url, params)

    #     self.assertEqual(url+"?first=firstvalue", browser.url())

    def test_alert(self):
        url = "https://testpages.herokuapp.com/styled/alerts/alert-test.html"

        browser = Browser()
        browser.visit(url)

        browser.where_attribute("id","confirmexample").first().click()
        browser.alert().accept()

        text = browser.where_attribute("id","confirmexplanation").first().text()

        self.assertEqual(text,"You clicked OK, confirm returned true.")

    # def test_select(self):

    #     url = "https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_option_value"

    #     browser = Browser()
    #     browser.visit(url)

    #     browser.webdriver().switch_to.frame("iframeResult")

    #     select = browser.where_attribute("name","cars").first()


    #     select.value("saab")

    #     self.assertEqual(select.value(), "saab")


    # def test_next_sibling(self):

    #     browser = Browser()
    #     browser.visit("https://github.com/public-apis/public-apis")
    #     sibling = browser.where_class_name("Box-row--focus-gray").first().next_sibling()

    #     print("==========")
    #     print("sibling")
    #     print("==========")
    #     print(sibling.text())
    #     print("==========")

    #     self.assertTrue(True)

    # def test_attributes(self):
    #     browser = Browser()
    #     browser.visit("https://github.com/public-apis/public-apis")
    #     attributes = browser.where_class_name("Box-row--focus-gray").first().attributes()
    #     print(attributes)

if __name__ == '__main__':
    unittest.main()