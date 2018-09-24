import sqlite3 # Sqlite'yı dahil ediyoruz

import time
from selenium import *

from selenium import webdriver

con = sqlite3.connect("darkorbit.db") # Tabloya bağlanıyoruz.

cursor = con.cursor() # cursor isimli değişken veritabanı üzerinde işlem yapmak için kullanacağımız imleç olacak.

def tablo_oluştur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık (Tarih TEXT, Tp INT, Şeref INT, Rütbe INT, Uridium INT)") # Sorguyu çalıştırıyoruz.
    con.commit() # Sorgunun veritabanı üzerinde geçerli olması için commit işlemi gerekli.
def deger_ekle(Tarih,Tp,Şeref,Rütbe,Uridium):
    cursor.execute("Insert into kitaplık Values(?,?,?,?,?)",(Tarih,Tp,Şeref,Rütbe,Uridium))
    con.commit()
def verileri_al():
    cursor.execute("Select * From kitaplık")
    data = cursor.fetchall()
    #print("Kitaplık Tablosunun bilgileri.....")
    for i in data:
        print(i)
def verileri_al2():   #tarihleri alıyor
    cursor.execute("Select Tarih From kitaplık")
    data = cursor.fetchall()
    print("Kitaplık Tablosunun bilgileri.....")
    for i in data:
        print(i)
def giris_yap():
    adi = input("Username : ")
    passwor = input("Password: ")


    driver = webdriver.Chrome()

    time.sleep(1)

    driver.get("https://lp.darkorbit.com/")
    time.sleep(3)
    # driver.minimize_window()

    bbb = driver.find_element_by_id("bgcdw_login_form_username")
    bbb.send_keys(adi)
    time.sleep(1)
    aaa = driver.find_element_by_id("bgcdw_login_form_password")
    aaa.send_keys(passwor)
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id='login']/div[1]/div/form/fieldset[2]/button[1]").click()
    time.sleep(2)

    url = "https://tr2.darkorbit.com/indexInternal.es?action=internalHallofFame&view=dailyRank"
    driver.get(url)
    time.sleep(1)
    rutbe = driver.find_element_by_id("hof_daily_points_points").text
    # rutbe  = point[17:]
    print(rutbe)

    tpp = driver.find_element_by_class_name("hof_units_amount").text  # tecrübe puanı
    print("tp: " + tpp)

    honor = driver.find_element_by_id("header_top_hnr").text
    print("şeref: " + honor)

    uri = driver.find_element_by_id("header_uri").text  # uridium
    print(uri)

    zaman = time.strftime('%c')

    deger_ekle(zaman, tpp, honor, rutbe, uri)

    print("işlem tamamlandı")
    print("""     Tarih                          TP           Şeref         Rütbe Puanı    Uridium """)
    print("""======================================================================================""")
    driver.close()

    verileri_al()

def verilerisil():

    cursor.execute("Select * From kitaplık")
    data = cursor.fetchall()
    liste=list()
    for i in data:
        liste.append(i)

    if len(liste) >= 11:
        return liste.pop(0)


    else:
        print(liste)




















###########################################################
giris_yap()
































































