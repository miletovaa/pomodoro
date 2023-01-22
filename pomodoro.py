from win11toast import toast

import threading

from time import strftime, gmtime, sleep

import sys
import os
from PyQt6.QtGui import QGuiApplication
from PyQt6.QtQml import QQmlApplicationEngine
from PyQt6.QtQuick import QQuickWindow
from PyQt6.QtCore import QObject, pyqtSignal

with open('config.txt') as file:
    config = file.readlines()
    work_time = float(config[0])
    rest_time = float(config[1])

def mintomilisec(min):
    return min * 60 * 10

w = mintomilisec(work_time)

class Timer(QObject):
    def __init__(self):
        QObject.__init__(self)
    updated = pyqtSignal(int, arguments=['updater'])
    def updater(self, passed_time):
        self.updated.emit(passed_time)
    def bootUp(self):
        t_thread = threading.Thread(target=self._bootUp)
        t_thread.daemon = True
        t_thread.start()
    def _bootUp(self):
        passed_time = 0
        while True:
            passed_time += 1
            self.updater(passed_time)
            progress_bar = passed_time / w * 100
            if (progress_bar == 100):
                toast('⌛ Work is over', duration='long', button='Rest')
                break
            sleep(0.1)


def runWorkTime():
    QQuickWindow.setSceneGraphBackend('software')
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    engine.quit.connect(app.quit)
    engine.load('./pomodoro.qml')
    timer = Timer()
    engine.rootObjects()[0].setProperty('workTime', w)
    engine.rootObjects()[0].setProperty('timer', timer)
    timer.bootUp()
    sys.exit(app.exec())

runWorkTime()