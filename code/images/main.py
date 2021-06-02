from PyQt5 import QtWidgets, QtGui, QtTest
import sys
import datetime

class MyWindow(QtWidgets.QMainWindow):

    def __init__(self, width, height):
        super(MyWindow, self).__init__()
        self.width, self.height = width, height
        self.setGeometry(500, 500, self.width, self.height)


class MyScene(QtWidgets.QGraphicsScene):

    def __init__(self):
        super(MyScene, self).__init__()

        self.time_editor = self.addWidget(QtWidgets.QTimeEdit())
        
        self.clock_ground = self.addPixmap(QtGui.QPixmap('clock_ground.png'))
        self.hour_hand = self.addPixmap(QtGui.QPixmap('hour_hand.png'))
        self.minute_hand = self.addPixmap(QtGui.QPixmap('minute_hand.png'))
        self.second_hand = self.addPixmap(QtGui.QPixmap('second_hand.png'))

        self.hour_hand.setTransformOriginPoint(256, 256)
        self.minute_hand.setTransformOriginPoint(256, 256)
        self.second_hand.setTransformOriginPoint(256, 256)
        self.hour_hand.rotation = 0
        self.minute_hand.rotation = 0
        self.second_hand.rotation = 0

    def setTime(self, ctime):
        hours = ctime.pop(0)
        minutes = ctime.pop(0)
        seconds = ctime.pop(0)
        self.hour_hand.rotation = (hours * 3600 + minutes * 60 + seconds) * 0.00833333333
        self.minute_hand.rotation = (minutes * 60 + seconds) * 0.1
        self.second_hand.rotation = seconds * 6



    def goClock(self):
        self.hour_hand.setRotation(self.hour_hand.rotation)
        self.minute_hand.setRotation(self.minute_hand.rotation)
        self.second_hand.setRotation(self.second_hand.rotation)
        
        self.hour_hand.rotation += 0.00833333333
        self.minute_hand.rotation += 0.1
        self.second_hand.rotation += 6


class MyView(QtWidgets.QGraphicsView):

    def __init__(self, parent):
        super(MyView, self).__init__(parent=parent)
        self.setGeometry(0, 0, parent.width, parent.height)
        self.scene = MyScene()
        self.setScene(self.scene)

    def work(self):
        # self.scene.setTime()
        self.scene.goClock()
        self.setScene(self.scene)


app = QtWidgets.QApplication(sys.argv)
win = MyWindow(1280, 720)
view = MyView(win)
win.show()
print(datetime.datetime.now().hour)
view.scene.setTime([datetime.datetime.now().hour, datetime.datetime.now().minute, datetime.datetime.now().second])
while True:
    view.work()
    QtTest.QTest.qWait(1000)

sys.exit(app.exec_())