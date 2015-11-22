#!/usr/bin/env python
"""
test web use selenium
"""

from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http://localhost:8000')
assert 'Django' in browser.title
