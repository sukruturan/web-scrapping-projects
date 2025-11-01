# Airbnb Web Scraper - project initialization
#IMPORT MODULES
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
import openpyxl
from bs4 import BeautifulSoup
import random
import re

#DESCIPTION URL AND BASE AGENT 
USER_AGENT = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.6668.89 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,tr;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"
} 
BASE_URL="https://www.airbnb.com"

#CHROME SETTİNGS
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",False)
options.add_argument("--start-maximazed")
options.add_argument(f"--user-agent={USER_AGENT}")

#OPEN CHROME
driver=webdriver.Chrome(options=options)
actions=ActionChains(driver)
try:
    driver.get(BASE_URL)
    driver.maximize_window()
    WebDriverWait(driver,15).until(EC.presence_of_all_elements_located((By.TAG_NAME,"body")))
    print("PAGE OPENED")
except:
    print("PAGE NOT OPEN")
class SeleniumButtons:
    def press_buton_class_name(the_driver,class_name):
        try:
            WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CLASS_NAME,class_name)))
            buton=the_driver.find_element(By.CLASS_NAME,class_name)
            actions.move_to_element(buton).perform()
            buton.click()
            time.sleep(1)
        except:
            print("class name tuşlama yapılmadı")
            pass
    def press_button_id(the_driver,id):
        try:
            WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID,id)))
            button=the_driver.find_element(By.ID,id)
            actions.move_to_element(button).perform()
            button.click()
            time.sleep(1)
        except:
            print("id tuşlama yapılmadı")
            pass
    def press_button_css_selector(the_driver,css_selector):
        try:
            WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,css_selector)))
            buton=the_driver.find_element(By.CSS_SELECTOR,css_selector)
            actions.move_to_element(buton).perform()
            buton.click()
            time.sleep(1)
        
        except:
            print("css selectore göre tuslama yapılmadı")
            pass
    def press_buton_xpath(the_driver,xpath):
        try:
            WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,xpath)))
            buton=the_driver.find_element(By.XPATH,xpath)
            actions.move_to_element(buton).perform()
            buton.click()
            time.sleep(1)
        except:
            print("xpathe göre tuşlama yapılmadı")
            pass
    def scroll_to_bottom(start,finish):
        driver.execute_script(f'window.scrollTo({start},{finish});')
        time.sleep(1)
    def find_elements_css(the_driver,css_selector):
        try:
            WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,css_selector)))
            buton=driver.find_elements(By.CSS_SELECTOR,f"{css_selector}")
            actions.move_to_element(buton).perform()
            buton.click()
            time.sleep(1)
        except:
            print("css selectore göre bulunamadı")
            pass  
    def find_elements_classname(the_driver,css_selector):
        try:
            WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CLASS_NAME,css_selector)))
            buton=the_driver.find_elements(By.CLASS_NAME,f"{css_selector}")
            actions.move_to_element(buton).perform()
            buton.click()
            time.sleep(1)
        except:
            print("class name göre bulunamadı")
            pass  
search_btn=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.NAME,"query")))
try:
     x2_btn=driver.find_element(By.CSS_SELECTOR,'button[aria-label="Kapat"]') 
     x2_btn.click()
except:
    pass
search_btn.click()
search_btn.send_keys("new york")
search_btn.send_keys(Keys.ENTER)
SeleniumButtons.press_button_css_selector(driver,"button[aria-label='Arama']")
SeleniumButtons.press_button_css_selector(driver,"button[aria-label='Kapat']")
WebDriverWait(driver,10).until(EC.visibility_of_all_elements_located((By.CLASS_NAME,"c965t3n ")))

#EXTRACING DATA
def take_link(the_driver):
    page=0
    datas=[]
    while True:
        time.sleep(2)
        WebDriverWait(the_driver,10).until(EC.presence_of_all_elements_located((By.CLASS_NAME,"with-new-header")))
        cards = driver.find_elements(By.CSS_SELECTOR,'a.rfexzly')
        for card in cards:
            link=card.get_attribute("href")
            print(link)
            datas.append(link)
        page+=1
        print("SAYFA=================",page)
        time.sleep(1)
        more_buttons = the_driver.find_elements(By.CSS_SELECTOR, "a[aria-label='Sonraki'], a[aria-label='Next']")
        if len(more_buttons) != 0:
            more_button = more_buttons[0]
            # Sayfanın ortasına kaydır
            the_driver.execute_script("arguments[0].scrollIntoView({block:'center'});", more_button)
            time.sleep(0.8)
            # Güvenli JS tıklama
            the_driver.execute_script("arguments[0].click();", more_button)
            time.sleep(1.5)
        else:
            print("daha fazla sayfa yok")
            break
    return datas
def open_page(the_driver,datas):        
    result=[]
    for link in datas:
        the_driver.get(link)
        time.sleep(1)
        WebDriverWait(the_driver,10).until(EC.presence_of_all_elements_located((By.CLASS_NAME,"with-new-header")))
        SeleniumButtons.press_button_css_selector(the_driver,'button[aria-label="Kapat"]')
        soup=BeautifulSoup(the_driver.page_source,"html.parser")
        
        try:
            title=soup.select_one('h1[elementtiming="LCP-target"]').text
        except:
            title=""
        try:
            location=soup.select_one('h2[elementtiming="LCP-target"]').text
        except:
            location=""
        try:
            room_type=soup.select_one('[data-plugin-in-point-id="OVERVIEW_DEFAULT_V2"] li').text
        except:
            room_type=""
        try:
            total_price = soup.find("span", string=re.compile(r"\d[\d.,]*\s?₺")).get_text(strip=True)
            nights = int(re.search(r"(\d+)\s*gece", soup.text).group(1))
        except:
            total_price=""
            nights=""
        try:
            if "Misafirlerin favorisi" in soup.text:
                fav = "YES"
            else:
                fav = "NO"
        except:
            fav=""
        try:
            rating=soup.text.split("Puanı 5 üzerinden")[1].split("yıldız")[0].strip()
        except:
            rating=""
        try:
            review = soup.text.split("değerlendirme")[0].split()[-1]
        except:
            review=""
        result.append({"title":title,
                        "location":location,
                        "room type":room_type,
                        "total":total_price,
                        "per night ":nights,
                        "quests fav":fav,
                        "rating":rating,
                        "review":review})  
    return result
datas=take_link(driver)
datas=list(set(datas))
datas=datas[:10]
results=open_page(driver,datas) 
print(len(datas))
print(len(results))

# SENDING EXEL FILE
df=pd.DataFrame(results)
df.to_excel("room.xlsx",index= False)









  
   
   
   

    
   
       
    
    
       


    



