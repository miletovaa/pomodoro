import threading, sys, os, time, signal

from multiprocessing import Process

from PyQt6.QtGui import QGuiApplication
from PyQt6.QtQml import QQmlApplicationEngine
from PyQt6.QtQuick import QQuickWindow
from PyQt6.QtCore import QObject, pyqtSignal

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
            progress_bar = passed_time / t * 100
            if (progress_bar == 100):
                break
            time.sleep(0.1)

def runTime():
    QQuickWindow.setSceneGraphBackend('software')
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    engine.quit.connect(app.quit)
    engine.load('./pomodoro.qml')
    timer = Timer()
    engine.rootObjects()[0].setProperty('time', t)
    engine.rootObjects()[0].setProperty('settingsShowTime', settings_show_time)
    engine.rootObjects()[0].setProperty('settingsShowPercents', settings_show_percents)
    engine.rootObjects()[0].setProperty('progressBarColor', progress_bar_color)
    engine.rootObjects()[0].setProperty('timer', timer)
    timer.bootUp()
    sys.exit(app.exec())


if __name__ == '__main__':
    with open('config.txt') as file:
        config = file.readlines()
        cond = config[0][0]
        work_time = int(config[1])
        rest_time = int(config[2])
        settings_show_time = config[3]
        settings_show_percents = config[4]

    if (cond == 'w'):
        progress_bar_color = '#539353'
        t = work_time * 600
    else:
        progress_bar_color = '#5d6da3'
        t = rest_time * 600

    runTime()