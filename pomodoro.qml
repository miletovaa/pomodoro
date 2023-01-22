import QtQuick
import QtQuick.Controls.Basic


ApplicationWindow {
    property double progressBar
    property int progressBarInt
    property int workTime
    property int passedTime
    property int leftTime
    property int leftMin
    property int leftSec
    property QtObject timer

    visible: true
    width: screen.desktopAvailableWidth
    height: 20
    title: "🍅 Pomodoro Timer"

    x: 0
    y: 0
    flags: Qt.FramelessWindowHint | Qt.Window | Qt.WindowStaysOnTopHint
    color: 'transparent'
    Rectangle {
        width: screen.desktopAvailableWidth/100 * progressBar
        height: 5
        color: '#539353'
    }
    Text {
        anchors.centerIn: parent
        text: leftMin + ':' + leftSec + ' left (' + progressBarInt + '%)'
        font.pixelSize: 10
        color: '#ffffff'
    }

    Connections {
        target: timer
        function onUpdated(msg) {
            passedTime = msg
            progressBar = passedTime / workTime * 100
            leftTime = (workTime - passedTime) / 10
            leftMin = leftTime / 60
            leftSec = leftTime - (leftMin * 60)
            progressBarInt = Math.floor(progressBar)
        }
    }
}