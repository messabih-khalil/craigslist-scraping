import scrapy

# import items 

from ..items import realstateScraperItem

class RealstateSpider(scrapy.Spider):
    name = 'realState'
    start_urls = ['https://albany.craigslist.org/search/apa']

    def parse(self, response):
        items = realstateScraperItem()
        # get all real state posts
        real_state_posts = response.css('li.result-row')
        # iterate in every post 
        for house in real_state_posts:
                     

       

            
            # real state title
            items['house_title'] = house.css('.result-title::text').extract_first()
            # real state link
            items['house_link'] = house.css('::attr(href)').get()
            # real state price 
            items['house_price'] = house.css('.result-price::text').extract_first()
            # real state published in  
            items['published_in'] = house.xpath('//div/time/@datetime').extract_first()


            yield items