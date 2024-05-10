##### S Maruthachalam - Functional Testing - 10.05.2024 #####import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time



CntWkgDir = os.getcwd()
driver = webdriver.Chrome()
url = driver.get("https://demo.dealsdray.com/")
driver.maximize_window()
time.sleep(5)

user_name_click = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div[2]/div/form/div[1]/div/div').click()
time.sleep(5)

user_name = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/form/div[1]/div/div/input').send_keys("prexo.mis@dealsdray.com")
time.sleep(5)

password_click = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div[2]/div/form/div[2]/div/div').click()
time.sleep(5)

password = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/form/div[2]/div/div/input').send_keys("prexo.mis@dealsdray.com")
time.sleep(5)

log_in = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div[2]/div/form/div[3]/div/button').click()
time.sleep(5)


## upload xml file

order_button_click = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div/div[2]/div[1]/div[2]/button').click()
time.sleep(5)

orders_click = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div/div[2]/div[1]/div[2]/div/div[1]/a/button').click()
time.sleep(5)

bulk_order_click = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div/div[2]/div[2]/button').click()
time.sleep(5)

choose_file_input = driver.find_element(By.XPATH, '//*[@id="mui-7"]')
choose_file_input.send_keys(r'D:\projects\dealsdray\functional_testing\demo-data.xlsx')

import_click = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div/div[2]/div[3]/button').click()

validate_click = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div/div[2]/div[3]/button').click()
time.sleep(8)

check_error_popup = driver.switch_to.alert.accept()
time.sleep(5)

dirName = CntWkgDir
FileName = "FinalOutputPage"
driver.save_screenshot(dirName+'/'+str(FileName)+'.png')
time.sleep(5)
driver.quit()





