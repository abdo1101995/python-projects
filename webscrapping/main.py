from selenium import webdriver
import csv
driver=webdriver.Chrome(r"D:\chrome_drive\ch\chromedriver.exe")
driver.get("https://www.sos.ca.gov/state-holidays")
date= driver.find_elements_by_xpath("//td[1]")
holidays= driver.find_elements_by_xpath("//td[2]")


for i in range(len(date)):
     print(date[i].text)
for i in range(len(holidays)):
     print(holidays[i].text)

with open('D:\holidays_date.csv', 'w', encoding='UTF8', newline='') as filecsv:
     csvwriter = csv.writer(filecsv, delimiter=',')
     csvwriter.writerow(["Date", 'holidays'])
     for i in range(0,len(date)):
          csvwriter.writerow([date[i].text, holidays[i].text])




