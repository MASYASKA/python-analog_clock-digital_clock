from PyQt5 import QtWidgets, QtGui, QtTest
import analog_clock_ui, math, datetime

class HoldRotatableItem(QtWidgets.QGraphicsPixmapItem):

    def __init__(self, name):
        super(HoldRotatableItem, self).__init__(QtGui.QPixmap(name))
        self.setTransformOriginPoint(256, 256)
        self.center = Container()
        self.center.x = 256/2
        self.center.y = 256/2
        self.rotation = 0

    def mousePressEvent(self, event):
        pass

    def mouseMoveEvent(self, event):
        last_position = event.lastScenePos()
        curr_position = event.scenePos()

        self.handler(last_position, curr_position)

    def handler(self, last_position, curr_position):
        a = math.sqrt((last_position.x() - self.center.x)**2 + (last_position.y() - self.center.y)**2)
        b = math.sqrt((curr_position.x() - self.center.x)**2 + (curr_position.y() - self.center.y)**2)
        c = math.sqrt((last_position.x() - curr_position.x())**2 + (last_position.y() - curr_position.y())**2)
        angle_cos = (a**2 + b**2 - c**2)/(2*a*b)
        angle = math.degrees(math.acos(angle_cos))
        self.rotation += angle
        self.setRotation(self.rotation)

class Ui_AnalogClock(analog_clock_ui.Ui_AnalogClock):

    def setupSceneUi(self, scene):
        self.scene = scene
        scene.clock_ground = scene.addPixmap(QtGui.QPixmap('images//clock_ground.png'))
        scene.hour_hand = HoldRotatableItem('images//hour_hand.png')
        scene.minute_hand = HoldRotatableItem('images//minute_hand.png')
        scene.second_hand = HoldRotatableItem('images//second_hand.png')

        scene.addItem(scene.hour_hand)
        scene.addItem(scene.minute_hand)
        scene.addItem(scene.second_hand)

        # scene.clock_ground = scene.addPixmap(QtGui.QPixmap('clock_ground.png'))
        # scene.hour_hand = scene.addPixmap(QtGui.QPixmap('hour_hand.png'))
        # scene.minute_hand = scene.addPixmap(QtGui.QPixmap('minute_hand.png'))
        # scene.second_hand = scene.addPixmap(QtGui.QPixmap('second_hand.png'))

        scene.clock_items = [scene.hour_hand, scene.minute_hand, scene.second_hand]


        for item in scene.clock_items:
            item.setTransformOriginPoint(256, 256)

        self.setTime(scene, [15,33,0])
        self.speed = 1000

    def goClock(self, scene):
        scene.hour_hand.rotation += 0.00833333333
        scene.minute_hand.rotation += 0.1
        scene.second_hand.rotation += 6

        for item in scene.clock_items:
            item.setRotation(item.rotation)

    def setTime(self, scene, time_lst):
        hours = time_lst.pop(0)
        minutes = time_lst.pop(0)
        seconds = time_lst.pop(0)

        scene.hour_hand.rotation = (hours * 3600 + minutes * 60 + seconds) * 0.00833333333
        scene.minute_hand.rotation = (minutes * 60 + seconds) * 0.1
        scene.second_hand.rotation = seconds * 6

        for item in scene.clock_items:
            item.setRotation(item.rotation)

    def getTime(self):
        hour = self.edit_time.time().hour()
        minute = self.edit_time.time().minute()
        second = self.edit_time.time().second()
        self.setTime(self.scene, [hour, minute, second])


    def setCurrentTime(self):
        hour = datetime.datetime.now().hour     
        minute = datetime.datetime.now().minute
        second = datetime.datetime.now().second
        self.setTime(self.scene, [hour, minute, second])


    def setx1(self):
        self.speed = 1000
        print(self.speed)

    def setx2(self):
        if self.speed // 2 == 0:
            self.speed = 1
        else:
            self.speed //= 2
        print(self.speed)

    def setx4(self):
        if self.speed // 4 == 0:
            self.speed = 1
        else:
            self.speed //= 4
        print(self.speed)

    def setx05(self):
        self.speed *= 2
        print(self.speed)

    def setx025(self):
        self.speed *= 4
        print(self.speed)














































# class AnalogClockScene(QtWidgets.QGraphicsScene):

#     def __init__(self, parent):
#         super(AnalogClockScene, self).__init__()
#         self.widget = QtWidgets.QWidget()
#         self.widget.ui = analog_clock.Ui_AnalogClock()
#         # self.widget.ui.setupUi(self.widget)
#         self.widget.ui.setupSceneUi(self)

#     def connecting(self, parent):
#         pass

#     def work(self, view):
#         while True:
#             QtTest.QTest.qWait(1000)
#             self.widget.ui.goClock(self)
#             view.setScene(self)











class MyScene(QtWidgets.QGraphicsScene):

    def __init__(self, parent):
        super(MyScene, self).__init__(parent=parent)
        self.clock_ground = self.addPixmap(QtGui.QPixmap('clock_ground.png'))
        self.hour_hand = self.addPixmap(QtGui.QPixmap('hour_hand.png'))
        self.minute_hand = self.addPixmap(QtGui.QPixmap('minute_hand.png'))
        self.second_hand = self.addPixmap(QtGui.QPixmap('second_hand.png'))

        self.clock_items = [self.hour_hand, self.minute_hand, self.second_hand]

        for item in self.clock_items:
            item.setTransformOriginPoint(256, 256)

    def setTime(self, time_lst):
        hours = time_lst.pop(0)
        minutes = time_lst.pop(0)
        seconds = time_lst.pop(0)

        self.hour_hand.rotation = (hours * 3600 + minutes * 60 + seconds) * 0.00833333333
        self.minute_hand.rotation = (minutes * 60 + seconds) * 0.1
        self.second_hand.rotation = seconds * 6

        for item in self.clock_items:
            item.setRotation(item.rotation)

    def goClock(self):
        self.hour_hand.rotation += 0.00833333333
        self.minute_hand.rotation += 0.1
        self.second_hand.rotation += 6

        for item in self.clock_items:
            item.setRotation(item.rotation)


class Container:
    pass