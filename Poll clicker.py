# -*- coding: utf-8 -*-
import codecs
import random
import list_of_locators as lst
from selenium import webdriver

driver = webdriver.Firefox()
driver.implicitly_wait(5)
base_url = "https://www.survio.com/"

try:
    # driver = webdriver.Firefox()
    driver.set_page_load_timeout(4)
    driver.get(base_url + "/survey/d/O7F2Y9I0V9J0Y7J4S")
except Exception:
    print('time out')
    driver.execute_script("window.stop();")

for i in lst.listing:
    driver.find_element_by_xpath(random.choice(i)).click()


driver.find_element_by_xpath("//textarea").clear()
driver.find_element_by_xpath("//textarea").send_keys(u"Купить Ире Оксюковской новый стул")
driver.find_element_by_xpath("//fieldset[9]/div/label/textarea").clear()

# чтение не юникодовского файла (кирилица)
randname = random.choice(list(codecs.open('names.txt', encoding='1251').readlines()))
driver.find_element_by_xpath("//fieldset[9]/div/label/textarea").send_keys(randname)

# driver.close()
