import scrapy
import json
import requests
from scrapy import Request
import re
import os.path
from urllib.parse import urljoin
from scrapy_to_excel.items import HealthgradesItem

class Healthgraderspider(scrapy.Spider):
	#memberi nama pada spider
	name = 'healthgrades'
	#untuk menyatakan domain yang dapat discraping
	allowed_domain=['https://www.healthgrades.com']
	start_url = ['https://www.healthgrades.com/family-practice-directory']
	SLOW_DOWNLOAD_TIMEOUT = 120
	found_entry_ids = []
	found_all_entry_ids = False
	remaining_listings = []

	def start_requests(self):
		for url in self.start_url:
			yield scrapy.Request(url,callback=self.parse)

	def parse(self,response):
		all_url = response.xpath('//ul[@class="directory-container-body__cards"]/div/div/li//a/@href').extract()
		base_url = 'https://www.healthgrades.com'
		for url in all_url:
			real_url = base_url + url
			yield Request(real_url,callback=self.parse_profil)
			break
	def parse_profil(self,response):
		full_name = response.xpath('//div[@class="summary-column"]/h1/text()').extract_first("").replace(',','')
		name = full_name.split(' ')
		print(name)
		if len(name) > 4:
			First_Name = name[1]
			Middle_Name = name[2:-3]
			Last_Name = name[-2]
			credential = name[-1]
		else:
			First_Name = name[1]
			Middle_Name = ' '
			Last_Name = name[-2]
			credential = name[-1]
		gender = response.xpath('//span[@data-qa-target="ProviderDisplayGender"]/text()').extract_first("")
		accept = response.xpath('//div[@data-qa-target="premium-accepting-patients"]/span/text()').extract_first("")
		if accept == 'Accepting new patients':
			accepting_new_patients = 'Yes'
		else:
			accepting_new_patients = 'No'
		speciality = response.xpath('//div[@class="profile-subsection profile-subsection-compressed"][1]/section[@class="about-me-subsection"]/div/ul/li/span/text()').extract()
		if speciality < 4:
			speciality_1 = speciality[0]
			speciality_2 = speciality[1]
		else:
			speciality_1 = speciality[0]
			speciality_2 = ' '
		print(f'speciality_1 :{speciality_1} ')
		print(f'speciality_2 :{speciality_2} ')
