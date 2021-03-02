#!/usr/bin/env python
# coding: utf-8
from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'C:/Users/cferr/Downloads/chromedriver_win32/chromedriver.exe') 

url = 'https://sisweb.ucd.ie/usis/W_HU_MENU.P_PUBLISH?p_tag=GYMBOOK'
driver.get(url)

# xpath for initial book button
initial_book = '//*[@id="SW300-1|2"]/td[6]/a'
#click the button
button = driver.find_element_by_xpath(initial_book)

# # clicking on the button
button.click()

student_path = '/html/body/main/div/div/div/div[2]/div/form/input[4]'

#wait for page to load
driver.implicitly_wait(10)

#click accept on the cookies pop up
consent_path = '//*[@id="onetrust-accept-btn-handler"]'
button = driver.find_element_by_xpath(consent_path)

# clicking on the button
button.click()

# get student number box path 
element= driver.find_element_by_xpath(student_path)
# your gym ID (student number) goes here
student_number = ''
#input student number into box
element.send_keys(student_number)

#xpath for book button
final_book ='/html/body/main/div/div/div/div[2]/div/form/input[5]'

#click the button once student number is inputted
button = driver.find_element_by_xpath(final_book)

# clicking on the button
button.click()

confirm_path = '//*[@id="single-column-content"]/div/div/div/div[2]/div/a[1]'

button = driver.find_element_by_xpath(confirm_path)

# clicking on the button
button.click()


