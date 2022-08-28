

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import pandas as pd
from random import randint
import time
import sys


# Variable that user has to input:
keyword = input("add your keyword: ")
clicks = input("How many questions do you want to scrap: ")
language = input("Select your langauge(for english insert en/ for french insert fr/ for spanish insert sn ) : ")

clicks = int(clicks) #parse string into an integer


# Search function, 

def search(keyword, clicks, language):
    
    #it won't open firefox everytime we run it
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.headless = True
    
    driver = webdriver.Firefox(options=firefox_options, executable_path='/home/elon_musk/selenium-firefox/drivers/geckodriver')
    driver.get("https://www.google.com?hl="+language)
    
    if language == "en":
        print('The keyword you selected is: ', keyword)
        print('Number of clicks we will do is: ', clicks)
        print('Search Language you selected is: ', language)
        
        driver.find_element(By.XPATH, "//input[@aria-label='Search']").send_keys(keyword+Keys.RETURN)
        print(keyword)
        clickingKW(clicks, driver)
    
    if language == "fr":
        print('', keyword)
        print('', clicks)
        print('', language)
        
        driver.find_element(By.XPATH, "//input[@aria-label='Rechercher']").send_keys(keyword+Keys.RETURN)
        print(keyword)
        clickingKW(clicks, driver)
        
    if language == "es":
        print('', keyword)
        print('', clicks)
        print('', language)
        
        driver.find_element(By.XPATH, "//input[@aria-label='Buscar']").send_keys(keyword+Keys.RETURN)
        print(keyword)
        clickingKW(clicks, driver)


# Function that clicks N Time:

def clickingKW(clicks, driver):
    
    rqp = driver.find_elements(By.CLASS_NAME, "related-question-pair")
    
    # loop
    for i in range(clicks):
        print('Clicking #', i+1)
        
        try:
            rqp[i].click()
            time.sleep(2)
            rqp = driver.find_element(By.CLASS_NAME, "wW0Jcd")
            
        except:
            continue
            raise Exception('Oops!!! There are no questions to click!')
            
    list_rqp = []
    for j in rqp:
        p = format(j.text)
        p = p.splitlines()
        
        list_rqp.append(p)
        
    df = pd.DataFrame(list_rqp, columns=['Questions'])
    
    df = df.dropna()
    
    
    print(df)
    df.to_csv(keyword+'.csv', index = False)
        
search(keyword, clicks, language)






