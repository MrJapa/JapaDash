from selenium import webdriver
import selenium
from selenium.webdriver.common import keys
from selenium.webdriver.common import by
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import *
import time
from selenium.webdriver.chrome.options import Options
import os

from selenium.webdriver.support.wait import WebDriverWait
os.chdir(os.path.dirname(os.path.abspath(__file__)))
options = Options()
options.headless = False
driver = webdriver.Chrome(executable_path='chromedriver.exe',options=options)
driver.get('https://www.praktikpladsen.dk/')

def loop():
    try:
        main = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((
                By.XPATH,'//*[@id="main-content"]/div/div/div[1]/div[1]/div/ul/li[1]/a')))
        main.click()
    except AttributeError:
        pass
    try:
        search = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((
                By.XPATH,'//*[@id="main-content"]/div/div/form/div[2]/button')))
    except AttributeError:
        pass
    try:
        searchinput = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((
                By.XPATH,'//*[@id="uddannelsespecialevaelger.input"]')))
        searchinput.send_keys('Datatekniker med speciale i programmering')
    except AttributeError:
        pass
    try:
        clickinput = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((
                By.XPATH,'//*[@id="uddannelsespecialevaelger.1"]')))
        clickinput.click()
    except:
        pass
    try:
        searchbutton = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((
                By.XPATH,'//*[@id="main-content"]/div/div/form/div[2]/button')))
        searchbutton.click()
    except:
        pass
    try:
        adresse = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((
                By.XPATH,'//*[@id="combobox:1"]/div[1]')))
        adresse.click()
    except:
        pass
    try:
        position = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((
                By.XPATH,'//*[@id="combobox:1.0"]')))
        position.click()
    except:
        pass
    try:
        afstand = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((
                By.XPATH,'//*[@id="input17"]')))
        afstand.click()
    except:
        pass
    try:
        km = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((
                By.XPATH,'//*[@id="input17"]/option[2]')))
        km.click()
    except:
        pass
    try:
        antal = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((
                By.XPATH,'//*[@id="resultater"]/div[1]/div/p')))
    except:
        pass
    i = 1
    while i < 6:
        print(antal.text)
        i += 1
    driver.quit


loop()

