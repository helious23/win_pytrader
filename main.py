import os
import win32com.client
import pythoncom
from dotenv import load_dotenv

load_dotenv()

# login event 클래스 구현
class XASessionEventHandler:
    login_state = 0

    def OnLogin(self, code, msg):
        if code == "0000":
            print("로그인 성공")
            XASessionEventHandler.login_state = 1
        else:
            print("로그인 실패")

# Instance 생성
instXASession = win32com.client.DispatchWithEvents("XA_Session.XASession", XASessionEventHandler)

id = os.getenv("ID")
passwd = os.getenv("PASSWD")
cert_passwd = os.getenv("CERT_PASSWD")

instXASession.ConnectServer("demo.ebestsec.co.kr", 20001) # 모의투자서버
instXASession.Login(id, passwd, cert_passwd, 0, 0)

# event 기다리기 위해 pythoncom.PumpWaitingMessage
while XASessionEventHandler.login_state == 0:
    pythoncom.PumpWaitingMessages()

# 계좌 조회
num_account = instXASession.GetAccountListCount()

for i in range(num_account):
    account = instXASession.GetAccountList(i)
    print(f"계좌번호: {account}")

RES_PATH = "C:\\eBest\\xingAPI\\Res"

# class 생성
class XAQueryEventHandlerT1102:
    query_state = 0

    def OnReceiveData(self, code):
        XAQueryEventHandlerT1102.query_state = 1

# instance 등록
instXAQueryT1102 = win32com.client.DispatchWithEvents("XA_DataSet.XAQuery",XAQueryEventHandlerT1102)

# t1102 등록
instXAQueryT1102.ResFileName = f"{RES_PATH}\\t1102.res"

# t1102 입력 데이터 설정
instXAQueryT1102.SetFieldData("t1102InBlock", "shcode", 0, "000250") # SetFieldData("블록명", "필드명", 단일데이터=0), "입력값"

# 입력 데이터 전송
instXAQueryT1102.Request(0)

while XAQueryEventHandlerT1102.query_state == 0:
    pythoncom.PumpWaitingMessages()

name = instXAQueryT1102.GetFieldData("t1102OutBlock", "hname", 0) # hname: 한글종목명
price = instXAQueryT1102.GetFieldData("t1102OutBlock", "price", 0) # price: 현재가
print(f"종목명: {name}\n현재가: {price}")

class XAQueryEventHandlerT8430:
    query_state = 0

    def OnReceiveData(self, code):
        XAQueryEventHandlerT8430.query_state = 1

instXaQueryT8430 = win32com.client.DispatchWithEvents("XA_DataSet.XAQuery", XAQueryEventHandlerT8430)
instXaQueryT8430.ResFileName = f"{RES_PATH}\\t8430.res"

instXaQueryT8430.SetFieldData("t8430InBlock", "gubun", 0, 2)
instXaQueryT8430.Request(0)

while XAQueryEventHandlerT8430.query_state == 0:
    pythoncom.PumpWaitingMessages()

T8430_OUT_BLOCK = "t8430OutBlock"

count = instXaQueryT8430.GetBlockCount(T8430_OUT_BLOCK)

for i in range(5):
    hname = instXaQueryT8430.GetFieldData(T8430_OUT_BLOCK, "hname", i)
    shcode = instXaQueryT8430.GetFieldData(T8430_OUT_BLOCK, "shcode", i)
    expcode = instXaQueryT8430.GetFieldData(T8430_OUT_BLOCK, "expcode", i)
    etfgubun = instXaQueryT8430.GetFieldData(T8430_OUT_BLOCK, "etfgubun", i)
    print(i, hname, shcode, expcode, etfgubun)


class XAQueryEventHandlerT8410:
    query_state = 0

    def OnReceiveData(self, code):
        XAQueryEventHandlerT8410.query_state = 1

instXaQueryT8410 = win32com.client.DispatchWithEvents("XA_DataSet.XAQuery", XAQueryEventHandlerT8410)
instXaQueryT8410.ResFileName = f"{RES_PATH}\\t8410.res"

T8410_IN_BLOCK = "t8410InBlock"
T8410_OUT_BLOCK = "t8410OutBlock1"

instXaQueryT8410.SetFieldData(T8410_IN_BLOCK, "shcode", 0, "000250")
instXaQueryT8410.SetFieldData(T8410_IN_BLOCK, "gubun", 0,"2")
instXaQueryT8410.SetFieldData(T8410_IN_BLOCK, "sdate", 0, "20240301")
instXaQueryT8410.SetFieldData(T8410_IN_BLOCK, "edate", 0, "20240314")
instXaQueryT8410.SetFieldData(T8410_IN_BLOCK, "comp_yn", 0, "N")

instXaQueryT8410.Request(0)

while XAQueryEventHandlerT8410.query_state == 0:
    pythoncom.PumpWaitingMessages()

count = instXaQueryT8410.GetBlockCount(T8410_OUT_BLOCK)
 
for i in range(count):
    date = instXaQueryT8410.GetFieldData(T8410_OUT_BLOCK, "date", i)
    open = instXaQueryT8410.GetFieldData(T8410_OUT_BLOCK, "open", i)
    high = instXaQueryT8410.GetFieldData(T8410_OUT_BLOCK, "high", i)
    low = instXaQueryT8410.GetFieldData(T8410_OUT_BLOCK, "low", i)
    close = instXaQueryT8410.GetFieldData(T8410_OUT_BLOCK, "close", i)
    print(date, open, high, low, close)
