from selenium import webdriver
import time


browser =webdriver.Chrome()
browser.get("https://www.instagram.com/")
time.sleep(2)

girişYap = browser.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[2]/p/a")
girişYap.click()
time.sleep(2)
username = browser.find_element_by_name("username")
password = browser.find_element_by_name("password")
username.send_keys("l4melif")
password.send_keys("1920215")

loginButton = browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/span/button")
loginButton.click()

time.sleep(2)
profil =browser.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[3]/a")
profil.click()
time.sleep(2)
takipciler =browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a")
takipciler.click()
time.sleep(5)
browser.close()





