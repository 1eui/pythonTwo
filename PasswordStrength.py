#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@File    ：PasswordStrength.py
@IDE     ：PyCharm
@Author  ：瑞瑞爱躺平..
@Date    ：2023/7/2 14:18
"""


def crypt(source, key):
    # 导入itertools模块中的cycle函数
    from itertools import cycle
    # 初始化结果字符串
    result = ''
    # 生成一个无限循环的迭代器，用于循环遍历密钥
    temp = cycle(key)
    # 遍历源字符串中的每个字符
    for ch in source:
        # 将源字符串中的字符与密钥中的字符进行异或运算，并将结果转换为字符，然后拼接到结果字符串中
        result = result + chr(ord(ch) ^ ord(next(temp)))
    # 返回加密后的结果字符串
    return result


# 定义源字符串和密钥
source = 'Shandong Institute of Business and Technology'
key = 'Dong Fufuo'
# 打印加密前的源字符串
print('Before Encryption:' + source)
# 调用crypt函数进行加密，并打印加密后的结果字符串
encrypted = crypt(source, key)
print('After Encryption:' + encrypted)
# 调用crypt函数进行解密，并打印解密后的结果字符串
decrypted = crypt(encrypted, key)
print('After Decryption:' + decrypted)

'''
该代码实现的功能是使用异或运算对字符串进行加密和解密。

代码的具体步骤如下：
1. 定义一个名为`crypt`的函数，该函数接受两个参数：`source`和`key`。
2. 导入`itertools`模块中的`cycle`函数。
3. 初始化一个空字符串`result`。
4. 使用`cycle`函数将`key`转换为一个可循环迭代的对象`temp`。
5. 对于`source`中的每个字符`ch`，执行以下操作：
   - 将`ch`与`temp`的下一个元素进行异或运算，并将结果转换为字符。
   - 将得到的字符添加到`result`中。
6. 返回加密后的字符串`result`。
7. 定义一个名为`source`的字符串变量，赋值为`'Shandong Institute of Business and Technology'`。
8. 定义一个名为`key`的字符串变量，赋值为`'Dong Fufuo'`。
9. 打印出加密前的字符串`source`。
10. 调用`crypt`函数，将`source`和`key`作为参数传入，将返回的加密后的字符串赋值给`encrypted`。
11. 打印出加密后的字符串`encrypted`。
12. 调用`crypt`函数，将`encrypted`和`key`作为参数传入，将返回的解密后的字符串赋值给`decrypted`。
13. 打印出解密后的字符串`decrypted`。
'''

import string


# 定义一个函数，用于检查密码的强度
def check(pwd):
    # 如果传入的参数不是字符串类型或者长度小于6，则返回提示信息
    if not isinstance(pwd, str) or len(pwd) < 6:
        return 'not suitable for password'

    # 定义一个字典，用于存储不同强度的密码对应的描述
    d = {1: 'weak', 2: 'below middle', 3: 'above middle', 4: 'strong'}

    # 定义一个列表，用于记录密码中包含的不同类型字符的情况
    r = [False] * 4

    # 遍历密码中的每个字符
    for ch in pwd:
        # 如果数字字符在密码中且之前没有出现过，则将r[0]设置为True
        if not r[0] and ch in string.digits:
            r[0] = True
        # 如果小写字母字符在密码中且之前没有出现过，则将r[1]设置为True
        elif not r[1] and ch in string.ascii_lowercase:
            r[1] = True
        # 如果大写字母字符在密码中且之前没有出现过，则将r[2]设置为True
        elif not r[2] and ch in string.ascii_uppercase:
            r[2] = True
        # 如果特殊字符在密码中且之前没有出现过，则将r[3]设置为True
        elif not r[3] and ch in ',.!;?<>':
            r[3] = True

    # 根据r中True的个数，返回对应的密码强度描述，如果r中True的个数不在d的键中，则返回'error'
    return d.get(r.count(True), 'error')


# 调用check函数，传入一个密码进行检查，并打印结果
print(check('a2Cd123E,'))
'''
该代码实现的功能是检查密码的强度。

代码的具体步骤如下：
1. 导入字符串模块。
2. 定义一个名为`check`的函数，该函数接受一个参数`pwd`，用于检查密码的强度。
3. 首先判断`pwd`是否为字符串类型且长度是否小于6，如果是，则返回"not suitable for password"。
4. 创建一个字典`d`，其中键为1、2、3、4，值分别为"weak"、"below middle"、"above middle"、"strong"，用于表示密码的强度级别。
5. 创建一个长度为4的布尔值列表`r`，用于记录密码中是否包含数字、小写字母、大写字母和特殊字符。
6. 遍历密码中的每个字符。
7. 如果`r[0]`为False且当前字符在数字字符串中，则将`r[0]`设置为True。
8. 否则，如果`r[1]`为False且当前字符在小写字母字符串中，则将`r[1]`设置为True。
9. 否则，如果`r[2]`为False且当前字符在大写字母字符串中，则将`r[2]`设置为True。
10. 否则，如果`r[3]`为False且当前字符在特殊字符字符串中，则将`r[3]`设置为True。
11. 返回字典`d`中对应`r`中True的数量的值，如果没有对应的值，则返回"error"。
12. 调用`check`函数并传入一个密码字符串作为参数，并将结果打印出来。
'''
