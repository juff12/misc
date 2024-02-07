from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import random
from bs4 import BeautifulSoup
import requests


driver = webdriver.Firefox()

email = '' # enter email
password = '' # enter password

driver.get('https://www.youtube.com/')
login_page = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
                            (By.XPATH,'//*[@id="buttons"]/ytd-button-renderer/yt-button-shape/a')))
login_page.click()
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id ="identifierId"]').send_keys(email)
driver.find_element(By.XPATH,'//*[@id ="identifierNext"]').click()
pword_entry = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
                            (By.XPATH,'//*[@id="password"]/div[1]/div/div[1]/input')))
pword_entry.send_keys(password)
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id ="passwordNext"]').click()
time.sleep(1)


# go to watch later
driver.get('https://www.youtube.com/playlist?list=WL')
time.sleep(2)
# ytd-playlist-video-renderer.style-scope:nth-child(1) > div:nth-child(3) > ytd-menu-renderer:nth-child(1) > yt-icon-button:nth-child(3) > button:nth-child(1) > yt-icon:nth-child(1) > yt-icon-shape:nth-child(1) > icon-shape:nth-child(1) > div:nth-child(1)

total_videos = driver.find_element(By.XPATH,'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-playlist-header-renderer/div/div[2]/div[1]/div/div[1]/div[1]/ytd-playlist-byline-renderer/div/yt-formatted-string[1]/span[1]')
#print(total_videos.text())
total_videos = int(total_videos.get_attribute('innerHTML'))

for _ in range(0,total_videos):
    button = WebDriverWait(driver,10).until(EC.element_to_be_clickable(
                                            (By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager'+\
                                            '/ytd-browse/ytd-two-column-browse-results-renderer/div[1]'+\
                                            '/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/'+\
                                            'div[3]/ytd-playlist-video-list-renderer/div[3]/ytd-playlist-video'+\
                                            '-renderer[2]/div[3]/ytd-menu-renderer/yt-icon-button/button/yt-icon/'+\
                                            'yt-icon-shape/icon-shape/div')))
    button.click()
    remove_video = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
                                (By.XPATH,'//*[@id="items"]/ytd-menu-service-item-renderer[3]/tp-yt-paper-item')))
    remove_video.click()
    time.sleep(1)