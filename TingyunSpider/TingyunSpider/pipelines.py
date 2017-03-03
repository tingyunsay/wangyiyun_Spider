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


class Count(object):
	def __init__(self):
		self.line = ""
		self.count = 0
		self.flag = 0


class TingyunspiderPipeline(object):
	def __init__(self):
		self.Concert = Count()
		self.Mv = Count()
		self.Artist = Count()
		self.Album = Count()
		self.Music = Count()
		self.Nettv = Count()
		self.Nettv_sp = Count()
		self.Movie = Count()
		self.Tv = Count()
		

	def process_item(self, item, spider):
		if re.search('artist',''.join(item['site_name'])):
				if self.Artist.count < 50:
						self.Artist.line += json.dumps(dict(item),ensure_ascii=False)+"\n"
						self.Artist.count += 1
				else:
						f = codecs.open('all_artist.json','a',encoding="utf-8")
						f.write(self.Artist.line)
						f.close()
						self.Artist.line = ""
						self.Artist.count = 0
		if re.search('music',''.join(item['site_name'])):
				if self.Music.count < 50:
						self.Music.line += json.dumps(dict(item),ensure_ascii=False)+"\n"
						self.Music.count += 1
				else:
						f = codecs.open('all_music.json','a',encoding="utf-8")
						f.write(self.Music.line)
						f.close()
						self.Music.line = ""
						self.Music.count = 0
				




