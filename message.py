import requests
import os
from .log import log
from .__init__ import __version__

__main_path__ = os.path.dirname(__file__)
file_name     = __file__.split('/')[-1]

class message:
    def __init__(self):
        self.url_message = "https://raw.githubusercontent.com/oaokm/AL-Khatma/main/DATA/message.json"
        
    def cheak_version(self):
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
                    log(
                    f'{file_name} > message system | Found New Version', 
                    f'We found new version({JSONFILE[0]["version"]}), Please enter "pip install AL-Khatma-lib -U" or "pip install AL-Khatma-lib --upgrade"'
                    ).write_message()
                    
                    print(JSONFILE[1][0]['Message'].format(JSONFILE[0]["version"]))
                
                else:
                    log(
                    f'{file_name} > message system | Last Version', 
                    f'This is version ({__version__}) is last.'
                    ).write_message()
            else:
                pass
        #? في حال عدم وجود إنترنت يتم رفض الأمر
        except requests.exceptions.ConnectionError as e:
            log(
            f"{file_name} > message system | Check The Internet Status",
            f"The WiFi connection error, please check your internet, {e}"
            ).write_message()
            