# -*- coding: latin-1 -*-
# -*- coding: iso-8859-15 -*-
# -*- coding: ascii -*-
# -*- coding: utf-8 -*-

from scrapy.http import Request
from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile


from random import choice
from scrapy.spider import BaseSpider
from scrapy.selector import Selector
import sys
from bs4 import BeautifulSoup

from selenium.webdriver.common.proxy import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException
import re
from selenium import selenium
import time
import sys



f = open("/home/desktop/proxy1")
ip_list = f.read().strip().split("\n")
f.close()



class DmozSpider(BaseSpider):
    
    name = "page4_link_to_linkii"
    allowed_domains = ["hindilinks4u.net"]

    def __init__(self, aval_urls=' '):

        extracted_link = []

        try:
            extracted_f  =  open("page4_watch_link__emlink")

            for l in extracted_f:
                extracted_link.append(l.split(",")[0])

            extracted_f.close()

        except:
           pass
         
        aval_urls = aval_urls.split(",")
        self.start_urls =  list(set(aval_urls) - set(extracted_link))

        print len(self.start_urls) ,  len(extracted_link)

        if len(self.start_urls) - len(extracted_link) ==0:
            return 0

       
        ip_port = choice(ip_list)
        user_pass = ip_port.split("@")[1].strip()
        prox = "--proxy=%s"%ip_port.split("@")[0].strip()
        service_args = [prox, '--proxy-auth='+user_pass, '--proxy-type=http',]
        #service_args = [prox, '--proxy-type=http',]
        self.driver = webdriver.PhantomJS(service_args =service_args)
        


    def __del__(self):
        self.driver.close()

     

    def parse(self, response):
        
        driver = self.driver

        wait = WebDriverWait(driver, 3)
        driver.get(str(response.url))
 
        wait.until(lambda driver: driver.find_element_by_xpath("/html/body/center/table/tbody/tr[2]/td"))

        try:
            data = driver.find_element_by_xpath("/html/body/center/table/tbody/tr[2]/td")
            result = data.find_element_by_tag_name("iframe").get_attribute("src")
       
        except:
            data = driver.find_element_by_xpath("/html/body/center/table/tbody/tr[2]/td")
            result = data.find_element_by_tag_name("embed").get_attribute("src")
           
        f = open("page4_watch_link__emlink", "a+")
        print >>f, ','.join([str(response.url), result])
        print str(response.url), result

