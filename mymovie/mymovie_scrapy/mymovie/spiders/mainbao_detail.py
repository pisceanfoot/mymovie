#coding=utf-8
from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from scrapy.http import Request
from scrapy import log
import re

from mymovie.items import MymovieItem
from mymovie.common.httpHelper import getUrl
from mymovie.common.itemHelper import itemValue, getNotEmpryList

class MainbaoDetailSpider(BaseSpider):
	name = "mianbao"
	allowed_domains = ["2tu.cc"]
	start_urls = ["http://www.2tu.cc"]
	homeUrl = 'http://www.2tu.cc'

	def parse(self, response):
		responseSelcter = Selector(response)

		# Home Page: 热播推荐
		movieRequestItems = self.parseHotToday(responseSelcter, '//*[@id="con_ph_1"]/li/a')
		#movieRequestItems2 = self.parseHotToday(responseSelcter, '//*[@id="con_ph_2"]/li/a')
		#movieRequestItems.extend(movieRequestItems2)
#
#		#movieRequestItems2 = self.parseHotToday(responseSelcter, '//*[@id="con_ph_3"]/li/a')
#		#movieRequestItems.extend(movieRequestItems2)
#
#		#movieRequestItems2 = self.parseHotToday(responseSelcter, '//*[@id="con_ph_4"]/li/a')
		#movieRequestItems.extend(movieRequestItems2)
		
		return movieRequestItems;

	def parseHotToday(self, responseSelcter, express):
		# Home Page: 热播推荐
		movieRequestItems = []
		selectedMovieNodeList = responseSelcter.xpath(express);

		for selectedMoveNode in selectedMovieNodeList:
			url = selectedMoveNode.xpath('@href').extract()[0]
			url = getUrl(self.homeUrl, url)

			log.msg('url:{0}'.format(url), level=log.DEBUG)

			requestItem = Request(url, callback=self.parse_detail)
			requestItem.meta['url'] = url

			movieRequestItems.append(requestItem)

		return movieRequestItems

	def parse_detail(self, response):
		responseSelcter = Selector(response)

		# 电影
		tabstore = responseSelcter.xpath('//*[@id="main"]/div/div[1]/div[1]/a[2]/text()').extract()
		# 动作片
		category = responseSelcter.xpath('//*[@id="main"]/div/div[1]/div[1]/a[3]/text()').extract()
		actor = responseSelcter.xpath('//*[@id="playinfo"]/div[2]/div[2]/p[1]/a/text()').extract()
		time = responseSelcter.xpath('//*[@id="playinfo"]/div[2]/div[2]/p[3]/b[2]/text()').extract()
		if(len(time)):
			time = time[0][5:]#上映年代：2013
		image = responseSelcter.xpath('//*[@id="playinfo"]/div[1]/img/@src').extract()

		title = responseSelcter.xpath('//*[@id="main"]/div/div/div[contains(@class, "tit")]/text()').extract()
		title = getNotEmpryList(title)
		title = title[-1:]
		title = title[0][5:]

		area = responseSelcter.xpath('//*[@id="playinfo"]/div[2]/div[2]/p[3]/b[1]/text()').extract()
		area = area[0][3:]
		description = responseSelcter.xpath('//*[@id="main"]/div/div[1]/div[@class="con4"]/div[@class="about_t"]').extract()
		description = re.sub(r'<[^>]*?>', '', str(description))
		description = description[0]

		# 迅雷下载链接
		thunderDownloadAddress = responseSelcter.xpath('//*[@id="main"]/div/div[1]/div[@class="con4"]/script/text()').extract();
		if len(thunderDownloadAddress):
			thunderDownloadAddress = thunderDownloadAddress[0][16:-2]
			thunderDownloadAddress = thunderDownloadAddress.split('###')


		item = MymovieItem()
		item['tabStore'] = itemValue(tabstore)
		item['category'] = itemValue(category)
		item['actor'] = itemValue(actor)
		item['time'] = itemValue(time)
		item['imageUrl'] = itemValue(image)
		item['url'] = itemValue(response.meta['url'])
		item['title'] = itemValue(title)
		item['area'] = itemValue(area)
		item['thunderDownloadAddress'] = itemValue(thunderDownloadAddress)
		item['description'] = ''#itemValue(description)

		item['fromSite'] = '2tc'

		#log.msg("2tu spider: %s" % item, level=log.DEBUG)

		return item;



