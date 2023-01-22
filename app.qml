import QtQuick
import QtQuick.Controls.Basic

ApplicationWindow {
    id: window

    property int workTime
    property int restTime
    property int settingsShowTime
    property int settingsShowPercents
    property QtObject changeSettings
    property QtObject startTimer

    visible: true
    width: 600
    height: 500
    title: "Pomodoro Timer"

    color: '#282828'

    Rectangle {
        width: window.width
        height: 100
        color: "transparent"
        Text {
            anchors.centerIn: parent
            text: "🍅 Pomdoro Timer"
            color: 'white'
            font.pixelSize: 42
        }
    }

    Rectangle {
        color: "transparent"

        y: 170
        x: 20

        Text {
            text: 'Work time: '
            font.pixelSize: 24
            color: '#ffffff'
        }
        TextField {
            id: work_time_field
            x: 130
            y: 4
            width: 50
            height: 32
            font.pixelSize: 18
            placeholderText: workTime
        }
        Text {
            x: 188
            y: 8
            text: 'min.'
            font.pixelSize: 20
            color: '#ffffff'
        }
        Button {
            x: 240
            y: 2
            width: 70
            height: 36
            onClicked: changeSettings.workTime(work_time_field.text)

            contentItem: Text {
                text: "SET"
                font.pixelSize: 16
                color: parent.down ? "#f0f0f0" : "white"
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
            }

            background: Rectangle {
                color: parent.down ? "#404040" : "#505050"
                radius: 5
            }
        }
    }

    Rectangle {
        color: "transparent"

        y: 250
        x: 20

        Text {
            text: 'Rest time: '
            font.pixelSize: 24
            color: '#ffffff'
        }
        TextField {
            id: rest_time_field
            x: 130
            y: 4
            width: 50
            height: 32
            font.pixelSize: 18
            placeholderText: restTime
        }
        Text {
            x: 188
            y: 8
            text: 'min.'
            font.pixelSize: 20
            color: '#ffffff'
        }
        Button {
            x: 240
            y: 2
            width: 70
            height: 36
            onClicked: changeSettings.restTime(rest_time_field.text)

            contentItem: Text {
                text: "SET"
                font.pixelSize: 16
                color: parent.down ? "#f0f0f0" : "white"
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
            }

            background: Rectangle {
                color: parent.down ? "#404040" : "#505050"
                radius: 5 
            }
        }
    }

    Rectangle {
        y: 180
        x: 370
        CheckBox {
            id: checkbox_time
            checked: settingsShowTime
            onClicked: changeSettings.checkboxTime(checkbox_time.checked)
        }
        Text {
            x: 50
            y: 4
            text: 'show time left'
            font.pixelSize: 18
            color: '#B3B3B3'
        }
        CheckBox {
            id: checkbox_percents
            y: 40
            checked: settingsShowPercents
            onClicked: changeSettings.checkboxPercents(checkbox_percents.checked)
        }
        Text {
            x: 50
            y: 44
            text: 'show percents left'
            font.pixelSize: 18
            color: '#B3B3B3'
        }
    }

    Rectangle {
        y: 320

        width: window.width
        height: 100
        color: "transparent"
        Button {
            id: start_session
            anchors.centerIn: parent
            width: 200
            height: 40
            onClicked: startTimer.startWork()

            contentItem: Text {
                text: "START SESSION"
                font.pixelSize: 20
                color: parent.down ? "#cbdfcb" : "white"
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
            }

            background: Rectangle {
                color: parent.down ? "#427642" : "#539353"
                radius: 5 
            }
        }
    }
}