# #!/usr/bin/env python
# # -*- coding: UTF-8 -*-
# """
# @File    ：pvp.py
# @IDE     ：PyCharm
# @Author  ：瑞瑞爱躺平..
# @Date    ：2023/9/13 14:57
# """
import re

import requests
from bs4 import BeautifulSoup


def get_image(page):
    try:
        response = requests.get(f'https://pvp.qq.com/web201605/herodetail/{page}.shtml')  # 发送GET请求获取网页内容
        response.raise_for_status()  # 检查请求是否成功
        response.encoding = response.apparent_encoding  # 设置响应的编码方式
        html = response.text  # 获取网页内容
        soup = BeautifulSoup(html, 'html.parser')  # 使用BeautifulSoup解析网页内容
        div_class = soup.select('div.zk-con1')  # 选择所有class为'zk-con1'的div元素
        href = []  # 创建一个空列表用于存储图片链接
        for div in div_class:  # 遍历所有选中的div元素
            style = div.get('style')  # 获取div元素的style属性值
            if style:  # 如果style属性值存在
                match = re.search(r'url\((.*?)\)', style)  # 使用正则表达式匹配图片链接
                if match:  # 如果匹配成功
                    href.append(match.group(1))  # 将匹配到的图片链接添加到列表中
        image = href[0]
        return image[3:-1]
    except requests.RequestException as e:  # 处理请求异常
        print(f'Request error: {e}')  # 打印请求异常信息
    except Exception as e:  # 处理其他异常
        print(f'Error: {e}')  # 打印其他异常信息


def get_name_skin():
    response = requests.get('https://pvp.qq.com/web201605/js/herolist.json')
    datas = response.json()
    # print(datas)
    with open("test.txt", "w", encoding='utf-8') as f:
        for data in datas:
            name = data['cname']
            # print(name)
            skin = data.get('skin_name')
            # print(skin)
            page = data['ename']
            # print(page)
            url = get_image(page)
            # print(url)
            # asdw
            if not url.startswith(('http://', 'https://')):  # 如果URL不以'http://'或'https://'开头
                url = 'https://' + url.strip()  # 在URL前添加'https://'，并去除首尾的空格
            with open(f"images/{name}.jpg", "wb") as img_file:
                img_file.write(requests.get(url).content)
                # ad
            f.write(name)
            f.write(' ')
            if skin is not None:
                f.write(skin)
            f.write(' ')
            f.write(url)
            f.write('\n')


if __name__ == '__main__':
    get_name_skin()
