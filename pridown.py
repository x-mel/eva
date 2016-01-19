# -*- coding: utf-8 -*-
"""
Created on Thu Dec 18 03:39:40 2015

@author: mel
"""

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException as WE
import sys
import numpy as np
import os

number_links=len(sys.argv)
for nl in np.arange(1, number_links):

    driver = webdriver.PhantomJS()
    wait = WebDriverWait(driver, 20)
    
    vlink= sys.argv[nl]
    driver.get(vlink)
    stream= [   {
                    'video'     : "/html/body/div[4]/div/div[1]/div/center/div/div/table/tbody/tr[2]/td/table/tbody/tr/td/div/div[6]/script[2]",
                    'name'      : "/html/body/div[4]/div/div[1]/div/center/div/h2",
                    'button'    : "/html/body/div[4]/div/div[1]/div/center/div/form/input[7]"
                },
                {
                    'video'     : "/html/body/div[3]/table[1]/tbody/tr/td/div[2]/script[2]",
                    'name'      : "/html/body/div[3]/h2",
                    'button'    : "/html/body/div[3]/form/input[8]"
                },
                {
                    'video'     : "/html/body/div/div[2]/center/table/tbody/tr[2]/td/table/tbody/tr/td/div/div[2]/script[2]",
                    'name'      : "/html/body/div[1]/div[2]/center/h2",
                    'button'    : "/html/body/div[1]/div[2]/center/form/input[7]",
                },
                {   'video'     : "/html/body/div[3]/div/div[2]/center/div[3]/script[2]",
                    'name'      : "/html/body/div[3]/div/div[2]/center/div[1]/h2",
                    'button'    : "/html/body/div[3]/div/div[2]/center/div[3]/form/center/input"
                },
                {   'video'     : "/html/body/div[2]/div[1]/a",
                    'name'      : "/html/body/div[2]/div[1]/span",
                    'button'    : "/html/body/div[2]/div[2]/form/button"
                },
                {   'video'     : "/html/body/div[2]/div[1]/a",
                    'name'      : "/html/body/div[2]/div[1]/span",
                    'button'    : "/html/body/div[2]/div[2]/form/button"
                }]


    url=str(driver.current_url)

    if 'vodlock' in url:
        c=0
    elif 'bestreams' in url:
        c=2
    elif 'vidlock' in url:
        c=1
    elif 'streamin' in url:
        c=3
    elif 'promptfile' in url:
        c=4
    elif 'brisk' in url:
        c=5

    else:
        print('Please enter a valid address -_-')
        exit(0)

    #print('Loading the page ..')
    button=stream[c]['button']
    jsloc= stream[c]['video']
    vname= stream[c]['name']

    #print('Getting name')

    # Wait and click the button

    # Download name
    if c==4 or c==5:
        name= driver.find_element_by_xpath(vname).get_attribute("title")
    else:
        name= driver.find_element_by_xpath(vname).text

    #print('Checking the clickables')

    #driver.implicitly_wait(10)

    # Wait till it is clickable
    wait.until(EC.element_to_be_clickable((By.XPATH,button)))


    #print('Clicking the button ..')
    driver.find_element_by_xpath(button).click()
    #driver.find_element_by_xpath(button).submit()

    #print('Loading the video ...')
    # Wait until the video play back page load and download link
    wait.until(EC.presence_of_element_located((By.XPATH, jsloc)))

    #print('Downloadin')
    # Download link
    if c==4 or c==5:
        link= driver.find_element_by_xpath(jsloc).get_attribute("href")
    else:
        link= driver.find_element_by_xpath(jsloc).get_attribute("text")
    driver.quit()


    if c==0 or c==1:
        # Generate name
        #dname=  name[6:]
        # Generating the download link parameters
        s1=link.index('http')
        s2= link.index('mp4')
        dlink=link[s1:s2+len('mp4')]
        dname=name[6:]+'.mp4'
    elif c==4 or c==5:
        dname=name
        dlink=link
    elif c==3 or c==2:
        #dname=name[6:]
        s1=link.index('http')
        s2=link.index('mp4?h=')
        s3=link.index('",')
        s4=link.index('i/')
        dlink=link[s1:s4]+ link[s2+len('mp4?h='):s3]+'/v.mp4'
        dname=name[6:]+'.mp4'

    print(dlink)
