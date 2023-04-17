from datetime import datetime as dt
try:
    import AL_Khatma
except ModuleNotFoundError:
    import __init__ as AL_Khatma
def nowing():
    return dt.now().timestamp()

class log:

    def __init__(self, title:str, mess:str):
        self.log      = open(f'{AL_Khatma.__main_path__}/DATA/loging.log', 'r+', encoding='utf8')
        self.title    = title
        self.mess     = mess
        self.log_list = self.log.read().split('\n')


    def write_message(self, time=True):
        
        if time: self.log.write(f"\n[{self.title}|({nowing()})] {self.mess}")
        
        else: self.log.write(f"\n[{self.title}] {self.mess}")

