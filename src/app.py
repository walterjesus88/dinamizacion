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

@app.route('/')
def index(): 
    options = webdriver.ChromeOptions()
    options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")

    options.add_argument('--headless')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    browser = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=options)
    #browser = webdriver.Chrome(executable_path="./chromedriver")
    browser.get("https://suite.npaw.com/login")
    #print(browser.page_source)
    #browser.maximize_window()
   
  
    u = browser.find_element_by_xpath('//*[@id="youbora__container"]/div[1]/form/div[1]/div/input').send_keys("PeruOps")
    p=  browser.find_element_by_xpath('//*[@id="youbora__container"]/div[1]/form/div[2]/div/input').send_keys("P3ru0ps")


    browser.execute_script("arguments[0].click();", WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="youbora__login_submit"]'))))


   
    browser.get("https://youbora.nicepeopleatwork.com/analytics/MainKPIsPeru/Phantasia-DINA")


    #browser.execute_script("arguments[0].click();", WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="youbora__container"]/main/div[1]/button'))))
    #browser.execute_script("arguments[0].click();", WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[3]/button[2]'))))

    return render_template(
        'form.html')

if __name__ == "__main__":
    app.run(debug=True)
    #web gunicorn --pythonpath src app:app