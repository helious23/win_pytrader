import win32com.client

instCpCodeMgr = win32com.client.Dispatch("CpUtil.CpCodeMgr")
industry_code_list = instCpCodeMgr.GetIndustryList()

for industry_code in industry_code_list:
    print(industry_code, instCpCodeMgr.GetIndustryName(industry_code))