from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
options = Options()
options.headless = True
driver = webdriver.Chrome(executable_path='chromedriver.exe',options=options)
#URL = 'https://pms.praktikpladsen.dk/soeg-opslag/0/Data-%20og%20kommunikationsuddannelsen/Datatekniker%20med%20speciale%20i%20programmering?aftaleFilter=alle&medarbejdereFilter=alle&adresse=d8af748d-01c9-4626-9cbb-261d611d949c&afstand=20'
driver.get('https://pms.praktikpladsen.dk/soeg-opslag/0/Data-%20og%20kommunikationsuddannelsen/Datatekniker%20med%20speciale%20i%20programmering?aftaleFilter=alle&medarbejdereFilter=alle&adresse=d8af748d-01c9-4626-9cbb-261d611d949c&afstand=20')

#p_element = driver.find_element_by_class_name('SoegOpslag_virksomhedsnavnContainer__3cBy9')
p_element = driver.find_elements_by_class_name('SoegOpslag_virksomhedsnavnContainer__3cBy9')[0].text
for value in p_element:
    print(p_element)
