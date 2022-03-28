import scrapy

class MlbsSpider(scrapy.Spider):
    name = 'mlbs'
    def start_requests(self):
        yield scrapy.Request(f'https://lista.mercadolivre.com.br/{self.s}')


    def parse(self, response, **kwargs):
        for i in response.xpath("//ol[@class='ui-search-layout ui-search-layout--grid']"):
            price = i.xpath('.//div[@class="ui-search-price__second-line"]//span/text()').getall()
            price = price[1:3]
            price = ''.join(price)
            title = i.xpath(".//h2[@class='ui-search-item__title ui-search-item__group__element']//text()").get()
            link = i.xpath('.//div[@class="ui-search-result__image"]/a/@href').getall()

            yield {

                'título': title,
                'preço': price,
                'link': link

            }

        next_page1 = response.xpath('//a[contains(@title,"Próxima")]/@href').get()
        next_page2 = response.xpath("//a[contains(@title, 'Seguinte')]/@href").get()
        if next_page1:
            yield scrapy.Request(url=next_page1, callback=self.parse)
        elif next_page2:
            yield scrapy.Request(url=next_page2, callback=self.parse)