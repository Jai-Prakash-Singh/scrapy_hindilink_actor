# -*- coding: latin-1 -*-
# -*- coding: iso-8859-15 -*-
# -*- coding: ascii -*-
# -*- coding: utf-8 -*-

# Importing base64 library because we'll need it ONLY in case if the proxy we are going to use requires authentication
import base64

from random import choice




f = open("/home/desktop/proxy1")
ip_list = f.read().strip().split("\n")
f.close()


class ProxyMiddleware(object):
    def process_request(self, request, spider):
        ip_port = choice(ip_list)
        #ip_port = "194.141.96.229:8080"
        request.meta['proxy'] = "http://"+ip_port
        #proxy_user_pass = 'SuperVIP79755:2GVkM4MIii'
        #encoded_user_pass = base64.encodestring(proxy_user_pass)
        #request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass
