import win32com.client

PATH = "C:\\Users\\max16\\Desktop\\Stocks\\pytrader"

instMarketEye = win32com.client.Dispatch("CpSysDib.MarketEye")
instStockCode = win32com.client.Dispatch("CpUtil.CpStockCode")
code = instStockCode.NameToCode("테크윙")

instMarketEye.SetInputValue(0, (4, 67, 70, 111)) # 현재가, PER, EPS, 최근분기년월
instMarketEye.SetInputValue(1, code)

instMarketEye.BlockRequest()


print(f"현재가: {instMarketEye.GetDataValue(0, 0)}")
print(f"PER: {instMarketEye.GetDataValue(1, 0)}")
print(f"EPS: {instMarketEye.GetDataValue(2, 0)}")
print(f"최근분기년월: {instMarketEye.GetDataValue(3, 0)}")
