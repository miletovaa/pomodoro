import sys
import os
import subprocess
from PyQt6.QtGui import QGuiApplication
from PyQt6.QtQml import QQmlApplicationEngine
from PyQt6.QtQuick import QQuickWindow
from PyQt6.QtCore import QObject, pyqtSlot as Slot, pyqtSignal as Signal,  QProcess

with open('config.txt') as file:
    config = file.readlines()
    work_time = config[0]
    rest_time = config[1]

def changeConfig(min, line):
    config[line] = min + '\n'
    with open('config.txt', 'w') as file:
        file.writelines(config)

class setTime(QObject):
    @Slot(str)
    def workTime(self, min):
        if int(min) > 0:
            changeConfig(min, 0)
    @Slot(str)
    def restTime(self, min):
        if int(min) > 0:
            changeConfig(min, 1)

class startTimer(QObject):
    @Slot()
    def startWork(self):
        print('Start')
        subprocess.Popen(["python", './pomodoro.py'])


set_time = setTime()
start_timer = startTimer()

QQuickWindow.setSceneGraphBackend('software')
app = QGuiApplication(sys.argv)
engine = QQmlApplicationEngine()
engine.quit.connect(app.quit)
engine.load('./app.qml')
obj = engine.rootObjects()[0]
obj.setProperty('workTime', work_time)
obj.setProperty('restTime', rest_time)
obj.setProperty('setTime', set_time)
obj.setProperty('startTimer', start_timer)
sys.exit(app.exec())