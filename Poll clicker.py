# -*- coding: utf-8 -*-

import codecs
import random

import list_of_locators as lst
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def clicker_method():
    profile = webdriver.FirefoxProfile()
    profile.set_preference("browser.cache.disk.enable", False)
    profile.set_preference("browser.cache.memory.enable", False)
    profile.set_preference("browser.cache.offline.enable", False)
    profile.set_preference("network.http.use-cache", False)
    driver = webdriver.Firefox(profile)
    driver.implicitly_wait(4)
    base_url = "https://www.survio.com/"

    try:
        driver.get(base_url + "/survey/d/O7F2Y9I0V9J0Y7J4S")
        # wait = WebDriverWait(driver, 5)
        # element = wait.until(EC.title_contains('Удовлетворенность'))
        driver.set_page_load_timeout(5)
        driver.execute_script("window.stop();")

    except Exception:
        print('time out')
        driver.execute_script("window.stop();")
    # заполняется основная часть опроса
    for i in lst.listing:
        driver.find_element_by_xpath(random.choice(i)).click()
    # заполняются текстовые поля
    driver.find_element_by_xpath("//textarea").clear()
    driver.find_element_by_xpath("//textarea").send_keys(u"Купить Ире Оксюковской новый стул")
    driver.find_element_by_xpath("//fieldset[9]/div/label/textarea").clear()

    # чтение не юникодовского файла (кирилица)
    randname = random.choice(list(codecs.open('names.txt', encoding='1251').readlines()))
    driver.find_element_by_xpath("//fieldset[9]/div/label/textarea").send_keys(randname)
    driver.delete_all_cookies()

    driver.close()


with open('names.txt', 'r') as file:
    for i in range(5):
        print(i+1)
        clicker_method()

    webdriver.Firefox.quit()
