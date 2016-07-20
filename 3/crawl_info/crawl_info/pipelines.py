# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from monkeylearn import MonkeyLearn

class CrawlInfoPipeline(object):
    def process_item(self, item, spider):
        ml = MonkeyLearn('0623a1da630f29d3ca432714178669a703b0db14')
        module_id = 'cl_roQT9QdZ'
        category_id_1 = 1701638
        category_id_2 = 1701639
        category_id_3 = 1701640

        samples = [
            (item['description'], category_id_3)
            # ('', category_id_2),
            # ('', category_id_3)
        ]
        res = ml.classifiers.upload_samples(module_id, samples)
        return item
