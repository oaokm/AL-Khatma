import requests
import os
import json
from .log import log
from tqdm import tqdm
import platform

main_path = os.path.dirname(__file__)

class cheak:

    def __init__(self):
        self.download_file = list()
        self.path_url      = list()
        self.system_path   = json.load(open(f'{main_path}/DATA/path_system.json', 'r'))
        try:
            self.system_path[platform.system()]
        except KeyError:
            log(
            f"{__file__} > cheak >  | Error: Key Error",
            f"Switch path system to '/' , system: {platform.system()}, uname:{platform.uname()}"
            ).write_message()
            self.system_path = '/'

        try:
            self.JSONFILE      = requests.get(
                url="https://raw.githubusercontent.com/oaokm/AL-Khatma/main/DATA/cheak_download.json").json()
        except requests.exceptions.ConnectionError as e:
            log(
            f"{__file__} > cheak > __init__ | Check The Internet Status",
            f"The WiFi connection error, please check your internet"
            ).write_message()
            print(f"[ cheak | __init__ > The WiFi connection error ] {e}")

    def find_DATA_folder(self, showme_log=False):
        for block in self.JSONFILE:
            path = f"{main_path}{self.system_path[platform.system()]}{block['name_folder']}"
            for ch in block['files']:
                cheak_file = os.path.exists(path=f"{path}{self.system_path[platform.system()]}{ch}")
                
                if showme_log: print(f'[{path}{self.system_path[platform.system()]}{ch}] {cheak_file}')
                
                if not cheak_file: self.download_file.append(f'{path}{self.system_path[platform.system()]}{ch}')
            else:
                continue


        for i in range(len(self.download_file)):
            text = self.download_file[i].split(self.system_path[platform.system()])
            for y in range(len(text)):
                if text[-y-1] == "AL_Khatma":
                    self.path_url.append("/".join(text[-y:]))
                    break
                else: continue
        return self.download_file

    def download(self):
        if self.path_url != []:
            print(f"# Download DATA Folder in {os.path.dirname(self.download_file[0])}")
            
            for download in tqdm(range(len(self.path_url))):
                if not os.path.exists(os.path.dirname(self.download_file[download])):
                    os.makedirs(os.path.dirname(self.download_file[download]))
                github_file = requests.get(
                        url=f"https://raw.githubusercontent.com/oaokm/AL-Khatma/main/{self.path_url[download]}"
                            )
                if github_file.status_code == 200:
                    with open(self.download_file[download], 'wb') as f:
                        f.write(github_file.content)
                        f.close()
                        
                else:
                    print(f"[INFO]\nURL: {github_file.url}\tStatus Code: {github_file.status_code}")
        else:
            print("[cheak.py] Status folder is very good")

if __name__ == '__main__':
    c = cheak()
    c.find_DATA_folder()
    c.download()