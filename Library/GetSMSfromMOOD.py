import os
import time
from appium import webdriver

def getSMSfromMood(sender,ipHost,index,udid):
    index = int(index)
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '4.2'
    desired_caps['deviceName'] = 'Android Emulator'
    desired_caps['appPackage'] = 'com.calea.echo'
    desired_caps['appActivity'] = 'com.calea.echo.MainActivity'
    desired_caps['udid'] = udid
    driver = webdriver.Remote('http://'+ipHost+'/wd/hub', desired_caps)
    name = driver.find_element_by_name(sender)
    name.click()
    time.sleep(5)
    sms = driver.find_elements_by_xpath("//*[@resource-id='com.calea.echo:id/imm_text']")
    return sms[len(sms)-index].get_attribute("text")
