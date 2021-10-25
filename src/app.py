from selenium import webdriver
import os

def inc(x):
    return x + 1

@app.route('/')
def index():    
    options = webdriver.ChromeOptions()
    options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")

    options.add_argument('--headless')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=options)


    driver.get("https://youtube.com")
    print(driver.page_source)

if __name__ == "__main__":
    app.run(debug=True)
    #web gunicorn --pythonpath src app:app