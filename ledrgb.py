from pyfirmata import Arduino 
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
from webdriver_manager.chrome import ChromeDriverManager
import time
board = Arduino("COM6")

ledrojo = board.get_pin('d:11:o')
ledverde = board.get_pin('d:10:o')
ledazul = board.get_pin('d:9:o')

eleccion = int(input("1.- Azul\n 2.- Verde\n 3.- Rojo\n 4.- Morado\n 5.-Cafe\n Seleccione el numero de color: "))
color = str("")

if eleccion == 1:
    ledazul.write(1)
    color = "Azul"
elif eleccion == 2:
    ledverde.write(1)
    color = "Verde"
elif eleccion == 3:
    ledrojo.write(1)
    color = "Rojo"
elif eleccion == 4:
    ledazul.write(1)
    ledrojo.write(1)
    color = "Morado"
elif eleccion == 5:
    ledrojo.write(1)
    ledverde.write(1)
    color = "Cafe"
    
driver = webdriver.Chrome(ChromeDriverManager().install())
phone = "6421021142"
driver.get('https://api.whatsapp.com/send?phone=521' + phone + '&text=&source=&data=')
driver.find_element_by_id("action-button").click()
time.sleep(5)
driver.find_element_by_link_text("usar WhatsApp Web").click()
print("Por favor registre su codigo QR")
time.sleep(15)
driver.find_element_by_class_name('_3u328').send_keys("El usuario eligio el color " + color)
time.sleep(10)
driver.find_element_by_class_name('_3M-N-').click()

"""while True:
    ledazul.write(1)
    time.sleep(3)
    ledazul.write(0)

    ledrojo.write(1)
    time.sleep(3)
    ledrojo.write(0)

    ledverde.write(1)
    time.sleep(3)
    ledverde.write(0)
    
    ledazul.write(1)
    ledrojo.write(1)
    time.sleep(3)
    ledazul.write(0)
    ledrojo.write(0)"""
    
  
     
    