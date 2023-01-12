# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyToExcelItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    brand = scrapy.Field()
    name_produk = scrapy.Field()
    image = scrapy.Field()
    discount_price = scrapy.Field()
    discount = scrapy.Field()
    original_price = scrapy.Field()

class HealthgradesItem(scrapy.Item):
    First_Name = scrapy.Field()
    Middle_Name = scrapy.Field()
    Last_Name = scrapy.Field()
    credential = scrapy.Field()
    gender = scrapy.Field()
    accepting_new_patients = scrapy.Field()
    speciality_1 = scrapy.Field()
    speciality_2 = scrapy.Field()
    pratice_name = scrapy.Field()
    education_type = scrapy.Field()
    education_name = scrapy.Field()
    street_address = scrapy.Field()
    city = scrapy.Field()
    state = scrapy.Field()
    zip_code = scrapy.Field()
    phone = scrapy.Field()
    response_count = scrapy.Field()
    average_score = scrapy.Field()
    number_5 = scrapy.Field()
    number_4 = scrapy.Field()
    number_3 = scrapy.Field()
    number_2 = scrapy.Field()
    number_1 = scrapy.Field()
    link = scrapy.Field()