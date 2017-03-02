# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs
import twisted
from scrapy import log
from scrapy.exceptions import DropItem
from pybloomfilter import BloomFilter
from scrapy.exceptions import CloseSpider
import re
import time
import os
from twisted.enterprise import adbapi
import MySQLdb.cursors


class TingyunspiderPipeline(object):
	def __init__(self):
		self.num_music = 0
		self.num_artist = 0
		self.artist = ""
		self.music = ""

	def process_item(self, item, spider):
		if re.search('artist',''.join(item['site_name'])):
				while self.num_artist < 100:
						self.artist += json.dumps(dict(item),ensure_ascii=False)+"\n"
						self.num_artist += 1
				f = codecs.open('all_artist.json','a',encoding="utf-8")
				f.write(self.artist)
				f.close()
				self.artist = ""
				self.num_artist = 0
		if re.search('music',''.join(item['site_name'])):
				while self.num_music < 100:
						self.music += json.dumps(dict(item),ensure_ascii=False)+"\n"
						self.num_music += 1
				self.music = ""
				self.num_music = 0
				self.file = codecs.open('all_music.json','a',encoding="utf-8")
				self.file.write(self.artist)
