from scrapy.spider import BaseSpider
from scrapy.selector import Selector
import sys
import MySQLdb

class DmozSpider(BaseSpider):
    name = "actor-link"
    allowed_domains = ["hindilinks4u.net"]
    start_urls = ["http://www.hindilinks4u.net/"]

    def parse(self, response):
        sel = Selector(response)

        tag_li  =  sel.xpath("/html/body/div/div[7]/div/ul/li[5]/ul/li")
        act_names = tag_li.xpath('a/text()').extract()
	act_links = tag_li.xpath('a/@href').extract()

        f = open("page1_actors_n_links","a+")
        for act_name, act_link in zip(act_names, act_links):
	    print >>f,   str(act_name).strip(),",", str(act_link).strip() 
        f.close()

	db = MySQLdb.connect("localhost","root","6Tresxcvbhy","hindilink_actor")
	cursor = db.cursor()

	sql = """create table IF NOT EXISTS  actor_n_actor_links (date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,actor_name varchar(100), actro_link varchar(255));"""

        cursor.execute(sql)

	f  = open("page1_actors_n_links")
        
	for act_name_link in f:
            act_name_link = tuple(act_name_link.split(","))
            sql = """ insert  into actor_n_actor_links (actor_name, actro_link)  values ("%s","%s")"""%(act_name_link)
            cursor.execute(sql)
            db.commit()




