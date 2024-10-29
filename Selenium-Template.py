from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.by import By
from IPython.display import display, HTML
from bs4 import BeautifulSoup

import chromedriver_autoinstaller
from pyvirtualdisplay import Display
display = Display(visible=0, size=(800, 800))  
display.start()

chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
                                      # and if it doesn't exist, download it automatically,
                                      # then add chromedriver to path

chrome_options = webdriver.ChromeOptions()    
# Add your options as needed    
options = [
  # Define window size here
   "--window-size=1200,1200",
    "--ignore-certificate-errors"
 
    #"--headless",
    #"--disable-gpu",
    #"--window-size=1920,1200",
    #"--ignore-certificate-errors",
    #"--disable-extensions",
    #"--no-sandbox",
    #"--disable-dev-shm-usage",
    #'--remote-debugging-port=9222'
]

for option in options:
    chrome_options.add_argument(option)

    
driver = webdriver.Chrome(options = chrome_options)

driver.get('https://samehadaku.email/shangri-la-frontier-season-2-episode-3/')
wait(driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'iframe[allowfullscreen=true]')))
#print(driver.page_source)
soup = BeautifulSoup(driver.page_source, "html.parser")
res = soup.find(allowfullscreen="true")
display(HTML(res.prettify()))

with open('./GitHub_Action_Results.txt', 'w') as f:
    f.write(f"This was written with a GitHub action {res.prettify()}")

