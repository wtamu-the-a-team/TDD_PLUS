from selenium import webdriver
import time

browser = webdriver.Firefox()

# Edith has heard about a cool new online to-do app. She goes
# to check out its homepage
browser.get('http://localhost:8000')

# assert 'To-Do' in browser.title

time.sleep(3)

browser.quit()