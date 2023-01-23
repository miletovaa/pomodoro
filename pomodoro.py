import threading, sys, os, time, signal

from multiprocessing import Process

from PyQt6.QtGui import QGuiApplication
from PyQt6.QtQml import QQmlApplicationEngine
from PyQt6.QtQuick import QQuickWindow
from PyQt6.QtCore import QObject, pyqtSignal

for line in sys.stdin:
    if 'q' == line.rstrip():
        break
    cond = line

if (cond == 'work'):
    progress_bar_color = '#539353'
else:
    progress_bar_color = 'red'


with open('config.txt') as file:
    config = file.readlines()
    work_time = float(config[0])
    rest_time = float(config[1])
    settings_show_time = config[2]
    settings_show_percents = config[3]

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
                break
            time.sleep(0.1)

def runWorkTime():
    QQuickWindow.setSceneGraphBackend('software')
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    engine.quit.connect(app.quit)
    engine.load('./pomodoro.qml')
    timer = Timer()
    engine.rootObjects()[0].setProperty('workTime', w)
    engine.rootObjects()[0].setProperty('settingsShowTime', settings_show_time)
    engine.rootObjects()[0].setProperty('settingsShowPercents', settings_show_percents)
    engine.rootObjects()[0].setProperty('progressBarColor', progress_bar_color)
    engine.rootObjects()[0].setProperty('timer', timer)
    timer.bootUp()
    sys.exit(app.exec())


if __name__ == '__main__':
    w = work_time * 60 * 10
    runWorkTime()