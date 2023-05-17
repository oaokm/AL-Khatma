'''
    MIT License | Copyright (C) 2023 Osamah Awadh (https://github.com/oaokm)
'''

import os
from .log import log
from .cheak import cheak
import json
import platform

#! لا تقم بتغير رقم الإصدار
#! Do not change the version
__version__   = '2.0.2'
__main_path__ = os.path.dirname(__file__)

class json_edit:
    def __init__(self, name_file:str, refresh=False):
        self.name_file = name_file
        self.refresh   = refresh
    
    def info_file(self):
        if not os.path.exists(path=f"{__main_path__}/DATA/info.json") or self.refresh:
            INFO = {
                "API_name": "AL-Khatma",
                "Version": __version__,
                "Is_a_new": "True",
                "License": "MIT",
                "Progjet_page": "https://github.com/oaokm/AL-Khatma",
                "Author": "Osamah Awadh",
                "system_tpye": platform.system(),
                "version_system": platform.version(),
                "platform": platform.platform(),
                "refresh": "True"
            }
            with open(f"{__main_path__}/DATA/info.json", 'w') as info :
                info.write(json.dumps(INFO, indent=4, ensure_ascii=False))
        else:
            pass
            

    def edit(self, arge:str ,value):
        with open(self.name_file, 'r+') as f:
            data = json.load(f)
            data[arge] = value
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()

def Download_DATA():
    log(
        f'{__file__} | Download DATA Request ', 
        f'The user to been request the cheak and download files form Github'
        ).write_message()
    json_edit(f'{__main_path__}/DATA/info.json', refresh=True).info_file()
    down       = cheak()
    list_files = down.find_DATA_folder()
    if list_files != []:
        down.download()
    else:
        print("[Download_DATA | Status Scan] All files are uploaded")

def where_me():
    log(
        f'{__file__} | Where Me Request ', 
        f'The user to been request the path program'
        ).write_message()
    return __main_path__

def show_me_log():
    log(
        f'{__file__} | Show Me Log Request ', 
        f'The user to been request the path log file'
        ).write_message()
    return f"{__main_path__}/DATA/loging.log"
