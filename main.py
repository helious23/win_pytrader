import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QAxContainer import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("👋Hello Stock📈")
        self.setGeometry(300, 300, 300, 150)
        
        self.kiwoom = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        self.kiwoom.dynamicCall("CommConnect()")
        
        # TextEdit 생성
        self.text_edit = QTextEdit(self)
        self.text_edit.setGeometry(10, 60, 280, 80)
        self.text_edit.setEnabled(False) # 입력기능 X
        
        # event 와 event 처리 메서드 연결
        self.kiwoom.OnEventConnect.connect(self.event_connect)
    
    def event_connect(self, err_code):
        if err_code == 0:
            self.text_edit.append("로그인 성공😁")
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()