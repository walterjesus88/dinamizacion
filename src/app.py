import os
from selenium import webdriver

options = webdriver.ChromeOptions()
options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")

options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(executable_path=str(os.environ.get("CHROMEDRIVER_PATH")),chrome_options=options)


driver.get("https://youtube.com")
print(driver.page_source)

def inc(x):
    return x + 1