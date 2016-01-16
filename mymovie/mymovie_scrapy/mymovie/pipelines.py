# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from twisted.enterprise import adbapi
from scrapy import log
from scrapy.item import Item
import datetime
import MySQLdb.cursors

class MySQLPipeline(object):
	def __init__(self):
		self.dbpool = adbapi.ConnectionPool('MySQLdb',  
				db = 'mymovie',  
				user = 'root',  
				passwd = '000201',  
				cursorclass = MySQLdb.cursors.DictCursor,  
				charset = 'utf8',
				use_unicode = False  
		)
	
	def process_item(self, item, spider):
		query = self.dbpool.runInteraction(self.conditional_insert, item)
		query.addErrback(self.handle_error)

		#log.msg('Run My Sql ===============', level=log.DEBUG)
		return item

	def conditional_insert(self, tx, item):
		tx.execute("select title from scrapymovie where title = %s", (item['title'],))
		result = tx.fetchone()
		if result:
			#log.msg("Item already stored in db: %s" % item, level=log.DEBUG)
			pass
		else:
			keyArray = []
			paramArray = []
			for key in item.keys():
				keyArray.append(key)
				paramArray.append('%s')

			keyArray.append('UpdateTime')
			paramArray.append('%s')

			itemArray = []
			for key in item.keys():
				itemArray.append(item[key])

			itemArray.append(datetime.datetime.now())

			tx.execute(\
					"insert into scrapymovie (" + ','.join(keyArray) + ")" 
					" values ("+ ','.join(paramArray) + ")",
					itemArray
				)
			#log.msg("Item stored in db: %s" % item, level=log.DEBUG)

	def _getItemValue(self, item):
		if len(item):
			return item[0]
		else:
			return item
			

	def handle_error(self, e):
		log.err(e)

