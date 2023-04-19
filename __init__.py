'''
    MIT License

    Copyright (C) 2023 Osamah Awadh (https://github.com/oaokm)

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
'''
import os

__version__   = '1.0.0'
__main_path__ = os.path.dirname(__file__)

os.chdir(path=__main_path__)
try:
    from AL_Khatma.log import log
except ModuleNotFoundError:
    from log import log

class ALKhatma:
    def __init__ (self):
        log(
                f'{__file__} | Conjugation Status ', 
                f'True'
                ).write_message()
        os.chdir(path=__main_path__)

    def License(self):
        log(
            f'{__file__} | License Request ', 
            f'The user to been request the program license'
            ).write_message()
        os.chdir(path=__main_path__)
        with open('./LICENSE', 'r', encoding='utf8') as license:
            return print(license.read())
    
    def where_me(self):
        log(
            f'{__file__} | Where Me Request ', 
            f'The user to been request the path program'
            ).write_message()
        return __main_path__

    def show_me_log(self):
        log(
            f'{__file__} | Show Me Log Request ', 
            f'The user to been request the path log file'
            ).write_message()
        return f"{__main_path__}/DATA/loging.log"

if __name__ == "__main__":
    print("")
