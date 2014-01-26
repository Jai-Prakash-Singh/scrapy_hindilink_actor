 
import base64
 
from scrapy.http import Request

f = open("/home/desktop/proxy1")
ip_list = f.read().strip().split("\n")
f.close()


ip_port = choice(ip_list)

proxy_ip_port = ip_port.split("@")[1].strip()

proxy_user_pass = ip_port.split("@")[0].strip()
 
request = Request(response.url, callback=self.parse)
 
# Set the location of the proxy
request.meta['proxy'] = "http://%s" % proxy_ip_port
 
# setup basic authentication for the proxy
encoded_user_pass=base64.encodestring(proxy_user_pass)
request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass
 
# Snippet imported from snippets.scrapy.org (which no longer works)
# author: redtricycle
# date : Nov 21, 2011
