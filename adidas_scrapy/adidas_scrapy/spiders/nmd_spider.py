import scrapy

class NMDSpider(scrapy.Spider):
    #NMD is a type of Adidas sneaker
    name = "nmd"
    start_url = [
        'http://www.adidas.ca/en/nmd-shoes'
    ]

    def parse(self, response):
        for shoe in response.css('div.innercard.col'):
            yield {
                'status': shoe.css('span.badge-text::text').extract_first().strip(),
                'name': shoe.css('span.title::text').extract_first(),
                'image': shoe.css('div.image.plp-image-bg a::attr(href)').extract_first(),
                'price': shoe.css('span.salesprice::text').extract_first()
            }

    #Purpose: Get the colorway of the shoe, since shoes have the same name, the only way to distinguish
    #a unique shoe is from the colorway
    def getcolorway(self, url):
        """
            From parse, scrape for the item page URL and pass it into this function
            This function will go into that url and return the colorway of the shoe
        """