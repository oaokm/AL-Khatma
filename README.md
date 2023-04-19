<p align="center">
  <img src="https://raw.githubusercontent.com/oaokm/AL-Khatma/main/Logo/AL_Khatma_logo_one.png" alt="AL-Khatma Logo For Arabic and English">
</p>

<p align="center">
  <a href="https://github.com/oaokm/AL-Khatma/blob/main/README.md">Arabic</a>
  &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="https://github.com/oaokm/AL-Khatma/blob/main/README_EN.md">English</a>
</p>

<p align="center">
  <a href="#فكرة_الختمة">فكرة الختمة</a>
  &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#تحميل_المكتبة">تحميل المكتبة</a>
  &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#التعامل_مع_المكتبة">التعامل مع المكتبة</a>
  &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#المصادر">المصادر</a>
  &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#الترخيص">الترخيص</a>
  &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="https://github.com/oaokm/AL-Khatma/UPDATE.md">التحديثات</a>
</p>

![GitHub](https://img.shields.io/github/license/oaokm/AL-Khatma) | ![](https://img.shields.io/badge/Programing%20Language-Python_3_and_top-orange)
--| --|


## **بيان**
في يوم الثالث من أبريل من عام 2023 الموافق الثاني عشر من رمضان لعام 1444 هـ في هذا اليوم بدأت الفكرة وبعدها قمت بتطبيق الفكرة وبناء أول API لي.

وفي اليوم التاسع عشر من أبريل من عام 2023 الموافق الثامن والعشرون من رمضان لعام 1444 هـ وبتوفيق من الله لقد أنهيت النسخة الأولى من هذا المشروع ولله الحمد.
وأشكر أخي وأختي اللذانِ دعمني وحفزاني لأتمّ هذا المشروع ❤️


## فكرة_الختمة
**الختمة** هو مشروع مفتوح المصدر تم بناءه لتوحيد المتعلقات المتعلقة بالديانة الإسلامية (كالقرأن الكريم، والأحاديث الشريفة ، والتفسير، والأدعية، وغيرها) في مكان واحد.
وتتمتع المكتبة بعدّة حزمّ، وأهمها:

* **حزمة القرأن الكريم**:.
  * استخراج جميع الأيات القرآنية وكاقة معلوماتها.
  * إمكانية البحث عن الأيات الكريمة.
  * إمكانية تحميل صور صفحات القرآن الكريم.
  * المكتبة مزودة بعدّة لغات. ومنها:
    * اللغة الإنجليزية
    * اللغة الصينية
    * اللغة التركية
    * اللغة الروسية
    * اللغة السويدية
    * اللغة الأردية
    * اللغة الفرنسية
    * اللغة الإسبانية
    * اللغة الإندنسية
    * اللغة الهندية
* **حزمة تختيم القرآن الكريم**.
  * كتابة عدد أيام التختيم، وإعطاء الخطة المناسبة لذلك بالتفاصيل

وهناك حزم إضافية يتم العمل عليها كـ:
* حزمة الأذكار
* حزمة التفسير القرآني

يثتم الإعلان عنها في الإصدارات القادمة -إن شاء الله-

## **تحميل_المكتبة**

### التحميل عن طريق **Github**
**الطريقة الأولى**: عن طريق سطر الأوامر:

* إنشاء ملف بأسم **`AL_Khatma`**
* افتح سطر الأوامر وأكتب هذا الأمر:

```sh
S git clone https://github.com/oaokm/AL-Khatma
```

**الطريقة الثانية**: تحميلها من المتصفح بصيغة ملف مضعوط `.zip`


### التحميل عن طريق **pypi**

```sh
$ pip install AL-Khatma
```
**أو**
```sh
$ pip3 install AL-Khatma
```

## **التعامل_مع_المكتبة**

حاليا هنالك حزمتين، وهي:

* حزمة القرآن الكريم
* حزمة تختيم القرآن الكريم

### **طباعة إصدار المكتبة**
لطباعة إصدار المكتبة يجب عليك أستدعاء المكتبة كما هو موضح:
```py
>>> import AL_Khatma
>>> AL_Khatma.__version__
'1.0.0'
```
### **طريقة أستخراج السور القرآنية الكريمة**
الأمر الذي يقوم بأستخراج محتوى القرآن الكريم هو `Quran().show_block_aya`. وهذا الأمر يقوم بإرجاع لك قيمة على شكل متغير القائمة(list) وتكون دائما عدد العناصر في القائمة مساوية لعدد الأيات الكريمة للسورة التي أستدعيتها.

```py
Quran.show_block_aya(
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
```

  > **مثلا للتوضيح**: فمثلا سورة الفاتحة عدد أياتها 7 مع البسملة فإن البرنامج سيعيد لك 7 عناصر داخل القائمة.

وكل عنصر يحتوي على معلومات للأية على شكل متغير القاموس (dict) ويكون شكله كالتالي:

```json
// Form JSON File 'main.json' (Arabic + English) //
{
        "ID": 1,
        "Name": "الفَاتِحة",
        "Transliteration": "Al-Fātiḥah",
        "translation": "The Opener",
        "type": "meccan",
        "total_verses": 7,
        "verses_no": 1,
        "jozz": 1,
        "page": 1,
        "verses_number": 1,
        "line_start": 2,
        "line_end": 2,
        "verses_text": "بِسۡمِ ٱللَّهِ ٱلرَّحۡمَٰنِ ٱلرَّحِيمِ",
        "verses_text_without_diacritical": "بسم الله الرحمن الرحيم",
        "verses_text_english": "In the name of Allah, the Entirely Merciful, the Especially Merciful",
        "verses_text_transliteration": "Bismi Allahi alrrahmani alrraheemi"
}
```
العنصر | تعريف
----- | ------
`ID`  |  مُعرف الخاص للأية الكريمة
`Name`|  أسم السورة الكريمة
`Transliteration`|  السورة الكريمة بلغات أخرى
`translation`| حرفي/تهجأ أسم اللسورة الكريمة لغير العرب
`type`|  نوع السورة الكريمة، إمّا مّكيِّة أو مدنيّة
`total_verses`|  إجمالي عدد أيات في السورة الكريمة
`verses_no`|  يوضج لك ترتيب السورة بين السور، بناءًا على نسخة القرآن الكريم لمجمع الملك فهد لطباعة المصحف الشريف
`jozz`|  يوضح لك مكان الأية الكريمة بالنسبة للجزء
`page`|  يوضح لك مكان الأية الكريمة بالنسبة للصفحة
`verses_number`|  يوضح لك موقع الأية الكريمة في السورة
`line_start`| يوضح لك موقع الأية بالنسبة لمكان ظهوره في بداية السطر(بناءًا على نسخة القرآن الكريم لمجمع الملك فهد لطباعة المصحف الشريف)
`line_end`| يوضح لك موقع الأية الكريمة بالنسبة لمكان ظهوره في نهاية السطر (بناءًا على نسخة القرآن الكريم لمجمع الملك فهد لطباعة المصحف الشريف)
`verses_text`| نص الأية الكريمة مع التشكيل
`verses_text_without_diacritical`| نص الأية الكريمة بدون التشكيل
`verses_text_english`| نص الأية الكريمة باللغات آخرى
`verses_text_transliteration`| حرفي/تهجأ الأية الكريمة لغير العرب



#### **الطريقة الأولى**: أستخراج الأيات من السورة فقط:

هناك عدّة طرق لكتابة أمر `show_block_aya`:

```py
>>> from AL_Khatma.quran import Quran # تقوم هنا بأستدعاء المكتبة
>>> quran = Quran() # أستدعاء للكائن
>>> sura  = quran.show_block_aya(1, []) # أمر أستدعاء السورة بناءًا على ترتيبها في الفهرس مع كافة أياتها ومعلوماتها
>>> sura
([{'ID': 1, 'Name': 'الفَاتِحة', 'Transliteration': 'Al-Fātiḥah', 'translation': 'The Opener', 'type': 'meccan', 'total_verses': 7, 'verses_no': 1, 'jozz': 1, 'page': 1, 'verses_number': 1, 'line_start': 2, 'line_end': 2, 'verses_text': 'بِسۡمِ ٱللَّهِ ٱلرَّحۡمَٰنِ ٱلرَّحِيمِ', 'verses_text_without_diacritical': 'بسم الله الرحمن الرحيم', 'verses_text_english': 'In the name of Allah, the Entirely Merciful, the Especially Merciful', 'verses_text_transliteration': 'Bismi Allahi alrrahmani alrraheemi'}, {'ID': 2, 'Name': 'الفَاتِحة', 'Transliteration': 'Al-Fātiḥah', 'translation': 'The Opener', 'type': 'meccan', 'total_verses': 7, 'verses_no': 1, 'jozz': 1, 'page': 1, 'verses_number': 2, 'line_start': 3, 'line_end': 3, 'verses_text': 'ٱلۡحَمۡدُ لِلَّهِ رَبِّ ٱلۡعَٰلَمِينَ', 'verses_text_without_diacritical': 'الحمد لله رب العالمين', 'verses_text_english': '[All] praise is [due] to Allah, Lord of the worlds', 'verses_text_transliteration': 'Alhamdu lillahi rabbi alAAalameena'}, {'ID': 3, 'Name': 'الفَاتِحة', 'Transliteration': 'Al-Fātiḥah', 'translation': 'The Opener', 'type': 'meccan', 'total_verses': 7, 'verses_no': 1, 'jozz': 1, 'page': 1, 'verses_number': 3, 'line_start': 4, 'line_end': 4, 'verses_text': 'ٱلرَّحۡمَٰنِ ٱلرَّحِيمِ', 'verses_text_without_diacritical': 'الرحمن الرحيم', 'verses_text_english': 'The Entirely Merciful, the Especially Merciful', 'verses_text_transliteration': 'Alrrahmani alrraheemi'}, {'ID': 4, 'Name': 'الفَاتِحة', 'Transliteration': 'Al-Fātiḥah', 'translation': 'The Opener', 'type': 'meccan', 'total_verses': 7, 'verses_no': 1, 'jozz': 1, 'page': 1, 'verses_number': 4, 'line_start': 4, 'line_end': 4, 'verses_text': 'مَٰلِكِ يَوۡمِ ٱلدِّينِ', 'verses_text_without_diacritical': 'مالك يوم الدين', 'verses_text_english': 'Sovereign of the Day of Recompense', 'verses_text_transliteration': 'Maliki yawmi alddeeni'}, {'ID': 5, 'Name': 'الفَاتِحة', 'Transliteration': 'Al-Fātiḥah', 'translation': 'The Opener', 'type': 'meccan', 'total_verses': 7, 'verses_no': 1, 'jozz': 1, 'page': 1, 'verses_number': 5, 'line_start': 5, 'line_end': 5, 'verses_text': 'إِيَّاكَ نَعۡبُدُ وَإِيَّاكَ نَسۡتَعِينُ', 'verses_text_without_diacritical': 'إياك نعبد وإياك نستعين', 'verses_text_english': 'It is You we worship and You we ask for help', 'verses_text_transliteration': 'Iyyaka naAAbudu waiyyaka nastaAAeenu'}, {'ID': 6, 'Name': 'الفَاتِحة', 'Transliteration': 'Al-Fātiḥah', 'translation': 'The Opener', 'type': 'meccan', 'total_verses': 7, 'verses_no': 1, 'jozz': 1, 'page': 1, 'verses_number': 6, 'line_start': 5, 'line_end': 6, 'verses_text': 'ٱهۡدِنَا ٱلصِّرَٰطَ ٱلۡمُسۡتَقِيمَ', 'verses_text_without_diacritical': 'اهدنا الصراط المستقيم', 'verses_text_english': 'Guide us to the straight path', 'verses_text_transliteration': 'Ihdina alssirata almustaqeema'}, {'ID': 7, 'Name': 'الفَاتِحة', 'Transliteration': 'Al-Fātiḥah', 'translation': 'The Opener', 'type': 'meccan', 'total_verses': 7, 'verses_no': 1, 'jozz': 1, 'page': 1, 'verses_number': 7, 'line_start': 6, 'line_end': 8, 'verses_text': 'صِرَٰطَ ٱلَّذِينَ أَنۡعَمۡتَ عَلَيۡهِمۡ غَيۡرِ ٱلۡمَغۡضُوبِ عَلَيۡهِمۡ وَلَا ٱلضَّآلِّينَ', 'verses_text_without_diacritical': 'صراط الذين أنعمت عليهم غير المغضوب عليهم ولا الضالين', 'verses_text_english': 'The path of those upon whom You have bestowed favor, not of those who have evoked [Your] anger or of those who are astray', 'verses_text_transliteration': 'Sirata allatheena anAAamta AAalayhim ghayri almaghdoobi AAalayhim wala alddalleena'}], [])
```
لتحديد أية بعينها تقوم بالتالي:

```py
>>> len(sura) # عدد العناصر المرجعة من أمر `quran.show_block_aya`
2
>>> sura[0][0] # طباعة معلومات الأية المحددة
{'ID': 1, 'Name': 'الفَاتِحة', 'Transliteration': 'Al-Fātiḥah', 'translation': 'The Opener', 'type': 'meccan', 'total_verses': 7, 'verses_no': 1, 'jozz': 1, 'page': 1, 'verses_number': 1, 'line_start': 2, 'line_end': 2, 'verses_text': 'بِسۡمِ ٱللَّهِ ٱلرَّحۡمَٰنِ ٱلرَّحِيمِ', 'verses_text_without_diacritical': 'بسم الله الرحمن الرحيم', 'verses_text_english': 'In the name of Allah, the Entirely Merciful, the Especially Merciful', 'verses_text_transliteration': 'Bismi Allahi alrrahmani alrraheemi'}
>>> sura[0][0]['verses_text_without_diacritical'] # طباعة شيء محدد من القاموس
'بسم الله الرحمن الرحيم'
```

#### **الطريقة الثانية**: أستخراج أيات محددة في السورة:
> **الملاحظة الأولى**: يمكنك وضع أكثر من أية، بشرط ألا تتعدى مجموع عدد الأيات في السورة؛ لأن البرنامج سيقوم بإرجاع لا شيء لقيمتك التي وضعتها.

> **الملاحظة الثانية**: يمكنك إهمال ترتيب الأيات(في متغير القائمة) ، ولكن حبذا أن يكون مرتبًا.

```py
>>> from AL_Khatma.quran import Quran # تقوم هنا بأستدعاء المكتبة
>>> quran = Quran() # أستدعاء للكائن
>>> sura  = quran.show_block_aya(1, [6, 7]) # نقوم هنا بأستدعاء السورة مع تحديد أيات التي نريدها
>>> sura[1] # قم بتحديد العنصر المخصص للأيات المخصصة
[{'ID': 6, 'Name': 'الفَاتِحة', 'Transliteration': 'Al-Fātiḥah', 'translation': 'The Opener', 'type': 'meccan', 'total_verses': 7, 'verses_no': 1, 'jozz': 1, 'page': 1, 'verses_number': 6, 'line_start': 5, 'line_end': 6, 'verses_text': 'ٱهۡدِنَا ٱلصِّرَٰطَ ٱلۡمُسۡتَقِيمَ', 'verses_text_without_diacritical': 'اهدنا الصراط المستقيم', 'verses_text_english': 'Guide us to the straight path', 'verses_text_transliteration': 'Ihdina alssirata almustaqeema'}, {'ID': 7, 'Name': 'الفَاتِحة', 'Transliteration': 'Al-Fātiḥah', 'translation': 'The Opener', 'type': 'meccan', 'total_verses': 7, 'verses_no': 1, 'jozz': 1, 'page': 1, 'verses_number': 7, 'line_start': 6, 'line_end': 8, 'verses_text': 'صِرَٰطَ ٱلَّذِينَ أَنۡعَمۡتَ عَلَيۡهِمۡ غَيۡرِ ٱلۡمَغۡضُوبِ عَلَيۡهِمۡ وَلَا ٱلضَّآلِّينَ', 'verses_text_without_diacritical': 'صراط الذين أنعمت عليهم غير المغضوب عليهم ولا الضالين', 'verses_text_english': 'The path of those upon whom You have bestowed favor, not of those who have evoked [Your] anger or of those who are astray', 'verses_text_transliteration': 'Sirata allatheena anAAamta AAalayhim ghayri almaghdoobi AAalayhim wala alddalleena'}]
>>> len(sura[1]) # معرفة عدد الأيات التي طلبنا تحديدها
2
```

### **التغير إلى لغات أُخرى**
توفر لك مكتبة الختمة عدد جيد من اللغات الأجنبية. ولمعرفة اللغات المتوفرة في المكتبة يمكنك كتابة الأمر التالي:

> **ملاحظة**: عند إستدعاء الكائن "Quran" فهو تلقائيًا يختار ملف الذي يحتوي على اللغتين العربية والإنجليزية. فلا داعي أن تحدد إذا أردت هذان اللغتين.

```py
>>> from AL_Khatma.quran import Quran
>>> quran = Quran(lang='?')
The Available Languages Of The Quran
[0] fr
[1] es
[2] tr
[3] ru
[4] bn
[5] zh
[6] id
[7] ar, en (main)
[8] sv
[9] ur
```
ترميز/رمز اللغة | اللغة
----- | ---------------
 ar   | اللغة العربية
 en   | اللغة الإنجليزية
 fr   | اللغة الفرنسية
 es   | اللغة الإسبانية
 tr   | اللغة التركية
 ru   | اللغة الروسية
 bn   | اللغة البنغالية
 zh   | اللغة الصينية
 id   | اللغة الإندنوسية
 sv   | اللغة السويدية
 ur   | اللغة الأردية

بعد معرفتنا باللغات المتوفرة ورموزها، نقوم بتعديل أمر `Quran(lang=[ترميز/رمز اللغة])`

```py
>>> from AL_Khatma.quran import Quran
>>> quran = Quran(lang='zh') # نقوم بوضع رمز اللغة الصينية كمثال
>>> sura  = quran.show_block_aya(1, []) 
>>> sura[0][0]  # قمّت بتحديد أول أية من سورة الفاتحة
{'ID': 1, 'Name': 'الفَاتِحة', 'Transliteration': 'Al-Fātiḥah', 'translation': '开端章', 'type': 'meccan', 'total_verses': 7, 'verses_no': 1, 'jozz': 1, 'page': 1, 'verses_number': 1, 'line_start': 2, 'line_end': 2, 'verses_text': 'بِسۡمِ ٱللَّهِ ٱلرَّحۡمَٰنِ ٱلرَّحِيمِ', 'verses_text_without_diacritical': 'بسم الله الرحمن الرحيم', 'verses_text_chinese': '奉至仁至慈的安拉之名', 'verses_text_transliteration': 'Bismi Allahi alrrahmani alrraheemi'}
```

### البحث في الأيات الكريمة
من مزايا حزمة القرآن الكريم ميزة البحث، بأستخدام أمر `Quran.searching()` 

```py
Quran.searching(
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
```

لنقوم بعملية البحث، قوم بأستدعاء الكائن "Quran" ونستدعي الدالة البحث كما هو موضح :

```py
>>> from AL_Khatma.quran import Quran
>>> quran = Quran()
>>> quran.searching('بسم الله الرحمن الرحيم')
[{'ID': 1, 'Name': 'الفَاتِحة', 'Transliteration': 'Al-Fātiḥah', 'translation': 'The Opener', 'type': 'meccan', 'total_verses': 7, 'verses_no': 1, 'jozz': 1, 'page': 1, 'verses_number': 1, 'line_start': 2, 'line_end': 2, 'verses_text': 'بِسۡمِ ٱللَّهِ ٱلرَّحۡمَٰنِ ٱلرَّحِيمِ', 'verses_text_without_diacritical': 'بسم الله الرحمن الرحيم', 'verses_text_english': 'In the name of Allah, the Entirely Merciful, the Especially Merciful', 'verses_text_transliteration': 'Bismi Allahi alrrahmani alrraheemi'}, {'ID': 3189, 'Name': 'النَّمل', 'Transliteration': 'An-Naml', 'translation': 'The Ant', 'type': 'meccan', 'total_verses': 93, 'verses_no': 27, 'jozz': 19, 'page': 379, 'verses_number': 30, 'line_start': 9, 'line_end': 10, 'verses_text': 'إِنَّهُۥ مِن سُلَيۡمَٰنَ وَإِنَّهُۥ بِسۡمِ ٱللَّهِ ٱلرَّحۡمَٰنِ ٱلرَّحِيمِ', 'verses_text_without_diacritical': 'إنه من سليمان وإنه بسم الله الرحمن الرحيم', 'verses_text_english': "Indeed, it is from Solomon, and indeed, it reads: 'In the name of Allah, the Entirely Merciful, the Especially Merciful", 'verses_text_transliteration': 'Innahu min sulaymana wainnahu bismi Allahi alrrahmani alrraheemi'}]
```

يمكنك طباعة تقرير بسيط، والتقرير يعطيك الزمن الذي قضها البرنامج ليبحث عن الكلمة أو الكلمات المدخلة مع نتائج البحث. والطريقة كما هو موضح:

```py
>>> quran.searching('بسم الله الرحمن الرحيم', print_report=True)
[REPORT]
Runing Time: 0.01329257398901973
Count Search: 2
Result Search: [
    {
        "ID": 1,
        "Name": "الفَاتِحة",
        "Transliteration": "Al-Fātiḥah",
        "translation": "The Opener",
        "type": "meccan",
        "total_verses": 7,
        "verses_no": 1,
        "jozz": 1,
        "page": 1,
        "verses_number": 1,
        "line_start": 2,
        "line_end": 2,
        "verses_text": "بِسۡمِ ٱللَّهِ ٱلرَّحۡمَٰنِ ٱلرَّحِيمِ",
        "verses_text_without_diacritical": "بسم الله الرحمن الرحيم",
        "verses_text_english": "In the name of Allah, the Entirely Merciful, the Especially Merciful",
        "verses_text_transliteration": "Bismi Allahi alrrahmani alrraheemi"
    },
    {
        "ID": 3189,
        "Name": "النَّمل",
        "Transliteration": "An-Naml",
        "translation": "The Ant",
        "type": "meccan",
        "total_verses": 93,
        "verses_no": 27,
        "jozz": 19,
        "page": 379,
        "verses_number": 30,
        "line_start": 9,
        "line_end": 10,
        "verses_text": "إِنَّهُۥ مِن سُلَيۡمَٰنَ وَإِنَّهُۥ بِسۡمِ ٱللَّهِ ٱلرَّحۡمَٰنِ ٱلرَّحِيمِ",
        "verses_text_without_diacritical": "إنه من سليمان وإنه بسم الله الرحمن الرحيم",
        "verses_text_english": "Indeed, it is from Solomon, and indeed, it reads: 'In the name of Allah, the Entirely Merciful, the Especially Merciful",
        "verses_text_transliteration": "Innahu min sulaymana wainnahu bismi Allahi alrrahmani alrraheemi"
    }
]
```
يمكنك البحث في لغات أخرى بتفعيل خيار البحث باللغات الثانية كما هو موضح:

> **ملاحظة هامة (1)**:  عندما تستخدم خاصية البحث باللغات الأخرى ربما لا يعمل بالكفاءة العالية كما في اللغة العربية والإنجليزية. ويمكن تحسين هذه المشاكل في النسخ القادمة إن وجدت مشاكل.

> **ملاحظة هامة (2)**:  في حال وجود أي خلل لا تتردد في كتابة المشكلة عبر صفحة [المشكلات الخاص للمشروع](https://github.com/oaokm/AL-Khatma/issues).

```py
>>> quran.searching('from solomon', search_second_lang=True)
[{'ID': 3189, 'Name': 'النَّمل', 'Transliteration': 'An-Naml', 'translation': 'The Ant', 'type': 'meccan', 'total_verses': 93, 'verses_no': 27, 'jozz': 19, 'page': 379, 'verses_number': 30, 'line_start': 9, 'line_end': 10, 'verses_text': 'إِنَّهُۥ مِن سُلَيۡمَٰنَ وَإِنَّهُۥ بِسۡمِ ٱللَّهِ ٱلرَّحۡمَٰنِ ٱلرَّحِيمِ', 'verses_text_without_diacritical': 'إنه من سليمان وإنه بسم الله الرحمن الرحيم', 'verses_text_english': "Indeed, it is from Solomon, and indeed, it reads: 'In the name of Allah, the Entirely Merciful, the Especially Merciful", 'verses_text_transliteration': 'Innahu min sulaymana wainnahu bismi Allahi alrrahmani alrraheemi'}]

```

### تحميل صفحات من القرآن الكريم
من المزايا الجميلة في حزمة القرآن الكريم هو تحميل صفحات عالية الدقة، وتخزينها في القرص الصلب.

```py
> Quran.page_pic(
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
```

> **معلومة مساعدة**: خاصية `return_imge` يمكن أستخدامها في بناء البوتات، كبوت في التليجرام مثلًا. بدلًا من أن تخزم محتوى الصورة في القرص الصلب، يمكون في متغير قائمة (list).

> **ملاحظة مهمة(1)**: في حال عدم إتصالك بالإنترنت فإن هذه الميزة لن تعمل، ويرجى التحقق من إتصالك للإنترنت.

> **ملاحظة مهمة(2)**: خيار `type` هو نوع أو شكل الصفحة التي تريدها، وحاليا هنالك فقط شكلان فقط، ويمكن الاطلاع عليه [بالضغط هنا لرؤية الخيارات المتاح](https://github.com/oaokm/AL-Khatma/blob/main/DATA/quran_books.json).


طريقة كتابة الأمر كالتالي:

```py
>>> from AL_Khatma.quran import Quran
>>> quran = Quran() # استدعاء الكائن
>>> quran.page_pic([1, 2 , 48], 'm-madinah_ksu', '~/Pictures', 'quran') # كتابة جميع المعطيات اللازمة
# Download Pages From Quran ... 
100%|███████████████████████████████████████| 3/3 [00:01<00:00,  1.69it/s]
```
<p align="center">
  <img src="https://raw.githubusercontent.com/oaokm/AL-Khatma/main/Pictures/Screenshot_for_page_pic.png" alt="picture_screenshot">
</p>


### تفسيم صفحات القرآن
في حزمة تختيم القرآن الكريم، طريقة لتقسيم الصفحات بهدف تختيم القرآن، وتوزيع التقسيم على الصفحات.

```py
>>> from AL_Khatma.khatma import khatma # أستدعاء الحزمة
>>> k = khatma(30) # استدعاء الكائن"khatma" وتحديد عدد الأيام اللازمة لحتم القرآن. فـ(30) يمثل عدد أيام
>>> k.Khatma_page(report=True) # أمر تقسيم الصفحات مع طباعة التقرير
[REPORT KHATMA]
Days: 30
Reading Rate: 20 (Page/Day)    # معدل القراءة اليومي لختم القرآن بناءا على عدد الأيام المدخلة
Weerd: [22, 22, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]
[22, 22, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]
```

يمكن كتابة أمر لـ(`khatma.Khatma_page`) بتقسيم وتطبيق التوزيع مباشرُا على المصحف وإرجاع قيمة كبيرة. مضمون هذه القيم الكبيرة هي الأيات اللازم قراءتها في اليوم الواحد. طريقة كتابتها كالتالي:

```py
>>> werrd = k.Khatma_page(werrd=True, report=True)
The process of dividing the Quranic verses begins ... 
100%|█████████████████████████████████████████████| 30/30 [00:00<00:00, 2016.04it/s]
[REPORT KHATMA]
Days: 30
Reading Rate: 20 (Page/Day)
Weerd: [22, 22, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]
Number of Werrd: 30
```

## **المصادر** 

لمبدأ الشفافية وللحساسية الدينية التي تقدمها المكتبة، سأذكر المصادر التي -والله الحمد- تم بناء هذه المكتبة. المصادر كالتالي:
* [أية -  API مفتوح المصدر للأذكار والقرآن والأحاديث](https://github.com/nawafalqari/ayah)
* [الأيات القرأنية باللغات الأخرى](https://github.com/risan/quran-json)
* مصادر تحميل صفحات القرآن الكريم:
  * [الموقع الرسمي لأيات لجامعة الملك سعود](https://quran.ksu.edu.sa/ayat/)
  * [موقع الباحث القرآني](https://tafsir.app/)


## **الترخيص**
ترخيص هو: إم آي تي ([MIT © Osamah Awadh](https://github.com/oaokm/AL-Khatma/blob/main/LICENSE))
