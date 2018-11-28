from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time
from bs4 import BeautifulSoup

# ***************Getting Updated files from Bugzero**************
chrome_option = webdriver.ChromeOptions()
os.chdir(r'D:\Users\kekishor\Desktop\project')

prefs = {"download.prompt_for_download" : False,
        'download.default_directory' : os.getcwd()}

chrome_option.add_experimental_option('prefs', prefs)

a = input('What do you want to search: ')

driver = webdriver.Chrome(options=chrome_option)
driver.get('https://www.google.com')

driver.find_element_by_name('q').send_keys(a)
time.sleep(2)

driver.find_element_by_name('btnK').click()

a = driver.page_source

source = BeautifulSoup(a, 'lxml')

links = []
for i in source.find_all('a'):
    try:
        links.append(i.get('href'))
    except:
        pass


