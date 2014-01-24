
# -*- coding: latin-1 -*-
# -*- coding: iso-8859-15 -*-
# -*- coding: ascii -*-
# -*- coding: utf-8 -*-

from scrapy.spider import BaseSpider
from scrapy.selector import Selector
import sys
from bs4 import BeautifulSoup
from scrapy.selector import HtmlXPathSelector
import re

class DmozSpider(BaseSpider):
    name = "movie_video_link"
    allowed_domains = ["hindilinks4u.net"]
    f = open("pag2_movielink")
    start_urls = re.findall(r'https?://[^\s<>"]+|www\.[^\s<>"]+', str(f.read())) 
    f.close()
  
    
    def parse(self, response):
        sel = Selector(response)
        page = response.body
        movielink = str(response.url).strip()
        soup = BeautifulSoup(page)
        data = soup.find_all("strong")
    
        for l in data:

            s = l.get_text().encode("ascii", "ignore")
            if re.search(r"Dailymotion", s):
                para = l.find_next("p")
                soup2 = BeautifulSoup(str(para))
                data2 = soup2.find_all("a")
                for m in data2:
                    movie_name = sel.xpath("/html/body/div/div[6]/h2/text()").extract()[0].encode("ascii","ignore")
                    movie_name = unicode(str(movie_name), errors='ignore')
                    watch = m.get_text().encode("ascii", "ignore")
                    watch_link = m.get("href").encode("ascii", "ignore")
                    f = open("page3_ml_mn_tp_prt_wt","a+")
                    print >>f, ",".join([movielink, movie_name, "dailymotion", watch , watch_link])
                    f.close()
                    f2 = open("page3_watch_link","a+")
                    print >>f2,  watch_link.strip()
                    f2.close()
                    print movielink, movie_name, "dailymotion", watch , watch_link
                        
                
            elif re.search(r"Youtube", s):
                para = l.find_next("p")
                soup2 = BeautifulSoup(str(para))
                data2 = soup2.find_all("a")
                for m in data2:
                    movie_name = sel.xpath("/html/body/div/div[6]/h2/text()").extract()[0].encode("ascii","ignore")
                    movie_name = unicode(str(movie_name), errors='ignore')
                    watch = m.get_text().encode("ascii", "ignore")
                    watch_link = m.get("href").encode("ascii", "ignore")
                    
                    f = open("page3_ml_mn_tp_prt_wt","a+")
                    print >>f, ",".join([movielink, movie_name, "youtube", watch , watch_link])
                    f.close()
                    f2 = open("page3_watch_link","a+")
                    print >>f2,  watch_link.strip()
                    f2.close()
                    print movielink, movie_name, "youtube", watch , watch_link
