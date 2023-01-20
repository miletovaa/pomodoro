from win11toast import toast

import threading

from time import strftime, gmtime, sleep

import sys
import os
from PyQt6.QtGui import QGuiApplication
from PyQt6.QtQml import QQmlApplicationEngine
from PyQt6.QtQuick import QQuickWindow
from PyQt6.QtCore import QObject, pyqtSignal

class Timer(QObject):
    def __init__(self):
        QObject.__init__(self)
    updated = pyqtSignal(str, arguments=['updater'])
    def updater(self, curr_time):
        self.updated.emit(curr_time)
    def bootUp(self):
        t_thread = threading.Thread(target=self._bootUp)
        t_thread.daemon = True
        t_thread.start()
    def _bootUp(self):
        while True:
            curr_time = strftime("%H:%M:%S", gmtime())
            self.updater(curr_time)
            sleep(0.1)

minutes = 5
w = minutes * 60 * 10

QQuickWindow.setSceneGraphBackend('software')
app = QGuiApplication(sys.argv)
engine = QQmlApplicationEngine()
engine.quit.connect(app.quit)
engine.load('./application.qml')
timer = Timer()
engine.rootObjects()[0].setProperty('timer', timer)
timer.bootUp()
sys.exit(app.exec())



# toast('Hello Python🐍')``