#coding:utf-8
import numpy as np
import pandas as pd
import datetime
import pandas_datareader.data as pdd

# 期間設定
date_from = datetime.date(2016, 11, 5)
date_to = datetime.date(2017, 1, 25)

# 単一銘柄の取得
aapl = pdd.DataReader('AAPL', "yahoo", date_from, date_to)
print ("AAPL")
print (aapl)
