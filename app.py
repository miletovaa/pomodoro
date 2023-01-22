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
    settings_show_time = config[2]
    settings_show_percents = config[3]

def changeConfig(min, line):
    config[line] = min + '\n'
    with open('config.txt', 'w') as file:
        file.writelines(config)

def trueFalse(val):
    if (val == 'true'):
        return '1'
    elif (val == 'false'):
        return '0'

class changeSettings(QObject):
    @Slot(str)
    def workTime(self, min):
        if int(min) > 0:
            changeConfig(min, 0)
    @Slot(str)
    def restTime(self, min):
        if int(min) > 0:
            changeConfig(min, 1)
    @Slot(str)
    def checkboxTime(self, val):
        changeConfig(trueFalse(val), 2)
    @Slot(str)
    def checkboxPercents(self, val):
        changeConfig(trueFalse(val), 3)

class startTimer(QObject):
    @Slot()
    def startWork(self):
        print('Start')
        subprocess.Popen(["python", './pomodoro.py'])


change_settings = changeSettings()
start_timer = startTimer()

QQuickWindow.setSceneGraphBackend('software')
app = QGuiApplication(sys.argv)
engine = QQmlApplicationEngine()
engine.quit.connect(app.quit)
engine.load('./app.qml')
obj = engine.rootObjects()[0]
obj.setProperty('workTime', work_time)
obj.setProperty('restTime', rest_time)
obj.setProperty('settingsShowPercents', settings_show_percents)
obj.setProperty('settingsShowTime', settings_show_time)
obj.setProperty('changeSettings', change_settings)
obj.setProperty('startTimer', start_timer)
sys.exit(app.exec())