    # To authenticate the proxy, you must set the Proxy-Authorization header. You *cannot* use the form http://user:pass@proxy:port in request.meta['proxy']
     
import base64
import re
import random
import base64
from scrapy import log
from scrapy.http import  Request




f = open("/home/desktop/proxy1")
ip_list = f.read().strip().split("\n")
f.close()

proxy_ip_port = random.choice(ip_list)
proxy_user_pass = "SuperVIP79755:2GVkM4MIii"
     
request = Request(url, callback=self.parse)
     
# Set the location of the proxy
request.meta['proxy'] = "http://%s" % proxy_ip_port
     
# setup basic authentication for the proxy
encoded_user_pass=base64.encodestring(proxy_user_pass)
request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass
    
# Snippet imported from snippets.scrapy.org (which no longer works)
# author: redtricycle
# date : Nov 21, 2011
     
