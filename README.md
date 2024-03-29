# Scrappier

Scrappier is a web scrapper which uses chrome in a headless mode. This library provides an easy-to-read syntaxis to navigate through the different elements and perform actions.

## Requirements

* python 3.8
* chrome driver installed in /usr/bin/chromedriver

## Instalation

`pip install scrappier`

## Basic usage

```python
from scrappier import Browser

browser = Browser()

cards = browser.where_class("card").get()

for card in cards:
    span = card.where_tag_name("span").first()

    print(span.text())
```

## Available methods for browser

### build()

### html()

### resize(width:int, height:int)

### screen(path:str)

### select(name:str, value:str)

### url()

### visit(url:str)

### wait(seconds:int)

### webdriver()

### where_inner_text(text)

### where_xpath(xpath:str)

### where_id(id:str)

### where_name(name:str)

### where_contain_text(name:str)

### where_class_name(name:str)

### where_tag_name(name:str)

### where_attribute()

### width()

## Available methods for ElementFinder

### until(seconds:int)

### get()

### first()

### where_xpath(xpath:str, driver, element=None)

### where_id(id:str, driver, element=None)

### where_inner_text(text:str, driver, element=None)

### where_contain_text(text, driver, element=None)

### where_class_name(name:str, driver, element=None)

### where_tag_name(name:str, driver, element=None)

### next_sibling(name:str, driver, element)

## Available methods for Element

### attributes() -> list

### enter()

### type(text:str)

### text()

### html()

### attribute(name:str)

### click()

### children()

### next_sibling()

### value(value:str = None)

gets the value of the element if there is no argument, but if an string was given, will set the input value

### where_tag_name(name:str)

### where_attribute(attribute:str, value:str)

## Colaborators

If you are a collaborator, please consider do the next:

1. Create your new functionality
2. Create a test of your new functionality
3. change the version of the package in setup.py
4. execute the next command: `python3 setup.py sdist bdist_wheel`
5. upload the package: `source venv/bin/active && twine upload dist/*<your-version>*`

## for developers

install twine: `python3 -m pip instal twine`
install setuptools: `pip3 install setuptools`
install setuptools: `python3 setup.py sdist bdist_wheel`
upload your changes: `twine upload dist/*`