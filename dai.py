import time

import requests
from bs4 import BeautifulSoup

urls = [f"https://pvp.qq.com/web201605/herodetail/{page}.shtml" for page in range(105, 600)]

begin = time.time()
sum_name = 0
for url in urls:
    response = requests.get(url)
    response.encoding = response.apparent_encoding
    html = response.text
    if response.status_code != 200:
        continue
    soup = BeautifulSoup(html)

    name = soup.select('h2.cover-name')

    print(name[0].text)
    sum_name += 1
print(sum_name)
end = time.time()
print(end - begin)


