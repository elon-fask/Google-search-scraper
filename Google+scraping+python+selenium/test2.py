from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time
import pandas as pd


keyword = input("insert it : ")
clicks = input("Number of quistion you wanna scrape : ")
clicks = int(clicks)

driver = webdriver.Firefox(executable_path="/home/kali/Desktop/geckodriver")
driver.get("https://google.com/search?q="+keyword+"&hl=en")

rqp = driver.find_elements(By.CLASS_NAME, "related-question-pair")
    
    # loop
for i in range(clicks):
    print('Clicking #', i+1)
        
    try:
        rqp[i].click()
        time.sleep(2)
        rqp = driver.find_element(By.CLASS_NAME, "wW0Jcd")
            
        print(rqp[0].text)    
            
    except:
        continue
        raise Exception('Oops!!! There are no questions to click!')
            
list_rqp = []
for j in rqp:
    p = format(j.text)
    p = p.splitlines()
        
    list_rqp.append(p)
        
df = pd.DataFrame(list_rqp, columns=len(list_rqp))
    
df = df.dropna()
    
    
print(df)
df.to_csv(keyword+'.csv', index = False)
