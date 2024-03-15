import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QAxContainer import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Kiwoom login
        self.kiwoom = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        self.kiwoom.dynamicCall("CommConnect()")
        
        # OpenAPI + Event
        self.kiwoom.OnEventConnect.connect(self.event_connect)
        self.kiwoom.OnReceiveTrData.connect(self.receive_trdata)
        
        self.setWindowTitle("👋Hello Stock")
        self.setGeometry(300, 300, 300, 150)
        
        label = QLabel("종목코드: ", self)
        label.move(20, 20)
        
        self.code_edit = QLineEdit(self)
        self.code_edit.move(80, 20)
        self.code_edit.setText("000250") # default
        
        # QPushButtin(텍스트, 부모 Widget)
        btn1 = QPushButton("조회", self)
        btn1.move(190, 20)
        btn1.clicked.connect(self.btn1_clicked)
        
        self.text_edit = QTextEdit(self)
        self.text_edit.setGeometry(10, 60, 280, 80)
        self.text_edit.setEnabled(False)
    
    def event_connect(self, err_code):
        if err_code == 0:
            self.text_edit.append("로그인 성공😍")
        else:
            self.text_edit.append("로그인 실패😒")
    
    def btn1_clicked(self):
        code = self.code_edit.text()
        self.text_edit.append(f"종목코드: {code}")
        
        # SetInputValue
        self.kiwoom.dynamicCall("SetInputValue(QString, QString)", "종목코드", code)
        
        #CommRqData("임의 문자-TR 구분 용도", 사용할 TR명, 0:단순조회, 화면번호)
        self.kiwoom.dynamicCall("CommRqData(QString, QString, int, QString)", "opt10001_req", "opt10001", 0, "0101")
        
    def receive_trdata(self, screen_no, rqname, trcode, recordname, prev_next, data_len, err_code, msg1, msg2):
        if rqname == "opt10001_req":
            name = self.kiwoom.dynamicCall("GetCommData(QString, QString, int, QString)", trcode, rqname, 0, "종목명")
            volume = self.kiwoom.dynamicCall("GetCommData(QString, QString, int, QString)", trcode, rqname, 0, "거래량")
            price = self.kiwoom.dynamicCall("GetCommData(QString, QString, int, QString)", trcode, rqname, 0, "현재가")
            
            self.text_edit.append(f"종목명: {name.strip()}")
            self.text_edit.append(f"거래량: {volume.strip()}")
            self.text_edit.append(f"현재가: {price.strip()}")
                
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()