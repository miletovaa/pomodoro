import QtQuick
import QtQuick.Controls.Basic


ApplicationWindow {
    id: window

    property double progressBar
    property int progressBarInt
    property int workTime
    property int passedTime
    property int leftTime
    property int leftMin
    property int leftSec
    property int settingsShowTime
    property int settingsShowPercents
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
        function showProgressBarText () {
            if (window.settingsShowTime == '1' && window.settingsShowPercents == '1') return leftMin + ':' + leftSec + ' left (' + progressBarInt + '%)';
            else if (window.settingsShowTime == '1') return leftMin + ':' + leftSec + ' left';
            else if (window.settingsShowPercents == '1') return progressBarInt + '%'
        }
        text: showProgressBarText()
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
            leftSec = (leftSec < 10) ? '0' + leftSec.toString() : leftSec
            progressBarInt = Math.floor(progressBar)
        }
    }
}