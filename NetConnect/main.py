from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
import sys
import os
from multiprocessing import Process
from clientoriginal import client_UDP
from serveroriginal import server_UDP



class Receipt(QMainWindow):
    protocol = ""
    check = ""
    namefile = ""
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

    def send_to_host(self):
        print("enviar host")
        if __name__ == '__main__':
            q = Process(target=server_UDP, args= (self.namefile,))
            p = Process(target=client_UDP, args= (self.namefile,))
            q.start()
            p.start()
            q.join()
            p.join()
        self.recivefile()

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