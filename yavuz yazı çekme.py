from selenium import webdriver
import time


browser = webdriver.Chrome()

browser.get("https://www.yeniakit.com.tr/yazarlar/yavuz-bahadiroglu/kainat-kuran-insan-ayet-25100.html")

time.sleep(3)

lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match=False
while(match==False):
    lastCount = lenOfPage
    time.sleep(3)
    lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    if lastCount == lenOfPage:
        match=True
time.sleep(5)

tweets = []

elements = browser.find_elements_by_css_selector(".entry")
for element in elements:
    tweets.append(element.text)

tweetCount = 1

with open("yazılar.txt","w",encoding = "UTF-8") as file:
    for tweet in tweets:
        file.write(str(tweetCount) + ".\n" + tweet + "\n")
        file.write("**************************\n")
        tweetCount += 1

browser.close()







