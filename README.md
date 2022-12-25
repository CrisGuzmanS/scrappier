# Scrappier

Scrappier is a web scrapper which uses chrome in a headless mode. This library provides an easy-to-read syntaxis to navigate through the different elements and perform actions.

## Requirements

* python 3.8
* chrome driver installed in /usr/bin/chromedriver

## Instalation

`pip install scrappier`

## Basic usage

    from scrappier import Browser

    browser = Browser()

    cards = browser.where_class("card").get()

    for card in cards:
        span = card.where_tag_name("span").first()

        print(span.text())

## Available methods for browser

### build()

### resize(width:int, height:int)

### screen(path:str)

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

### where_tag_name(name:str)

### where_attribute(attribute:str, value:str)

