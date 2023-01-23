import sys, os, time, subprocess, multiprocessing


from win11toast import toast

from PyQt6.QtGui import QGuiApplication
from PyQt6.QtQml import QQmlApplicationEngine
from PyQt6.QtQuick import QQuickWindow
from PyQt6.QtCore import QObject, pyqtSlot as Slot

with open('config.txt') as file:
    config = file.readlines()
    work_time = config[1]
    rest_time = config[2]
    settings_show_time = config[3]
    settings_show_percents = config[4]

def changeConfig(arg, line):
    config[line] = arg + '\n'
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
        if (int(min) > 0):
            changeConfig(min, 0)
        else:
            return True
    @Slot(str)
    def restTime(self, min):
        if (int(min) > 0):
            changeConfig(min, 1)
        else:
            return True
    @Slot(str)
    def checkboxTime(self, val):
        changeConfig(trueFalse(val), 2)
    @Slot(str)
    def checkboxPercents(self, val):
        changeConfig(trueFalse(val), 3)

class startTimer(QObject):
    @Slot()
    def startWork(self):
        print('Start work')
        changeConfig('w', 0)
        p = subprocess.Popen(["python", './pomodoro.py'])
        time.sleep(int(work_time)*60)
        p.kill()
        changeConfig('r', 0)
        toast('⌛ Work is over. Relax ;)', duration='long', on_click=lambda args: self.startRest())

    def startRest(self):
        print('Start rest')
        p = subprocess.Popen(["python", './pomodoro.py'])
        time.sleep(int(rest_time)*60)
        p.kill()
        changeConfig('w', 0)
        toast('⌛ Rest is over. Time to work!', duration='long', on_click=lambda args: self.startWork)


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

