import requests
import os
import json
from .log import log
from .__init__ import __version__
from .__init__ import json_edit
from random import randint
import webbrowser

__main_path__ = os.path.dirname(__file__)
file_name     = __file__.split('/')[-1]


class message:
    def __init__(self):
        self.url_message = "https://raw.githubusercontent.com/oaokm/AL-Khatma/main/DATA/message.json"
        self.info        = json.load(open(f'{__main_path__}/DATA/info.json', 'r+'))

    def cheak_version(self, show_me_last=False):
        #? احتمالية ظهور الرسالة 2/5
        if randint(1, 5) == 3:
            try:
                JSONWEB = requests.get(url=self.url_message, timeout=5)
                log(
                    f'{file_name} > message system | Status JSON File Cheak', 
                    f'Read: True, url: {self.url_message}'
                    ).write_message()
                log(
                f'{file_name} > message system | Status Code to request json file', 
                f'code: {JSONWEB.status_code}, url: {self.url_message}'
                ).write_message()

                if JSONWEB.status_code == 200:
                    JSONFILE = JSONWEB.json()
                    if JSONFILE[0]['version'] != __version__:
                        json_edit(f'{__main_path__}/DATA/info.json').edit('Is_a_new', "False")

                        log(
                        f'{file_name} > message system | Found New Version', 
                        f'We found new version({JSONFILE[0]["version"]}), Please enter "pip install AL-Khatma-lib -U" or "pip install AL-Khatma-lib --upgrade"'
                        ).write_message()
                        
                        print(JSONFILE[1][0]['Message'].format(JSONFILE[0]["version"]))
                    
                    elif JSONFILE[0]['version'] == __version__ and self.info['Is_a_new'] == "False":
                        json_edit(f'{__main_path__}/DATA/info.json').edit('Version', __version__)
                        json_edit(f'{__main_path__}/DATA/info.json').edit('Is_a_new', "True")
                        print("\n\n\t Now opening update page on github, Please wait... \n\n")
                        webbrowser.open_new_tab('https://github.com/oaokm/AL-Khatma/blob/main/UPDATE.md')
                    
                    else:
                        log(
                        f'{file_name} > message system | Last Version', 
                        f'This is version ({__version__}) is last.'
                        ).write_message()
                        if show_me_last: print(f'This is version ({__version__}) is last.')
                else:
                    pass
            #? في حال عدم وجود إنترنت يتم رفض الأمر
            except requests.exceptions.ConnectionError as e:
                log(
                f"{file_name} > message system | Check The Internet Status",
                f"The WiFi connection error, please check your internet, {e}"
                ).write_message()
        else:
            pass