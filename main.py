import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib.request
import os
path ='C:\Alok\chromedriver'
path_dir ="C:\Tada"
jarvis = webdriver.Chrome(path)

jarvis.set_window_size(3000,1000)
# Find the search bar element by name attribute and send the search query
jarvis.get('https://www.google.com/imghp?hl=EN')
search = jarvis.find_element(By.CLASS_NAME,'gLFyf')
search.send_keys('tadasana pose sketch')
search.send_keys(Keys.RETURN)

try:
    islmp = WebDriverWait(jarvis, 10).until(EC.presence_of_element_located((By.ID, 'islmp')))
    sub_element = islmp.find_elements(By.TAG_NAME, 'img')
    for i, j in enumerate(sub_element):
        if i<500:
            src = j.get_attribute('src')
            if src!=None:
                src = str(src)
                urllib.request.urlretrieve(src, os. path.join(path_dir, str(i)+".jpg"))
finally:
    jarvis.quit()
# Wait for 5 seconds before closing the driver

