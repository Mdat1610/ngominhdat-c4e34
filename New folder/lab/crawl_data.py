from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import OrderedDict
# 1. Open Connection
url = "https://dantri.com.vn"
conn = urlopen(url)
raw_data = conn.read()
content = raw_data.decode('utf8')
# print(content)

# 2. Find ROI(ROI là vùng mình cần lấy)
soup = BeautifulSoup(content, "html.parser")
ul = soup.find("ul","ul1 ulnew")
# print(ul.prettify())

# 3. Extract ROI
li_list = ul.find_all("li")
m = []
for li in li_list:

# li = li_list[0]


    a = li.h4.a

    title = a.string.strip()
    
    link = url + a["href"]
    n = OrderedDict({
        "title": title,
        "link": link,
    }) 
    m.append(n)



# 4. Save data
import pyexcel

pyexcel.save_as(records=m, dest_file_name="your_file.xls")