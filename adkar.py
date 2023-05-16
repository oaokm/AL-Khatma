from .log import log
from .message import message
from time import perf_counter
import json
import os


__main_path__ = os.path.dirname(__file__)
file_name     = __file__.split('/')[-1]

class Adkar:
    def __init__(self):
        #! التحقق من وجود تحديث جديد للمكتبة
        message().cheak_version()
        self.adkar = json.load(open(f'{__main_path__}/DATA/Adkar/adkar.json', 'r'))

    def show_me_categorys(self):
        #! التحقق من وجود تحديث جديد للمكتبة
        message().cheak_version()
        categorys = list()
        for cheak_title in self.adkar:
            if not cheak_title['category'] in categorys:
                categorys.append(cheak_title['category'])
            else:
                continue
        log(
            f'{file_name} > show_me_categorys | request categorys', 
            f'The user a request all categorys on Databeas'
            ).write_message()
        return categorys
    
    def call_block(self, category:str, report=False):
        #! التحقق من وجود تحديث جديد للمكتبة
        message().cheak_version()
        results = list()
        start   = perf_counter()
        
        #* البحث في قاعدة بيانات الأذكار
        for search in self.adkar:
            #* تطابق عدد الفئة من قاعدة البيانات مع الفئة الذي وضعها المستخدم
            if search['category'] == category:
                results.append(search)
            else:
                continue
        end = perf_counter()
        
        if report: print(f"[REPORT]\nRuning Time: {end-start}\nNumber of Results: {len(results)}\nResults: {json.dumps(results, indent=4, ensure_ascii=False)}")
        log(
            f'{file_name} > call_block | request call block', 
            f'The user a request category: {category}, and report: {report}'
            ).write_message()
        return results
