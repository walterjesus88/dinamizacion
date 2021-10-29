from flask import Flask, request, render_template
import pandas as pd
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

import datetime
from datetime import datetime, timedelta
import os
from flask import send_file
app = Flask(__name__,template_folder='../template')

def inc(x):
    return x + 1

def login(browser):

    #browser.get("https://suite.npaw.com/login")
    #browser.maximize_window()


 

    #print('browser')

  



    #browser.execute_script("arguments[0].click();", WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="youbora__container"]/main/div[1]/button'))))
    #browser.execute_script("arguments[0].click();", WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[3]/button[2]'))))

    return browser

@app.route('/')
def index(): 
    options = webdriver.ChromeOptions()
    #options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")

    #options.add_argument('--headless')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    #driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=options)
    driver = webdriver.Chrome(executable_path="./chromedriver")



    driver.get("https://suite.npaw.com/login")   
  
    driver.find_element_by_xpath('//*[@id="youbora__container"]/div[1]/form/div[1]/div/input').send_keys("PeruOps")
    driver.find_element_by_xpath('//*[@id="youbora__container"]/div[1]/form/div[2]/div/input').send_keys("P3ru0ps")
    driver.find_element_by_xpath('//*[@id="youbora__login_submit"]').click()
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="youbora__home__app__analytics"]').click()


    time.sleep(5)
    element_to_hover_over = driver.find_element_by_id("sidebar")#click()

    hover = ActionChains(driver).move_to_element(element_to_hover_over)
    hover.perform()

    #driver.find_element_by_id("sidebar").click()
    #driver.find_element_by_css_selector('aside.youbora__sidebar sidebar-0-3-1 sidebar-d4-0-3-10')
    
    #driver.find_element_by_xpath('/html/body/div/aside').click()
    #driver.find_element_by_xpath('//*[@id="sidebar-pinner"]').click() 
    #hover = ActionChains(driver).move_to_element(element_to_hover_over)
    #hover.perform()



    driver.find_element_by_xpath('//*[@id="sidebar"]/div[2]/div[1]/div/div/input').send_keys("Phantasia")
    driver.find_element_by_xpath('//*[@id="sidebar"]/div[1]/div/div[1]/div/div/div[3]/div').click()
    driver.find_element_by_xpath('//*[@id="sidebar"]/div[1]/div/div[1]/div/div/div[7]/div/a/div').click()
    element_to_hover_over = driver.find_element_by_id("youbora__container")#click()

    hover = ActionChains(driver).move_to_element(element_to_hover_over)
    hover.perform()


    #driver.get("https://suite.npaw.com/analytics/MainKPIsPeru/Phantasia-DINA")
    driver.find_element_by_xpath('//*[@id="youbora__container"]/main/div[1]/button').click()
    driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div[3]/button[2]').click()
    #driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="youbora__login_submit"]'))))
    #browser = login(dri)

    return render_template(
        'form.html')

if __name__ == "__main__":
    app.run(debug=True)
    #web gunicorn --pythonpath src app:app