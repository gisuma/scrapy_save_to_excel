import scrapy
import json
import requests
from scrapy import Request
import re
import os.path
from urllib.parse import urljoin
from scrapy_to_excel.items import ScrapyToExcelItem

class excelspider(scrapy.Spider):
	#memberi nama pada spider
	name = 'excel'
	#untuk menyatakan domain yang dapat discraping
	allowed_domain=['https://www.6pm.com']
	start_url = ['https://www.6pm.com/p/calvin-klein-maraselle-black-1/product/9321908/color/125647']
	SLOW_DOWNLOAD_TIMEOUT = 120
	found_entry_ids = []
	found_all_entry_ids = False
	remaining_listings = []

	def start_requests(self):
		for url in self.start_url:
			yield scrapy.Request(url,callback=self.parse)

	def parse(self, response):
		brand = response.xpath('//a[@itemprop="url"]/span/text()').extract_first("")
		name_produk = response.xpath('//span[@itemprop="brand"]/following-sibling::span/text()').extract_first("")
		image = response.xpath('//div[@id="productThumbnails"]//picture/img/@src').extract()
		price = response.xpath('//div[@itemprop="offers"]')
		discount_price = price.xpath('./span/@aria-label').extract_first("")
		discount = price.xpath('./span[2]/span/span/text()').extract_first("")
		original_price = price.xpath('./span[2]/span[2]/span[2]/text()').extract_first("")

		item = ScrapyToExcelItem()
		item["brand"] = brand
		item["name_produk"] = name_produk
		item["image"] = image
		item["discount_price"] = discount_price
		item["discount"] = discount
		item["original_price"] =original_price
		yield item
