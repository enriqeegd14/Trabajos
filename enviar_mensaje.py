from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
from webdriver_manager.chrome import ChromeDriverManager
import time 

driver = webdriver.Chrome(ChromeDriverManager().install())
phone = "6421021142"
driver.get('https://api.whatsapp.com/send?phone=521' + phone + '&text=&source=&data=')
driver.find_element_by_id("action-button").click()
time.sleep(5)
driver.find_element_by_link_text("usar WhatsApp Web").click()
print("Por favor registre su codigo QR")
time.sleep(15)
driver.find_element_by_class_name('_3u328').send_keys("hola")
driver.find_element_by_class_name('_3M-N-').click()

"""
options = webdriver.ChromeOptions()
options.add_argument("--disable-notifications")
options.add_argument("--disable-infobars")
options.add_argument("--mute-audio")
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

phone = "6623326359"
driver.get('https://api.whatsapp.com/send?phone=521' + phone + '&text=&source=&data=')
time.sleep(5)
send_button = driver.find_element_by_id('action-button').click()
time.sleep(5)
use_whatsapp = driver.find_element_by_link_text('use WhatsApp Web').click()
time.sleep(25)
print(driver.find_element_by_class_name('wjdTm').value())
"""