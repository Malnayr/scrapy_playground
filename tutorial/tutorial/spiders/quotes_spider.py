import scrapy

class QuotesSpider(scrapy.Spider):
    #Used to identify the spider - Can't use the same name for different spiders
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/'
    ]

    #Do not need this anymore - Since we will be using a shortcut to the start_requests method
    # #Purpose: Return a iterable which the spider will crawl from
    # def start_requests(self):
    #     urls = [
    #         'http://quotes.toscrape.com/page/1/',
    #         'http://quotes.toscrape.com/page/2/'
    #     ]
    #     for url in urls:
    #         #Returns a generator - A iterable/list of items from the current URL
    #         yield scrapy.Request(url=url, callback=self.parse)

    #Purpose: Holds page content
    def parse(self, response):
        page = response.url.split("/")[-2]
        #Make file name
        filename = 'quotes-%s.html' % page
        #Open file to write into
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

#Run "scrapy crawl quotes"

#Using Scrappy Shell:
    #Run "scrapy shell 'http://quotes.toscrape.com/page/1/'

