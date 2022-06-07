from selenium import webdriver 
from selenium.webdriver.common.by import By
import pandas as pd
# from selenium.webdriver.commom.keys import Keys 
import time
import os

dt = pd.read_csv(os.getcwd() +"\\"+ 'data.csv')


url = "http://localhost:1085/"

driver = webdriver.Chrome("chromedriver.exe")
driver.get(url)

dir(driver)

email = driver.find_element(by=  By.NAME, value='name')
email.send_keys(dt['name'][0])
time.sleep(2)
email = driver.find_element(by = By.NAME, value='email')
email.send_keys(dt['email'][0])
time.sleep(2)


email = driver.find_element(by = By.NAME, value='next').click()
time.sleep(2)
email = driver.find_element(by = By.NAME, value='username')
email.send_keys(dt['username'][0])
time.sleep(2)
email = driver.find_element(by = By.NAME, value='password')
email.send_keys(dt['password'][0])
time.sleep(2)

email = driver.find_element(by = By.NAME, value='next').click()
time.sleep(2)

email = driver.find_element(by = By.NAME, value='number')
dt['number'] = dt['number'].to_string()
email.send_keys(dt['number'][0])
time.sleep(2)
email = driver.find_element(by = By.NAME, value='DOB')
email.send_keys(dt['DOB'][0])
time.sleep(2)
email = driver.find_element(by = By.NAME, value='next').click()
time.sleep(2)

if dt['gender'][0] == "Male":
    email = driver.find_element_by_xpath("//html//body//form//div[4]//input[1]").click()
elif dt['gender'][0] == "Female":
    email = driver.find_element_by_xpath("//html//body//form//div[4]//input[2]").click()
else:
    email = driver.find_element_by_xpath("//html//body//form//div[4]//input[3]").click()
time.sleep(2)

driver.close()

# email = driver.find_element_by_name('address')
# email.send_keys(dt['address'][0])
# time.sleep(2)
# email = driver.find_element_by_name('fname')
# email.send_keys(dt['fname'][0])
# time.sleep(2)
# email = driver.find_element_by_name('lname')
# email.send_keys(dt['lname'][0])
# time.sleep(2)


driver.quit()