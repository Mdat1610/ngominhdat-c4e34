from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import OrderedDict
from youtube_dl import YoutubeDL
url = "https://www.apple.com/itunes/charts/songs/"
conn =urlopen(url)
raw_data = conn.read()
content = raw_data.decode("utf8")
# print(content)
soup = BeautifulSoup(content, "html.parser")
ul = soup.find("section","section chart-grid")
# print(ul.prettify())
li_list = ul.find_all("li")
m = []
for li in li_list:
    a = li.h3.a
    b = li.h4.a
    name_song = a.string.strip()
    artist = b.string.strip()
    n = OrderedDict({
        "name_song": name_song,
        "artist": artist,
    })
    m.append(n)
    options = {'default_search': 'ytsearch', 
    'max_downloads': 1}
    dl = YoutubeDL(options)
    dl.download(['{0} {1}'. format(name_song,artist )])
import pyexcel
pyexcel.save_as(records=m, dest_file_name="itunes.xls")

    

