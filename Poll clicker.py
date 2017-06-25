# -*- coding: utf-8 -*-

# import codecs
import random
from time import sleep
import time

import list_of_locators as lst
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait

driver = webdriver.Chrome()
driver.set_window_size(800, 600)
driver.set_page_load_timeout(5)
base_url = 'https://www.survio.com/survey/d/O7F2Y9I0V9J0Y7J4S'


def clicker_method():
	# first_result = WebDriverWait(driver, 5).until(lambda browser: browser.find_element_by_class_name('input-group-addon'))
	# first_link = first_result.find_element_by_tag_name('a')
	driver.get(base_url)
	starttime = time.time()
	print(starttime)
	# driver.execute_script('window.stop();')
	sleep(1)
	stoptime = time.time()
	print(starttime - stoptime)
	# WebDriverWait.until(EC.title_contains('Удовлетворенность'))


	# print('time out')
	# driver.execute_script('window.stop();')
	# заполняется основная часть опроса

	for locator in lst.listing:
		# print(locator)
		choice = random.choice(locator)
		print(choice)
		driver.find_element_by_xpath(choice).click()

	# заполняются текстовые поля
	# driver.find_element_by_xpath('//fieldset[8]/div/label/textarea').click()
	# driver.find_element_by_xpath('//fieldset[8]/div/label/textarea').send_keys('write something')

	driver.find_element_by_xpath('//fieldset[9]/div/label/textarea').clear()

	# рандомное чтение  строк из файла
	randname = random.choice(open('names.txt').read().splitlines())
	driver.find_element_by_xpath('//fieldset[9]/div/label/textarea').send_keys(randname)
	driver.delete_all_cookies()
	driver.close()


# with open('names.txt', 'r') as file:
for i in range(5):
	print(i + 1)
	clicker_method()

webdriver.Firefox.quit()
