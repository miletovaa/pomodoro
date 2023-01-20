from win11toast import toast
import sys
import os
from PyQt6.QtGui import QGuiApplication
from PyQt6.QtQml import QQmlApplicationEngine
from PyQt6.QtQuick import QQuickWindow
from PyQt6.QtCore import QObject, pyqtSignal

class Backend(QObject):
    def __init__(self):
        QObject.__init__(self)
QQuickWindow.setSceneGraphBackend('software')


QQuickWindow.setSceneGraphBackend('software')
app = QGuiApplication(sys.argv)
engine = QQmlApplicationEngine()
engine.quit.connect(app.quit)
engine.load('./application.qml')
sys.exit(app.exec())



# toast('Hello Python🐍')``