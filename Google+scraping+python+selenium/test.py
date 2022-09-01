from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException  
import csv
import time



# fetch all java related questions and answers
search = input("insert your keyword : ")

options = webdriver.FirefoxOptions()
options.headless = True

    
driver = webdriver.Firefox(options=options, executable_path='/home/elon_musk/selenium-firefox/drivers/geckodriver')


options = webdriver.FirefoxOptions()
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver.get('https://www.google.com')
driver.implicitly_wait(5)
driver.find_element(By.NAME,"q").send_keys(search + Keys.ENTER)
limit = 20 # no of questions to be fetched
counter = 1
qno=1
header = ["question","answer"]
data = []
while counter <= limit:
    qq=aa=""
    try:
        question = driver.find_element(By.CSS_SELECTOR, 'div[jsname="N760b"] > div:nth-child(' + str(counter) + ')')
        qq=question.text
        if search not in qq:  # this is just to ignore UN RELATED questions
            counter+=1        # the keyword must be in questions 
            continue
    except NoSuchElementException:
        counter +=1
        continue
    print (qno, question.text) 
    #driver.implicitly_wait(60) # wait after each click
    # wait for 1 seconds
    time.sleep(1)
    question.click()
     
    try:
        answer = question.find_element(By.CSS_SELECTOR, 'div:nth-child(2) > div > div > div:nth-child(2) > div:nth-child(1) > div > div:nth-child(1) > div > div > span:nth-child(1) > span')
    except NoSuchElementException:
        answer = ""
    if answer == '':
        print ('different format')
        aa=""
    else:
        print (answer.text)
        aa = answer.text
    print ('-------------------------------------')
    counter += 1
    qno +=1
    row = [qq, aa]
    data.append(row)
with open('q.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(data)
