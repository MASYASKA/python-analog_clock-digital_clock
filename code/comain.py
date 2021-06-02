from PyQt5 import QtWidgets, QtGui, QtTest, QtCore
import main_menu, digital_clock, analog_clock, widget_ui
import sys

# abstract classes

class MainView(QtWidgets.QGraphicsView):
    ''' базовый виджет отображения '''

    def __init__(self, width, height):
        super(MainView, self).__init__()
        self.width, self.height = width, height; del width, height
        self.setGeometry(100, 100, self.width, self.height)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)


class MainScene(QtWidgets.QGraphicsScene):
    ''' базовая сцена, которая содержит виджет, который предусматривает
        установку в него ui'''

    def __init__(self, ui_class, parent):
        super(MainScene, self).__init__()
        self.setSceneRect(0, 0, parent.width-2, parent.height-2)
        self.view = parent
        self.widget = QtWidgets.QWidget()
        self.widget.main_ui = widget_ui.Ui_MainWidget()
        self.widget.main_ui.setupUi(self.widget)
        self.widget.ui = ui_class()
        self.widget.ui.setupUi(self.widget)
        self.widget.main_ui.button_dragn = PanelHoldButton(self.widget, self)
        self.pwidget = self.addWidget(self.widget)

        self.widget.main_ui.button_close.clicked.connect(parent.close)
        self.widget.main_ui.button_roll.clicked.connect(parent.showMinimized)

    def connecting(self):
        ''' abstract method
            метод соединения сигналов объектов ui со слотами ui '''
        raise NotImplementedError("Необходимо переопределить метод")

    def work(self, view):
        while True:
            self.widget.ui.goClock(self)
            QtTest.QTest.qWait(self.widget.ui.speed)
            if self.going:
                view.setScene(self)


# local classes

class MyView(MainView):
    ''' настроеный виджет отображения, который является главным окном '''

    def __init__(self, width, height):
        super(MyView, self).__init__(width, height)
        self.width, self.height = width, height
        # scenes setup
        self.main_menu_scene = MainMenuScene(main_menu.Ui_MainMenu, self)
        self.main_menu_scene.connecting(self)
        self.digital_clock_scene = DigitalClockScene(digital_clock.Ui_DigitalClock, self)
        self.digital_clock_scene.connecting(self)
        self.analog_clock_scene = AnalogClockScene(analog_clock.Ui_AnalogClock, self)
        self.analog_clock_scene.connecting(self)

        self.setScene(self.main_menu_scene)

    # scene change functions
    def setMainMenu(self):
        self.analog_clock_scene.going = False
        self.digital_clock_scene.going = False
        self.setScene(self.main_menu_scene)

    def setDigitalClock(self):
        self.setScene(self.digital_clock_scene)
        self.digital_clock_scene.going = True
        self.digital_clock_scene.work(self)

    def setAnalogClock(self):
        self.setScene(self.analog_clock_scene)
        self.analog_clock_scene.going = True
        self.analog_clock_scene.work(self)


class MainMenuScene(MainScene):

    def connecting(self, parent):
        self.widget.ui.button_digital.clicked.connect(parent.setDigitalClock)
        self.widget.ui.button_analog.clicked.connect(parent.setAnalogClock)


class DigitalClockScene(MainScene):

    def __init__(self, ui_class, parent):
        super(DigitalClockScene, self).__init__(ui_class, parent)
        self.widget.ui.setupSceneUi()
        self.widget.ui.setTime(self, [0, 0, 0])
        self.going = True

    def connecting(self, parent):
        self.widget.main_ui.button_back.clicked.connect(parent.setMainMenu)
        self.widget.ui.button_x1.clicked.connect(self.widget.ui.setx1)
        self.widget.ui.button_x2.clicked.connect(self.widget.ui.setx2)
        self.widget.ui.button_x4.clicked.connect(self.widget.ui.setx4)
        self.widget.ui.button_x05.clicked.connect(self.widget.ui.setx05)
        self.widget.ui.button_x025.clicked.connect(self.widget.ui.setx025)
        self.widget.ui.button_setTime.clicked.connect(self.widget.ui.getTime)
        self.widget.ui.button_setCurrentTime.clicked.connect(self.widget.ui.setCurrentTime)


class AnalogClockScene(MainScene):

    def __init__(self, ui_class, parent):
        super(AnalogClockScene, self).__init__(ui_class, parent)
        self.widget.ui.setupSceneUi(self)
        self.clock_ground.moveBy(1080/2-512/2-150, 720/2-512/2)
        for item in self.clock_items:
            item.moveBy(1080/2-512/2-150, 720/2-512/2)

    def connecting(self, parent):
        self.widget.main_ui.button_back.clicked.connect(parent.setMainMenu)
        self.widget.ui.button_x1.clicked.connect(self.widget.ui.setx1)
        self.widget.ui.button_x2.clicked.connect(self.widget.ui.setx2)
        self.widget.ui.button_x4.clicked.connect(self.widget.ui.setx4)
        self.widget.ui.button_x05.clicked.connect(self.widget.ui.setx05)
        self.widget.ui.button_x025.clicked.connect(self.widget.ui.setx025)
        self.widget.ui.button_setTime.clicked.connect(self.widget.ui.getTime)
        self.widget.ui.button_setCurrentTime.clicked.connect(self.widget.ui.setCurrentTime)

# help classes


class PanelHoldButton(QtWidgets.QPushButton):
    ''' центральная верхняя панель, с помощью которой
        осуществляется перетаскивание окна '''

    def __init__(self, parent, scene):
        super(PanelHoldButton, self).__init__(parent=parent)
        self.scene = scene
        self.setGeometry(40, 0, 960, 30)
        self.setStyleSheet("QPushButton{\n""    \
            background-color: rgb(11, 159, 182);\n""}")

    def mousePressEvent(self, event):
        self.mp = event.globalPos() - self.scene.view.pos() # изначальная позиция мышки при начале перетаскивания

    def mouseMoveEvent(self, event):
        self.scene.view.move(event.globalPos() - self.mp)


app = QtWidgets.QApplication(sys.argv)
view = MyView(1080, 720)
# win.setCentralWidget(view)
# win.show()
view.show()
sys.exit(app.exec_())
