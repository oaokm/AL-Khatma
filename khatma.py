from .quran import Quran
from .message import message
from .log import log
from .pdf_page import quran_pdf
from tqdm import tqdm
from time import perf_counter
import os

__main_path__ = os.path.dirname(__file__)
file_name     = __file__.split('/')[-1]

class khatma:
    def __init__(self, days:int):
        log(
            f"{file_name} > khatma | Status The Class",
            f"True, days(int): {days}"
            ).write_message()
        
        #! التحقق من وجود تحديث جديد للمكتبة
        message().cheak_version()

        self.days       = days
        self.werrd_page = list()
        self.quran      = Quran().quran_blocks()

    #* دالة تقوم على تقسيم صفحات القرآن لهدف إنهاء قراءة القرآن في يوم معين
    def Khatma_page(self, report=False, werrd=False, pdf=False, down_path_pdf=str()):
        """
        Khatma_page(func): هي دالة تقوم بتقسيم صفحات القرآن الكريم بهدف إنهاء قراءتها
        report(bool): في حال تفعيل الخيار يتم طباعة تقرير عن النتائج التي تم تحليلها من هذه الدالة
        werrd(bool): في حال تفعيل الخيار تتم عملية تقسيم القرآن بناءًا على عدد الأيام الذي أدخلها المستخدم. في حال عدم تفعيل هذا الخيار يقوم البرنامج بإعادة قيمة عدد الصفحات اليومية الازمة لإنهاء قراءة القرآن كاملة
        pdf(bool): في حال تفعيل هذا الخيار، سيتم تطبيق التقسيم وإنشاء ملفات بي دي أف للقرأن
        dwon_path_pdf(str): مسار تنزيل ملفات البي دي أف
        """
        #! التحقق من وجود تحديث جديد للمكتبة
        message().cheak_version()
        log(
            f"{file_name} > khatma > Khatma_page | Info",
            f"Days:{self.days}, report: {report}, werrd: {werrd}"
            ).write_message()
        #* عدد صفحات القرآن الكريم حسب نسخة مجمع الملك فهد لطباعة المصحف الشريف
        pages            = 604
        #* الأيام التي نريد ختم القرآن به
        Fdays            = self.days
        Fdays_pages      = list()
        #* بأستخدام الخوارزمية الجشعة لتقسيم صفحات القرأن الكريم
        deno             = [int(pages/Fdays), 2, 1]
        for day in deno:
            while day <= pages:
                Fdays_pages.append(day)
                pages -= day
            else:
                continue
        #* التحقق من أن عدد العناصر في Fdays_pages أكبر من عدد الأيام المدخلة
        if len(Fdays_pages) > self.days:
            #? هنا يقوم بعمل مُوازنة لعدد العناصر مع عدد الأيام في حال إذا كان عدد العناصر أكبر من عدد الأيام
            rest               = Fdays_pages[-(len(Fdays_pages) - Fdays):]
            Fdays_pages_N      = Fdays_pages[:-(len(Fdays_pages) - Fdays)]
            #? تحدث هنا عملية الموازنة لكي تصبح متساوية مع عدد الأيام المدخلة
            for i in range(len(rest)):
                Fdays_pages_N[i] += rest[i]
            report_pages_N = f"[REPORT KHATMA]\nDays: {self.days}\nReading Rate: {int(sum(Fdays_pages_N)/len(Fdays_pages_N))} (Page/Day)\nWeerd: {Fdays_pages_N}"
            #? التحقق من أن مجموع الصفحات المقسمة تساوي عدد صفحات القرآن الكريم
            if sum(Fdays_pages_N) == 604:
                self.werrd_page = Fdays_pages_N
                #* في حالة طلب المستخدم عدم تفعيل التقسيم على القرآن يتم تنفيذ هذه العملية
                if werrd or pdf == False:
                    if report: print(report_pages_N)
                    return Fdays_pages_N
            #! في حال وجود مشكلة يتم تنفيذ هذا الأمر، وهي مشكلة في عملية الموازنة
            else:
                log(
                f"{file_name} > khatma > Khatma_page | Partition Error ",
                f"An error has occurred that is not supposed to happen. Value: len(Fdays_pages) > self.days: {len(Fdays_pages) > self.days}, len(Fdays_pages):{len(Fdays_pages)}, Fdays_pages: {Fdays_pages}, days: {self.days}"
                ).write_message()
                print("[ khatma > Khatma_page | Partition Error ] An error has occurred that is not supposed to happen, Visit the library's Issues page: https://github.com/oaokm/AL-Khatma/issues")
        #* إذا كانت عملية التقسيم تساوية مع عدد الأيام يتم تنفيذ هذا الأمر مباشرًا
        else:
            report = f"[REPORT KHATMA]\nDays: {self.days}\nReading Rate: {int(sum(Fdays_pages)/len(Fdays_pages))} (Page/Day)\nWeerd: {Fdays_pages}"
            #? التحقق من أن مجموع الصفحات المقسمة تساوي عدد صفحات القرآن الكريم
            if sum(Fdays_pages) == 604:
                self.werrd_page = Fdays_pages
                if werrd or pdf == False:
                    if report: print(report)
                    return Fdays_pages
            else: 
                if werrd or pdf == False:
                    if report: print(report)
                    return Fdays_pages

        #* في حال تفعيل هذا الخيار، تبدأ عملية تقسيم القرآن الكريم على عدد الأيام المدخلة
        if werrd:
            """
            [تعريف المتغيرات]
            0. page_per_day(list): يكون عدد العناصر في هذا المتغير مساوي لعدد الأيام المدخلة، وكل عنصر يحتوي على عدد الأيات التي يجب قرأتها
            1. for_day(list): يتم تسجيل معلومات الأيات لكي تم لاحقًا إلى متغير page_per_day
            2. stop_id(int): هذا المتغير يساعد في عملية التقسيم، ووضيفته هو معرفة مُعرف الأية الكريمة لتتم عملية التقسيم بسهولة
            """
            page_per_day = list()
            for_day      = list()
            stop_id      = int() # int() = 0
            
            #* تبدا هنا عملية التقسيم
            print("The process of dividing the Quranic verses begins ... ")
            for i in tqdm(range(1, len(self.werrd_page)+1)):
                #? يأخذ quran قيمة self.quran مع آخر مُعرف تم التوقف عنه
                for quran in self.quran[stop_id:]:
                    for_day.append(quran)
                    #? في حال أن عدد الأيات أكبر من مجموع الأيات الموجودة في قائمة التقسيم يتم تنفيذ العملية
                    if quran['page'] > sum(self.werrd_page[:i]):
                        #* تسجيل آخر مُعرف 
                        stop_id = quran['ID']
                        #* تدوين الأيات إلى page_per_day + تصقير for_day + الإزاحة من عملية التكرار
                        page_per_day.append(for_day)
                        for_day = []
                        break
                    else:
                        continue
                #* تسجيل آخر قيمة (اليوم الأخير)
                if len(page_per_day) == len(self.werrd_page)-1:
                    page_per_day.append(self.quran[stop_id:])
                else:
                    continue
            report = f"[REPORT KHATMA]\nDays: {self.days}\nReading Rate: {int(sum(self.werrd_page)/len(self.werrd_page))} (Page/Day)\nWeerd: {self.werrd_page}\nNumber of Werrd: {len(page_per_day)}"
            if report: print(report)
            log(
                f"{file_name} > khatma > Khatma_page > (werrd) | Status",
                f"True"
                ).write_message()
            #* إرجاع قيمة العملية
            return page_per_day

        #* تطبيق التقسيم مباشرًأ على pdf
        elif pdf and down_path_pdf != '':
            last_value = 1
            pdf        = quran_pdf()
            start      = perf_counter()
            for day in range(len(self.werrd_page)):
                print(f"# {day+1} of {self.days}\tFrom {last_value} -> {self.werrd_page[day]+last_value-1} Page")
                pdf.creating('./weerds',
                            From=last_value, to=self.werrd_page[day]+last_value-1, 
                            cover=True, 
                            cover_title=f'Number of Weerd: {day+1} of {self.days} Days')
                last_value += self.werrd_page[day]
            end    = perf_counter()
            report = f"\n[REPORT KHATMA - PDF]\nRuning Time: {end-start}\nDays: {self.days}\nReading Rate: {int(sum(self.werrd_page)/len(self.werrd_page))} (Page/Day)\nWeerd: {self.werrd_page}\nNumber of Werrd: {len(self.werrd_page)}\nPath: {os.path.abspath(down_path_pdf)}"
            if report: print(report) 
        elif down_path_pdf == '':print("[Khatma | PDF] The option (down_path_pdf) is False, Please change to True, like this:\n\n\tkhatma(30).Khatma_page(pdf=True, dwon_path_pdf='./weerds', report=True)\n\n")

        else: pass
