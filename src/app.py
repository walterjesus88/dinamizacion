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

def _login(browser, email, password):

    browser.get("https://suite.npaw.com/login")
    browser.maximize_window()
    time.sleep(5)
  
    u = browser.find_element_by_xpath('//*[@id="youbora__container"]/div[1]/form/div[1]/div/input').send_keys("PeruOps")
    p=  browser.find_element_by_xpath('//*[@id="youbora__container"]/div[1]/form/div[2]/div/input').send_keys("P3ru0ps")

    print(browser)

    browser.execute_script("arguments[0].click();", WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="youbora__login_submit"]'))))
    time.sleep(5)
    browser.get("https://youbora.nicepeopleatwork.com/analytics/MainKPIsPeru/Phantasia-DINA")
    browser.execute_script("arguments[0].click();", WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="youbora__container"]/main/div[1]/button'))))
    browser.execute_script("arguments[0].click();", WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[3]/button[2]'))))
    return browser

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

    browser.find_element(By.XPATH,'//*[@id="date-picker-calendar"]/div[3]/div[3]/button[2]').click()
    browser.execute_script("arguments[0].click();", WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="youbora__container"]/main/header/div[2]/button[2]'))))
    browser.find_element(By.XPATH,'/html/body/div[2]/div[3]/div[3]/div[1]/div[2]/div/div/div/div[1]/p/div/div/input').send_keys('Device')
    browser.find_element(By.XPATH,'/html/body/div[2]/div[3]/div[3]/div[1]/div[2]/div/div/div/div[1]/p/div/div/input').send_keys(Keys.ENTER)
  
    time.sleep(3)
    browser.find_element(By.XPATH,'//*[@id="youbora__filters_wizard"]//p[text()="STB"]').click()

    time.sleep(3)
    #Exclude   
    browser.find_element(By.XPATH,'/html/body/div[2]/div[3]/div[3]/div[1]/div[1]/div/div/div/div[1]/p/div/div/input').send_keys("Exclude")
    time.sleep(3)
    browser.find_element(By.XPATH,'/html/body/div[2]/div[3]/div[3]/div[1]/div[1]/div/div/div/div[1]/p/div/div/input').send_keys(Keys.ENTER)
    browser.execute_script("arguments[0].click();", WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="youbora__filters_wizard"]/div[3]/div[3]/button'))))
    time.sleep(3)
    browser.find_element(By.XPATH,'/html/body/div[2]/div[3]/div[3]/div[1]/div[2]/div/div/div/div[1]/p/div/div/input').send_keys("Title")
    browser.find_element(By.XPATH,'/html/body/div[2]/div[3]/div[3]/div[1]/div[2]/div/div/div/div[1]/p/div/div/input').send_keys(Keys.ENTER)
    browser.find_element(By.XPATH,'//*[@id="youbora__filters_wizard"]/div[3]/div[3]/div[2]/div[1]/div/input').send_keys(CANAL)
    time.sleep(3)  

    browser.find_element(By.XPATH,'//*[@id="youbora__filters_wizard"]/div[3]/div[3]/div[2]/div[2]/div/table/tbody/div/tr/td[1]/div/span/span[1]/input').click()
                                                                                                              
    time.sleep(3)
    browser.find_element(By.XPATH,'/html/body/div[2]/div[3]/div[3]/div[1]/div[1]/div/div/div/div[1]/p/div/div/input').send_keys("Include")
    browser.find_element(By.XPATH,'/html/body/div[2]/div[3]/div[3]/div[1]/div[1]/div/div/div/div[1]/p/div/div/input').send_keys(Keys.ENTER)

    time.sleep(3)

    browser.execute_script("arguments[0].click();", WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="youbora__filters_wizard"]/div[3]/div[3]/button'))))
    browser.execute_script("arguments[0].click();", WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="youbora__filters_wizard"]/div[3]/div[5]/div/button[2]'))))
    time.sleep(3)

    suscribers = browser.find_element(By.XPATH,'//*[@id="fc446df0-cd91-4ba1-a33e-1bff36d845bd"]/div/div[2]/div/div[1]/p')
    hours = browser.find_element(By.XPATH,'//*[@id="52194ecc-0755-44a7-b329-3e2775623aa4"]/div/div[2]/div/div[1]/p')

    total = { 'canal': CANAL+' '+FECHA,'suscribers':suscribers.text,'hours': hours.text }
 

    browser.execute_script("arguments[0].click();", WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="youbora__container"]/main/div[1]/button'))))
    browser.execute_script("arguments[0].click();", WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[3]/button[2]'))))
    return total

def vod():
    pass

def franja():
    pass

def live():
    options = webdriver.ChromeOptions()
    options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")

    options.add_argument('--headless')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=options)
    driver.get("https://youbora.nicepeopleatwork.com/")
    print(driver.page_source)
    #browser = _login(driver, 'PeruOps', 'P3ru0ps')

    browser.get("https://suite.npaw.com/login")
    #browser.maximize_window()
    time.sleep(1)
  
    u = browser.find_element_by_xpath('//*[@id="youbora__container"]/div[1]/form/div[1]/div/input').send_keys("PeruOps")
    p=  browser.find_element_by_xpath('//*[@id="youbora__container"]/div[1]/form/div[2]/div/input').send_keys("P3ru0ps")

    print(browser)

    browser.execute_script("arguments[0].click();", WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="youbora__login_submit"]'))))
    time.sleep(1)
    browser.get("https://youbora.nicepeopleatwork.com/analytics/MainKPIsPeru/Phantasia-DINA")
    browser.execute_script("arguments[0].click();", WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="youbora__container"]/main/div[1]/button'))))
    browser.execute_script("arguments[0].click();", WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[3]/button[2]'))))
   


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

def inc(x):
    return x + 1

@app.route('/')
def index():
    #"hello "
    live()

    # return render_template(
    #     'index.html',
    #     data=[{'name':'VOD'}, {'name':'LIVE'}, {'name':'FRANJA'}])

@app.route("/test" , methods=['GET', 'POST'])
def test():

    select = request.form.get('comp_select')
    #options = webdriver.ChromeOptions()

    #options.add_argument('--ignore-certificate-errors')
    #options.add_argument('--incognito')
    #options.add_argument('--headless')
    #driver = webdriver.Chrome(executable_path="./chromedriver")



    if select == 'LIVE':
        file = live()
       
    elif select == 'FRANJA':
        franja()
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