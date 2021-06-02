class MainScene(QtWidgets.QGraphicsScene): # интерфейс сцены, в этой сцене есть все атрибуты сцены, которые использует вью

    def __init__(self, ui_class, parent):
        super(MainScene, self).__init__()
        self.setSceneRect(0, 0, parent.width-2, parent.height-2)
        self.widget = QtWidgets.QWidget()
        self.widget.main_ui = widget_ui.Ui_MainWidget()
        self.widget.main_ui.setupUi(self.widget)
        self.widget.ui = ui_class()
        self.widget.ui.setupUi(self.widget)
        self.pwidget = self.addWidget(self.widget)

        self.widget.main_ui.button_close.clicked.connect(parent.close)
        self.widget.main_ui.button_roll.clicked.connect(parent.showMinimized)