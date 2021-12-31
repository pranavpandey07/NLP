# Scrapy settings for gadgets project
import scraper_helper as sh
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'gadgets'

SPIDER_MODULES = ['gadgets.spiders']
NEWSPIDER_MODULE = 'gadgets.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'gadgets (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = sh.get_dict(
'''
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
Cache-Control: max-age=0
Connection: keep-alive
Cookie: T=TI163904946183100165424897875554518265956490804570397638367670129077; _pxvid=80b1eb91-58e3-11ec-beee-545376674769; AMCVS_17EB401053DAF4840A490D4C%40AdobeOrg=1; Network-Type=4g; pxcts=a286f2f1-66cb-11ec-8a4c-fb26f9324fe9; AMCV_17EB401053DAF4840A490D4C%40AdobeOrg=-227196251%7CMCIDTS%7C18989%7CMCMID%7C37283480343930169265798855680291779282%7CMCAID%7CNONE%7CMCAAMLH-1641183337%7C12%7CMCAAMB-1641183337%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI%7CMCOPTOUT-1640585737s%7CNONE; s_cc=true; qH=5a2004e9a5a5938c; SN=VI98FCB01E46024ECABD59A4A4070BD2D7.TOK0A7269BF390249DBBA5439F38CDD1A61.1640578792.LO; gpv_pn=Read%20Review%3A%20POCO%20X3%20%28Cobalt%20Blue%2C%20128%20GB%29; gpv_pn_t=Read%20Review; s_sq=%5B%5BB%5D%5D; S=d1t18CWtqCT98PAI/P34/fT8LPwp6IvruDAgPdIK/w8tgye1m8S24Lbee2KyciIcsmCHZo0uFL0BkUqXF605+SlAANA==; _px3=3f83071a1b4842f073aa5bfb02abde33cc6509d1ceb818ef49e530bb514a9633:TGgnK6K49soSazbBkZzS4mKeflE/LcE+sXLKTeCvjoxcdciJW3E3Dv4oX1zwODaqnASrAmSYd76osS84JGz2nw==:1000:hIKDlu+GoiLhX9xrpTCDhilAH33MTz+Go1cScWvzOMv6Ftx+WWQzKCvnG6KZmgxhN4bsuoCtfJdcULkLSLlk8X9X8jShuvH4en7gQ4xPEoMKsrDxWF5WKAh2cq3ZZe9+20+fywisH90mdTacGkOIwy6pV7P8ZCoihCzsk2ZNPfN7INuvjJcTo/uERMvARR5Y5L7iyChgKwlSXRCrZtAJAw==
Host: www.flipkart.com
sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36
'''
)

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'gadgets.middlewares.GadgetsSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'gadgets.middlewares.GadgetsDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'gadgets.pipelines.GadgetsPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
