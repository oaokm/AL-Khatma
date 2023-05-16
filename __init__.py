'''
    MIT License | Copyright (C) 2023 Osamah Awadh (https://github.com/oaokm)
'''

import os
from .log import log
from .cheak import cheak

#! لا تقم بتغير رقم الإصدار
#! Do not change the version
__version__   = '2.0.0'
__main_path__ = os.path.dirname(__file__)


def Download_DATA():
    log(
        f'{__file__} | Download DATA Request ', 
        f'The user to been request the cheak and download files form Github'
        ).write_message()
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
