# Scrapy settings for mymovie project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'mymovie'

SPIDER_MODULES = ['mymovie.spiders']
NEWSPIDER_MODULE = 'mymovie.spiders'
ITEM_PIPELINES = ['mymovie.pipelines.MySQLPipeline']
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'mymovie (+http://www.yourdomain.com)'
