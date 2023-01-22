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
    updated = pyqtSignal(float, arguments=['updater'])

    def __init__(self, work_time):
        QObject.__init__(self)
        self.w = mintomilisec(work_time)

    
    def updater(self, progress_bar):
        self.updated.emit(progress_bar)
    
    
    def bootUp(self):
        t_thread = threading.Thread(target=self._bootUp)
        t_thread.daemon = True
        t_thread.start()
        print('bootup exit')


    def _bootUp(self):
        passed_time = 0
        while True:
            passed_time += 1
            progress_bar = passed_time / self.w * 100
            self.updater(progress_bar)
            if (progress_bar == 100):
                break
            sleep(0.1)
        print('_bootUp Exit')
        return

def getWorkTime():
    with open('config.txt') as file:
        config = file.readlines()
        work_time = float(config[0])
    return work_time

def getRestTime():
    with open('config.txt') as file:
        config = file.readlines()
        rest_time = float(config[1])
    return rest_time

def runTime(time, progress_bar_color):
    QQuickWindow.setSceneGraphBackend('software')
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    engine.quit.connect(app.quit)
    engine.load('./pomodoro.qml')
    timer = Timer(time)
    engine.rootObjects()[0].setProperty('timer', timer)
    engine.rootObjects()[0].setProperty('barColor', progress_bar_color)
    timer.bootUp()
    print('runtime exit')
    sys.exit(app.exec())
    print('target')

def runWorkTime(time):
    bar_color = '#455567'
    runTime(time, bar_color)
    print('target 2')
    toast('⌛ Work is over', duration='long', button='Rest', on_click=runRestTime(getRestTime()))


def runRestTime(time):
    bar_color = '#488900'
    runTime(time, bar_color)
    toast('⌛ Work is over', duration='long', button='Work', on_click=runWorkTime(getWorkTime()))


def mintomilisec(min):
    return min * 60 * 10


if __name__ == "__main__":
    runWorkTime(getWorkTime())