
import requests
import os
import urllib.request
from bs4 import BeautifulSoup


class GetXkcdData:

    def __init__(self):
        r = requests.get("https://c.xkcd.com/random/comic/")
        soup = BeautifulSoup(r.text, "html.parser")

        # Div That Contains Actual Comic Image
        img_div = soup.find(id="comic")

        self.img_src = 'https://'
        self.img_src += img_div.find('img')['src'][2:]

        self.img_save_name = self.img_src.split("/")[-1]

        self.img_title = img_div.find('img')['title']

    def post_title(self):
        # limiting character count
        if len(self.img_title) >= 280:
            return(self.img_title[:200] + "... #xkcd #botlife #comic")
        return(self.img_title + " #xkcd #botlife #comic")

    def download_xkcd_comic(self):
        d = urllib.request.urlretrieve(self.img_src, self.img_save_name)
        return d[0]
        print("#posting#")

    def delete_xkcd_comic(self):
        os.remove(self.img_save_name)
        print("deleting file")
