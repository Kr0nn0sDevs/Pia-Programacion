import requests
from bs4 import BeautifulSoup
import re
import pyautogui,time,subprocess
import os
import logging

def validate(url):
    regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    
    if re.match(regex, url):
        urls=url
        return urls
    else:
        urls="http://"+url
        return urls
    
def web_scraping(urls):
    with open('data.txt', 'w') as f:
        urls_a = urls
        page = requests.get(urls_a)
        soup = BeautifulSoup(page.content, "html.parser")
        for a_href in soup.find_all("a", href=True):
            f.write(a_href["href"] + "\n")

def auto_open():
    simp_pathx = 'data.txt'
    abs_pathx = os.path.abspath(simp_pathx)
    pyautogui.press("win")
    time.sleep(1)
    pyautogui.typewrite(abs_pathx)
    time.sleep(1)
    pyautogui.press('enter')
"""
if __name__ == '__main__':
    url=str(input("Ingrese la url para el web scraping: "))
    
urls=validate(url)
web_scraping(urls)
auto_open()
"""