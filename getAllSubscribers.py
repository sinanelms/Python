from selenium import webdriver

import time


browser = webdriver.Chrome()

browser.get("https://www.instagram.com/")

time.sleep(2)

girisYap = browser.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[2]/p/a")

girisYap.click()

time.sleep(2)

username = browser.find_element_by_name("username")
password = browser.find_element_by_name("password")

username.send_keys("...)
password.send_keys("...")


loginButton = browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[4]/button")

loginButton.click()

time.sleep(3)

loginButton = browser.find_element_by_xpath("/html/body/div[3]/div/div/div[3]/button[2]")

loginButton.click()


time.sleep(2)


profileButton = browser.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[3]/a")


profileButton.click()

time.sleep(3)


"""

buttons = browser.find_elements_by_css_selector("._bnq48")

followersButton = buttons[1]

followersButton.click()

time.sleep(5)

jscommand = """"""2
followers = document.querySelector("._gs38e");
followers.scrollTo(0, followers.scrollHeight);
var lenOfPage=followers.scrollHeight;
return lenOfPage;

""""""
lenOfPage = browser.execute_script(jscommand)
match=False
while(match==False):
    lastCount = lenOfPage
    time.sleep(1)
    lenOfPage = browser.execute_script(jscommand)
    if lastCount == lenOfPage:
        match=True
time.sleep(5)
followersList = []

followers = browser.find_elements_by_css_selector("._2g7d5.notranslate._o5iw8")



for follower in followers:
    
    followersList.append(follower.text)
    
with open("followers.txt","w",encoding = "UTF-8") as file:
    for follower in followersList:
        file.write(follower + "\n")
        





"""





          
browser.close()


