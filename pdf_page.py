from .log import log
from .message import message
from .quran import Quran
from tqdm import tqdm
from fpdf import FPDF
import os


__main_path__ = os.path.dirname(__file__)
file_name     = __file__.split('/')[-1]

def Latin_to_english(text:str):
    Letters ={
        'ā':'a',
        'ḥ':'h',
        'ī':'i',
        'Ā':'A',
        '‘':'',
        '’':'',
        'Ḥ':'H',
        'ṣ':'s',
        'ū':'u',
        'Ṭ':'T',
        'ū':'u',
        'ṭ':'t',
        'Ṣ':'S',
        'ḍ':'d',
        'Ḍ':'D',
    }
    for i in text:
        try:
            text =text.replace(i, Letters[i])
        except KeyError:
            continue
    return text

def add_to_table(From:int, To:int):
    # النتيجة
    results     = []
    # عدم تكرار أسم السورة
    dont_dap    = []
    From        = From
    to          = To
    stop        = False
    quran_pages = Quran().quran_blocks()
    #* التحقق من القيم
    if From and to <= 604 and to >= From and (From and to) != 0:
        for quran_cheak in quran_pages:
            #* تم وضع رينج أو حد يقوم البرنامج بإتباعة
            #? إذا كان رقم الصفحة أكبر من أو يساوي صفحة البداية يتم تنفيذ الأمر
            if quran_cheak['page'] >= From and quran_cheak['page'] <= to :
                #? يتم تفعيل متغير التوقف عند دخول الحد الموضوع
                stop = True
                #? هذا الشرط إذا تحقق سوف يسجل اسم السورة في قائمة؛ وهذا لمنع تكرار القيم
                if not quran_cheak['translation'] in dont_dap:
                    dont_dap.append(quran_cheak['translation'])
                    results.append(quran_cheak)
                #? هذا الشرط يمنع تكرار أرقام الصفحات، وينظر إلى الصفحة الأخيرة والأية الأخيرة في الصفحة
                elif quran_cheak['verses_number'] == quran_cheak['total_verses'] or quran_cheak['page'] == to:
                    try:
                        #? هذا الشرط يتحقق من الأية الأخير في الصفحة الأخير. وذلك عن طريقة التحقق من الصفحة التالية
                        if quran_pages[quran_cheak['ID']]['page'] == to+1:
                            results.append(quran_cheak)
                        #? هذا الشرط يتحقق من الأية الأخيرة في السورة، إلى أن يصل إلى الصفحة الأخير الذي أدخلها المستخدم
                        elif dont_dap[-1] == quran_cheak['translation'] and quran_cheak['verses_number'] == quran_cheak['total_verses']:
                            results.append(quran_cheak)
                        else:
                            continue
                    #? نفس الشروط السابقة داخل هذه الحلقة؛ ولكن المفارقة عندما يظهر لنا هذا الخطأ يتم تنفيذ هذا الشرط
                    except IndexError:
                        if quran_pages[quran_cheak['ID']-1]['page'] == to+1:
                            results.append(quran_cheak)
                        elif dont_dap[-1] == quran_cheak['translation'] and quran_cheak['verses_number'] == quran_cheak['total_verses']:
                            results.append(quran_cheak)
                else:
                    continue
            else:
                #* يتم التوقف عند الإنتهاء من الحد
                if stop: break
    else:
        print("I have exceeded 114 Quranic chapters. Please adhere to the number of Quranic chapters (from 1 to 114)")
    
    table = [["Sura name", "From", "To", "Start Page", "End Page", "Pages"]]
    out  = list()
    for write in range(len(results)//2):
        info = results[write*2:(write+1)*2]
        table.append([
            Latin_to_english(str(info[0]['Transliteration'])),
            str(info[0]['verses_number']),
            str(info[-1]['verses_number']),
            str(info[0]['page']),
            str(info[-1]['page']),
            str((info[-1]['page']-info[0]['page'])+1)]
            )
    SUM=int()
    for p in range(len(table[1:])):
        # if table[1:][p][3] != table[1:][p-1][4] and p != 0 : SUM += int(table[1:][p][-1])
        # elif p == 1 and table[1:][p][3] == table[1:][p-1][4] : SUM += int(table[1:][p][-1])
        # else: continue
        SUM += int(table[1:][p][-1])
    table.append(['', '', '', '', '', str(SUM)])

    return table

class PDF(FPDF):
    def header(self):
        self.image(
            f"{__main_path__}/Logo/AL_Khatma_logo_one.png",
            x= 79.02 , 
            y= 7.38,
            w= 51.97,
            h= 12.92
            )
        self.ln(20)

    def footer(self):
        self.set_y(-15)
        self.set_font("times", "IB", 11) 
        self.cell(0, 10, f"{self.page_no()}/{{nb}}", align="C")
    
    def cover(self ,title:str, TABLE_DATA):
        self.add_page()
        # pdf.cell(0,20,title, ln=True)
        self.ln(h=50)
        self.set_font("Times","B", size=23)
        self.cell(txt=title, h=-10)
        self.set_font("Times", size=16)
        with self.table(borders_layout="SINGLE_TOP_LINE", text_align="CENTER") as table:
            for data_row in TABLE_DATA:
                row = table.row()
                for datum in data_row:
                    row.cell(datum)

class quran_pdf:
    def __init__(self, block=list()):
        #! التحقق من وجود تحديث جديد للمكتبة
        message().cheak_version()
        
        self.quran    = Quran()
        self.block    = block
        self.pic_path = f"{__main_path__}/Pictures"

        log(
            f'{file_name} > quran_pdf | A values', 
            f'block: {self.block}'
            ).write_message()

        if not os.path.exists(path=f"{self.pic_path}/quran_pages"):
            log(
                f'{file_name} > quran_pdf | Create a folder', 
                f'Create a folder which will have high resolution images of the Quran'
                ).write_message()
            os.makedirs(f"{self.pic_path}/quran_pages")
        else:
            pass
        
    def download_pages(self):
        #! التحقق من وجود تحديث جديد للمكتبة
        message().cheak_version()
        log(
            f'{file_name} > download_pages | Download a pages of Quran', 
            f'Download a pages of Quran'
            ).write_message()
        self.quran.page_pic([page for page in range(1, 605)], 'm-madinah_tafsir', self.pic_path, 'quran_pages')

    def creating(self, path_pdf:str, From=int(), to=int(), cover=True, cover_title=str()):
        #! التحقق من وجود تحديث جديد للمكتبة
        message().cheak_version()
        log(
            f'{file_name} > creating | A values for creating', 
            f'path_pdf: {path_pdf}, From: {From}, to: {to}, cover: {cover}, cover_title: {cover_title}'
            ).write_message()
        pdf   = PDF("P", "mm", "A4")
        if self.block == []:
            start_page = From
            end_page   = to
            log(
            f'{file_name} > creating | A values for Start and End page', 
            f'Start page: {start_page}, end page: {end_page}'
            ).write_message()
        else:
            start_page = self.block[0]['page']
            end_page   = self.block[-1]['page']
            log(
            f'{file_name} > creating | A values for Start and End page', 
            f'Start page: {start_page}, end page: {end_page}'
            ).write_message()
        if cover_title == '': cover_title = f'Sura Information(From: {start_page} to: {end_page} Page):'
        else: pass
        if cover:
            pdf.cover(cover_title,
            add_to_table(start_page, end_page)
            )
        #* get total page numbers
        pdf.alias_nb_pages()

        #* Page Break
        pdf.set_auto_page_break(auto=True, margin=15)

        if not os.path.exists(path=path_pdf): os.mkdir(path=path_pdf)
        
        try:
            PDF_name = os.path.abspath(f'{path_pdf}/Quran_from_{start_page}_to_{end_page}.pdf')
            print(f"# Creating PDF file ... [{PDF_name}]")
            for i in tqdm(range(start_page, end_page+1)):
                pdf.add_page()
                pdf.image(f'{__main_path__}/Pictures/quran_pages/{i}.png', w=169.12, h=250.46, x=20.44, y=25.10)
                

            pdf.output(PDF_name)
        except FileNotFoundError:
            print("Opes! We found lost a files. now download all pages of Quran .... ")
            self.download_pages()
