# _*_ coding=utf-8 _*_

import pandas as pd

"""Series的整数索引:
    索引与标签均为整数，存在相等的情况
"""

arr = pd.Series([1, 2, 3, 4, 5], index=[1, 2, 3, 4,5])
# 直接访问或默认为使用标签
# print(arr[-1])    # 使用[-1]会报错
print(arr[2])

# lock将索引解释为标签
print(arr.loc[2])

# ilock将索引解释为下标
print(arr.iloc[2])
