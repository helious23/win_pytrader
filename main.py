import win32com.client

instCpCodeMgr = win32com.client.Dispatch("CpUtil.CpCodeMgr")
instMarketEye = win32com.client.Dispatch("CpSysDib.MarketEye")

target_code_list = instCpCodeMgr.GetGroupCodeList(5)

# Get PER
instMarketEye.SetInputValue(0, 67)
instMarketEye.SetInputValue(1, target_code_list)

# BlockRequest
instMarketEye.BlockRequest()

#GetHeaderValue
num_stock = instMarketEye.GetHeaderValue(2)

sum_per = 0
for i in range(num_stock):
    sum_per += instMarketEye.GetDataValue(0, i)

print(f"Average PER: {sum_per / num_stock}")