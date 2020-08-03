from selenium.webdriver import Firefox
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

from Frases_Bot import frase


browser = Firefox()
def Login():
    '''Entra no facebook'''
    url = 'https://www.facebook.com/pg/Bot-Frases-3000-104987001205567/posts/?ref=page_internal'
    browser.get(url)

    '''Loga no facebook'''
    user = browser.find_element_by_id('email')
    user.send_keys('pedro.botfrases@gmail.com')
    password = browser.find_element_by_id('pass')
    password.send_keys('botfrases')
    entrar = browser.find_element_by_id('u_0_3')
    entrar.click()
    
    
    

def Postagem():
    '''Posta na página'''
    post = '/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div/form/div[1]/div/div[2]/textarea'
    postar = browser.find_element_by_xpath(post)
    postar.send_keys(frase())
    time.sleep(5)
    botao = '/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div[1]/div[2]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div[3]/div[2]/div[2]/div/button'
    enter = browser.find_element_by_xpath(botao)
    enter.click()
    enter.click()
    page = 'https://www.facebook.com/pg/Bot-Frases-3000-104987001205567/posts/?ref=page_internal'
    time.sleep(20)
    browser.close()
    
while True:
    Login()
    Postagem()
    time.sleep(600)
