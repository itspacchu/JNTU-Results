import numpy as np
import urllib3 as uli
from selenium import webdriver
import os
import requests
from PIL import Image
import pytesseract
from Screenshot import Screenshot_Clipping
import cv2

#baking webpage captcha constants below
left = 426
top = 428
bottom = 444
right = 588
randbirthday = "2001-09-15"
#ENTER RNO
rno = ""


ob=Screenshot_Clipping.Screenshot()
chromedriver = "D:\\PyStuff\\SomeRandomGizmos\\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
#driver.get("http://epayments.jntuh.ac.in/results") got some weird tag issues here

#DIRECT LINK FOR R18 2-1 Results
driver.get("http://epayments.jntuh.ac.in/results/jsp/SearchResult.jsp?degree=btech&amp;examCode=1391&amp;etype=r17&amp;type=grade17")

driver.find_element_by_name("htno").send_keys(rno)
elem = driver.find_element_by_id('txtCaptcha')
img_url=ob.full_Screenshot(driver, save_path=r'.', image_name='testscr.png') 
text = pytesseract.image_to_string(Image.open(r"D:\\PyStuff\\SomeRandomGizmos\\testscr.png").crop( ( left, top, right, bottom ) ))
driver.find_element_by_id("txtInput").send_keys(text)
driver.find_element_by_id("datepicker").send_keys(randbirthday)
print("\nPredicted Captcha: ",text)
#Button1
driver.find_element_by_xpath("//*[@id=\"myForm\"]/div/table/tbody/tr[5]/td[3]/input").click()

#for now it just goes to results page directly
