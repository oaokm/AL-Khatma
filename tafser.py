from .log import log
from .message import message
import json
import os
from time import perf_counter

__main_path__ = os.path.dirname(__file__)
file_name     = __file__.split('/')[-1]

def show_me_files(mess=str()):
    if mess != "": print(mess)
    books = os.listdir(path=f'{__main_path__}/DATA/Tafser/')
    print(f"The Available Tafser The Quran:")
    for i in range(len(books)):
        nameFile = books[i].split(".")[0]
        print(f"[{i}] {nameFile}")

class tafser:

    def __init__(self, tafser_book:str):
        #! التحقق من وجود تحديث جديد للمكتبة
        message().cheak_version()
        
        try:
            if tafser_book != '?' :
                self.tafser = json.load(open(f'{__main_path__}/DATA/Tafser/{tafser_book}.json', 'r'))
                log(
                f'{file_name} > tafser > tafser_book | Book ', 
                f'The book of tafser is : {tafser_book}'
                ).write_message()
            else:
                log(
                f'{file_name} > tafser > tafser_book | Request books list', 
                f'The user a request book list for tafser'
                ).write_message()
                show_me_files()

        except FileNotFoundError:
            show_me_files(mess="[tafser]: The Books is not available.")
    def call_block(self,
                   sura:int,
                   aya=list(),
                   report=False
                   ):
        #! التحقق من وجود تحديث جديد للمكتبة
        message().cheak_version()
        if sura <= 114 :
            #? تسجيل النتائج
            results = list()
            try:
                start = perf_counter()
                #* البحث في قاعدة بيانات التفسير
                for search in self.tafser:
                    #* تطابق عدد رقم السورة من قاعدة البيانات مع رقم السورة الذي وضعها المستخدم
                    if search['Sura'] == sura and aya == []:
                        results.append(search)
                    #* نفس الشرط السابق، المُفارقة هي طلب أيات محددة
                    elif search['Sura'] == sura and aya != []:
                        #? ترتيب الأرقام
                        aya.sort()
                        #* حلقة البحث عن المتطابقات.
                        for num in range(len(aya)):
                            if search['Sura'] == sura and aya[num] == search['verses_number']:
                                results.append(search)
                            else:
                                continue
                    else:
                        continue
                end = perf_counter()
                if report: print(f"[REPORT]\nRuning Time: {end-start}\nNumber of Results: {len(results)}\nResults: {json.dumps(results, indent=4, ensure_ascii=False)}")
                return results
            except AttributeError as e:
                log(
                f'{file_name} > tafser | Entering ', 
                f'Falus | The user has been entered for an unavailable tafser'
                ).write_message()
                
                show_me_files(mess=f'[{file_name}] Sorry, the tafser is your enter is not available.')

            log(
            f"{file_name} > call_block | Verses Over Error",
            f"I have exceeded 114 Quranic chapters. Please adhere to the number of Quranic chapters (from 1 to 114)."
            ).write_message()
            print('I have exceeded 114 Quranic chapters. Please adhere to the number of Quranic chapters (from 1 to 114).')
            return (False,)

    def all_blocks(self):
        #! التحقق من وجود تحديث جديد للمكتبة
        message().cheak_version()
        log(
            f'{file_name} > all_blocks | request all blocks on Databeas', 
            f'The user a request all blocks on Databeas'
            ).write_message()
        return self.tafser

    def searching(self, text:str, report=False):
        #! التحقق من وجود تحديث جديد للمكتبة
        message().cheak_version()
        if text != '':
            results = list()
            start   = perf_counter()

            for tafserSearch in self.tafser:
                    Tafser_text = tafserSearch['Text_without_diacritical']
                    search      = Tafser_text.find(text)
                    if search != -1:
                        results.append(tafserSearch)
                    else:
                        continue
            end = perf_counter()
            if report: print(f"[REPORT]\nRuning Time: {end-start}\nResults Search: {json.dumps(results, indent=4, ensure_ascii=False)}\nThe Number Of Search Results: {len(results)}")
            return results
        else:
            log(
            f"{file_name} > Quran > searching | The Search Status",
            f"The search failed; the user has not made any input in search zone or input empty."
            ).write_message()
            print("[tafser > searching]: The search failed; the user has not made any input in search zone or input empty.")

