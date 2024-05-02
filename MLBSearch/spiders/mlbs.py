import scrapy

class MlbsSpider(scrapy.Spider):
    name = 'mlbs'
    def start_requests(self):
        yield scrapy.Request(f'https://lista.mercadolivre.com.br/{self.s}')

    def parse(self, response, **kwargs):
        for i in response.xpath('/html/body/main/div/div[3]/section/ol'):
            title = i.xpath('.//div[@class="ui-search-item__group ui-search-item__group--title"]/a/h2/text()').getall()
            price = i.xpath('//*/div[2]/div[2]/div[1]/div[1]/div/div/div/span[1]/span[2]/text()').getall()
            link = i.xpath('.//div[@class="ui-search-item__group ui-search-item__group--title"]/a/@href').getall()

            for t, p, l in zip(title, price, link):
                yield {
                    'title': t,
                    'price': f'R$ {p}',
                    'link': l
                }

        next_page1 = response.xpath('//a[contains(@title,"Próxima")]/@href').get()
        next_page2 = response.xpath("//a[contains(@title, 'Seguinte')]/@href").get()
        if next_page1:
            yield scrapy.Request(url=next_page1, callback=self.parse)
        elif next_page2:
            yield scrapy.Request(url=next_page2, callback=self.parse)