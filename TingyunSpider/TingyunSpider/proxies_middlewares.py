# -*- coding: utf-8 -*-
import base64
import random


class ProxyMiddleware(object):
		def __init__(self):
				#self.proxy_list = settings.get('PROXY_LIST')
				with open('ip_proxy.txt') as f:
						self.proxies = [ip.strip() for ip in f]
		def process_request(self,request,spider):
				request.meta['proxy'] = 'http://{}'.format(random.choice(self.proxies))
				print "now the ip is ",request.meta['proxy'],"#############"
				
				



