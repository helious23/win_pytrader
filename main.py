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
        # self.kiwoom.OnEventConnect.connect(self.event_connect)
        # self.kiwoom.OnReceiveTrData.connect(self.receive_trdata)
        
        self.setWindowTitle("👋Hello Stock")
        self.setGeometry(300, 300, 500, 450)
        
        btn1 = QPushButton("종목 얻기", self)
        btn1.move(400, 10)
        btn1.clicked.connect(self.btn1_clicked)
        
        self.listWidget = QListWidget(self)
        self.listWidget.setGeometry(10, 10, 300, 200)
        
    def btn1_clicked(self):
        ret = self.kiwoom.dynamicCall("GetCodeListByMarket(QString)", ["0"])
        kospi_code_list = ret.split(";")
        kospi_code_name_list = []
        
        for x in kospi_code_list:
            name = self.kiwoom.dynamicCall("GetMasterCodeName(QString)", [x])
            kospi_code_name_list.append(f"{x} : {name}")
        
        self.listWidget.addItems(kospi_code_name_list)
          
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()