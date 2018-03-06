import tushare as ts

sdf = ts.get_stock_basics()
stock_list = list(sdf.index)
for code in stock_list:
	df = ts.get_hist_data(code)
	if df is not None:
		df.to_csv("..\\data\\" + code + ".csv")
	else:
		print(code)

