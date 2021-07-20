import numpy as np
from selenium import webdriver
from selenium.common import exceptions as SeleniumExcept
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import os
import time

def initSeleniumDriver():
    chromedriver = "chromedriver.exe"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)
    return driver

def isItValidRollNumber(RollNumber):
    checks = 0
    if(len(RollNumber) != 10):
        return False
    try:
        int(RollNumber[:2])
    except ValueError:
        return False
    try:
        int(RollNumber[-3:], base=16)
    except ValueError:
        return False

    return True

def JntuResultScraper(RollNumber, ExamCode="1454", _type_="intgrade"):
    resultDict = {}
    randbirthday = "2001-11-11"
    if(isItValidRollNumber(RollNumber)):
        pass
    else:
        raise(ValueError,"Roll-Number not Valid")
    jntuResultUrl = f"http://results.jntuh.ac.in/jsp/SearchResult.jsp?degree=btech&examCode={ExamCode}&etype=r17&type={_type_}"
    driver = initSeleniumDriver()
    
    driver.get(jntuResultUrl)
    time.sleep(0.1)
    rollNoField  = driver.find_element_by_id('htno')
    time.sleep(0.1)
    rollNoField.click()
    rollNoField.send_keys(RollNumber)
    time.sleep(0.1)

    datePicker = driver.find_element_by_id("datepicker")
    datePicker.send_keys(randbirthday)
    time.sleep(0.1)
    driver.find_element_by_xpath( "/html/body/form/div/table/tbody/tr[2]/td[1]").click()
    time.sleep(0.1)

    captchaTxt = driver.find_element_by_id('txtCaptcha').get_attribute('value')
    time.sleep(0.1)
    driver.find_element_by_id("txtInput").send_keys(captchaTxt)
    time.sleep(0.1)
    driver.find_element_by_xpath("//*[@id=\"myForm\"]/div/table/tbody/tr[5]/td[3]/input").click()
    
    time.sleep(2)
    try:
        myElem = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.TAG_NAME, 'img')))
        print("Loaded")
    except TimeoutException:
        raise(TimeoutException,"Took took much time to load")
    # result table iterator
    ResEndFlag = True
    rowIter = 1
    while(ResEndFlag):
        try:
            currentCol = []
            for colIter in range(1,8):            
                try:
                    val = driver.find_element_by_xpath(f"/html/body/form/div[1]/table/tbody/tr[{rowIter}]/td[{colIter}]/h4/b").text
                except:
                    val = driver.find_element_by_xpath(f"/html/body/form/div[1]/table/tbody/tr[{rowIter}]/td[{colIter}]/b").text
                currentCol.append(val)
            rowIter+=1
            resultDict[currentCol[0]] = {
                'SUB_NAME':currentCol[1],
                'INTERNAL':currentCol[2],
                'EXTERNAL':currentCol[3],
                'TOTAL':currentCol[4],
                'GRADE':currentCol[5],
                'CREDIT':currentCol[6]
            }
            print('\n')
        except SeleniumExcept.NoSuchElementException as e:
            print(e)
            break
    
    return resultDict

if __name__ == "__main__":
    resultDict = JntuResultScraper("18AG1A0401")
    print(resultDict)


    
