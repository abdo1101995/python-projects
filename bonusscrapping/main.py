from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import numpy as np
import re
driver=webdriver.Chrome(r"D:\chrome_drive\ch\chromedriver.exe")
driver.get("http://books.toscrape.com/catalogue/category/books_1/page-1.html")
# date= driver.find_elements_by_xpath("//td[1]")
# holidays= driver.find_elements_by_xpath("//td[2]")