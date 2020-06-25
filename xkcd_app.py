
import requests
import urllib.request
from textblob import TextBlob
from bs4 import BeautifulSoup


class GetXkcdData:

    r = requests.get("https://c.xkcd.com/random/comic/")
    soup = BeautifulSoup(r.text, "html.parser")

    # Div That Contains Actual Comic Image
    img_div = soup.find(id="comic")

    img_src = 'https://'
    img_src += img_div.find('img')['src'][2:]

    img_save_name = img_src.split("/")[-1]

    img_title = img_div.find('img')['title']

    def post_title(self):
        return(self.img_title)

    def download_xkcd_comic(self):
        d = urllib.request.urlretrieve(self.img_src, self.img_save_name)
        return d[0]


a = GetXkcdData()

print(a.post_title())
