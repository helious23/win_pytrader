import win32com.client

PATH = "C:\\Users\\max16\\Desktop\\Stocks\\pytrader"

instStockChart = win32com.client.Dispatch("CpSysDib.StockChart")

instStockChart.SetInputValue(0, "A089030") # 종목코드
instStockChart.SetInputValue(1, ord("1")) # 1: 기간, 2: 갯수
instStockChart.SetInputValue(2, 20240313) # 종료일
instStockChart.SetInputValue(3, 20230314) # 시작일
# instStockChart.SetInputValue(4, 10) # 요청 개수
instStockChart.SetInputValue(5, (0, 2, 3, 4, 5, 8)) # 필드
instStockChart.SetInputValue(6, ord("D")) # 차트 구분 D:일
instStockChart.SetInputValue(9, ord("1"))

instStockChart.BlockRequest()

num_data = instStockChart.GetHeaderValue(3)

# SetInputValue(5, xxx) 에서 요청한 필드의 수
num_field = instStockChart.GetHeaderValue(1)

print(num_data)
print(num_field)
print("일자", "시가", "고가", "저가", "종가", "거래량")
for i in range(num_data):
    for j in range(num_field):
        print(instStockChart.GetDataValue(j, i), end=" ")
    print("")