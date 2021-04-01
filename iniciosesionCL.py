from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pandas as pd





options =  webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')


driver_path = 'C:\\Users\\ConiPum\\Downloads\\chromedriver_win32\\chromedriver.exe'
driver = webdriver.Chrome(driver_path, chrome_options=options)


# Inicializamos el navegador
driver.get('https://www.estec.cl/')


WebDriverWait(driver, 2)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'li.for-flex')))\
    .click()



WebDriverWait(driver, 12)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input#user_login')))\
    .send_keys('correo1@gmail.com') 

WebDriverWait(driver, 13)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input#user_pass')))\
    .send_keys('correo1') 


WebDriverWait(driver, 13)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input#wp-submit')))\
    .click()  