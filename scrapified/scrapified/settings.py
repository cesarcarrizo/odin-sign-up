# Scrapy settings for scrapified project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "scrapified"

SPIDER_MODULES = ["scrapified.spiders"]
NEWSPIDER_MODULE = "scrapified.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "scrapified (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

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
#DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "scrapified.middlewares.ScrapifiedSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    "scrapified.middlewares.ScrapifiedDownloaderMiddleware": 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    "scrapified.pipelines.ScrapifiedPipeline": 300,
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
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

# Configure a delay between requests to the same website (in seconds)
DOWNLOAD_DELAY = 2

# Adjust the maximum concurrent requests performed by Scrapy (recommended values)
CONCURRENT_REQUESTS = 8
CONCURRENT_REQUESTS_PER_DOMAIN = 4
CONCURRENT_REQUESTS_PER_IP = 0  # Set to 0 for dynamic IP rotation

# Obey robots.txt rules (True by default, set to False to ignore robots.txt)
ROBOTSTXT_OBEY = False

# Configure user agent to simulate different browsers/clients
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'

# Enable and configure auto-throttling to automatically adjust crawling speed
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 5  # Initial delay (in seconds) for auto-throttling
AUTOTHROTTLE_MAX_DELAY = 60   # Maximum delay (in seconds) for auto-throttling
AUTOTHROTTLE_TARGET_CONCURRENCY = 4  # Aim to maintain this number of concurrent requests

# Retry settings to handle temporary failures (HTTP response codes 500, 502, 503, 504, 408)
RETRY_ENABLED = True
RETRY_TIMES = 3               # Number of retries for failed requests
RETRY_HTTP_CODES = [500, 502, 503, 504, 408]

# Enable and configure HTTP caching (optional, can improve performance if needed)
HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 86400  # Cache expiration time (in seconds)
HTTPCACHE_DIR = 'httpcache'
HTTPCACHE_IGNORE_HTTP_CODES = []   # Ignore caching for specific HTTP response codes
HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# Disable cookies (enable if needed for sessions/authentication)
COOKIES_ENABLED = False

# Enable or disable Telnet console for remote debugging (disabled by default)
TELNETCONSOLE_ENABLED = False

# Enable or disable the DNS cache
DNSCACHE_ENABLED = True

# Reduce log verbosity (options: CRITICAL, ERROR, WARNING, INFO, DEBUG)
LOG_LEVEL = 'INFO'

# Enable or disable compression of stored data (e.g., feeds, storages)
FEED_COMPRESS = 'gzip'

# Enable or disable item pipelines (refer to your custom pipelines)
ITEM_PIPELINES = {
    # 'myproject.pipelines.MyPipeline': 300,
}

# Configure settings for your custom extensions (if any)
EXTENSIONS = {
    'scrapy.extensions.telnet.TelnetConsole': None,
}

# Configure the maximum depth that the Scrapy spider will crawl (optional)
DEPTH_LIMIT = 3

