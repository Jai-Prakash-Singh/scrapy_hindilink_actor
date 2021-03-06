# Scrapy settings for director project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'director'

SPIDER_MODULES = ['director.spiders']
NEWSPIDER_MODULE = 'director.spiders'


RETRY_TIMES = 10
RETRY_HTTP_CODES = [500, 503, 504, 400, 403, 404, 408]

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'director (+http://www.yourdomain.com)'


DOWNLOADER_MIDDLEWARES = {
                          'scrapy.contrib.downloadermiddleware.retry.RetryMiddleware': 90,
                          #'director.proxy_middle': 100, 
                          'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
                          'director.proxy_middle2.ProxyMiddleware': 100,
                         }
