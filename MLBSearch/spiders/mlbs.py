import scrapy

class MlbsSpider(scrapy.Spider):
    name = 'mlbs'
    def start_requests(self):
        yield scrapy.Request(f'https://lista.mercadolivre.com.br/{self.s}')


    def parse(self, response, **kwargs):
        for i in response.xpath('/html/body/main/div/div[3]/section/ol'):
            price = i.xpath('.//div[@class="ui-search-price__second-line"]/span[@class="andes-money-amount ui-search-price__part ui-search-price__part--medium andes-money-amount--cents-superscript"]').getall()
            price = price[1:3]
            price = ''.join(price)
            title = i.xpath(".//h2[@class='ui-search-item__title']//text()").get()
            link = i.xpath('.//div[@class="ui-search-item__group ui-search-item__group--title"]/a/@href').getall()

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