from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import OrderedDict
url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"
conn =urlopen(url)
raw_data = conn.read()
content = raw_data.decode("utf8")
# print(content)
soup = BeautifulSoup(content, "html.parser")
ul = soup.find("div","cf_ResearchDataHistoryInfo")
l = ul.find_all("td")
m =[]
for i in l:
    