from selenium import webdriver 
from selenium.webdriver.common.by import By
import pandas as pd
# from selenium.webdriver.commom.keys import Keys 
import time
import os

class Insert():



    def __init__(self,driver):
        self.driver = driver
        # self.driver = webdriver.Chrome("chromedriver.exe")
        self.url = "http://localhost:1085/"
        self.driver.get(self.url)


    def get_data(self,data):
        self.data = data
        self.dt = pd.read_csv(os.getcwd() +"\\"+ self.data)

# dt = pd.read_csv(os.getcwd() +"\\"+ 'data.csv')


# url = "http://localhost:1085/"

# driver = webdriver.Chrome("chromedriver.exe")
# driver.get(url)

    def insert(self):
        
                

        email = self.driver.find_element(by=  By.NAME, value='name')
        email.send_keys(self.dt['name'][0])
        time.sleep(2)
        email = self.driver.find_element(by = By.NAME, value='email')
        email.send_keys(self.dt['email'][0])
        time.sleep(2)


        email = self.driver.find_element(by = By.NAME, value='next').click()
        time.sleep(2)
        email = self.driver.find_element(by = By.NAME, value='username')
        email.send_keys(self.dt['username'][0])
        time.sleep(2)
        email = self.driver.find_element(by = By.NAME, value='password')
        email.send_keys(self.dt['password'][0])
        time.sleep(2)

        email = self.driver.find_element(by = By.NAME, value='next').click()
        time.sleep(2)

        email = self.driver.find_element(by = By.NAME, value='number')
        self.dt['number'] = self.dt['number'].to_string()
        email.send_keys(self.dt['number'][0])
        time.sleep(2)
        email = self.driver.find_element(by = By.NAME, value='DOB')
        email.send_keys(self.dt['DOB'][0])
        time.sleep(2)
        email = self.driver.find_element(by = By.NAME, value='next').click()
        time.sleep(2)

        if self.dt['gender'][0] == "Male":
            email = self.driver.find_element_by_xpath("//html//body//form//div[4]//input[1]").click()
        elif self.dt['gender'][0] == "Female":
            email = self.driver.find_element_by_xpath("//html//body//form//div[4]//input[2]").click()
        else:
            email = self.driver.find_element_by_xpath("//html//body//form//div[4]//input[3]").click()
        time.sleep(2)

        self.driver.close()

# email = driver.find_element_by_name('address')
# email.send_keys(dt['address'][0])
# time.sleep(2)
# email = driver.find_element_by_name('fname')
# email.send_keys(dt['fname'][0])
# time.sleep(2)
# email = driver.find_element_by_name('lname')
# email.send_keys(dt['lname'][0])
# time.sleep(2)

if __name__ =="__main__":


    driver = webdriver.Chrome("chromedriver.exe")
    pp = Insert(driver)
    data = 'data.csv'
    pp.get_data(data=data)
    pp.insert()
