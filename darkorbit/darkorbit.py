from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


count = int(input("Kaç defa denesin: "))
refreshrate = int(input("Kaç saniyede bir: "))
beşlatma = time.strftime('%c')
print("başlatma tarihi : " + str(beşlatma))
print("==============================")


for i in range(count):
    time.sleep(refreshrate)
    b = time.strftime('%c')
    print(str(i + 1) + ". deneme başladı...  {}".format(b))

    #os.startfile("topluv3.py")
    driver = webdriver.Firefox()
    driver.maximize_window()
    time.sleep(2)

    driver.get("https://lp.darkorbit.com/")

    time.sleep(3)

    bbb = driver.find_element_by_id("bgcdw_login_form_username")
    bbb.send_keys("marjinalcapulcu")
    time.sleep(1)
    aaa = driver.find_element_by_id("bgcdw_login_form_password")
    aaa.send_keys("1329146219803")
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id='login']/div[1]/div/form/fieldset[2]/button[1]").click()
    time.sleep(2)
    # hasar
    driver.get("https://tr2.darkorbit.com/indexInternal.es?action=internalAuction")
    time.sleep(1)
    driver.find_element_by_xpath(
        "/html/body/div[12]/div/div/div[2]/div[4]/div/div[2]/div/div[5]/div[2]/div[1]/table/tbody[2]/div/div[1]/tr[40]/td[3]").click()
    driver.find_element_by_name("credits").clear()
    time.sleep(1)
    driver.find_element_by_name("credits").send_keys("20000000")
    time.sleep(1)
    driver.find_element_by_name("auction_buy_button").send_keys(Keys.ENTER)
    time.sleep(1)

    driver.get("https://tr2.darkorbit.com/indexInternal.es?action=internalAuction")

    # tp
    time.sleep(1)

    driver.find_element_by_xpath(
        "/html/body/div[12]/div/div/div[2]/div[4]/div/div[2]/div/div[5]/div[2]/div[1]/table/tbody[2]/div/div[1]/tr[38]/td[3]").click()
    driver.find_element_by_name("credits").clear()
    time.sleep(1)
    driver.find_element_by_name("credits").send_keys("5000000")
    time.sleep(1)
    driver.find_element_by_name("auction_buy_button").send_keys(Keys.ENTER)
    time.sleep(1)

    # şeref
    driver.get("https://tr2.darkorbit.com/indexInternal.es?action=internalAuction")

    time.sleep(1)

    driver.find_element_by_xpath(
        "/html/body/div[12]/div/div/div[2]/div[4]/div/div[2]/div/div[5]/div[2]/div[1]/table/tbody[2]/div/div[1]/tr[42]/td[3]").click()
    driver.find_element_by_name("credits").clear()
    time.sleep(1)
    driver.find_element_by_name("credits").send_keys("10000000")
    time.sleep(1)
    driver.find_element_by_name("auction_buy_button").send_keys(Keys.ENTER)
    time.sleep(1)

    # dp #/html/body/div[12]/div/div/div[2]/div[4]/div/div[2]/div/div[5]/div[2]/div[1]/table/tbody[2]/div/div[1]/tr[45]/td[3]
    driver.get("https://tr2.darkorbit.com/indexInternal.es?action=internalAuction")

    time.sleep(1)

    driver.find_element_by_xpath(
        "/html/body/div[12]/div/div/div[2]/div[4]/div/div[2]/div/div[5]/div[2]/div[1]/table/tbody[2]/div/div[1]/tr[45]/td[3]").click()
    driver.find_element_by_name("credits").clear()
    time.sleep(1)
    driver.find_element_by_name("credits").send_keys("1000000")
    time.sleep(1)
    driver.find_element_by_name("auction_buy_button").send_keys(Keys.ENTER)
    time.sleep(1)

    # kalkan(/html/body/div[12]/div/div/div[2]/div[4]/div/div[2]/div/div[5]/div[2]/div[1]/table/tbody[2]/div/div[1]/tr[39]/td[3])
    driver.get("https://tr2.darkorbit.com/indexInternal.es?action=internalAuction")

    time.sleep(1)

    driver.find_element_by_xpath(
        "/html/body/div[12]/div/div/div[2]/div[4]/div/div[2]/div/div[5]/div[2]/div[1]/table/tbody[2]/div/div[1]/tr[39]/td[3]").click()
    driver.find_element_by_name("credits").clear()
    time.sleep(1)
    driver.find_element_by_name("credits").send_keys("5000000")
    time.sleep(1)
    driver.find_element_by_name("auction_buy_button").send_keys(Keys.ENTER)
    time.sleep(1)

    # x3 #/html/body/div[12]/div/div/div[2]/div[4]/div/div[2]/div/div[5]/div[2]/div[1]/table/tbody[2]/div/div[1]/tr[2]/td[3]

    driver.get("https://tr2.darkorbit.com/indexInternal.es?action=internalAuction")

    time.sleep(1)

    driver.find_element_by_xpath(
        "/html/body/div[12]/div/div/div[2]/div[4]/div/div[2]/div/div[5]/div[2]/div[1]/table/tbody[2]/div/div[1]/tr[2]/td[3]").click()
    driver.find_element_by_name("credits").clear()
    time.sleep(1)
    driver.find_element_by_name("credits").send_keys("100000")
    time.sleep(1)
    driver.find_element_by_name("auction_buy_button").send_keys(Keys.ENTER)
    time.sleep(1)

    # kamufle
    driver.get("https://tr2.darkorbit.com/indexInternal.es?action=internalAuction")
    time.sleep(1)

    driver.find_element_by_xpath(
        "/html/body/div[12]/div/div/div[2]/div[4]/div/div[2]/div/div[5]/div[2]/div[1]/table/tbody[2]/div/div[1]/tr[11]/td[2]").click()
    driver.find_element_by_name("credits").clear()
    time.sleep(1)
    driver.find_element_by_name("credits").send_keys("100000000")
    time.sleep(1)
    driver.find_element_by_name("auction_buy_button").send_keys(Keys.ENTER)
    time.sleep(2)

    driver.quit()





































































    q = time.strftime('%c')

    print(str(i + 1) + ". deneme tamamlandı...  {}".format(q))

    print("##################################")









