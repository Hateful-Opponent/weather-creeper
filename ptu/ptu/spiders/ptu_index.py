import scrapy
from scrapy import Request
from ptu.items import PtuItem
class PtuIndexSpider(scrapy.Spider):
    name = "ptu_index"
    allowed_domains = ["lishi.tianqi.com"]
    start_urls = ["https://lishi.tianqi.com/putian/202401.html"]


    def start_requests(self):
        for page in range(202401,202413):
            yield Request(url=f'https://lishi.tianqi.com/putian/{page}.html', callback=self.parse)


    def parse(self, response,**kwargs):

        for i in response.xpath('/html/body/div[7]/div[1]'):

            date = response.xpath('.//div[4]/ul/li[1]/ div[1]/text()').get()[:7]

            avange_high_temp  = i.xpath('.//div[3]/ul/li[1]/div[1]/div[1]/text()').get()
            avange_low_temp = i.xpath('.//div[3]/ul/li[1]/div[2]/div[1]/text()').get()

            higgest_temp = i.xpath('.//div[3]/ul/li[2]/div[1]/text()').get()
            lowest_temp = i.xpath('.//div[3]/ul/li[3]/div[1]/text()').get()

            avange_air = i.xpath('.//div[3]/ul/li[4]/div[1]/text()').get()
            best_air = i.xpath('.//div[3]/ul/li[5]/div[1]/text()').get()
            worst_air = i.xpath('.//div[3]/ul/li[6]/div[1]/text()').get()


            item = PtuItem()
            item['date'] = date

            item['avange_high_temp'] = avange_high_temp
            item['avange_low_temp'] = avange_low_temp

            item['higgest_temp'] = higgest_temp
            item['lowest_temp'] = lowest_temp

            item['avange_air'] = avange_air
            item['best_air'] = best_air
            item['worst_air'] = worst_air

            yield item

