import sqlite3 # Sqlite'yı dahil ediyoruz
from selenium import webdriver
import time
import locale
from datetime import datetime



şu_an = datetime.now()
zaman = datetime.strftime(şu_an,"%Y %B %A")
print(zaman)
print(locale.setlocale(locale.LC_ALL,""))