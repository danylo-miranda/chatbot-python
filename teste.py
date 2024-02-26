from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
import time
import requests

#ABRIR PAGINA WEB E CARREGAR WHATSAPP
dir_path = os.getcwd()
chrome_options2 = Options()
chrome_options2.add_argument(r'user-data-dir=' + dir_path + 'profile/whatsapp')
driver = webdriver.Chrome(chrome_options2)
driver.get('https://web.whatsapp.com/')
time.sleep(5)

#class="l7jjieqr cfzgl7ar ei5e7seu h0viaqh7 tpmajp1w c0uhu3dl riy2oczp dsh4tgtl sy6s5v3r gz7w46tb lyutrhe2 qfejxiq4 fewfhwl7 ovhn1urg ap18qm3b ikwl5qvt j90th5db aumms1qt"

'''
#API EDITA CODIGO
agent = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
token = 'pWmEh5QY1Ra6mKBmilRuvmldKtrSinhh'
api = requests.get(f"https://editacodigo.com.br/index/api-whatsapp/{token}" ,  headers=agent)
time.sleep(1)
api = api.text
api = api.split(".n.")
bolinha_notificacao = api[3].strip()
contato_cliente = api[4].strip()
caixa_msg = api[5].strip()
msg_cliente = api[6].strip()
caixa_msg2 = api[7].strip()
caixa_pesquisa = api[8].strip()
'''


def bot():
    try:
        bolinha = driver.find_element(By.CLASS_NAME,'aumms1qt')
        bolinha = driver.find_elements(By.CLASS_NAME,'aumms1qt')
        clica_bolinha = bolinha[-1]
        acao_bolinha = webdriver.common.action_chains.ActionChains(driver)
        acao_bolinha.move_to_element_with_offset(clica_bolinha,0,-20)
        acao_bolinha.click()
        acao_bolinha.perform()
        acao_bolinha.click()
        acao_bolinha.perform()
        time.sleep(1)
        # GET FONE
        num_cliente = driver.find_element(By.XPATH,'//*[@id="main"]/header/div[2]/div/div/div/span')
        telefone = num_cliente.text
        print(telefone)
        time.sleep(1)
        #GET MENSAGENS
        all_messages = driver.find_elements(By.CLASS_NAME,'_21Ahp')
        all_messages_text = [e.text for e in all_messages]
        msg = all_messages_text[-1]
        print(msg)
        time.sleep(2)
        #RESPONDER
        campo_texto = driver.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div[2]/div[1]/p')
        campo_texto.click()
        time.sleep(1)
        campo_texto.send_keys('Ola, essa é a primeira mensagem padrão do meu novo sistema', Keys.ENTER)
        #FECHAR CONTATO
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    except:
        print('Aguardando novas mensagens')

while True:
    bot()
