import time
from selenium import webdriver
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.header import Header

def requests_fun():
    res = requests.get('http://www.weather.com.cn/weather1d/101010100.shtml')
    res.encoding='utf-8'
    soup = BeautifulSoup(res.text,'html.parser')
    tianqi  = soup.find('input',id='hidden_title')['value']
    chuanyi = soup.find('li',id='chuanyi').find('p').text
    return (tianqi,chuanyi)

def selenium_fun():
    driver = webdriver.Chrome()
    driver.get('http://www.weather.com.cn/weather1d/101010100.shtml')
    time.sleep(2)
    tianqi  = driver.find_element_by_id('hidden_title').get_attribute('value')
    chuanyi = driver.find_element_by_id('chuanyi').find_element_by_tag_name('p').text
    return str(tianqi,chuanyi)
    driver.close()
