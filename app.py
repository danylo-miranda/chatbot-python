from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
import time
import requests
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys

#ABRIR PAGINA WEB E CARREGAR WHATSAPP
dir_path = os.getcwd()
chrome_options2 = Options()
chrome_options2.add_argument(r'user-data-dir=' + dir_path + 'profile/whatsapp')
driver = webdriver.Chrome(chrome_options2)
driver.get('https://web.whatsapp.com/')
time.sleep(5)

def bot():
    try:
        new_msg = driver.find_element(By.CLASS_NAME,'aumms1qt')
        new_msg = driver.find_elements(By.CLASS_NAME,'aumms1qt')
        open_new_msg = new_msg[-1]
        act_new_msg = webdriver.common.action_chains.ActionChains(driver)
        act_new_msg.move_to_element_with_offset(open_new_msg,0,-20)
        act_new_msg.click()
        act_new_msg.perform()
        act_new_msg.click()
        act_new_msg.perform()
        time.sleep(1)
        # GET FONE
        num_client = driver.find_element(By.XPATH,'//*[@id="main"]/header/div[2]/div/div/div/span')
        telefone = num_client.text
        print(telefone)
        time.sleep(1)
        #GET MENSAGENS
        all_messages = driver.find_elements(By.CLASS_NAME,'_21Ahp')
        all_messages_text = [e.text for e in all_messages]
        msg = all_messages_text[-1]
        print(msg)
        time.sleep(2)
        #RESPONDER
        field_text = driver.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div[2]/div[1]/p')
        field_text.click()
        time.sleep(1)
        return_msg = 'Bom dia !'
        field_text.send_keys(f'{return_msg}', Keys.ENTER)
        #FECHAR CONTATO
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    except:
        pass

def waiting_new_msg():
    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, '_21Ahp'))
        )
    except:
        sys.stdout.write('\rAguardando novas mensagens...')
        sys.stdout.flush()
        animate()

def animate():
    while True:
        for char in "|/-\\":
            sys.stdout.write('\rAguardando novas mensagens ' + char)
            sys.stdout.flush()
            time.sleep(0.1)

while True:
    waiting_new_msg()
    bot()





