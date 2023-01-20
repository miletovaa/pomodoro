import QtQuick
import QtQuick.Controls.Basic


ApplicationWindow {
    property string currTime: "00:00:00"
    property QtObject timer

    visible: true
    width: screen.desktopAvailableWidth
    height: 20
    title: "🍅 Pomodoro Timer"

    x: 0
    y: 0
    flags: Qt.FramelessWindowHint | Qt.Window
    color: 'transparent'
    Rectangle {
        width: screen.desktopAvailableWidth/100
        height: 5
        color: '#539353'
    }
    Text {
        /* y: 5 */
        anchors.centerIn: parent
        /* text: "🍅 Pomodoro Timer" */
        text: currTime
        font.pixelSize: 10
        color: '#ffffff'
    }

    Connections {
        target: timer
        function onUpdated(msg) {
            currTime = msg
        }
    }
}