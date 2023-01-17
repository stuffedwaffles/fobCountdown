import time as t
from datetime import datetime as dt
import pytz
from pytz import timezone
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import * 
import sched

#add a hooray at the end


windowHeight = 300
windowWidth = 1000

app = QApplication([])

est = timezone("US/Eastern")
pst = timezone("US/Pacific")

release_timeEST = dt(2023,1,18,10,0,0,0)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("with love from the other side")
        self.setMinimumSize(QSize(windowWidth, windowHeight))
        self.setStyleSheet("background-color : black")

        font = QFont('Arial', 75)
    
        self.tdelta_label = QLabel()
        self.tdelta_label.setStyleSheet("color : white")
        self.setCentralWidget(self.tdelta_label)
        self.tdelta_label.move(100,100)
        self.tdelta_label.setFont(font)
        self.tdelta_label.adjustSize()



        
        timer = QTimer(self)
        timer.timeout.connect(self.onTimeout)
        timer.start(1000)

    def onTimeout(self):
        current_est = dt.now()
        current_pst = dt.now(pst)

        tdelta = release_timeEST- current_est
        s = tdelta.seconds
        hours, remainder = divmod(s, 3600)
        minutes, seconds = divmod(remainder, 60)
        time_until = '{:02}:{:02}:{:02}'.format(int(hours), int(minutes), int(seconds))

        print(f"Eastern Time: {current_est.strftime('%m/%d/%Y %H:%M:%S')}")
        print(f"Pacific Time: {current_pst.strftime('%m/%d/%Y %H:%M:%S')}")
        print(f"Time Until Release: {tdelta.days} days, {time_until}")

        self.tdelta_label.setText(f"    {tdelta.days} days, {time_until}")




window = MainWindow()

window.show()
app.exec()
