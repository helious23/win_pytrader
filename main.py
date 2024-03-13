import win32com.client

PATH = "C:\\Users\\max16\\Desktop\\Stocks\\pytrader"


def check_volume(instStockChart, code):
    # SetInputValue
    instStockChart.SetInputValue(0, code)
    instStockChart.SetInputValue(1, ord('2')) # 갯수로 요청
    instStockChart.SetInputValue(4, 60) # 60일치
    instStockChart.SetInputValue(5, 8) # 거래량
    instStockChart.SetInputValue(6, ord("D")) # 일봉
    instStockChart.SetInputValue(9, ord("1"))

    # BlockRequest
    instStockChart.BlockRequest()

    # GetData
    volumes= []
    num_data = instStockChart.GetHeaderValue(3)
    for i in range(num_data):
        volume = instStockChart.GetDataValue(0, i)
        volumes.append(volume)

    # Calculate average volume
    average_volume = (sum(volumes) - volumes[0]) / (len(volumes) -1)

    if(volumes[0] > average_volume *10):
        return 1
    else:
        return 0

if __name__ == "__main__":
    instStockChart = win32com.client.Dispatch("CpSysDib.StockChart")
    instStockCode = win32com.client.Dispatch("CpUtil.CpStockCode")

    instCpCodeMgr = win32com.client.Dispatch("CpUtil.CpCodeMgr")
    code_list = instCpCodeMgr.GetStockListByMarket(1)

    buy_list = []


    for code in code_list:
        if check_volume(instStockChart, code) == 1:
            buy_list.append(code)
            print(instStockCode.CodeToName(code))