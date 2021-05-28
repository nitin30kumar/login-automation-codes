import selenium
from selenium import webdriver
import time
#from webdriver_manager.chrome import ChromeDriverManager

print('Enter the gmailid and password')
gmailId, passWord = map(str, input().split())
try:
	#driver = webdriver.Chrome(ChromeDriverManager().install())
    driver = webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe")
    driver.get(r'https://accounts.google.com/signin/v2/identifier?continue=' + \
               'https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1' + \
               '&flowName=GlifWebSignIn&flowEntry = ServiceLogin')
    driver.implicitly_wait(15)
    time.sleep(5)

    loginBox = driver.find_element_by_xpath('//*[@id ="identifierId"]')
    loginBox.send_keys(gmailId)
    time.sleep(5)

    nextButton = driver.find_elements_by_xpath('//*[@id ="identifierNext"]')
    nextButton[0].click()
    time.sleep(5)

    passWordBox = driver.find_element_by_xpath(
        '//*[@id ="password"]/div[1]/div / div[1]/input')
    passWordBox.send_keys(passWord)

    nextButton = driver.find_elements_by_xpath('//*[@id ="passwordNext"]')
    nextButton[0].click()

    print('Login Successful...!!')
except:
    print('Login Failed')
