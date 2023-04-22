import AL_Khatma
from log import log
import json
import requests
import os
from tqdm import tqdm
import urllib3
from time import perf_counter


class Quran:
    def __init__(self, lang='main'):
        """
        Quran(class): 
        lang: اللغة التي تريد عرضها
        """
        try:
            #* قراءة ملف اللغات
            os.chdir(path=AL_Khatma.__main_path__)
            self.quran = json.load(open(f"./DATA/Language/{lang}.json", "r", encoding="utf8"))
            log(
                f'{__file__} > Quran | Status JSON File ', 
                f'Read: True, Language: {lang}'
                ).write_message()
        except FileNotFoundError as e:
            #* في حال طلب المستخدم استعراض اللغات

            if lang == '?':
                log(
                f'{__file__} > Quran | Show All Language ', 
                f'The user has requested to view the available languages of the Quran'
                ).write_message()

                lang = os.listdir(path='./DATA/Language')
                print('the available languages of the Quran'.title())
                for i in range(len(lang)):
                    nameFile = lang[i].split(".")[0]
                    if nameFile == 'main': print(f"[{i}] ar, en ({nameFile})")
                    else: print(f"[{i}] {nameFile}")
            else:
                log(
                f'{__file__} > Quran | Status JSON File ', 
                f'Falus | The user has been entered for an unavailable language'
                ).write_message()
                
                print('[Quran] Sorry, the language is your enter is not available.\nthe available languages of the Quran:')
                
                #// إنتبه: قم بتغير مسار لكي لا تحصل مشاكل
                #// قم بوضع طريقة لقراءة جميع الملفات دون مشاكل عدم معرفه موقعها
                lang = os.listdir(path='./DATA/Language')               
                for i in range(len(lang)):
                    nameFile = lang[i].split(".")[0]
                    if nameFile == 'main': print(f"[{i}] ar, en ({nameFile})")
                    else: print(f"[{i}] {nameFile}")


    def show_block_aya(
            self,
            verses_no:int,
            verses_number:list,
            orderly=False,
            ):
        """
        show_block_aya(func): هي دالة تقوم بإستخراج ما يدرده المستخدم من ملف اللغة
        verses_no(int): أستخراج السروة التي تريدها
        verses_number(list): في حالة أنك ترد صورة بعينها يمكنك ذلك بكتابة رقم أيتها. ويمكن أن تجعلعا فارغة
        orderly(bool): إذا أردت أن ترى النتيجة مطبوعة بشكل يمكن قراءتها
        """
        log(
            "quran.py > Quran > show_block_aya | info",
            f"verses_no: {verses_no}, verses_number: {verses_number}, orderly: {orderly}"
        ).write_message()

        if verses_no <= 114:
            log(
            f"{__file__} > Quran > show_block_aya | number of Surahs of the Qur’an is good",
            f"The number entered did not exceed the number of Surahs of the Qur’an"
            ).write_message()
            #? لتدوين أيات جميع السورة المحددة
            results = list()
            #? تدوين أعداد السورة المطلوبة
            verses = list()
            #* يحدث عملية البحث عن السورة المطلوبة
            for search in range(len(self.quran)):
                #* التأكد من السورة المطلوبة من ترتيبها
                if self.quran[search]['verses_no'] == verses_no:
                    
                    #* تسجيل جميع الأيات السورة في قائمة + تسجيل الأيات المطلوبة في قائمة منفصلة(إن وجد)
                    for i in range(self.quran[search]['total_verses']):
                        results.append(self.quran[search+i])

                        #? هنا تحدث عملية رصد الأيات المطلوبة تزامُنا مع علميلة رصد أيات السورة المطلوبة
                        for cheaking in verses_number:
                            #? التحقق من أن الأية المطلوبة ضمن عدد أيات السورة + التأكد من الأية بعينها لإضافتها في قائمة مخصصة
                            if self.quran[search+i]['total_verses'] >= cheaking and cheaking == self.quran[search+i]['verses_number']:
                                verses.append(self.quran[search+i])
                            else:
                                continue

                    #* طباعة تقرير مُنسق مع إرجاع قينتين للعمليتين السابقتين
                    if orderly:
                        txt = ('results'.upper(), 'verses'.upper())
                        print(f'\n\n\n{txt[0]:.^50}\n\n\n')
                        print(json.dumps(results, indent=4, ensure_ascii=False))
                        print(f'\n\n\n{txt[1]:.^50}\n\n\n')
                        print(json.dumps(verses, indent=4, ensure_ascii=False))
                        
                        return (results, verses)
                    #* إرجاع القيمتين السابقين فقط
                    else: return (results, verses)
                #? هذا في حالة عدم إجاد السورة فإنه يستمر حتى يجد السورة المطلوب
                else: continue
        #? في حالة تجاوز 114 سورة قرأنية يتم رفض الطلب
        else:
            log(
            f"{__file__} > Quran > show_block_aya | Verses Over Error",
            f"I have exceeded 114 Quranic chapters. Please adhere to the number of Quranic chapters (from 1 to 114)."
            ).write_message()
            print('I have exceeded 114 Quranic chapters. Please adhere to the number of Quranic chapters (from 1 to 114).')
            return (False,)


    #* هذا للبحث عن كلمة أو مجموعة كلمات في القرآن
    def searching(
            self, 
            text:str, 
            search_second_lang=False, 
            print_report=False
            ):
        """
        searching(func): هي دالة للبحث بين السطور القرآنية
        text(str): الكلمة المراد بحثها
        search_second_lang(bool): في حال تفعيل هذه الخاصية سيتم البحث بنائا على اللغة الثانية في ملف اللغة
        print_report(bool): في حال تفعيل هذه الخاصية قوم بطباعة تقرير منظم عن نتائج البحث
        """
        log(
            f"{__file__} > Quran > searching | Search Info",
            f"Search: {text}, search_my_lang: {search_second_lang}, print_report: {print_report}"
            ).write_message()
        start = perf_counter()
        #? في حال إذا كان النص فارغ لا يتم تنفيذ الطلب
        if text != '':
            log(
            f"{__file__} > Quran > searching | The Search Status",
            f"True"
            ).write_message()
            end = perf_counter()
            # * يكون جميع النص lower
            text    = text.lower()
            #* لتحزين النتائج
            results = list()
            #? في حال إذا كان خيار search_my_lang مفعل، تقوم خوارزمية للكشف عن نص اللغة الأخرى
            lang    = ['English', 'Bengali', 'Chinese', 'Spanish', 'French', 'Indonesian', 'Russian', 'Swedish', 'Turkish', 'Urdu']
            if search_second_lang:
                try:
                    #* استكشاف اللغة المناسبة من ملف اللغة
                    for LANG in lang:
                        lang_ues    = f'verses_text_{LANG.lower()}'
                        verses_text = self.quran[0][lang_ues]
                        break
                except KeyError:
                    lang_ues = 'verses_text_without_diacritical'

            #* تبدأ هنا عملية البحث
            for i in range(len(self.quran)):
                #? يتم تطبيق هذا الأمر في حالة تفعيل خيار search_my_langsearch_my_lang
                if search_second_lang:
                    verses_text = self.quran[i][lang_ues].lower()
                    search      = verses_text.find(text)
                #? في حال عدم تفعيل search_my_lang فإنهُ يتم تنفيذ الأمر
                else:
                    verses_text = self.quran[i]['verses_text_without_diacritical']
                    search      = verses_text.find(text)
                #* التحقق من عملية البحث
                #? -1 يمثل أن قيمة البحث سلبية، وهذا يعني أن النص المطلوب غير متوفر
                if search != -1:
                    results.append(self.quran[i])
                else:
                    continue
            #* إرجاع قيمة البحث
            end = perf_counter()
            if print_report: print(f"[REPORT]\nRuning Time: {end-start}\nCount Search: {len(results)}\nResult Search: {json.dumps(results, indent=4, ensure_ascii=False)}")
            return results
        
        else:
            log(
            f"{__file__} > Quran > searching | The Search Status",
            f"The search failed; the user has not made any input in search zone or input empty."
            ).write_message()
            end = perf_counter()
            if print_report: print(f"[REPORT]\nRuning Time: {end-start}\nResults Search: {json.dumps(results, indent=4, ensure_ascii=False)}\nThe Number Of Search Results: {len(results)}")
            return (False, )
    

    #? لإرجاع قيمة self.quran
    def quran_blocks(self):
        log(
                f'{__file__} > quran_blocks | Return All The Quran Data ', 
                f'The user return all data quran from json file'
                ).write_message()
        return self.quran
    

    #* تحميل صفحات القرآن الكريم
    def page_pic(
            self,
            page:list,
            type:str,
            path:str, 
            name_folder:str,
            return_imge=False):
        """
        page_pic(func): دالة تقوم على تحميل صفحات القرآن من الإنترنت
        page(list): تقوم بوضع عدد الأيات التي تريد تحميلها
        path(str): المسار تنزيل الصور
        name_folder(str): أسم الملف الذي ستكون فيها الصور الصفحات
        return_imge(bool): في حال تم تفعيل الخيار، سيتم تحميل الصفحات على شكل بايت (Binary)
        """
        #? التحقق من موجود إنترنت
        try:
            requests.get('https://github.com/oaokm')
            log(
            f"{__file__} > Quran > page_pic | Check The Internet Status",
            f"The internet is good"
            ).write_message()

            #* قراءة ملف الذي يحتوي على رابط صفحات القرأن كاملة وبجودة عالية
            quran_books = json.load(open('./DATA/quran_books.json', 'r', encoding='utf8'))
            try:
                log(
                    f"{__file__} > Quran > page_pic | Check For Read JSON File",
                    f"The file (quran_books.json) is good"
                ).write_message()
                
                web_pic = quran_books[type]
            except KeyError as e:
                log(
                    f"{__file__} > Quran > page_pic | Check For Read JSON File",
                    f"Error(keyError): {e}"
                ).write_message()
                print(f'[ Quran > page_pic | KeyError ]: {e}')
            #* في حالة إذا كان خاصية (return_imge) مفعلة يتم تسجيل محتويات الصورة كبِّت(صيغة ثنائية)
            pics = list()
            
            #? هنا تبدأ عملية الوصول للصفحات وتحميلها
            print("# Download Pages From Quran ... ")
            for p in tqdm(page):
                #? التحقق من إذا كان المدخل لا يتخطى عدد صفحات القرأن
                if p <= 604:
                    #* عملية الإتصال بالموقع لسحب الصورة الصفحة
                    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
                    url    = web_pic.format(p)
                    r_page = requests.get(url=url, verify=False)
                    
                    #* عملية إنشاء ملف تمهيدًا لتحميل الصفحات
                    PATH = f'{path}/{name_folder}'
                    #? في حال كان خيار return_imge مفعل فسوف يتم تحميل الصور كبٍّت(النظام الثنائي)
                    if return_imge:
                        pics.append([p, r_page.content])
                    else:
                        #! في حال إذا الملف الذي أدخل المستخدم غير موجود على القرص سيتم تنزيل مباشرًا
                        if not os.path.exists(PATH):
                            os.makedirs(PATH)
                        #* نحميل الصور
                        with open(f"{PATH}/{p}.png", 'wb') as f:
                            f.write(r_page.content)
                            f.close()
                else:
                    print('I have exceeded 604 Page. Please adhere to the number of Page (from 1 to 604).')
            #? في جال إذا خيار return_imge مُفعل، يتم إرجاع قيمتها
            if return_imge:
                return pics
        #? في حال عدم وجود إنترنت يتم رفض الأمر
        except requests.exceptions.ConnectionError as e:
            log(
            f"{__file__} > Quran > page_pic | Check The Internet Status",
            f"The WiFi connection error, please check your internet"
            ).write_message()
            print(f"[ Quran | page_pic > The WiFi connection error ] {e}")

if __name__ == '__main__':
    print('[quran.py] This file is not to run')