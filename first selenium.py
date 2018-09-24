from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.set_page_load_timeout(10) #sayfa yüklendikten sonra anlamına geliyor
driver.get("http://google.com")
driver.find_element_by_name("q").send_keys("ne aramak istiyorsunuz")
driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
time.sleep(4)
driver.maximize_window()
time.sleep(2)
driver.quit()
time.sleep(5)
river = webdriver.Chrome()
driver.set_page_load_timeout(10) #sayfa yüklendikten sonra anlamına geliyor
driver.get("http://google.com")
driver.find_element_by_name("q").send_keys("ne aramak istiyorsunuz")
driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
time.sleep(4)
driver.maximize_window()
driver.refresh()
time.sleep(3)
driver.quit()


print("işlem başarılı")