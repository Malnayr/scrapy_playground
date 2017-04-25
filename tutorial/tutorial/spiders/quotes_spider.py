import scrapy

class QuotesSpider(scrapy.Spider):
    #Used to identify the spider - Can't use the same name for different spiders
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/'
    ]

    #Purpose: Holds page content
    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text' : quote.css('span.text::text').extract_first(),
                'author' : quote.css('small.author::text').extract_first(),
                'tags': quote.css('div.tags a.tag::text').extract()
            }

        # page = response.url.split("/")[-2]
        # filename = 'quotes-%s.html' % page
        # with open(filename, 'wb') as f:
        #     f.write(response.body)

        #Check if there is another page to move to - Previously we had a hardcoded pages in start_urls
        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            #build a full absolute url using urljoin()
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

#Run "scrapy crawl quotes"

#Using Scrappy Shell:
    #Run "scrapy shell 'http://quotes.toscrape.com/page/1/'

#scrapy crawl quotes -o quotes.json
#scrapy crawl quotes -o quotes.jl

