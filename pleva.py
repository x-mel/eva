# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 02:39:40 2015

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

# Dictionnary of the xpaths of the objects
stream= [   {
                    'site'	: "vodlocker",
                    'video'     : "/html/body/div[4]/div/div[1]/div/center/div/div/table/tbody/tr[2]/td/table/tbody/tr/td/div/div[6]/script[2]",
                    'name'      : "/html/body/div[4]/div/div[1]/div/center/div/h2",
                    'button'    : "/html/body/div[4]/div/div[1]/div/center/div/form/input[7]"
                },
                {
                    'site'	: "vidlocker",
                    'video'     : "/html/body/div[3]/table[1]/tbody/tr/td/div[2]/script[2]",
                    'name'      : "/html/body/div[3]/h2",
                    'button'    : "/html/body/div[3]/form/input[8]"
                },
                {
                    'site'	: "bestreams",
                    'video'     : "/html/body/div[1]/div[2]/center/table/tbody/tr[2]/td/table/tbody/tr/td/div/div[3]/script[2]",
                    'name'      : "/html/body/div[1]/div[2]/center/h2",
                    'button'    : "/html/body/div[1]/div[2]/center/form/input[7]",
                },
                {
                    'site'	: "streamin",
                    'video'     : "/html/body/div[3]/div/div[2]/center/div[3]/script[2]",
                    'name'      : "/html/body/div[3]/div/div[2]/center/div[1]/h2",
                    'button'    : "/html/body/div[3]/div/div[2]/center/div[3]/form/center/input"
                },
                {
                    'site'	: "promptfile",
                    'video'     : "/html/body/div[2]/div[1]/a",
                    'name'      : "/html/body/div[2]/div[1]/span",
                    'button'    : "/html/body/div[2]/div[2]/form/button"
                },
                {
                    'site'	: "briskfile",
                    'video'     : "/html/body/div[2]/div[1]/a",
                    'name'      : "/html/body/div[2]/div[1]/span",
                    'button'    : "/html/body/div[2]/div[2]/form/button"
                },
                {
                    'site'	: "vidbull",
                    'video'     : "/html/body/div[2]/div[1]/a",
                    'name'      : "/html/body/div[3]/div[3]/div[2]/center/h3",
                    'button'    : "/html/body/div[3]/div[3]/div[2]/center/form/table[2]/tbody/tr/td[2]/center/div/input"
                },
                {
                    'site'	: "filenuke",
                    'video'     : "/html/body/div[1]/div[2]/div/div[4]/script[2]",
                    'name'      : "/html/body/div[1]/div[2]/div/dl/dd[1]",
                    'button'    : "/html/body/div/div[2]/div/table/tbody/tr[1]/td[3]/a"
                },
                {
                    'site'	: "vidzi",
                    'name'      : "/html/body/div[1]/section/div/div[1]/h2",
                    'video'     : "",
                    'button'    : ""
                },
                {
                    'site'	: "nosvideo",
                    'video'     : "/html/body/div/div/video",
                    'name'      : "/html/body/section[1]/div/div/div[1]",
                    'button'    : "/html/body/section[1]/div/div/div[3]/table/tbody/tr[2]/td/div/a"
                },
                {
                    'site'	: "thevideo.me",
                    'video'     : "/html/body/div[1]/div/div/script[3]",
                    'name'      : "/html/body/div[1]/div/div/div[1]/h1",
                    'button'    : "/html/body/div[1]/div/div/div[2]/div/form/div[5]/button"
                },
                {
                    'site'	: "vshare",
                    'video'     : "/html/body/section/div/div/div/form/div[1]/script[2]",
                    'name'      : "/html/body/section/div/div/div/h2/span",
                    'button'    : "/html/body/section/div/div/div/form/input[6]"
                },
                ]

number_links=len(sys.argv)

for nl in np.arange(1, number_links):
    driver = webdriver.PhantomJS()
    #driver = webdriver.Firefox()
    wait = WebDriverWait(driver, 20)

    vlink= sys.argv[nl]
    #vlink = "http://vshare.eu/9dja8i6adrfq.htm"
    driver.get(vlink)

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
    elif 'filenuke' in url:
        c=7
    elif 'vidzi' in url:
        c=8
    elif 'nosvideo' in url:
        c=9
    elif 'thevideo.me' in url:
        c=10
    elif 'vshare' in url:
        c=11
    else:
        print('Fuck you, enter a valid address you moron -_-')

    print('Loading the page ..')

    button=stream[c]['button']
    jsloc= stream[c]['video']
    vname= stream[c]['name']


    print('Getting name')

    # Wait and click the button

    # Download name
    if c==4 or c==5:
        name= driver.find_element_by_xpath(vname).get_attribute("title")
    elif c==9:
        name= driver.find_element_by_xpath(vname).get_attribute("innerHTML")
        # so here is the thing you have innerHTML, innerText, outerHTML, you know how that goes ..
    else:
        name= driver.find_element_by_xpath(vname).text

    if c!=8:
        if c!=3:
            print('Checking the clickables')
        #driver.implicitly_wait(10)
        # Wait till it is clickable
            wait.until(EC.element_to_be_clickable((By.XPATH,button)))
            print('Clicking the button ...')
            driver.find_element_by_xpath(button).click()
        #elif c==3:
            #while EC.presence_of_element_located((By.XPATH, button)) is True:
            #wait.until(EC.presence_of_element_located((By.XPATH, button)))
                #driver.find_element_by_xpath(button).submit()
                #print("So basically pushed the fucking button.")

    # Wait until the video play back page load and download link
    if c!=2 and c!=8 and c!=3 and c!=11:
        print('Loading the video ...')
        #print(str(driver.current_url))
        wait.until(EC.presence_of_element_located((By.XPATH, jsloc)))

    print('Downloadin')
    # Download link
    if c==4 or c==5:
        link= driver.find_element_by_xpath(jsloc).get_attribute("href")
    elif c==2 or c==8 or c==11:
        link= driver.page_source
    elif c==3:
        try:
            driver.implicitly_wait(10)
            driver.find_element_by_xpath(button).submit()
            #print("Okay I guess")
            print(driver.find_element_by_xpath(jsloc).get_attribute("text"))
        except:
            driver.implicitly_wait(10)
            driver.find_element_by_xpath(button).submit()
            #print("Trying it again")
            link=driver.find_element_by_xpath(jsloc).get_attribute("text")


    elif c==9:
        link= driver.find_element_by_xpath(jsloc).get_attribute("src")
    #elif c==3:
    #    print("Let's get that motha fucking video")
    #    link= driver.find_element_by_xpath(jsloc).get_attribute("text")
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
    elif c==4 or c==5 or c==9:
        dname=name
        dlink=link
    elif c==2:
        #dname=name[6:]
        s1=link.index('image: "')
        s2=link.index('mp4?h=')
        s3=link.index('",\n                          stream')
        dlink=link[s1+len('image: "'):link.index('i/')]+ link[s2+len('mp4?h='):s3]+'/v.mp4'
        dname=name[6:]+'.mp4'

    elif c==3:
        s1= link.index("file:\'")
        s2= link.index("','provid")
        dlink=link[s1+len("file:\'"):s2]
        dname=name[6:]

    elif c==7:
        s1=link.index('lnk234 = \'')
        s2=link.index("';")
        dlink= link[s1+len('lnk234 = \''):s2]
        dname=name[:len(name)-len('.mp4')]

    elif c==8:
        s1= link.index('[IMG]')
        s2= link.index('[/IMG]')
        s0= link[s1:s2]
        s3= link.index('mp4|')
        s4= link.index('|hls|')
        dlink= s0[len('[IMG]'):s0.index('i/')]+link[s3+len('mp4|'):s4]+'/v.mp4'
        dname=name

    elif c==10:
        s1=link.index("360p', file: '")
        s2=link.index("\' }],\n\t\t\t}")
        dlink=link[s1+len("360p', file: '"):s2]
        dname=name[6:]

    elif c==11:
        s1=link.index('file: "')
        s2=link.index('",\n               flashplayer')
        dlink=link[s1+len('file: "'):s2]
        dname=name

    # Launch wget to download the file
    print('"%s"\n"%s"'  %(dname, dlink))
    #os.system('qrencode "%s" -o -| display &' %dlink)
    os.system('smplayer -add-to-playlist  "%s" &'  %(dlink))


