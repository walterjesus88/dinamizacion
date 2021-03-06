# save this as app.py
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

def find_element_key(path,sendkey,browser):
    while True:
        try:
            browser.find_element(By.XPATH,path).send_keys(sendkey)
            break
        except Exception as e:
            print(e)

    return browser

def find_element_click(path,browser):
    while True:
        try:
            browser.find_element(By.XPATH,path).click()
            break
        except Exception as e:
            print(e)

    return browser

def find_element_cc(path,browser):
    while True:
        try:
            browser.find_element(By.XPATH,path)
            break
        except Exception as e:
            print(e)

    return browser

def _login():

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')

    driver = webdriver.Chrome(executable_path="./chromedriver")
    driver.get("https://suite.npaw.com/MainKPIsPeru/Phantasia-DINA")   
    time.sleep(3)
  
    driver.find_element_by_xpath('//*[@id="youbora__container"]/div[1]/form/div[1]/div/input').send_keys("PeruOps")
    driver.find_element_by_xpath('//*[@id="youbora__container"]/div[1]/form/div[2]/div/input').send_keys("P3ru0ps")
    driver.find_element_by_xpath('//*[@id="youbora__login_submit"]').click()
    time.sleep(5)
    #driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="youbora__home__app__analytics'))))

    #driver.find_element_by_xpath('//*[@id="youbora__home__app__analytics"]').click()
    find_element_click('//*[@id="youbora__home__app__analytics"]',driver)

    time.sleep(1)

    actions = ActionChains(driver) 
    actions.send_keys(Keys.TAB * 2)
    actions.perform()
    actions.click()
    time.sleep(5)

    driver.find_element_by_xpath('//*[@id="sidebar-pinner"]').click()

    driver.find_element_by_xpath('//*[@id="sidebar"]/div[2]/div[1]/div/div/input').send_keys("Phantasia")
    #driver.find_element_by_xpath('//*[@id="sidebar"]/div[1]/div/div[1]/div/div/div[3]/div').click()
    
    find_element_click('//*[@id="sidebar"]//span[text()="Main KPIs Peru"]',driver)
    #driver.find_element_by_xpath('//*[@id="sidebar"]/div[1]/div/div[1]/div/div/div[7]/div/a/div').click()
    #driver.find_element_by_xpath('//*[@id="sidebar"]/div[1]/div/div[1]/div/div//span[text()="Phantasia - DINA"]').click()
    find_element_click('//*[@id="sidebar"]/div[1]/div/div[1]/div/div//span[text()="Phantasia - DINA"]',driver)


    element_to_hover_over = driver.find_element_by_id("youbora__container").click()

    time.sleep(3)

    find_element_click('//*[@id="youbora__container"]/main/div[1]/button',driver)

    #driver.find_element_by_xpath('//*[@id="youbora__container"]/main/div[1]/button').click()
    find_element_click('/html/body/div[2]/div[3]/div/div[3]/button[2]',driver)
    #driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div[3]/button[2]').click()
    return driver

#def my_form():
#    return render_template('form.html')

def convertir_suscribers(x):

    x1= str(x).replace(".","")
    print(x1)
    return float(x1)


def convertir_hours(x):
    a= str(x).split(" ")
    aa= str(a[0]).replace("h", "")
    aa1 = float(aa.replace(".",""))

    if len(a)>1:
        bb= str(a[1]).replace("m", "")
        a_hours = float(bb)/60
    else:
        a_hours=0

    return aa1+a_hours

def semanal_deportes(x,browser):

    calendar = browser.find_element_by_id('element-calendar').click()
   
    CANAL=x['canal']
    FECHA=x['fecha']
    time_ini= datetime.strptime(FECHA, '%Y-%m-%d %H:%M:%S').time()
    time_tuple =  datetime.strptime(FECHA, '%Y-%m-%d %H:%M:%S') +  timedelta(hours=1,minutes=59)
    time_2horas = time_tuple.time()

    print(time_2horas)
    print(time_ini)
 
    d = datetime.strptime(FECHA, '%Y-%m-%d %H:%M:%S')
    dia  = str(d.strftime('%a %b %d %Y'))
 
    DIA='//*[@id="date-picker-calendar"]//div[@aria-label="'+dia+'"]'

    time.sleep(2) 
    browser.execute_script("arguments[0].click();", WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, DIA)))) #'//*[@id="date-picker-calendar"]//div[@aria-label="Tue Jul 13 2021"]'
    browser.execute_script("arguments[0].click();", WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, DIA))))

    time.sleep(1) 
    browser.find_element(By.XPATH,'//*[@id="date-picker-calendar"]/div[3]/div[1]/div[2]/div[2]/div/div/div/input').send_keys(Keys.CONTROL,"a")
    browser.find_element(By.XPATH,'//*[@id="date-picker-calendar"]/div[3]/div[1]/div[2]/div[2]/div/div/div/input').send_keys(str(time_ini))
 
    browser.find_element(By.XPATH,'//*[@id="date-picker-calendar"]/div[3]/div[1]/div[3]/div[2]/div/div/div/input').send_keys(Keys.CONTROL,"a")
    browser.find_element(By.XPATH,'//*[@id="date-picker-calendar"]/div[3]/div[1]/div[3]/div[2]/div/div/div/input').send_keys(str(time_2horas))

    find_element_click('//*[@id="date-picker-calendar"]/div[3]/div[3]/button[2]',browser)
    #browser.find_element(By.XPATH,'//*[@id="date-picker-calendar"]/div[3]/div[3]/button[2]').click()
    
    find_element_click('//*[@id="youbora__container"]/main/header/div[2]/button[2]',browser)

    #browser.execute_script("arguments[0].click();", WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="youbora__container"]/main/header/div[2]/button[2]'))))
    
    find_element_key('/html/body/div[2]/div[3]/div[3]/div[1]/div[2]/div/div/div/div[1]/p/div/div/input','Device type',browser)
    #browser.find_element(By.XPATH,'/html/body/div[2]/div[3]/div[3]/div[1]/div[2]/div/div/div/div[1]/p/div/div/input').send_keys('Device type')
    
    find_element_key('/html/body/div[2]/div[3]/div[3]/div[1]/div[2]/div/div/div/div[1]/p/div/div/input',Keys.ENTER,browser)

    #browser.find_element(By.XPATH,'/html/body/div[2]/div[3]/div[3]/div[1]/div[2]/div/div/div/div[1]/p/div/div/input').send_keys(Keys.ENTER)
  
    #time.sleep(3)
    #browser.find_element(By.XPATH,'//*[@id="youbora__filters_wizard"]//p[text()="STB"]').click()
    find_element_click('//*[@id="youbora__filters_wizard"]//p[text()="STB"]',browser)

    #time.sleep(3)
    #Exclude   
    find_element_key('/html/body/div[2]/div[3]/div[3]/div[1]/div[1]/div/div/div/div[1]/p/div/div/input','Exclude',browser)
    #browser.find_element(By.XPATH,'/html/body/div[2]/div[3]/div[3]/div[1]/div[1]/div/div/div/div[1]/p/div/div/input').send_keys("Exclude")
    #time.sleep(3)
    find_element_key('/html/body/div[2]/div[3]/div[3]/div[1]/div[1]/div/div/div/div[1]/p/div/div/input',Keys.ENTER,browser)
    #browser.find_element(By.XPATH,'/html/body/div[2]/div[3]/div[3]/div[1]/div[1]/div/div/div/div[1]/p/div/div/input').send_keys(Keys.ENTER)

    #browser.execute_script("arguments[0].click();", WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="youbora__filters_wizard"]/div[3]/div[3]/button'))))
    find_element_click('//*[@id="youbora__filters_wizard"]/div[3]/div[3]/button',browser)
    
    #time.sleep(3)
    find_element_key('/html/body/div[2]/div[3]/div[3]/div[1]/div[2]/div/div/div/div[1]/p/div/div/input','Title',browser)

    #browser.find_element(By.XPATH,'/html/body/div[2]/div[3]/div[3]/div[1]/div[2]/div/div/div/div[1]/p/div/div/input').send_keys("Title")
    find_element_key('/html/body/div[2]/div[3]/div[3]/div[1]/div[2]/div/div/div/div[1]/p/div/div/input',Keys.ENTER,browser)
    
    #browser.find_element(By.XPATH,'/html/body/div[2]/div[3]/div[3]/div[1]/div[2]/div/div/div/div[1]/p/div/div/input').send_keys(Keys.ENTER)
    find_element_key('//*[@id="youbora__filters_wizard"]/div[3]/div[3]/div[2]/div[1]/div/input',CANAL,browser)
    
    #browser.find_element(By.XPATH,'//*[@id="youbora__filters_wizard"]/div[3]/div[3]/div[2]/div[1]/div/input').send_keys(CANAL)
    time.sleep(1)  



    #browser.find_element(By.XPATH,'//*[@id="youbora__filters_wizard"]/div[3]/div[3]/div[2]/div[2]/div/table/tbody/div/tr/td[1]/div/span/span[1]/input').click()
    #browser.find_element(By.XPATH,'//*[@id="youbora__filters_wizard"]//p[text()='+CANAL+']').click()


    DEVICE=browser.find_elements_by_xpath('//*[@id="youbora__filters_wizard"]/div[3]/div[3]/div[2]/div[2]/div/table/tbody/div/tr/td/div/p')
    for option in DEVICE:
        print('-----------------option----------->')
        print(option.text)
        print('-----------------option----------->')
        if option.text == CANAL:
            option.click() # select() in earlier versions of webdriver
            break

    time.sleep(1)
    find_element_key('/html/body/div[2]/div[3]/div[3]/div[1]/div[1]/div/div/div/div[1]/p/div/div/input','Include',browser)

    #browser.find_element(By.XPATH,'/html/body/div[2]/div[3]/div[3]/div[1]/div[1]/div/div/div/div[1]/p/div/div/input').send_keys("Include")
    find_element_key('/html/body/div[2]/div[3]/div[3]/div[1]/div[1]/div/div/div/div[1]/p/div/div/input',Keys.ENTER,browser)
    
    #browser.find_element(By.XPATH,'/html/body/div[2]/div[3]/div[3]/div[1]/div[1]/div/div/div/div[1]/p/div/div/input').send_keys(Keys.ENTER)

    #time.sleep(3)

    find_element_click('//*[@id="youbora__filters_wizard"]/div[3]/div[3]/button',browser)
    #browser.execute_script("arguments[0].click();", WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="youbora__filters_wizard"]/div[3]/div[3]/button'))))
    find_element_click('//*[@id="youbora__filters_wizard"]/div[3]/div[5]/div/button[2]',browser)
    #browser.execute_script("arguments[0].click();", WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="youbora__filters_wizard"]/div[3]/div[5]/div/button[2]'))))
    time.sleep(2)

    suscribers = browser.find_element(By.XPATH,'//*[@id="fc446df0-cd91-4ba1-a33e-1bff36d845bd"]/div/div[2]/div/div[1]/p')
    hours = browser.find_element(By.XPATH,'//*[@id="52194ecc-0755-44a7-b329-3e2775623aa4"]/div/div[2]/div/div[1]/p')

    total = { 'canal': CANAL+' '+FECHA,'suscribers':suscribers.text,'hours': hours.text }
 
    find_element_click('//*[@id="youbora__container"]/main/div[1]/button',browser)
    #browser.execute_script("arguments[0].click();", WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="youbora__container"]/main/div[1]/button'))))
    find_element_click('/html/body/div[2]/div[3]/div/div[3]/button[2]',browser)
    #browser.execute_script("arguments[0].click();", WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[3]/button[2]'))))
    return total

def semanal_franja(x,browser):
    #limpiar filtros por defecto
    calendar = browser.find_element_by_id('element-calendar').click()

    CANAL=x['canal']
    FECHA_INIT=x['fecha_init']
    FECHA_FIN=x['fecha_fin']
    time_ini= datetime.strptime(FECHA_INIT, '%Y-%m-%d %H:%M:%S').time()
    time_fin= datetime.strptime(FECHA_FIN, '%Y-%m-%d %H:%M:%S').time()   
         
    d = datetime.strptime(FECHA_INIT, '%Y-%m-%d %H:%M:%S')
    dia  = str(d.strftime('%a %b %d %Y'))
    #'Tue Jul 13 2021'
    DIA='//*[@id="date-picker-calendar"]//div[@aria-label="'+dia+'"]'
    driver = browser
    time.sleep(0.5) 
    driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, DIA)))) #'//*[@id="date-picker-calendar"]//div[@aria-label="Tue Jul 13 2021"]'
    driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, DIA))))
 
    time.sleep(0.5) 
    browser.find_element(By.XPATH,'//*[@id="date-picker-calendar"]/div[3]/div[1]/div[2]/div[2]/div/div/div/input').send_keys(Keys.CONTROL,"a")
    browser.find_element(By.XPATH,'//*[@id="date-picker-calendar"]/div[3]/div[1]/div[2]/div[2]/div/div/div/input').send_keys(str(time_ini))
 
    browser.find_element(By.XPATH,'//*[@id="date-picker-calendar"]/div[3]/div[1]/div[3]/div[2]/div/div/div/input').send_keys(Keys.CONTROL,"a")
    browser.find_element(By.XPATH,'//*[@id="date-picker-calendar"]/div[3]/div[1]/div[3]/div[2]/div/div/div/input').send_keys(str(time_fin))
    #APPLY CALENDAR
    browser.find_element(By.XPATH,'//*[@id="date-picker-calendar"]/div[3]/div[3]/button[2]').click()

    #FILTER 
    #browser.find_element(By.XPATH,'//*[@id="youbora__container"]/main/header/div[2]/button[2]').click()
    browser.execute_script("arguments[0].click();", WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="youbora__container"]/main/header/div[2]/button[2]'))))
    
    find_element_key('/html/body/div[2]/div[3]/div[3]/div[1]/div[2]/div/div/div/div[1]/p/div/div/input','Device type',browser)

    #browser.find_element(By.XPATH,'/html/body/div[2]/div[3]/div[3]/div[1]/div[2]/div/div/div/div[1]/p/div/div/input').send_keys('Device type')
    #browser.find_element(By.XPATH,'/html/body/div[2]/div[3]/div[3]/div[1]/div[2]/div/div/div/div[1]/p/div/div/input').send_keys(Keys.ENTER)
    find_element_key('/html/body/div[2]/div[3]/div[3]/div[1]/div[2]/div/div/div/div[1]/p/div/div/input',Keys.ENTER,browser)
    #Elejir STB
    #time.sleep(5)
    #'/html/body/div[2]/div[3]/div[3]/div[2]/div[2]/div/table/tbody/div/tr[3]/td[1]/div/span/span[1]/input
    find_element_click('//*[@id="youbora__filters_wizard"]//p[text()="STB"]',browser)
    #browser.find_element(By.XPATH,'//*[@id="youbora__filters_wizard"]//p[text()="STB"]').click()

    #browser.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="youbora__filters_wizard"]//p[text()="STB"]'))))

    #time.sleep(4)
    #Exclude   
    find_element_key('/html/body/div[2]/div[3]/div[3]/div[1]/div[1]/div/div/div/div[1]/p/div/div/input','Exclude',browser)
    #browser.find_element(By.XPATH,'/html/body/div[2]/div[3]/div[3]/div[1]/div[1]/div/div/div/div[1]/p/div/div/input').send_keys("Exclude")
    #time.sleep(4)
    find_element_key('/html/body/div[2]/div[3]/div[3]/div[1]/div[1]/div/div/div/div[1]/p/div/div/input',Keys.ENTER,browser)
    #browser.find_element(By.XPATH,'/html/body/div[2]/div[3]/div[3]/div[1]/div[1]/div/div/div/div[1]/p/div/div/input').send_keys(Keys.ENTER)
    #APPLY FILTER
    #browser.find_element(By.XPATH,'//*[@id="youbora__filters_wizard"]/div[3]/div[3]/button').click()
    #driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="youbora__filters_wizard"]/div[3]/div[3]/button'))))
    find_element_click('//*[@id="youbora__filters_wizard"]/div[3]/div[3]/button',browser)
    ############################################################
    #time.sleep(2)
    #browser.find_element(By.XPATH,'/html/body/div[2]/div[3]/div[3]/div[1]/div[2]/div/div/div/div[1]/p/div/div/input').send_keys("Title")
    find_element_key('/html/body/div[2]/div[3]/div[3]/div[1]/div[2]/div/div/div/div[1]/p/div/div/input',"Title",browser)
    
    #time.sleep(2)
    
    #browser.find_element(By.XPATH,'/html/body/div[2]/div[3]/div[3]/div[1]/div[2]/div/div/div/div[1]/p/div/div/input').send_keys(Keys.ENTER)
    find_element_key('/html/body/div[2]/div[3]/div[3]/div[1]/div[2]/div/div/div/div[1]/p/div/div/input',Keys.ENTER,browser)
    
    #time.sleep(2)
    
    #browser.find_element(By.XPATH,'//*[@id="youbora__filters_wizard"]/div[3]/dv[3]/div[2]/div[1]/div/input[1]').send_keys(CANAL)
    find_element_key('//*[@id="youbora__filters_wizard"]/div[3]/div[3]/div[2]/div[1]/div/input[1]',CANAL,browser)
    #time.sleep(5)  
    

    find_element_click('//*[@id="youbora__filters_wizard"]/div[3]/div[3]/div[2]/div[2]/div/table/tbody/div/tr/td[1]/div/span/span[1]/input',browser)

    #browser.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="youbora__filters_wizard"]/div[3]/div[3]/div[2]/div[2]/div/table/tbody/div/tr/td[1]/div/span/span[1]/input'))))
                                                                                                                         
    #time.sleep(2)
    #browser.find_element(By.XPATH,'/html/body/div[2]/div[3]/div[3]/div[1]/div[1]/div/div/div/div[1]/p/div/div/input').send_keys("Include")
    #browser.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div[3]/div[1]/div[1]/div/div/div/div[1]/p/div/div/input')))).send_keys("Include")
    find_element_key('/html/body/div[2]/div[3]/div[3]/div[1]/div[1]/div/div/div/div[1]/p/div/div/input','Include',browser)
    
    #time.sleep(1)

    #browser.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div[3]/div[1]/div[1]/div/div/div/div[1]/p/div/div/input')))).send_keys(Keys.ENTER)
    #browser.find_element(By.XPATH,'/html/body/div[2]/div[3]/div[3]/div[1]/div[1]/div/div/div/div[1]/p/div/div/input').send_keys(Keys.ENTER)
    find_element_key('/html/body/div[2]/div[3]/div[3]/div[1]/div[1]/div/div/div/div[1]/p/div/div/input',Keys.ENTER,browser)
    #time.sleep(1)
 
    #APPLY
    #driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="youbora__filters_wizard"]/div[3]/div[3]/button'))))
    find_element_click('//*[@id="youbora__filters_wizard"]/div[3]/div[3]/button',browser)
    #time.sleep(2)
    
    #driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="youbora__filters_wizard"]/div[3]/div[5]/div/button[2]'))))
    find_element_click('//*[@id="youbora__filters_wizard"]/div[3]/div[5]/div/button[2]',browser)
    time.sleep(2)

    suscribers = browser.find_element(By.XPATH,'//*[@id="fc446df0-cd91-4ba1-a33e-1bff36d845bd"]/div/div[2]/div/div[1]/p')
    #find_element_cc('//*[@id="fc446df0-cd91-4ba1-a33e-1bff36d845bd"]/div/div[2]/div/div[1]/p',browser)
    time.sleep(2)
    print(suscribers)
    
    hours = browser.find_element(By.XPATH,'//*[@id="52194ecc-0755-44a7-b329-3e2775623aa4"]/div/div[2]/div/div[1]/p')
    #find_element_cc('//*[@id="fc446df0-cd91-4ba1-a33e-1bff36d845bd"]/div/div[2]/div/div[1]/p',browser)
    print(hours)
    total = { 'canal': CANAL+' '+FECHA_INIT,'suscribers':suscribers.text,'hours': hours.text }
 
    time.sleep(2)

    find_element_click('//*[@id="youbora__container"]/main/div[1]/button',browser)
    #driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="youbora__container"]/main/div[1]/button'))))
    
    #time.sleep(1)
    find_element_click('/html/body/div[2]/div[3]/div/div[3]/button[2]',browser)
    #driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[3]/button[2]'))))
    return total

def vod():
    pass

def franja(browser):
    franja =  pd.read_csv('FRANJAS.csv')
    franja = franja[['canal','fecha_init','fecha_fin']]

    total_sus = []
    total_hou = []
    KPI = []
    #time.sleep(2)

    for index,row in franja.iterrows():
       
        x ={'canal':row['canal'],'fecha_init':row['fecha_init'],'fecha_fin':row['fecha_fin']} 
      
        total=semanal_franja(x,browser)
 
        KPI.append(total) 

    #df = pd.read_json(KPI)
    print(KPI)
    df = pd.DataFrame(data=KPI)
    print(df)
    df['suscribers']=df['suscribers'].apply(convertir_suscribers)
    df['hours']=df['hours'].apply(convertir_hours)
    df.to_csv('RES_FRANJAS.csv', index = None)
    path = "../RES_FRANJAS.csv"
    return send_file(path, as_attachment=True)

def live(browser):
    deportes =  pd.read_csv('DEPORTES.csv')
    deportes = deportes[['canal','fecha']]
    print(deportes)
    total_sus = []
    total_hou = []
    KPI = []
    KPI_antes = []
    time.sleep(2)

    for index,row in deportes.iterrows():
        print(row['canal'])
        print(row['fecha'])
        x ={'canal':row['canal'],'fecha':row['fecha']}

    
        week_after = datetime.strptime(x['fecha'], '%Y-%m-%d %H:%M:%S') -  timedelta(days=7)
      

        x_before = {'canal': x['canal'],'fecha':str(week_after)}

        total=semanal_deportes(x,browser)
        total_before=semanal_deportes(x_before,browser)
        KPI.append(total)
        KPI_antes.append(total_before)

    print(KPI)
    df = pd.DataFrame(data=KPI)
    print(df)
    df['suscribers']=df['suscribers'].apply(convertir_suscribers)
    df['hours']=df['hours'].apply(convertir_hours)
    df2 = pd.DataFrame(data=KPI_antes)
    print(df2)
    df2['suscribers']=df2['suscribers'].apply(convertir_suscribers)
    df2['hours']=df2['hours'].apply(convertir_hours)

    df.to_excel("resultados_partidos1.xlsx",index=False)
    df2.to_excel("resultados_partidos2.xlsx",index=False)

    path = "../resultados_partidos1.xlsx"
    return send_file(path, as_attachment=True)
    #return df2,df


def inc(x):
    return x + 1

@app.route('/')
def index():
    #"hello "
    return render_template(
        'index.html',
        data=[{'name':'VOD'}, {'name':'LIVE'}, {'name':'FRANJA'}])

@app.route("/test" , methods=['GET', 'POST'])
def test():

    select = request.form.get('comp_select')
    # options = webdriver.ChromeOptions()
    # #options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    # options.add_argument('--headless') 
    # #options.add_argument('--ignore-certificate-errors')
    # #options.add_argument('--incognito')
    # options.add_argument('--no-sandbox')
    # options.add_argument('--disable-dev-shm-usage')
    # #driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=options)
    # driver = webdriver.Chrome(executable_path="./chromedriver")
    #driver.get("https://youbora.nicepeopleatwork.com/")
   
    browser = _login()

    if select == 'LIVE':
        file = live(browser)
       
    elif select == 'FRANJA':
        file = franja(browser)
    else:
        vod()
    #return(str(select))
    return file

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.upper()
    return processed_text

@app.route("/upload", methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        print(request.files['file'])
        f = request.files['file']
        print(f)
        data_xls = pd.read_csv(f)
        return data_xls.to_html()
    return '''
    <!doctype html>
    <title>Upload an excel file</title>
    <h1>Excel file upload (csv, tsv, csvz, tsvz only)</h1>
    <form action="" method=post enctype=multipart/form-data>
    <p><input type=file name=file><input type=submit value=Upload>
    </form>
    '''

@app.route("/export", methods=['GET'])
def export_records():
    return 


@app.route('/download')
def downloadFile ():
    #For windows you need to use drive name [ex: F:/Example.pdf]
    path = "../resultados_partidos1.xlsx"
    return send_file(path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
    #web gunicorn --pythonpath src app:app