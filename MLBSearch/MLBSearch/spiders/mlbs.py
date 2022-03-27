import scrapy

class MlbsSpider(scrapy.Spider):
    name = 'mlbs'
    def start_requests(self):
        yield scrapy.Request(f'https://lista.mercadolivre.com.br/{self.s}')


    def parse(self, response, **kwargs):
        for i in response.xpath("//div[@class='andes-card andes-card--flat andes-card--default ui-search-result ui-search-result--core andes-card--padding-default']"):
            price = i.xpath('.//div[@class="ui-search-price__second-line"]//span//text()').getall()
            price = price[1:5]
            price = ''.join(price)
            title = i.xpath(".//h2[@class='ui-search-item__title']//text()").get()
            link = i.xpath('.//div[@class="ui-search-result__image"]/a/@href').getall()

            yield {

                'título': title,
                'preço': price,
                'link': link

            }
