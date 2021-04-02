from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
import pandas as pd





options =  webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')


driver_path = 'C:\\Users\\ConiPum\\Downloads\\chromedriver_win32\\chromedriver.exe'
driver = webdriver.Chrome(driver_path, chrome_options=options)


# Inicializamos el navegador

driver.get('http://www.xlsebio.es/')
options.add_experimental_option('excludeSwitches',['enable-automation'])
#
wait = WebDriverWait(driver, 10)
download_menu = driver.find_element_by_id("nav-menu-item-508")

action = ActionChains(driver)
#hover on download_menu first
action.move_to_element(download_menu).perform()
documents = wait.until(EC.element_to_be_clickable((By.ID, "nav-menu-item-508")))
documents.click()


WebDriverWait(driver, 12)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input#username')))\
    .send_keys('correo1@gmail.com') 

WebDriverWait(driver, 13)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input#password')))\
    .send_keys('Correo1.1') 
 

WebDriverWait(driver, 13)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input[name=login]')))\
    .click()   
