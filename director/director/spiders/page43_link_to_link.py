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
    name = "page43_link_to_linkii"

    allowed_domains = ["hindilinks4u.net"]
    
    extracted_link = []
 
    try:
        extracted_f  =  open("page4_watch_link__emlink")

        for l in extracted_f:
            extracted_link.append(l.split(",")[0])

	extracted_f.close()
    except:
       pass
    
  
    f = open("page3_watch_link")

    aval_urls = f.read().strip().split("\n")

    val = len(aval_urls)/10
    val1 = val*2
    val2 = val*3

    aval_urls = aval_urls[val1:val2]


    start_urls =  list(set(aval_urls) - set(extracted_link))
    #print type(start_urls)
    #sys.exit()
    f.close()
    
    print len(start_urls) ,  len(extracted_link)
    if len(start_urls) - len(extracted_link) ==0:
        sys.exit()
            


    def __init__(self):
        ip_port = choice(ip_list)
        user_pass = ip_port.split("@")[1].strip()
        prox = "--proxy=%s"%ip_port.split("@")[0].strip()
        service_args = [prox, '--proxy-auth='+user_pass, '--proxy-type=http',]
        
        #service_args = [prox, '--proxy-type=http',]
        self.driver = webdriver.PhantomJS(service_args =service_args)
        #self.driver = webdriver.PhantomJS()
        

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

