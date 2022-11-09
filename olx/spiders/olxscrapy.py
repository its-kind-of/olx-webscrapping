import scrapy
#from scrapy.crawler import CrawlerProcess


class OlxscrapySpider(scrapy.Spider):
    name = 'olxscrapy'
    url = 'https://www.olx.in/api/relevance/v2/search?category=1725&facet_limit=100&lang=en-IN&location=1000001&location_facet_limit=20&platform=web-desktop&size=40&user=1837563232ex1edb9129'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0;Win64;x64) AppleWebKit/537.36 (KHTML, likeGecko) Chrome/105.0.0.0 Safari/537.36'
    }

    def parse(self, response, **kwargs):
        yield scrapy.Request(url=self.url + '&page=1', headers=self.headers, callback=self.start_scrapping)

    @staticmethod
    def start_scrapping(response):
        print(response.text)


# run scraper
#process = CrawlerProcess()
#process.crawl(OlxscrapySpider)
#process.start()
