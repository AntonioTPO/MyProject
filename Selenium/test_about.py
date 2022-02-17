import time
import random
from selenium import webdriver

driver = webdriver.Chrome('C:\chromedriver.exe')  # Optional argument, if not specified will search path.

driver.get('http://127.0.0.1:8000/login')


time.sleep(5) # Let the user actually see something!

search_name = driver.find_element_by_name('username')
search_name.send_keys('heartbroken12')

search_pas = driver.find_element_by_name('password')
search_pas.send_keys('Dan447728842')

btn_elem = driver.find_element_by_id('125')
btn_elem.click()
time.sleep(2)

btn_elem1 = driver.find_element_by_id('124')
btn_elem1.click()
time.sleep(2)

btn_elem2 = driver.find_element_by_id('116')
btn_elem2.click()
time.sleep(2)

btn_elem3 = driver.find_element_by_id('115')
btn_elem3.click()
time.sleep(2)


UserTest = 'TestUser{}'.format(random.randint(2,100))
search_name = driver.find_element_by_name('username')
search_name.send_keys(UserTest)

search_pas = driver.find_element_by_name('password')
search_pas.send_keys('TestUser123123')

search_pas1 = driver.find_element_by_name('password1')
search_pas1.send_keys('TestUser123123')

search_pas2 = driver.find_element_by_name('password2')
search_pas2.send_keys('TestUser123123')

btn_elem4 = driver.find_element_by_name('reg_button')
btn_elem4.click()
time.sleep(2)

btn_elem5 = driver.find_element_by_id('111')
btn_elem5.click()
time.sleep(2)

btn_elem6 = driver.find_element_by_id('117')
btn_elem6.click()
time.sleep(2)

btn_elem7 = driver.find_element_by_id('127')
btn_elem7.submit()
time.sleep(2)



time.sleep(30) # Let the user actually see something!

driver.quit()