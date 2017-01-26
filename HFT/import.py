import pandas_datareader.data as web
start = "1949/5/12"
end = "2016/12/31"
N225 = web.DataReader("NIKKEI225", 'find', start, end)
N225.head(1)
