import win32com.client

PATH = "C:\\Users\\max16\\Desktop\\Stocks\\pytrader"

instStockChart = win32com.client.Dispatch("CpSysDib.StockChart")
instStockCode = win32com.client.Dispatch("CpUtil.CpStockCode")
code = instStockCode.NameToCode("테크윙")

instStockChart.SetInputValue(0, code)
instStockChart.SetInputValue(1, ord('2')) # 갯수로 요청
instStockChart.SetInputValue(4, 60) # 60일치
instStockChart.SetInputValue(5, 8) # 거래량
instStockChart.SetInputValue(6, ord("D")) # 일봉
instStockChart.SetInputValue(9, ord("1"))

instStockChart.BlockRequest()

volumes= []
num_data = instStockChart.GetHeaderValue(3)
for i in range(num_data):
    volume = instStockChart.GetDataValue(0, i)
    volumes.append(volume)

average_volume = (sum(volumes) - volumes[0]) / (len(volumes) -1)

if(volumes[0] > average_volume *10):
    print("대박 주")
else:
    print("일반 주", volumes[0] / average_volume)
