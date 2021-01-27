from bs4 import BeautifulSoup
import time
import csv
import pandas as pd
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#url = input("Url Giriniz")

driver =webdriver.Chrome()
driver.maximize_window()
url="https://twitter.com/search?q=(from%3Aahmetkonanc)%20until%3A2020-09-22%20since%3A2020-09-05%20-filter%3Alinks%20-filter%3Areplies&src=typed_query&f=live"
#file_name=input("dosya adi giriniz (ornek.csv)")
driver.get(url)
time.sleep(2)

file =open("ahmet1.csv","w",encoding="utf-8")
writer=csv.writer(file)
writer.writerow(["Twitler","Cevaplar","Retweet","Like","Kullanici","Date"])

j=0
while j<1:


    lastHeight = driver.execute_script("return document.body.scrollHeight")
    i=0
    while i<10:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(4)
        newHeight = driver.execute_script("return document.body.scrollHeight")
    
        if newHeight == lastHeight:
            break
        else:
            lastHeight = newHeight
    
        i = i+1
        
        #i=0
        #while i<50:
        #    action =webdriver.ActionChains(driver)
        #    action.key_down(Keys.SPACE).key_up(Keys.SPACE)
        #    action.perform()
        #    time.sleep(2)
        #    i+=1

        pageSource=driver.page_source

        soup=BeautifulSoup(pageSource,"html.parser")
        #   time.sleep(2)
        tweets=soup.find_all("div",attrs={"data-testid":"tweet"})
        for element in tweets:
            try:
                tweet=element.find("div", attrs={"class":"css-901oao r-18jsvk2 r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0"}).text
                reply=element.find("div",attrs={"data-testid":"reply"}).text
                rt=element.find("div",attrs={"data-testid":"retweet"}).text
                like=element.find("div",attrs={"data-testid":"like"}).text
                userId=element.find("span",attrs={"class":"css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0"}).text
                date=element.find("a",attrs={"class":"css-4rbku5 css-18t94o4 css-901oao r-m0bqgq r-1loqt21 r-1q142lx r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-3s2u2q r-qvutc0"}).text
                writer.writerow([tweet,reply,rt,like,userId,date])
            except:
                print("Hata Oldu!!")
    j+=1

