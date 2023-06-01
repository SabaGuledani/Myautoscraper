import os
os.system('pip install selenium')
os.system('pip install chromedriver-binary==113.0.5672.63.0')  # konkretulad es aris 113 versia chromesi
# sxvanairad kodi ver imushavebs errors agdebs shesabamisi versiebi tu araa biblioteka da chrome
# os.system('pip install chromedriver-binary==112.0.5615.49.0')#es 112 versisitvis tu dzveli giyeniat
# os.system('pip install chromedriver-binary==114.0.5735.90.0')#an 114
import time
from random import randint
import requests
from selenium import webdriver
import chromedriver_binary
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import csv

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument("window-size=800,1080")  # ase dayeneba schirdeba rom ekranze ar gaxsnas saiti da
# konkretuli zomebi mieces rom info wamoigos
wd = webdriver.Chrome(options=options)
wd.implicitly_wait(15)

for i in range(1, 6):
    url = f"https://www.myauto.ge/ka/s/spec-teqnika?vehicleType=1&bargainType=&mansNModels=&currId=3&mileageType=1&page={i}"

    wd.get(url)  # aq saiti chairtveba
    elem = WebDriverWait(wd, 15).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/header/div/div/div/div[1]/div[1]'))
        # This is a dummy element
    )  # velodebit bolomde chatvirtvas
    time.sleep(2)

    content = wd.page_source
    soup = BeautifulSoup(content, 'html.parser')  # vparsavt
    all_items_white = soup.find_all('div', {'class': 'rounded mb-10px bg-white'})
    all_items_green = soup.find_all('div', {'class': 'rounded mb-10px rgba-green-500-5 border border-green-500'})
    all_items = all_items_white + all_items_green
    f = open("data.csv", "a", newline='\n', encoding='UTF-8_sig')
    write_obj = csv.writer(f)

    for item in all_items:
        my_list = []
        name = item.find('a', {'class': 'text-gray-800'}).text
        item_info = item.find_all('div',
                                  {'class': 'd-flex align-item-center font-size-12 font-size-md-13 text-gray-800'})
        my_list.append(name)
        for item in item_info:
            my_list.append(item.text)
        write_obj.writerow(my_list)

    f.close()
    time.sleep(randint(5, 15))
