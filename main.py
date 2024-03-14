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

# class 생성
class XAQueryEventHandlerT1102:
    query_state = 0

    def OnReceiveData(self, code):
        XAQueryEventHandlerT1102.query_state = 1

# instance 등록
instXAQueryT1102 = win32com.client.DispatchWithEvents("XA_DataSet.XAQuery",XAQueryEventHandlerT1102)

# t1102 등록
instXAQueryT1102.ResFileName = "C:\\eBest\\xingAPI\\Res\\t1102.res"

# t1102 입력 데이터 설정
instXAQueryT1102.SetFieldData("t1102InBlock", "shcode", 0, "000250") # SetFieldData("블록명", "필드명", 단일데이터=0), "입력값"

# 입력 데이터 전송
instXAQueryT1102.Request(0)

while XAQueryEventHandlerT1102.query_state == 0:
    pythoncom.PumpWaitingMessages()

name = instXAQueryT1102.GetFieldData("t1102OutBlock", "hname", 0) # hname: 한글종목명
price = instXAQueryT1102.GetFieldData("t1102OutBlock", "price", 0) # price: 현재가
print(f"종목명: {name}\n현재가: {price}")
