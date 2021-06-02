from PyQt5 import QtWidgets, QtGui, QtTest
import digital_clock_ui, datetime

class Ui_DigitalClock(digital_clock_ui.Ui_DigitalClock):

    def setupSceneUi(self):
        self.match_lst = {0: QtGui.QPixmap('images//digital_zero.png'), 
                        1 : QtGui.QPixmap('images//digital_one.png'), 2 : QtGui.QPixmap('images//digital_two.png'), 3 : QtGui.QPixmap('images//digital_three.png'),
                           4 : QtGui.QPixmap('images//digital_four.png'), 5 : QtGui.QPixmap('images//digital_five.png'), 6 : QtGui.QPixmap('images//digital_six.png'),
                           7 : QtGui.QPixmap('images//digital_seven.png'), 8 : QtGui.QPixmap('images//digital_eight.png'), 9 : QtGui.QPixmap('images//digital_nine.png')}
        self.clock_lst = [self.pixmap_hour_1, self.pixmap_hour_2,
                                     self.pixmap_minute_1, self.pixmap_minute_2,
                                     self.pixmap_second_1, self.pixmap_second_2]


    def goClock(self, scene):
        self.minutes += self.seconds // 60
        self.seconds = self.seconds % 60
        self.hours += self.minutes // 60
        self.minutes = self.minutes % 60
        self.hours = self.hours % 24

        self.pixmap_hour_1.setPixmap(self.match_lst[int(self.hours)%10])
        self.pixmap_hour_2.setPixmap(self.match_lst[self.hours//10])
        self.pixmap_minute_1.setPixmap(self.match_lst[self.minutes%10])
        self.pixmap_minute_2.setPixmap(self.match_lst[self.minutes//10])
        self.pixmap_second_1.setPixmap(self.match_lst[self.seconds%10])
        self.pixmap_second_2.setPixmap(self.match_lst[self.seconds//10])

        self.seconds += 1


    def setTime(self, scene, qtime=[0, 0, 0]):
        if len(qtime) != 3: raise TypeError('wrong time data, you must put data in list like that [12,34,56]')
        for unit in qtime:
            if unit > 60: raise TypeError('wrong time data! hour, min, sec < 60')
        self.hours = qtime.pop(0)
        self.minutes = qtime.pop(0)
        self.seconds = qtime.pop(0)
        self.speed = 1000

    def getTime(self):
        hour = self.edit_time.time().hour()
        minute = self.edit_time.time().minute()
        second = self.edit_time.time().second()
        self.setTime(None, [hour, minute, second])

    def setCurrentTime(self):
        hour = datetime.datetime.now().hour
        minute = datetime.datetime.now().minute
        second = datetime.datetime.now().second
        self.setTime(None, [hour, minute, second])

    def setx1(self):
        self.speed = 1000

    def setx2(self):
        if self.speed // 2 == 0:
            self.speed = 1
        else:
            self.speed //= 2

    def setx4(self):
        if self.speed // 4 == 0:
            self.speed = 1
        else:
            self.speed //= 4

    def setx05(self):
        self.speed *= 2

    def setx025(self):
        self.speed *= 4