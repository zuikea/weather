import requests
 2 import time
 3 import schedule
 4 from selenium import webdriver
 5 from bs4 import BeautifulSoup
 6 import smtplib
 7 from email.mime.text import MIMEText
 8 from email.header import Header
 9 
10 def requests_fun():
11     res = requests.get('http://www.weather.com.cn/weather1d/101010100.shtml')
12     res.encoding='utf-8'
13     soup = BeautifulSoup(res.text,'html.parser')
14     tianqi  = soup.find('input',id='hidden_title')['value']
15     chuanyi = soup.find('li',id='chuanyi').find('p').text
16     return (tianqi,chuanyi)
17 
18 def selenium_fun():
19     driver = webdriver.Chrome()
20     driver.get('http://www.weather.com.cn/weather1d/101010100.shtml')
21     time.sleep(2)
22     tianqi  = driver.find_element_by_id('hidden_title').get_attribute('value')
23     chuanyi = driver.find_element_by_id('chuanyi').find_element_by_tag_name('p').text
24     return str(tianqi,chuanyi)
25     driver.close()
