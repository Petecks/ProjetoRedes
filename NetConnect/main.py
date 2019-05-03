from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
import sys
import os
from multiprocessing import Process
from clientoriginal import client_UDP,client_TCP
from serveroriginal import server_UDP,server_TCP



class Receipt(QMainWindow):
    protocol = ""
    check = ""
    namefile = ""
    IP = ""
    Port = 0
    def __init__(self):
        super().__init__()
        self.ui = None
        self.load_ui()
        self.load_signals()
        self.actionBefehle.triggered.connect(self.open)
        self.actionDatai.triggered.connect(self.openfile)
        self.actionAudio.triggered.connect(self.openimage)
        self.radioButton.toggled.connect(self.udp_state)
        self.radioButton_3.toggled.connect(self.tcp_state)
        self.Checksum.toggled.connect(self.checksum_check)
        self.radioButton_2.toggled.connect(self.crc_check)
        self.pushButton.clicked.connect(self.send_to_host)
        self.pushButton_2.clicked.connect(self.adquire_host)



    def send_to_host(self):
        if self.protocol == "UDP":
            if __name__ == '__main__':
                q = Process(target=server_UDP, args= (self.namefile,))
                p = Process(target=client_UDP, args= (self.namefile,))
                q.start()
                p.start()
                q.join()
                p.join()
            self.recivefile()
        elif self.protocol == "TCP":
            if __name__ == '__main__':
                q = Process(target=server_TCP, args= (self.namefile,))
                p = Process(target=client_TCP, args= (self.namefile,))
                q.start()
                p.start()
                q.join()
                p.join()
            self.recivefile()
        self.add_cs()

    def adquire_host(self):
        self.IP= QInputDialog.getText(self, "Config destino", "IP:")
        self.Port= QInputDialog.getInt(self, "Config destino", "Port:")
        if self.protocol == "UDP":
            if __name__ == '__main__':
                q = Process(target=server_UDP, args= (self.namefile,self.IP, self.Port,))
                p = Process(target=client_UDP, args= (self.namefile,self.IP, self.Port,))
                q.start()
                p.start()
                q.join()
                p.join()
            self.recivefile()
        elif self.protocol == "TCP":
            if __name__ == '__main__':
                q = Process(target=server_TCP, args= (self.namefile,self.IP, self.Port,))
                p = Process(target=client_TCP, args= (self.namefile,self.IP, self.Port,))
                q.start()
                p.start()
                q.join()
                p.join()
            self.recivefile()
        self.add_cs()

    def add_cs(self):
        readtweets = open("responsecscl", "r")
        tweetlist = readtweets.read()
        self.label_4.setText(tweetlist)
        readtweets.close()
        readtweets = open("responsecssv", "r")
        tweetlist = readtweets.read()
        self.label_5.setText(tweetlist)
        readtweets.close()
    def checksum_check(self):
        self.check = 'CS'

    def crc_check(self):
        self.check = 'CRC'

    def udp_state(self):
        self.protocol = 'UDP'

    def tcp_state(self):
        self.protocol = 'TCP'

    def load_ui(self):
        self.ui = loadUi('mainwindow.ui', self)
        self.show()

    def load_signals(self):
        pass

    def openfile(self):
        file,okpressed = QInputDialog.getText(self,"nome do arquivo","entrada:")
        self.namefile = file
        readtweets = open(file, "r")
        tweetlist = readtweets.read()
        self.textEdit.setText(tweetlist)
        readtweets.close()

    def recivefile(self):
        readtweets = open("response" + self.namefile, "r")
        tweetlist = readtweets.read()
        self.textEdit_2.setText(tweetlist)

    def openimage(self):
        label = QLabel(self)
        file, okpressed = QInputDialog.getText(self, "nome da imagem", "entrada:")
        pixmap = QPixmap('layout')
        label.setPixmap(pixmap)

    def open(self):
        QMessageBox.about(self, 'Sobre o programa', "INFOS A RESPOEITO DO PROGRAMA\n - FUNÇÃO IMAGEM ESTA DESABILITADA\n -Na função data, o arquivo em questão será passado na mensagem\n certifique-se de setar as informações de Protocolos e checagem antes de enviar o arquivo\n")


app = QApplication(sys.argv)
receipt = Receipt()
sys.exit(app.exec_())