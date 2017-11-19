#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: mel

"""

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

import requests as r
import os
import sys

def start_chrome():

    user_agent= 'user-agent= "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36 Edge/12.0" '
    user_agent= 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, likeGecko) Chrome/39.0.2171.71 Safari/537.36 Edge/12.0'
    options = webdriver.ChromeOptions()

    options.binary_location = '/usr/bin/google-chrome-stable'
    options.add_argument('window-size=1300x600')
    options.add_argument('headless')
    options.add_argument(user_agent)

    driver = webdriver.Chrome(chrome_options=options)
    return(driver)


def p_openload(url):

    driver=start_chrome()
    driver.get(url)

    l=driver.find_element_by_xpath("/html/body/div[3]/div/div/div[4]/span[2]").get_attribute("innerHTML")
    t=driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div/h3").get_attribute("innerHTML")
    link="https://openload.co/stream/"+l

    print(t, link, flush=True)
    driver.quit()
    return t, link


def primewire_show_all_links(driver, url):

    driver.get(url)
    wait= WebDriverWait(driver,10)

    xp_links = "/html/body/div[2]/div[2]/div/div[3]/div[4]/div[2]/table[*]/tbody/tr/td[2]/span/a"
    xp_names = "/html/body/div[2]/div[2]/div/div[3]/div[4]/div[2]/table[*]/tbody/tr/td[3]/span"

    e_links = wait.until(EC.presence_of_all_elements_located((By.XPATH, xp_links)))
    e_names = wait.until(EC.presence_of_all_elements_located((By.XPATH, xp_names)))

    v= [i.get_attribute("title") for i in e_links if i.get_attribute("title") is not '']
    l= [r.get("https://www.primewire.ag/"+i.get_attribute("href")).url for i in e_links if i.get_attribute("title") is not '']
    n= [i.text for i in e_names]

    o= zip(v, n, l)
    print(o)



def primewire_openload(driver, url):

    driver.get(url)
    wait= WebDriverWait(driver,10)

    xp_links = "/html/body/div[2]/div[2]/div/div[3]/div[4]/div[2]/table[*]/tbody/tr/td[2]/span/a"
    xp_names = "/html/body/div[2]/div[2]/div/div[3]/div[4]/div[2]/table[*]/tbody/tr/td[3]/span"

    try:
        e_links = wait.until(EC.presence_of_all_elements_located((By.XPATH, xp_links)))
        e_names = wait.until(EC.presence_of_all_elements_located((By.XPATH, xp_names)))

        n= [i.text for i in e_names]

        if ('oload' in n or 'openload.co' in n):
            index=[indx for indx, value in enumerate(n) if "openload" in value]
            m = max(index)
        else:
            print('No openload link found')
            driver.quit()
            sys.exit()

        l= [r.get(i.get_attribute("href")).url for i in e_links[:m*2+3] if i.get_attribute("title") is not '']

    except:
        print("Something went wrong - check the page at\n"+url, flush=True )
        driver.quit()
        sys.exit()

    driver.quit()

    for i, c in enumerate(l):
        print(i, c, sep="\t")

    url_number= int(input("Choose which Openload link you want to download\n"))

    title, link= p_openload(l[url_number])
    os.system('aria2c -c -x6 -s6 "%s"  -o "%s"'  %(link, title))



def primewire_movie_openload(driver, url):

    driver.get(url)
    wait= WebDriverWait(driver,10)

    xp_links = "/html/body/div[2]/div[2]/div/div[3]/div[4]/div/table[*]/tbody/tr/td[2]/span/a"
    xp_names = "/html/body/div[2]/div[2]/div/div[3]/div[4]/div/table[*]/tbody/tr/td[3]/span"

    try:
        e_links = wait.until(EC.presence_of_all_elements_located((By.XPATH, xp_links)))
        e_names = wait.until(EC.presence_of_all_elements_located((By.XPATH, xp_names)))

        n= [i.text for i in e_names]

        if ('oload' in n or 'openload.co' in n):
            index=[indx for indx, value in enumerate(n) if "openload" in value]
            m = max(index)
        else:
            print('No openload link found')
            driver.quit()
            sys.exit()

        l= [r.get(i.get_attribute("href")).url for i in e_links[:m*2+3] if i.get_attribute("title") is not '']
        driver.quit()

    except:
        print("Something went wrong - check the page at\n"+url, flush=True )
        driver.quit()
        sys.exit()

    for i, c in enumerate(l):
        print(i, c, sep="\t")

    url_number= int(input("Choose which Openload link you want to download\n"))

    title, link= p_openload(l[url_number])
    os.system('aria2c -c -x6 -s6 "%s"  -o "%s"'  %(link, title))



def check_url(url):

    if ('oload' in url or 'goto.php' in url or 'openload.co' in url):
        print('Openload url Detected', flush=True)
        title, link= p_openload(url)
        os.system('aria2c -c -x6 -s6 "%s"  -o "%s"'  %(link, title))

    elif 'primewire' in url:
        print('Primewire Link Detected', flush=True)

        if '-episode-' in url:
            primewire_openload(start_chrome(), url)
        else :
            primewire_movie_openload(start_chrome(), url)

    else:
        print('Please insert a valid link', flush=True)


if __name__ == "__main__":
    url=sys.argv[1]
    check_url(url)

