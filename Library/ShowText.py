import ShowMe
import os
from selenium import webdriver

def play_button(self):
    ShowMe.Show("GG WP")
def TextWebMon(str):
    chromedriver = "C:/workspace/chromedriver.exe"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)
    driver.get(str)
