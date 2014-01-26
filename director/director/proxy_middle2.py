# -*- coding: latin-1 -*-
# -*- coding: iso-8859-15 -*-
# -*- coding: ascii -*-
# -*- coding: utf-8 -*-

# Importing base64 library because we'll need it ONLY in case if the proxy we are going to use requires authentication
import base64

from random import choice
import sys
from scrapy.http import Request
from  random import choice 


f = open("/home/desktop/proxy2")
ip_list = f.read().strip().split("\n")
f.close()


class ProxyMiddleware(object):
    def process_request(self, request, spider):
        ip_pass = choice(ip_list)
        #proxy_ip_port = ip_pass.split("@")[0].strip()
        #proxy_user_pass = ip_pass.split("@")[1].strip()
        #request.meta['proxy'] = "http://%s" % proxy_ip_port
        #encoded_user_pass=base64.encodestring(proxy_user_pass)
        #request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass
        request.meta['proxy'] = "http://%s" %ip_pass

