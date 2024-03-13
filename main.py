import win32com.client

PATH = "C:\\Users\\max16\\Desktop\\Stocks\\pytrader"

instCpCybos = win32com.client.Dispatch("CpUtil.CpCodeMgr")
excel = win32com.client.Dispatch("Excel.Application")
excel.Visible = True
wb = excel.Workbooks.Add()
ws = wb.Worksheets("Sheet1")

code_list = instCpCybos.GetStockListByMarket(1)

for i, code in enumerate(code_list):
    second_code = instCpCybos.GetStockSectionKind(code)
    name = instCpCybos.CodeToName(code)
    ws.Range(f"A{i + 1}").Value = i + 1
    ws.Range(f"B{i + 1}").Value = code
    ws.Range(f"C{i + 1}").Value = second_code
    ws.Range(f"D{i + 1}").Value = name

wb.SaveAs(f"{PATH}\\kospi.xlsx")
excel.Quit()
    
