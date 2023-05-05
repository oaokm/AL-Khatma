<p align="center">
  <img src="https://raw.githubusercontent.com/oaokm/AL-Khatma/main/Logo/AL_Khatma_logo_one.png" alt="AL-Khatma Logo For Arabic and English">
</p>

<p align="center">
  <a href="https://github.com/oaokm/AL-Khatma/blob/main/README.md">Arabic</a>
  &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="https://github.com/oaokm/AL-Khatma/blob/main/README_EN.md">English</a>
</p>

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
     * Indian 
* **The Holy Quran Seal Package**.
   * Write the number of days of completion, and give the appropriate plan for that in details.

>**Note**: It will be announced in the next versions.

There are additional packages being working on, such as:
* Azkar package.
* Quranic interpretation package.


## **Download**

### **The First Way: Download From Github**
- One: Form Command Line:
```sh
S git clone https://github.com/oaokm/AL-Khatma
```

- Two: Form Github Page: Download it from your browser as a .zip file.


### **The Second Way: Pypi**
```sh
$ pip install AL-Khatma-lib
```
**OR**
```sh
$ pip3 install AL-Khatma-lib
```

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
