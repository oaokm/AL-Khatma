<p align="center">
  <img src="https://raw.githubusercontent.com/oaokm/AL-Khatma/main/Logo/AL_Khatma_logo_one.png" alt="AL-Khatma Logo For Arabic and English">
</p>

<p align="center">
  <a href="https://github.com/oaokm/AL-Khatma/blob/main/README.md">Arabic</a>
  &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="https://github.com/oaokm/AL-Khatma/blob/main/README_EN.md">English</a>
</p>

<p align="center">*Under Revisioning...*</p>

<p align="center">
  <a href="#Program-Idea">Program idea</a>
  &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#Download">Download</a>
  &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#How-to-use-it">How to use it</a>
  &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#Sources">Sources</a>
  &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#License">License</a>
  &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="https://github.com/oaokm/AL-Khatma/blob/main/UPDATE_EN.md">Updates</a>
  &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="https://github.com/oaokm/AL-Khatma/issues">Issues Page</a>
  &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="https://github.com/oaokm/AL-Khatma/issues/new/choose">New Issues</a>
</p>

![GitHub](https://img.shields.io/github/license/oaokm/AL-Khatma) | ![](https://img.shields.io/badge/Programing%20Language-Python_3_and_top-orange) | ![PyPI](https://img.shields.io/pypi/v/AL-Khatma-lib) | ![GitHub repo size](https://img.shields.io/github/repo-size/oaokm/AL-Khatma)
--| --| -- | --| 

> **Message to Everyone**: If you use the library when you see any problem (bugs or Errors), please [report a problem](https://github.com/oaokm/AL-Khatma/issues/new/choose).
This helps me develop the library and find out the problems.
Especially when it comes to the architecture of the operating system.
This means that the architecture of the Linux operating system is completely different from Windows, and it may differ from the Macintosh system of Apple. If there is a problem, please [report the problem on the problems page](https://github.com/oaokm/AL-Khatma/issues).
Thank you.


## **What is "AL-Khatma"?**
**AL-Khatma** or **Khatma** ([Arabic](https://en.wikipedia.org/wiki/Arabic): الختمة أو ختمة) is one of the many names of the [Holy Qur’an](https://en.wikipedia.org/wiki/Quran), and it is also the name of the way to finish reading the [Qur’an](https://en.wikipedia.org/wiki/Quran).



## **Program Idea**
**AL-Khatma** is an open source project that was built to unify the belongings related to the Islamic religion (such as the Holy Quran, hadiths, interpretation, supplications, etc.) in one place.
The library has several packages, the most important of which are:

* **The Holy Quran Package**:.
   * Extracting all Quranic verses and all their information.
   * Possibility to search for verses.
   * Possibility to download images of the Holy Quran pages.
   * The library is provided in several languages. Such as:
     * English 
     * Chinese 
     * Turkish 
     * Russian 
     * Swedish 
     * Urdu 
     * French 
     * Spanish
     * Andansi 
* **Holy Quran Seal Package**.
  * Write the number of closing days, and give the appropriate plan for that in detail
  * Issuing a PDF file and giving each day a file containing the verses that he likes to recite to finish the entire Qur'an.
* **Holy Quran PDF Pack**
  * Issue any number of pages and export them to PDF file
  * Split the pages of the Holy Quran, and export daily roses as a PDF file
  * The quality of the pages used in the export is high
  * A specific surah can be issued with all its verses
* **Interpretation package for the Holy Quran, currently contains the following books:**
  * The facilitator interpretation of the Holy Qur'an
  * Book of interpretation of the manual of the Holy Quran
* **Remembrance Package**
  * Contains more than 130 categories or males

Work is underway on the audio package, which will be announced in the next versions -hopefully-


## **Download**

### **The First Way: Pypi(The Best)**
```sh
$ pip install AL-Khatma-lib
```
**OR**
```sh
$ pip3 install AL-Khatma-lib
```

### **The Second Way: Download From Github**
- One: Form Command Line:
```sh
S git clone https://github.com/oaokm/AL-Khatma
```

- Two: Form Github Page: Download it from your browser as a .zip file.


### **Download Important Files**
The important files are the languages file and some files that help the program work, by typing the following command:

```py
>>> import AL_Khatma
>>> AL_Khatma.Download_DATA()
```
Wait for the download process to complete successfully.


## **How to use it?**
**Wrating Anything Here**

### **Show Library Version**

```py
>>> import AL_Khatma
>>> AL_Khatma.__version__
'1.0.0'
```

### **Method of extraction of the Holy Quran surahs**
The command that extracts the content of the Holy Quran is `Quran.show_block_aya()`. This command returns a value to you in the form of the list variable, and the number of items in the list is always equal to the number of verses of the surah that you called.

```py
Quran.show_block_aya(
            self,
            verses_no:int,
            verses_number:list,
            orderly=False,
            ):
        """
        show_block_aya(func): It is a function that extracts what the user wants from the language file
        verses_no(int): Extract the surah you want
        verses_number(list): In the event that you want a specific surah, you can do so by writing its number. And you can make it empty
        orderly(bool): If you want to see the result printed in a readable format
        """
```
> **For example**, Surat Al-Fatihah, the number of its verses is 7, with the Basmala, so the program will return 7 items to you in the list variable.

Each element contains information for the verse in the form of a dictionary variable (dict), and its form is as follows:

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

Element | Definition
----- | ------
`ID`  |  The special identifier for the verse
`Name`|  The name of the surah
`Transliteration`|  The Surah in other languages
`translation`| Letters/spellings of the name of the Surah for non-Arabs
`type`|  The type of the noble surah, either `Meccan` or `Medinan`
`total_verses`| The total number of verses in the surah
`verses_no`|  The order of the surah between the surahs, based on the copy of the Holy Quran of the King Fahd Complex for the Printing of the Holy Quran
`jozz`| The place of the verse in relation to the part
`page`| The place of the verse in relation to the page
`verses_number`|  The position of the verse in the surah
`line_start`| Shows you the position of the verse relative to where it appears at the beginning of the line (based on the copy of the Quran of the King Fahd Complex for the Printing of the Noble Quran)
`line_end`| It shows you the location of the verse in relation to where it appears at the end of the line (based on the copy of the Quran of the King Fahd Complex for the Printing of the Noble Quran)
`verses_text`| The text of the verses with diacritical
`verses_text_without_diacritical`| The text of the verses without diacritical
`verses_text_english`| The text of the verses in other languages
`verses_text_transliteration`|Letter/spelling of the verse for non-Arabs


### **The First Method: Extract The Verses From The Surah Only**

There are several ways to write a command `Quran.show_block_aya()`

```py
>>> from AL_Khatma.quran import Quran # Here you call the library
>>> quran = Quran() # Call to the object
>>> sura  = quran.show_block_aya(1, []) # The command to recall the surah based on its order in the index with all its verses and information
>>> sura
([{'ID': 1, 'Name': 'الفَاتِحة', 'Transliteration': 'Al-Fātiḥah', 'translation': 'The Opener', 'type': 'meccan', 'total_verses': 7, 'verses_no': 1, 'jozz': 1, 'page': 1, 'verses_number': 1, 'line_start': 2, 'line_end': 2, 'verses_text': 'بِسۡمِ ٱللَّهِ ٱلرَّحۡمَٰنِ ٱلرَّحِيمِ', 'verses_text_without_diacritical': 'بسم الله الرحمن الرحيم', 'verses_text_english': 'In the name of Allah, the Entirely Merciful, the Especially Merciful', 'verses_text_transliteration': 'Bismi Allahi alrrahmani alrraheemi'}, {'ID': 2, 'Name': 'الفَاتِحة', 'Transliteration': 'Al-Fātiḥah', 'translation': 'The Opener', 'type': 'meccan', 'total_verses': 7, 'verses_no': 1, 'jozz': 1, 'page': 1, 'verses_number': 2, 'line_start': 3, 'line_end': 3, 'verses_text': 'ٱلۡحَمۡدُ لِلَّهِ رَبِّ ٱلۡعَٰلَمِينَ', 'verses_text_without_diacritical': 'الحمد لله رب العالمين', 'verses_text_english': '[All] praise is [due] to Allah, Lord of the worlds', 'verses_text_transliteration': 'Alhamdu lillahi rabbi alAAalameena'}, {'ID': 3, 'Name': 'الفَاتِحة', 'Transliteration': 'Al-Fātiḥah', 'translation': 'The Opener', 'type': 'meccan', 'total_verses': 7, 'verses_no': 1, 'jozz': 1, 'page': 1, 'verses_number': 3, 'line_start': 4, 'line_end': 4, 'verses_text': 'ٱلرَّحۡمَٰنِ ٱلرَّحِيمِ', 'verses_text_without_diacritical': 'الرحمن الرحيم', 'verses_text_english': 'The Entirely Merciful, the Especially Merciful', 'verses_text_transliteration': 'Alrrahmani alrraheemi'}, {'ID': 4, 'Name': 'الفَاتِحة', 'Transliteration': 'Al-Fātiḥah', 'translation': 'The Opener', 'type': 'meccan', 'total_verses': 7, 'verses_no': 1, 'jozz': 1, 'page': 1, 'verses_number': 4, 'line_start': 4, 'line_end': 4, 'verses_text': 'مَٰلِكِ يَوۡمِ ٱلدِّينِ', 'verses_text_without_diacritical': 'مالك يوم الدين', 'verses_text_english': 'Sovereign of the Day of Recompense', 'verses_text_transliteration': 'Maliki yawmi alddeeni'}, {'ID': 5, 'Name': 'الفَاتِحة', 'Transliteration': 'Al-Fātiḥah', 'translation': 'The Opener', 'type': 'meccan', 'total_verses': 7, 'verses_no': 1, 'jozz': 1, 'page': 1, 'verses_number': 5, 'line_start': 5, 'line_end': 5, 'verses_text': 'إِيَّاكَ نَعۡبُدُ وَإِيَّاكَ نَسۡتَعِينُ', 'verses_text_without_diacritical': 'إياك نعبد وإياك نستعين', 'verses_text_english': 'It is You we worship and You we ask for help', 'verses_text_transliteration': 'Iyyaka naAAbudu waiyyaka nastaAAeenu'}, {'ID': 6, 'Name': 'الفَاتِحة', 'Transliteration': 'Al-Fātiḥah', 'translation': 'The Opener', 'type': 'meccan', 'total_verses': 7, 'verses_no': 1, 'jozz': 1, 'page': 1, 'verses_number': 6, 'line_start': 5, 'line_end': 6, 'verses_text': 'ٱهۡدِنَا ٱلصِّرَٰطَ ٱلۡمُسۡتَقِيمَ', 'verses_text_without_diacritical': 'اهدنا الصراط المستقيم', 'verses_text_english': 'Guide us to the straight path', 'verses_text_transliteration': 'Ihdina alssirata almustaqeema'}, {'ID': 7, 'Name': 'الفَاتِحة', 'Transliteration': 'Al-Fātiḥah', 'translation': 'The Opener', 'type': 'meccan', 'total_verses': 7, 'verses_no': 1, 'jozz': 1, 'page': 1, 'verses_number': 7, 'line_start': 6, 'line_end': 8, 'verses_text': 'صِرَٰطَ ٱلَّذِينَ أَنۡعَمۡتَ عَلَيۡهِمۡ غَيۡرِ ٱلۡمَغۡضُوبِ عَلَيۡهِمۡ وَلَا ٱلضَّآلِّينَ', 'verses_text_without_diacritical': 'صراط الذين أنعمت عليهم غير المغضوب عليهم ولا الضالين', 'verses_text_english': 'The path of those upon whom You have bestowed favor, not of those who have evoked [Your] anger or of those who are astray', 'verses_text_transliteration': 'Sirata allatheena anAAamta AAalayhim ghayri almaghdoobi AAalayhim wala alddalleena'}], [])
```

To select verses particular we do the following:
```py
>>> len(sura) # The number of items returned
2
>>> sura[0][0] # Print the information of the selected verse
{'ID': 1, 'Name': 'الفَاتِحة', 'Transliteration': 'Al-Fātiḥah', 'translation': 'The Opener', 'type': 'meccan', 'total_verses': 7, 'verses_no': 1, 'jozz': 1, 'page': 1, 'verses_number': 1, 'line_start': 2, 'line_end': 2, 'verses_text': 'بِسۡمِ ٱللَّهِ ٱلرَّحۡمَٰنِ ٱلرَّحِيمِ', 'verses_text_without_diacritical': 'بسم الله الرحمن الرحيم', 'verses_text_english': 'In the name of Allah, the Entirely Merciful, the Especially Merciful', 'verses_text_transliteration': 'Bismi Allahi alrrahmani alrraheemi'}
>>> sura[0][0]['verses_text_without_diacritical'] # Print something specific from the dictionary variable
'بسم الله الرحمن الرحيم'
```

### **The Second Method: Extract Part of The Surah**

> **Note one**: You can add more than one verse, provided that it does not exceed the total number of verses in the surah. Because the program will return nothing to your value

> **Note Two**: You can neglect the order of the verses (in the list variable), but preferably in order

```py
>>> from AL_Khatma.quran import Quran # Call the library
>>> quran = Quran() # Call the Object
>>> sura  = quran.show_block_aya(1, [6, 7]) # We are here to call the surah with specifying the verses that we want
>>> sura[1] # Select the item for custom verses
[{'ID': 6, 'Name': 'الفَاتِحة', 'Transliteration': 'Al-Fātiḥah', 'translation': 'The Opener', 'type': 'meccan', 'total_verses': 7, 'verses_no': 1, 'jozz': 1, 'page': 1, 'verses_number': 6, 'line_start': 5, 'line_end': 6, 'verses_text': 'ٱهۡدِنَا ٱلصِّرَٰطَ ٱلۡمُسۡتَقِيمَ', 'verses_text_without_diacritical': 'اهدنا الصراط المستقيم', 'verses_text_english': 'Guide us to the straight path', 'verses_text_transliteration': 'Ihdina alssirata almustaqeema'}, {'ID': 7, 'Name': 'الفَاتِحة', 'Transliteration': 'Al-Fātiḥah', 'translation': 'The Opener', 'type': 'meccan', 'total_verses': 7, 'verses_no': 1, 'jozz': 1, 'page': 1, 'verses_number': 7, 'line_start': 6, 'line_end': 8, 'verses_text': 'صِرَٰطَ ٱلَّذِينَ أَنۡعَمۡتَ عَلَيۡهِمۡ غَيۡرِ ٱلۡمَغۡضُوبِ عَلَيۡهِمۡ وَلَا ٱلضَّآلِّينَ', 'verses_text_without_diacritical': 'صراط الذين أنعمت عليهم غير المغضوب عليهم ولا الضالين', 'verses_text_english': 'The path of those upon whom You have bestowed favor, not of those who have evoked [Your] anger or of those who are astray', 'verses_text_transliteration': 'Sirata allatheena anAAamta AAalayhim ghayri almaghdoobi AAalayhim wala alddalleena'}]
>>> len(sura[1]) # Knowing the number of verses that we asked to identify
2
```

### **Change to other languages**

Al Khatma Library provides you with a good number of foreign languages. To find out which languages are available in the library, you can type the following command:

> **Note**: when the object is called `Quran()` it automatically selects a file that contains both Arabic and English. You do not need to specify if you want these two languages.

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

Markup/Symbol Language | Language
-- | --
 ar   | Arabic
 en   | English
 fr   | French 
 es   | Spanish
 tr   | Turkish
 ru   | Russian
 bn   | Bengali
 zh   | Chinese
 id   | Indonesian
 sv   | Swedish
 ur   | Urdu

After knowing the available languages and their symbols, we modify the command `Quran(lang=[language encoding/code])`


```py
>>> from AL_Khatma.quran import Quran
>>> quran = Quran(lang='zh') # We take the Chinese language code as an example
>>> sura  = quran.show_block_aya(1, []) 
>>> sura[0][0]  # You selected the first verse of Surat Al-Fatihah
{'ID': 1, 'Name': 'الفَاتِحة', 'Transliteration': 'Al-Fātiḥah', 'translation': '开端章', 'type': 'meccan', 'total_verses': 7, 'verses_no': 1, 'jozz': 1, 'page': 1, 'verses_number': 1, 'line_start': 2, 'line_end': 2, 'verses_text': 'بِسۡمِ ٱللَّهِ ٱلرَّحۡمَٰنِ ٱلرَّحِيمِ', 'verses_text_without_diacritical': 'بسم الله الرحمن الرحيم', 'verses_text_chinese': '奉至仁至慈的安拉之名', 'verses_text_transliteration': 'Bismi Allahi alrrahmani alrraheemi'}
```

### **Searching For The Noble Verses**

One of the advantages of the Quran package is the search feature, using the `Quran.searching()` command:

```py
Quran.searching(
            self, 
            text:str, 
            search_second_lang=False, 
            print_report=False
            ):
        """
        searching(func): It is the search function between the lines of the Qur’an
        text(str): The word to be searched
        search_second_lang(bool): If this feature is activated, the search will be based on the second language in the language file
        print_report(bool): If this feature is activated, print an organized report on the search results
        """
```
To perform the search, call the object "Quran". and calling the search function as shown:

```py
>>> from AL_Khatma.quran import Quran
>>> quran = Quran()
>>> quran.searching('بسم الله الرحمن الرحيم')
[{'ID': 1, 'Name': 'الفَاتِحة', 'Transliteration': 'Al-Fātiḥah', 'translation': 'The Opener', 'type': 'meccan', 'total_verses': 7, 'verses_no': 1, 'jozz': 1, 'page': 1, 'verses_number': 1, 'line_start': 2, 'line_end': 2, 'verses_text': 'بِسۡمِ ٱللَّهِ ٱلرَّحۡمَٰنِ ٱلرَّحِيمِ', 'verses_text_without_diacritical': 'بسم الله الرحمن الرحيم', 'verses_text_english': 'In the name of Allah, the Entirely Merciful, the Especially Merciful', 'verses_text_transliteration': 'Bismi Allahi alrrahmani alrraheemi'}, {'ID': 3189, 'Name': 'النَّمل', 'Transliteration': 'An-Naml', 'translation': 'The Ant', 'type': 'meccan', 'total_verses': 93, 'verses_no': 27, 'jozz': 19, 'page': 379, 'verses_number': 30, 'line_start': 9, 'line_end': 10, 'verses_text': 'إِنَّهُۥ مِن سُلَيۡمَٰنَ وَإِنَّهُۥ بِسۡمِ ٱللَّهِ ٱلرَّحۡمَٰنِ ٱلرَّحِيمِ', 'verses_text_without_diacritical': 'إنه من سليمان وإنه بسم الله الرحمن الرحيم', 'verses_text_english': "Indeed, it is from Solomon, and indeed, it reads: 'In the name of Allah, the Entirely Merciful, the Especially Merciful", 'verses_text_transliteration': 'Innahu min sulaymana wainnahu bismi Allahi alrrahmani alrraheemi'}]
```

You can print a simple report, and the report gives you the time spent by the program to search for the word or words entered with the search results. And the method is as shown:

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

You can search in other languages by activating the search in second languages option as shown:

> **Important Note One**: When you use the search feature in other languages, it may not work as efficiently as in Arabic and English. These problems can be improved in the next versions if any problems

> **Important Note Two**: In the event of any defect, do not hesitate to write the problem on the [Issues page](https://github.com/oaokm/AL-Khatma/issues)

```py
>>> quran.searching('from solomon', search_second_lang=True)
[{'ID': 3189, 'Name': 'النَّمل', 'Transliteration': 'An-Naml', 'translation': 'The Ant', 'type': 'meccan', 'total_verses': 93, 'verses_no': 27, 'jozz': 19, 'page': 379, 'verses_number': 30, 'line_start': 9, 'line_end': 10, 'verses_text': 'إِنَّهُۥ مِن سُلَيۡمَٰنَ وَإِنَّهُۥ بِسۡمِ ٱللَّهِ ٱلرَّحۡمَٰنِ ٱلرَّحِيمِ', 'verses_text_without_diacritical': 'إنه من سليمان وإنه بسم الله الرحمن الرحيم', 'verses_text_english': "Indeed, it is from Solomon, and indeed, it reads: 'In the name of Allah, the Entirely Merciful, the Especially Merciful", 'verses_text_transliteration': 'Innahu min sulaymana wainnahu bismi Allahi alrrahmani alrraheemi'}]
```

### **Download pages from the Quran**

One of the nice features in the Quran package is downloading high-resolution pages and storing them on the hard drive.

```py
> Quran.page_pic(
            self,
            page:list,
            type:str,
            path:str, 
            name_folder:str,
            return_imge=False):
        """
        page_pic(func): A function based on downloading the pages of the Qur’an from the Internet
        page(list): You put the number of verses that you want to download
        path(str): Image upload path
        name_folder(str): The name of the file in which the images will be pages
        return_imge(bool): If the option is enabled, pages are loaded in binary format in list valuable
        """
```

> **Help Info**: The `return_imge` property can be used to build bots, such as a Telegram bot. Instead of storing the content of the image to the hard disk, it is stored in a list variable.

> **Important Note One**: If you are not connected to the Internet, this feature will not work, please check your Internet connection

> **Important Note Two**: The `type` option is the type or format of the page that you want, and currently there are only two forms, and it can be viewed [by clicking here to see the available options](https://github.com/oaokm/AL-Khatma/blob/main/DATA/quran_books.json).

> **Important Note Three**: When you put the path where you will download the images, you must put the full path as shown in the example

The way to write the command is as follows:

```py
>>> from AL_Khatma.quran import Quran
>>> quran = Quran() # Call the Object
>>> quran.page_pic([1, 2 , 48], 'm-madinah_ksu', '/home/oaokm/Pictures', 'quran') # Write down all necessary data
# Download Pages From Quran | [/home/oaokm/Pictures/Quran] 
100%|███████████████████████████████████████| 3/3 [00:01<00:00,  1.69it/s]
```
<p align="center">
  <img src="https://raw.githubusercontent.com/oaokm/AL-Khatma/main/Pictures/Screenshot_for_page_pic.png" alt="picture_screenshot">
</p>

### **Dealing with the interpretation package of the Holy Quran**
> **Note**: This package it working in 2.0.0 and top, and all interpretation(Tafser) books for Arabic.

One of the most important advantages of the seal library is the interpretation package(Tafser package). This package currently contains two of the most famous tafsir books at the moment, and perhaps in the coming weeks or months a number of tafsir books will be added.

To see what books are in this package, write this command:

```py
>>> from AL_Khatma.tafser import tafser
>>> taf = tafser('?')
The Available Tafser The Quran:
[0] muyassar
[1] mukhtasar
```
Part of the contents of the books of interpretation:

```py
// From JSON file ./DATA/Tafser/mukhtasar.json
{
        "ID": 1,
        "Tafser_type": "mukhtasar",
        "Sura": 1,
        "verses_number": 1,
        "Text": "* سورة الفاتحة مكية * مِن مَّقاصِدِ السُّورَةِ:\nتحقيق التوجه لله تعالى بكمال العبودية له وحده. * التَّفْسِيرُ:\nسُمِّيت سورةَ الفاتحة لافتتاح كتاب الله بها، وتسمَّى أم القرآن لاشتمالها على موضوعاته، من توحيد لله، وعبادة، وغير ذلك، وهي أعظم سورة في القرآن، وهي السَّبعُ المثاني.\nباسم الله أبدأ قراءة القرآن، مستعينًا به تعالى متبركًا بذكر اسمه. وقد تضمنت البسملة ثلاثة من أسماء الله الحسنى، وهي:\n• «الله»، أي: المعبود بحق، وهو أخص أسماء الله تعالى، ولا يسمى به غيره سبحانه.\n• «الرَّحْمَن»، أي: ذو الرحمة الواسعة. فهو الرحمن بذاته.\n• «الرَّحِيم»، أي: ذو الرحمة الواصلة. فهو يرحم برحمته من شاء من خلقه ومنهم المؤمنون من عباده.",
        "Text_without_diacritical": "* سورة الفاتحة مكية * من مقاصد السورة:\nتحقيق التوجه لله تعالى بكمال العبودية له وحده. * التفسير:\nسميت سورة الفاتحة لافتتاح كتاب الله بها، وتسمى أم القرآن لاشتمالها على موضوعاته، من توحيد لله، وعبادة، وغير ذلك، وهي أعظم سورة في القرآن، وهي السبع المثاني.\nباسم الله أبدأ قراءة القرآن، مستعينا به تعالى متبركا بذكر اسمه. وقد تضمنت البسملة ثلاثة من أسماء الله الحسنى، وهي:\n• «الله»، أي: المعبود بحق، وهو أخص أسماء الله تعالى، ولا يسمى به غيره سبحانه.\n• «الرحمن»، أي: ذو الرحمة الواسعة. فهو الرحمن بذاته.\n• «الرحيم»، أي: ذو الرحمة الواصلة. فهو يرحم برحمته من شاء من خلقه ومنهم المؤمنون من عباده.",
        "URL": "https://tafsir.app/mukhtasar/1/1"
}
```
Definition | Itme
---------- | ----
`ID`  |  Private ID for noble verses
`Tafser_type`  |   Type of interpretation (interpretation book)
`verses_number`  |  The number of the noble verse in the surah
`Text`  |  Interpretation text for Arabic
`Text_without_diacritical`  |  Interpretation text without diacritics for Arabic
`URL`  |  Source of interpretation

#### **Know the interpretation of Surah in full**
You can put the order of the surah on the 'call_block' command and it will respond to you by returning the value of the operation.

> **Note to the Modesty**: In other words, Surah Al-Fatihah is arranged in the first Qur'an, so 'call_block' will return 7 items. These elements are equal to the total number of verses of Surat Al-Fatihah

```py
>>> from AL_Khatma.tafser import tafser
>>> taf = tafser('mukhtasar') # Select type of interpretation
>>> taf.call_block(1) # Interpretation of Surat Al-Fatihah
[{'ID': 1, 'Tafser_type': 'mukhtasar', 'Sura': 1, 'verses_number': 1, 'Text': '* سورة الفاتحة مكية * مِن مَّقاصِدِ السُّورَةِ:\nتحقيق التوجه لله تعالى بكمال العبودية له وحده. * التَّفْسِيرُ:\nسُمِّيت سورةَ الفاتحة لافتتاح كتاب الله بها، وتسمَّى أم القرآن لاشتمالها على موضوعاته، من توحيد لله، وعبادة، وغير ذلك، وهي أعظم سورة في القرآن، وهي السَّبعُ المثاني.\nباسم الله أبدأ قراءة القرآن، مستعينًا به تعالى متبركًا بذكر اسمه. وقد تضمنت البسملة ثلاثة من أسماء الله الحسنى، وهي:\n• «الله»، أي: المعبود بحق، وهو أخص أسماء الله تعالى، ولا يسمى به غيره سبحانه.\n• «الرَّحْمَن»، أي: ذو الرحمة الواسعة. فهو الرحمن بذاته.\n• «الرَّحِيم»، أي: ذو الرحمة الواصلة. فهو يرحم برحمته من شاء من خلقه ومنهم المؤمنون من عباده.', 'Text_without_diacritical': '* سورة الفاتحة مكية * من مقاصد السورة:\nتحقيق التوجه لله تعالى بكمال العبودية له وحده. * التفسير:\nسميت سورة الفاتحة لافتتاح كتاب الله بها، وتسمى أم القرآن لاشتمالها على موضوعاته، من توحيد لله، وعبادة، وغير ذلك، وهي أعظم سورة في القرآن، وهي السبع المثاني.\nباسم الله أبدأ قراءة القرآن، مستعينا به تعالى متبركا بذكر اسمه. وقد تضمنت البسملة ثلاثة من أسماء الله الحسنى، وهي:\n• «الله»، أي: المعبود بحق، وهو أخص أسماء الله تعالى، ولا يسمى به غيره سبحانه.\n• «الرحمن»، أي: ذو الرحمة الواسعة. فهو الرحمن بذاته.\n• «الرحيم»، أي: ذو الرحمة الواصلة. فهو يرحم برحمته من شاء من خلقه ومنهم المؤمنون من عباده.', 'URL': 'https://tafsir.app/mukhtasar/1/1'}, {'ID': 2, 'Tafser_type': 'mukhtasar', 'Sura': 1, 'verses_number': 2, 'Text': 'جميع أنواع المحامد من صفات الجلال والكمال هي له وحده دون من سواه، إذ هو رب كل شيء وخالقه ومدبره. و«العالمون» جمع «عالَم» وهم كل ما سوى الله تعالى.', 'Text_without_diacritical': 'جميع أنواع المحامد من صفات الجلال والكمال هي له وحده دون من سواه، إذ هو رب كل شيء وخالقه ومدبره. و«العالمون» جمع «عالم» وهم كل ما سوى الله تعالى.', 'URL': 'https://tafsir.app/mukhtasar/1/2'}, {'ID': 3, 'Tafser_type': 'mukhtasar', 'Sura': 1, 'verses_number': 3, 'Text': 'ثناء على الله تعالى بعد حمده في الآية السابقة.', 'Text_without_diacritical': 'ثناء على الله تعالى بعد حمده في الآية السابقة.', 'URL': 'https://tafsir.app/mukhtasar/1/3'}, {'ID': 4, 'Tafser_type': 'mukhtasar', 'Sura': 1, 'verses_number': 4, 'Text': 'تمجيد لله تعالى بأنه المالك لكل ما في يوم القيامة، حيث لا تملك نفس لنفس شيئًا. فـ«يوم الدين»: يوم الجزاء والحساب.', 'Text_without_diacritical': 'تمجيد لله تعالى بأنه المالك لكل ما في يوم القيامة، حيث لا تملك نفس لنفس شيئا. فـ«يوم الدين»: يوم الجزاء والحساب.', 'URL': 'https://tafsir.app/mukhtasar/1/4'}, {'ID': 5, 'Tafser_type': 'mukhtasar', 'Sura': 1, 'verses_number': 5, 'Text': 'نخصُّك وحدك بأنواع العبادة والطاعة، فلا نشرك معك غيرك، ومنك وحدك نطلب العون في كل شؤوننا، فبِيَدِكَ الخير كله، ولا مُعين سواك.', 'Text_without_diacritical': 'نخصك وحدك بأنواع العبادة والطاعة، فلا نشرك معك غيرك، ومنك وحدك نطلب العون في كل شؤوننا، فبيدك الخير كله، ولا معين سواك.', 'URL': 'https://tafsir.app/mukhtasar/1/5'}, {'ID': 6, 'Tafser_type': 'mukhtasar', 'Sura': 1, 'verses_number': 6, 'Text': 'دُلَّنا إلى الصراط المستقيم، واسلك بنا فيه، وثبِّتنا عليه.، وزدنا هدى. و«الصراط المستقيم» هو الطريق الواضح الذي لا اعوجاج فيه، وهو الإسلام الذي أرسل الله به محمدًا ﷺ.', 'Text_without_diacritical': 'دلنا إلى الصراط المستقيم، واسلك بنا فيه، وثبتنا عليه.، وزدنا هدى. و«الصراط المستقيم» هو الطريق الواضح الذي لا اعوجاج فيه، وهو الإسلام الذي أرسل الله به محمدا ﷺ.', 'URL': 'https://tafsir.app/mukhtasar/1/6'}, {'ID': 7, 'Tafser_type': 'mukhtasar', 'Sura': 1, 'verses_number': 7, 'Text': 'طريق الذين أنعمت عليهم من عبادك بهدايتهم، كالنبيين والصدِّيقين والشهداء والصالحين وحَسُنَ أولئك رفيقًا، غير طريق المغضوب عليهم الذين عرفوا الحق ولم يتبعوه كاليهود، وغير طريق الضالين عن الحق الذين لم يهتدوا إليه لتفريطهم في طلب الحق والاهتداء إليه كالنصارى. * من فوائد الآيات:\n• افتتح الله تعالى كتابه بالبسملة، ليرشد عباده أن يبدؤوا أعمالهم وأقوالهم بها طلبًا لعونه وتوفيقه.\n• من هدي عباد الله الصالحين في الدعاء البدء بتمجيد الله والثناء عليه سبحانه ثم ليشرع في الطلب.\n• تحذير المسلمين من التقصير في طلب الحق كالنصارى الضالين، أو عدم العمل بالحق الذي عرفوه كاليهود المغضوب عليهم.\n• دلَّت السورة على أن كمال الإيمان يكون بإخلاص العبادة لله تعالى وطلب العون منه وحده دون سواه.', 'Text_without_diacritical': 'طريق الذين أنعمت عليهم من عبادك بهدايتهم، كالنبيين والصديقين والشهداء والصالحين وحسن أولئك رفيقا، غير طريق المغضوب عليهم الذين عرفوا الحق ولم يتبعوه كاليهود، وغير طريق الضالين عن الحق الذين لم يهتدوا إليه لتفريطهم في طلب الحق والاهتداء إليه كالنصارى. * من فوائد الآيات:\n• افتتح الله تعالى كتابه بالبسملة، ليرشد عباده أن يبدؤوا أعمالهم وأقوالهم بها طلبا لعونه وتوفيقه.\n• من هدي عباد الله الصالحين في الدعاء البدء بتمجيد الله والثناء عليه سبحانه ثم ليشرع في الطلب.\n• تحذير المسلمين من التقصير في طلب الحق كالنصارى الضالين، أو عدم العمل بالحق الذي عرفوه كاليهود المغضوب عليهم.\n• دلت السورة على أن كمال الإيمان يكون بإخلاص العبادة لله تعالى وطلب العون منه وحده دون سواه.', 'URL': 'https://tafsir.app/mukhtasar/1/7'}]
```
#### **Calling all the interpretations of the surahs**
You can summon all the surahs with their interpretations, by typing the following command:
```py
>>> from AL_Khatma.tafser import tafser
>>> taf = tafser('mukhtasar') # Select type of interpretation
>>> taf..all_blocks()
```


### **Dealing with the remembrance(adhkar) package**
> **Note**: This package it working in 2.0.0 and top, and all interpretation(Tafser) books for Arabic.

The remembrance(Adhkar) package gives you control and review of all kinds of remembrances. Where the package database contains more than 130 items 

To see all items, type the following command:  * Write the number of closing days, and give the appropriate plan for that in detail
```py
>>> from AL_Khatma.adkar import Adkar
>>> adkar = Adkar()
>>> adkar.show_me_categorys()
['أذكار الصباح', 'أذكار المساء', 'أذكار الاستيقاظ من النوم', 'دعاء لبس الثوب', 'دعاء لبس الثوب الجديد', 'ما يقول إذا وضع الثوب', 'دعاء دخول الخلاء', 'دعاء الخروج من الخلاء', 'الذكر قبل الوضوء', 'الذكر بعد الفراغ من الوضوء', 'الذكر عند الخروج من المنزل', 'الذكر عند دخول المنزل', 'دعاء الذهاب إلى المسجد', 'دعاء دخول المسجد', 'دعاء الخروج من المسجد', 'أذكار الآذان', 'دعاء الاستفتاح', 'دعاء الركوع', 'دعاء الرفع من الركوع', 'دعاء السجود', 'دعاء الجلسة بين السجدتين', 'دعاء سجود التلاوة', 'التشهد', 'الصلاة على النبي بعد التشهد', 'الدعاء بعد التشهد الأخير قبل السلام', 'الأذكار بعد السلام من الصلاة', 'دعاء صلاة الاستخارة', 'أذكار النوم', 'الدعاء إذا تقلب في الليل', 'دعاء الفزع في النوم و من بلي بالوحشة', 'ما يفعل من رأى الرؤيا أو الحلم في النوم', 'دعاء قنوت الوتر', 'الذكر عقب السلام من الوتر', 'دعاء الهم والحزن', 'دعاء الكرب', 'دعاء لقاء العدو و ذي السلطان', 'الدعاء على العدو', 'ما يقول من خاف قوما', 'دعاء من أصابه وسوسة في الإيمان', 'دعاء قضاء الدين', 'دعاء الوسوسة في الصلاة و القراءة', 'دعاء من استصعب عليه أمر', 'ما يقول ويفعل من أذنب ذنبا', 'دعاء طرد الشيطان و وساوسه', 'الدعاء حينما يقع ما لا يرضاه أو غلب على أمره', 'ﺗﻬنئة المولود له وجوابه', 'ما يعوذ به الأولاد', 'الدعاء للمريض في عيادته', 'فضل عيادة المريض', 'دعاء المريض الذي يئس من حياته', 'تلقين المحتضر', 'دعاء من أصيب بمصيبة', 'الدعاء عند إغماض الميت', 'الدعاء للميت في الصلاة عليه', 'الدعاء للفرط في الصلاة عليه', 'دعاء التعزية', 'الدعاء عند إدخال الميت القبر', 'الدعاء بعد دفن الميت', 'دعاء زيارة القبور', 'دعاء الريح', 'دعاء الرعد', 'من أدعية الاستسقاء', 'الدعاء إذا نزل المطر', 'الذكر بعد نزول المطر', 'من أدعية الاستصحاء', 'دعاء رؤية الهلال', 'الدعاء عند إفطار الصائم', 'الدعاء قبل الطعام', 'الدعاء عند الفراغ من الطعام', 'دعاء الضيف لصاحب الطعام', 'التعريض بالدعاء لطلب الطعام أو الشراب', 'الدعاء إذا أفطر عند أهل بيت', 'دعاء الصائم إذا حضر الطعام ولم يفطر', 'ما يقول الصائم إذا سابه أحد', 'الدعاء عند رؤية باكورة الثمر', 'دعاء العطاس', 'ما يقال للكافر إذا عطس فحمد الله', 'الدعاء للمتزوج', 'دعاء المتزوج و شراء الدابة', 'الدعاء قبل إتيان الزوجة', 'دعاء الغضب', 'دعاء من رأى مبتلى', 'ما يقال في اﻟﻤﺠلس', 'كفارة اﻟﻤﺠلس', 'الدعاء لمن قال غفر الله لك', 'الدعاء لمن صنع إليك معروفا', 'ما يعصم الله به من الدجال', 'الدعاء لمن قال إني أحبك في الله', 'الدعاء لمن عرض عليك ماله', 'الدعاء لمن أقرض عند القضاء', 'دعاء الخوف من الشرك', 'الدعاء لمن قال بارك الله فيك', 'دعاء كراهية الطيرة', 'دعاء الركوب', 'دعاء السفر', 'دعاء دخول القرية أو البلدة', 'دعاء دخول السوق', 'الدعاء إذا تعس المركوب', 'دعاء المسافر للمقيم', 'التكبير و التسبيح في سير السفر', 'دعاء المسافر إذا أسحر', 'الدعاء إذا نزل مترلا في سفر أو غيره', 'ذكر الرجوع من السفر', 'ما يقول من أتاه أمر يسره أو يكرهه', 'فضل الصلاة على النبي صلى الله عليه و سلم', 'إفشاء السلام', 'كيف يرد السلام على الكافر إذا سلم', 'الدعاء عند سماع صياح الديك ونهيق الحمار', 'دعاء نباح الكلب بالليل', 'الدعاء لمن سببته', 'ما يقول المسلم إذا مدح المسلم', 'ما يقول المسلم إذا زكي', 'كيف يلبي المحرم في الحج أو العمرة ؟', 'التكبير إذا أتى الركن الأسود', 'الدعاء بين الركن اليماني والحجر الأسود', 'دعاء الوقوف على الصفا والمروة', 'الدعاء يوم عرفة', 'الذكر عند المشعر الحرام', 'التكبير عند رمي الجمار مع كل حصاة', 'دعاء التعجب والأمر السار', 'ما يفعل من أتاه أمر يسره', 'ما يقول من أحس وجعا في جسده', 'دعاء من خشي أن يصيب شيئا بعينه', 'ما يقال عند الفزع', 'ما يقول عند الذبح أو النحر', 'ما يقول لرد كيد مردة الشياطين', 'الاستغفار و التوبة', 'التسبيح، التحميد، التهليل، التكبير', 'كيف كان النبي يسبح؟', 'من أنواع الخير والآداب الجامعة', 'الرُّقية الشرعية من القرآن الكريم', 'الرُّقية الشرعية من السنة النبوية']
```
To see the category details use 'call_block' as placed:
```py
>>> adkar.call_block('أذكار الصباح')
```


### **Splitting The Pages of The Quran**
In the Holy Quran stamping package, a method of dividing pages with the aim of sealing the Quran, and distributing the division among the pages.

```py
>>> from AL_Khatma.khatma import khatma # Package call
>>> k = khatma(30) # Call the object "khatma" and determine the number of days required to determine. (30) represents the number of days
>>> k.Khatma_page(report=True) # Split Pages command with report printing
[REPORT KHATMA]
Days: 30
Reading Rate: 20 (Page/Day)    # Daily reading rate of Quran completion based on the number of days entered
Weerd: [22, 22, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]
[22, 22, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]
```
A command can be written for ('khatma. Khatma_page') by dividing and applying the distribution directly to the Qur'an and returning a large value. The content of these great values are the verses to be read per day. The way to write it is as follows:

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

#### **Export Khatma to PDF**
> *This package is working on version number: 2.0.0 and top*

You can export khatma to a PDF file, and it's easy, and you should follow these steps

* **First Step**: Download Quran pages for the PDF package:
All you have to do is type this command, which in turn will load the high-resolution Quran pages to your device
```py
>>> from AL_Khatma.pdf_page import quran_pdf
>>> pdf = quran_pdf()
>>> pdf.download_pages()
```

* **Step Two**: Splitting the Qur'an and exporting it to PDF file:
All you have to type is this command, which in turn will export a file. Each file has its own day:
```py
>>> from AL_Khatma.khatma import khatma # Library is called
>>> k = khatma(30) 
>>> k.Khatma_page(pdf=True, down_path_pdf='./weerds', report=True) # The 'pdf' option is activated and the path to which the file will be exported is set by activating the 'down_path_pdf' feature ووضع المسار فيه
# 1 of 30	From 1 -> 22 Page
# Creating PDF file ... [/home/oaokm/weerds/Quran_from_1_to_22.pdf]
100%|████████████████████| 22/22 [00:04<00:00,  4.81it/s]
# 2 of 30	From 23 -> 44 Page
# Creating PDF file ... [/home/oaokm/weerds/Quran_from_23_to_44.pdf]
100%|████████████████████| 22/22 [00:03<00:00,  5.52it/s]
# 3 of 30	From 45 -> 64 Page
# Creating PDF file ... [/home/oaokm/weerds/Quran_from_45_to_64.pdf]
100%|████████████████████| 20/20 [00:03<00:00,  6.09it/s]
# 4 of 30	From 65 -> 84 Page
# Creating PDF file ... [/home/oaokm/weerds/Quran_from_65_to_84.pdf]
100%|████████████████████| 20/20 [00:03<00:00,  5.68it/s]
# 5 of 30	From 85 -> 104 Page
# Creating PDF file ... [/home/oaokm/weerds/Quran_from_85_to_104.pdf]
100%|████████████████████| 20/20 [00:03<00:00,  6.00it/s]
...
# 28 of 30	From 545 -> 564 Page
# Creating PDF file ... [/home/oaokm/weerds/Quran_from_545_to_564.pdf]
100%|████████████████████| 20/20 [00:03<00:00,  5.63it/s]
# 29 of 30	From 565 -> 584 Page
# Creating PDF file ... [/home/oaokm/weerds/Quran_from_565_to_584.pdf]
100%|████████████████████| 20/20 [00:03<00:00,  5.52it/s]
# 30 of 30	From 585 -> 604 Page
# Creating PDF file ... [/home/oaokm/weerds/Quran_from_585_to_604.pdf]
100%||████████████████████| 20/20 [00:03<00:00,  5.75it/s]

[REPORT KHATMA - PDF]
Runing Time: 123.4863281300004
Days: 30
Reading Rate: 20 (Page/Day)
Weerd: [22, 22, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]
Number of Werrd: 30
Path: /home/oaokm/weerds
```
### **Dealing with the PDF package of the Holy Quran**
> *Only works in '2.0.0' and top*

One of the best features of the Al-Khatima Library is the PDF package

There are two ways to export, but before that you must upload high-resolution images of the Holy Quran before taking any steps to handle the package.
The download method is as follows:
```py
>>> from AL_Khatma.pdf_page import quran_pdf
>>> pdf = quran_pdf()
>>> pdf.download_pages()
```

* **First method**: Export the surah:
```py
>>> from AL_Khatma.pdf_page import quran_pdf
>>> from AL_Khatma.quran import Quran
>>> quran = Quran()
>>> sura_one = quran.show_block_aya(1, [])[0]
>>> pdf = quran_pdf(sura_one)
>>> pdf.creating('./quran_pdf')
# Creating PDF file ... [/home/oaokm/quran_pdf/Quran_from_1_to_1.pdf]
100%|██████████████████████| 1/1 [00:00<00:00,  4.72it/s]
```

* **Second method** Using page numbers:
```py
>>> from AL_Khatma.pdf_page import quran_pdf
>>> pdf = quran_pdf()
>>> pdf.creating('./quran_pdf', From=1, to= 10)
# Creating PDF file ... [/home/oaokm/quran_pdf/Quran_from_1_to_10.pdf]
100%|█████████████████████| 10/10 [00:01<00:00,  5.69it/s]
```
You can replace the title of the first page, by adding the 'cover_title=<any text>':

>>> pdf.creating('./quran_pdf', From=1, to= 10, cover_title='al salam alaikum')
# Creating PDF file ... [/home/oaokm/quran_pdf/Quran_from_1_to_10.pdf]
100%|█████████████████████|10/10 [00:01<00:00,  5.86it/s]
```
<p align="center">
  <img src="https://github.com/oaokm/AL-Khatma/blob/main/Pictures/Screenshot_for_a_file_pdf.png?raw=true" alt="picture_screenshot">
</p>

You can export Holy Quran pages to PDF without the first page (cover), by activating the 'cover=False' feature:
```py
>>> from AL_Khatma.pdf_page import quran_pdf
>>> pdf = quran_pdf()
>>> pdf.creating('./quran_pdf', From=1, to= 10, cover=False)
# Creating PDF file ... [/home/oaokm/quran_pdf/Quran_from_1_to_10.pdf]
100%|█████████████████████| 10/10 [00:01<00:00,  5.69it/s]
```

## **Sources**
For the sake of the principle of transparency and religious sensitivity offered by the library, I will mention the sources upon which this library is built.

The sources are as follows:
* [Aya API(Arabic)](https://github.com/nawafalqari/ayah)
* [Quranic verses in other languages](https://github.com/risan/quran-json)
* Sources download pages of the Holy Quran:
  * [The official website of Ayat King Saud University](https://quran.ksu.edu.sa/ayat/)
  * [Quranic researcher website(Arabic)](https://tafsir.app/)


## **License**
[MIT License © Osamah Awadh](https://github.com/oaokm/AL-Khatma/blob/main/LICENSE)
