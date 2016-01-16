from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from tutorial.items import TutorialItem


class DmozSpider(BaseSpider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

    def parse(self, response):
        #filename = response.url.split("/")[-2]
        #open(filename, 'wb').write(response.body)
		sel = Selector(response)
		sites = sel.xpath('//ul/li')
		items = []
		
		for site in sites:
			item = TutorialItem()

			title = site.xpath('a/text()').extract()
			link = site.xpath('a/@href').extract()
			desc = site.xpath('text()').extract()

			item['title'] = title
			item['link'] = link
			item['desc'] = desc

			items.append(item)
		
		return items