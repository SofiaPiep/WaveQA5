import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


from selenium import webdriver

def test_simple():
 driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

 driver.get("https://www.saucedemo.com/")

 assert driver.title == "Swag Labs"

 driver.quit()
