from datetime import datetime as dt
import os

__main_path__ = os.path.dirname(__file__)

def nowing():
    return dt.now().timestamp()

class log:

    def __init__(self, title:str, mess:str):
        if os.path.exists(path=f'{__main_path__}/DATA/loging.log'):
            self.log      = open(f'{__main_path__}/DATA/loging.log', 'a+', encoding='utf8')
            self.title    = title
            self.mess     = mess
            self.log_list = self.log.read().split('\n')
        else:
            try:
                os.makedirs(f'{__main_path__}/DATA/')
            except FileExistsError:
                pass
            self.log      = open(f'{__main_path__}/DATA/loging.log', 'a+', encoding='utf8')
            self.title    = title
            self.mess     = mess
            self.log_list = self.log.read().split('\n')

    def write_message(self, time=True):
        
        if time: self.log.write(f"\n[{self.title}|({nowing()})] {self.mess}")
        
        else: self.log.write(f"\n[{self.title}] {self.mess}")

