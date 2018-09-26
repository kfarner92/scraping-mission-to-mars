#Dependencies
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from splinter import Browser
import os
import time
import tweepy
from config import consumer_key, consumer_secret, access_token, access_token_secret

def init_browser():
    executable_path = {"executable_path":"/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless = False)

def scrape():
    browser = init_browser()
    mars_data = {}


    executable_path = {"executable_path":"/usr/local/bin/chromedriver"}
    browser = Browser("chrome", **executable_path, headless = False)

    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html,"html.parser")

    news_title= soup.find("div",class_="content_title").text
    news_p = soup.find("div",class_="article_teaser_body").text
    
    mars_data["news_title"] = news_title
    mars_data["summary"] = news_p

    # url2 = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    # browser.visit(url2)

    # html = browser.html
    # soup = BeautifulSoup(html,"html.parser")

    # browser.click_link_by_partial_text("FULL IMAGE")
    # time.sleep(1)
    # browser.click_link_by_partial_text('more info')
    # time.sleep(1)

    # featured_image_url = soup.find("article")
    # featured_image_url = featured_image_url.find("a")

    # mars_data["featured_image_url"] = featured_image_url


    url2 = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url2)

    html = browser.html
    soup = BeautifulSoup(html,"html.parser")

    browser.click_link_by_partial_text("FULL IMAGE")
    time.sleep(1)
    browser.click_link_by_partial_text('more info')
    time.sleep(1)
    browser.click_link_by_partial_href('/spaceimages/images')
    featured_image_url = (str(browser.url))
    mars_data["featured_image_url"] = featured_image_url

    # # Twitter API Keys
    # consumer_key = consumer_key
    # consumer_secret = consumer_secret
    # access_token = access_token
    # access_token_secret = access_token_secret

    # # Setup Tweepy API Authentication
    # auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    # auth.set_access_token(access_token, access_token_secret)
    # api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

    url_weather = "https://twitter.com/marswxreport?lang=en"
    browser.visit(url_weather)
    html_weather = browser.html
    soup = BeautifulSoup(html_weather, "html.parser")
    mars_weather = soup.find("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text

    mars_data["mars_weather"] = mars_weather

    url3 = 'https://space-facts.com/mars/'
    
    mars_facts = pd.read_html(url3)

    mars_df = mars_facts[0]
    mars_df.columns = ['Measure','Values']
    mars_df = mars_df.set_index('Measure')
    mars_df.head()
    mars_table =mars_df.to_html(classes='marstable')
    mars_table=mars_table.replace('\n',' ')

    mars_data["mars_table"] = mars_table

    # hemisphere_image_urls = []

    # url3 = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    # browser.visit(url3)
    # browser.click_link_by_partial_text('Cerberus Hemisphere Enhanced')
    # html = browser.html
    # soup = BeautifulSoup(html,"html.parser")
    # hem1title= soup.find(class_='title').text
    # browser.click_link_by_partial_href('http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg')
    # hem1 = (str(browser.url))
    # hemisphere_image_urls.append({"title": hem1title, "img_url": hem1})

    # browser.visit(url3)
    # browser.click_link_by_partial_text('Schiaparelli Hemisphere Enhanced')
    # html = browser.html
    # soup = BeautifulSoup(html,"html.parser")
    # hem2title= soup.find(class_='title').text
    # browser.click_link_by_partial_href("http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg")
    # hem2 = (str(browser.url))
    # hemisphere_image_urls.append({"title": hem2title, "img_url": hem2})
    
    # browser.visit(url3)
    # browser.click_link_by_partial_text('Syrtis Major Hemisphere Enhanced')
    # html = browser.html
    # soup = BeautifulSoup(html,"html.parser")
    # hem3title= soup.find(class_='title').text
    # browser.click_link_by_partial_href("http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg")
    # hem3 = (str(browser.url))
    # hemisphere_image_urls.append({"title": hem3title, "img_url": hem3})

    # browser.visit(url3)
    # browser.click_link_by_partial_text('Valles Marineris Hemisphere Enhanced')
    # html = browser.html
    # soup = BeautifulSoup(html,"html.parser")
    # hem4title= soup.find(class_='title').text
    # browser.click_link_by_partial_href("http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg")
    # hem4 = (str(browser.url))
    # hemisphere_image_urls.append({"title": hem4title, "img_url": hem4})

    

    # # hemisphere_image_urls.append({"title": hem1title, "img_url": hem1})
    # # hemisphere_image_urls.append({"title": hem2title, "img_url": hem2})
    # # hemisphere_image_urls.append({"title": hem3title, "img_url": hem3})
    # # hemisphere_image_urls.append({"title": hem4title, "img_url": hem4})
    # mars_data["mars_hemis"] = hemisphere_image_urls
    return mars_data


    