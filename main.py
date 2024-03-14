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
    print(account)