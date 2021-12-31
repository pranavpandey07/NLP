import scrapy

reviews_url='https://www.flipkart.com/poco-f1-steel-blue-64-gb/product-reviews/itmf8fyhgyg3aggg?pid=MOBF85V7ZJGSTXGN&lid=LSTMOBF85V7ZJGSTXGNSFZXH2&marketplace=FLIPKART&page={}'
page_num=[str(i) for i in range(1,3019)]
class ReviewsSpider(scrapy.Spider):
    name = 'reviews'

    def start_requests(self):
        for page in page_num :
            url=reviews_url.format(page)
            yield scrapy.Request(url)
        
    

    def parse(self, response):
        for review in response.xpath('//div[@class="_1AtVbE col-12-12"]'):
            item={
                
                'ratings':review.xpath('//div[@class="_3LWZlK _1BLPMq"]/text() ').get(),
                
                'review':review.xpath('//div[@class="t-ZTKy"]//text()').get()
            }
            yield item
