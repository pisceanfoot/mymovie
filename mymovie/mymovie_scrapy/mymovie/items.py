# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class MymovieItem(Item):
    # define the fields for your item here like:
    # name = Field()
    tabStore = Field()
    category = Field()
    subCategory = Field()

    area = Field()

    title = Field()
    url = Field()
    actor = Field()
    time = Field()
    imageUrl = Field()

    description = Field()

    downloadAddressType = Field()
    downloadTitle = Field()
    downloadAddress = Field()

    onlineAddressType = Field()
    onlineTitle = Field()
    onlineAddress = Field()

    thunderDownloadAddress = Field()

    reviewAvg = Field()

    fromSite = Field()