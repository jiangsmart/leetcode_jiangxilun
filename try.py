# -*- coding:utf-8 -*-
# write code here
s = "afdadsf"
hash_str = {}                    # 初始化新的hash
for c in s:
    if hash_str.get(c) == None:  # 获取该键值下的value，没有返回None
        hash_str.update({c: 1})  # 更新字典的操作/为字典添加新的元素
    else:
        hash_str[c] += 1         # 更改hash下的vale
for c in s:
    if hash_str.get(c) == 1:
        print c
        break
