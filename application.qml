import QtQuick
import QtQuick.Controls.Basic


ApplicationWindow {
    property double progressBar
    property int progressBarInt
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
        /* y: 5 */
        anchors.centerIn: parent
        /* text: "🍅 Pomodoro Timer" */
        text: progressBarInt + '%'
        font.pixelSize: 10
        color: '#ffffff'
    }

    Connections {
        target: timer
        function onUpdated(msg) {
            progressBar = msg
            progressBarInt = Math.floor(progressBar)
        }
    }
}