# MLBSearch - Mercado Livre Scrapy Webscraper
This is a Mercado Livre spider for Scrapy, in Python. Therefore, what you see here is my own implementation of Scrapy for my needs. The reason I'm making this public is because other people have published their own works from which I could learn and fix my own bugs also because I was be inspired on them. I hope MLBSearch can help you in some way, feel free to take my spider and modify it to your needs.

## What does it need?

You need [Scrapy](https://scrapy.org/) installed. If you want to use it via command line in PowerShell, for example, as I do, you need to add it to your HOME Path. I installed it using Anaconda as they recommend for Windows users. Obviously you also need Python...

## What does it scrape?

MLB takes for you some of these results:

| Value | Description |
| --- | --- |
| título | The name of the product.|
| preço  | The original price of the product |
| link   | The link that sends you to the product |
 


[preview json file](preview.json)

## What does it do?

The standard flow goes like this:
 
1. Goes to the MLBSearch directory by following the command `cd MLBSEarch`, after that MLB will take the params that you send on the command line `scrapy runspider -o <name-of-json-file>.json -a s=<what-you-want-to-search> spiders/mlbs.py`
Note that in 's=' you should put full names with '-': 'samsung-galaxy-s20' like this.

2. With this parameters, the spider will open a formated link that contains the product that you want to search and take all of products that you want.

3. Finnaly, all this proccess will generate a json file for you that have that infos cited before.

## What to do after?

Whatever you want! In my case I've been used this json file to analises what option it's better to buy and compare prices when I want to sell something.

## FAQ

### F\*, is that spanish?
Nop, It's portuguese, because I'm Brazillian and makes this script to meet my needs, but feel free to modify all the script, and wether possible, share me your modifications, I'll be glad to see that my piece of code helps someone.


### But it's too little information
Yeah, because it's the first version of this, and I intend to update to get more and more improvements as soon as possible

### Bad structure, bad documentation, no good practices...
I know. I'm not a professional programmer, this is my first 'serious' project with python, and it's only one class. It works, it does what I need, and I love it.

## License
Distributed under the MIT License.

## Contact
Send your suggestions or any other message to <jeffersonvargas745@gmail.com>

## Special thanks

@VictorVSa

Thank you by the inspiration of content and as you can see, by the README.md hahaha

Saludos desde @JeffeVargasP