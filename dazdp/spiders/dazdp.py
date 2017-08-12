import json
import logging
import random
import uuid
from urllib.parse import urlparse

import scrapy

from dazdp.items import DianpingItem
from dazdp.spiders.exception import ParseNotSupportedError

logger = logging.getLogger('dazdp')


class Dazdp(scrapy.Spider):
    name = "dazdp"
    rotete_user_agent = True

    def __init__(self):
        # start_urls = [
        #     'http://www.dianping.com/search/category/1/10'
        #     # 'http://www.dianping.com/search/category/1/10'
        #     # 'http://www.dianping.com/search/category/1/10/g3243r9'
        #     # 'http://www.dianping.com/search/category/1/10/g109r5938'
        #     #http://www.dianping.com/search/category/7/10/g117
        # ]
        self.location = [
                    'r5', 'r2', 'r6', 'r1', 'r3', 'r4', 'r12', 'r10', 'r7', 'r9', 'r13', 'r8', 'r5937', 'r5938',
                    'r5939', 'r8846', 'r8847', 'c3580', 'r801', 'r802', 'r804', 'r865', 'r860', 'r803', 'r835', 'r812',
                    'r842', 'r846', 'r849', 'r806', 'r808', 'r811', 'r839', 'r854',
                    'r1325', 'r1326', 'r1327', 'r1328', 'r1329', 'r1330', 'r3110', 'r1331', 'r1332', 'r6338', 'r6339', 'r25986',
                    'r26247']

        self.foodtype = ['g101', 'g113', 'g132', 'g112', 'g117', 'g110', 'g116', 'g111', 'g103', 'g114', 'g508', 'g102',
                    'g115', 'g109', 'g106', 'g104', 'g248', 'g3243', 'g251', 'g26481', 'g203', 'g107', 'g105', 'g108',
                    'g215', 'g247', 'g1338', 'g1783', 'g118']

    ## 爬取顺序:
    ## 1. 先爬取基础数据结构 location, foodtype  --> 独立
    ## 2. 根据基础数据组合出要爬取的 url , 即某一地区某菜系的所有商户页面
    ##    2.1  抓取这个页面有多少 分页 数据
    ##    2.2
    def start_requests(self):
        url = 'http://www.dianping.com/search/category/{0}/10/{1}'
        for i in range(1,2501):
            for ft in self.foodtype:
                new_url = url.format(i,ft)
                yield scrapy.Request(new_url,callback=self.parse_list_first)

    def parse_list_first(self, response):
        selector = scrapy.Selector(response)
        #########################################
        ################获取分页#################
        pg = 0
        pages = selector.xpath('//div[@class="page"]/a/@data-ga-page').extract()
        if len(pages) > 0:
            pg = pages[len(pages) - 2]
        pg=int(str(pg))+1
        url = str(response.url)
        for p in range(1,pg):
            ul = url+'p'+str(p)
            yield scrapy.Request(ul,callback=self.parse_list)

    def parse_list(self, response):
        item = DianpingItem()
        location=response.css('a.city.J-city::text').extract_first()
        selector = scrapy.Selector(response)
        div = selector.xpath('//div[@id="shop-all-list"]/ul/li')
        for dd in div:
            shopnames = dd.xpath('div[2]/div[1]/a[1]/h4/text()').extract()
            item['shopname']=shopnames[0]
            print(shopnames[0])

            shopurls = dd.xpath('div[2]/div[1]/a[1]/@href').extract()
            item['shopurl'] = 'http://www.dianping.com'+str(shopurls[0])

            shoplevels = dd.xpath('div[2]/div[2]/span/@title').extract()
            item['shoplevel'] = shoplevels[0]

            commentnums = dd.xpath('div[2]/div[2]/a[1]/b/text()').extract()
            if len(commentnums)>0:
                item['commentnum'] = commentnums[0]
            else:
                item['commentnum'] = '0'

            avgcosts = dd.xpath('div[2]/div[2]/a[2]/b/text()').extract()

            if len(avgcosts) > 0:
                item['avgcost'] = ''.join(avgcosts) # filter(str.isdigit, str(avgcosts[0]))
            else:
                item['avgcost'] = '0'

            tastes = dd.xpath('div[2]/span/span[1]/b/text()').extract()
            if len(tastes) > 0:
                item['taste'] = tastes[0]
            else:
                item['taste'] = '0'

            envis = dd.xpath('div[2]/span/span[2]/b/text()').extract()
            if len(envis) > 0:
                item['envi'] = envis[0]
            else:
                item['envi'] = '0'

            services = dd.xpath('div[2]/span/span[3]/b/text()').extract()
            if len(services) > 0:
                item['service'] = services[0]
            else:
                item['service'] = '0'

            foodtypes = dd.xpath('div[2]/div[3]/a[1]/span/text()').extract()
            item['foodtype'] = foodtypes[0]

            locs = dd.xpath('div[2]/div[3]/a[2]/span/text()').extract()
            item['loc'] = locs[0]

            item['item_name'] = 'shop'
            item['location'] = location
            yield item


