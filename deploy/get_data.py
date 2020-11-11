import requests as rq
from bs4 import BeautifulSoup
import re
import time
import os
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import InvalidSessionIdException
from selenium.common.exceptions import TimeoutException

def donwload_search_page(query, page):
    options = webdriver.FirefoxOptions()
    options.add_argument("--window-size 1920,1080")
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    url = "https://www.amazon.com/s?k={query}&page={page}".format(query = query, page = page)
    driver.get(url)
    html = driver.page_source
    
    driver.close()
    time.sleep(2)
    
    return html

def parse_search_page(page_html):
    soup = BeautifulSoup(page_html, 'html.parser')
    parsed = [link.get('href') for link in soup.findAll('a',{'class':'a-link-normal a-text-normal'})]
    
    book_list = []

    for j in range(len(parsed)):
        book_list.append(parsed[j])
            
    book_list = list(dict.fromkeys(book_list))
    book_list = [x for x in book_list if not x.startswith('/dp/B0') and not x.startswith('https://') and not x.startswith('/gp/slredirect/')]
    
    return book_list

def download_book_page(link):
    try:
        url = "https://www.amazon.com{link}".format(link = link)
        options = webdriver.FirefoxOptions()
        options.add_argument("--window-size 1920,1080")
        options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)
        driver.get(url)
        html = driver.page_source
        driver.close()
        time.sleep(2)
    except (AttributeError, InvalidSessionIdException, TimeoutException) as e:
        driver.close()
        time.sleep(2)
        pass
    
    return html

def parse_book_page(page_html):
    parsed = BeautifulSoup(page_html, 'html.parser')
    
    data = dict()

    #Reviews
    try:
        reviews = parsed.find('span', id = 'acrCustomerReviewText').text.strip()
        if len(reviews) == 12:
            rev = reviews[0:4]
        elif len(reviews) == 11:
            rev = reviews[0:3]
        elif len(reviews) == 10:
            rev = reviews[0:2]
        else:
            rev = reviews[0:1]
        data['reviews'] = rev
    except:
        data['reviews'] = '0'
    
    #Titulo
    try:
        titulo = parsed.find('span', class_ = 'a-size-extra-large').text.strip()
    except:
        titulo = 'Title Error'
    data['title'] = titulo
    
    #Image_link
    try:
        if parsed.find('img', id = 'imgBlkFront', class_ = 'a-dynamic-image a-stretch-vertical') == None:
            img = parsed.find('img', id = 'ebooksImgBlkFront', class_ = 'a-dynamic-image a-stretch-vertical').get('src')
        else:
            img = parsed.find('img', id = 'imgBlkFront', class_ = 'a-dynamic-image a-stretch-vertical').get('src')
    except:
        img = 'Image Link Error'
    data['image'] = img
    
    #Classification
    try:
        star = parsed.find('span', class_ = 'a-size-medium a-color-base').text
        if len(star) == 12:
            star_c = star[0:3]
        else:
            star_c = star[0]
        data['classification'] = star_c
    except:
        data['classification'] = '0'
    
    return data