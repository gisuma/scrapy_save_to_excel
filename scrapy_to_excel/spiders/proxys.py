# import scrapy
# import json


# class proxyspider(scrapy.Spider):
# 	name = 'proxys'
# 	allowed_domain = ['https://www.certik.org/']
# 	SLOW_DOWNLOAD_TIMEOUT = 120
# 	start_url = ['https://www.certik.org/_next/data/JZT8zM1UiK3CamolEWX8P/index.json']

# 	def parse(self,response):
# 		x = response.body
# 		print(x)
# 		//div[@style="padding-left:6px;padding-right:6px;display:flex;align-items:center"]/a/@href
# 		