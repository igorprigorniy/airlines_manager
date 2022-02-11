from PyQt5 import QtCore, QtGui, QtWidgets
import parser

class Ui_main_window(object):
    def setupUi(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(1500, 1000)
        main_window.setMinimumSize(QtCore.QSize(1500, 1000))
        main_window.setMaximumSize(QtCore.QSize(1500, 1000))

        self.central_widget = QtWidgets.QWidget(main_window)
        self.central_widget.setObjectName("central_widget")

        self.table_widget = QtWidgets.QTableWidget(self.central_widget)
        self.table_widget.setGeometry(QtCore.QRect(0, 0, 1500, 900))
        self.table_widget.setObjectName("table_widget")
        self.table_widget.setColumnCount(8)
        self.table_widget.setRowCount(0)

        item = QtWidgets.QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(7, item)

        self.table_widget.setColumnWidth(0, 50)
        self.table_widget.setColumnWidth(1, 50)
        self.table_widget.setColumnWidth(2, 170)
        self.table_widget.setColumnWidth(3, 170)
        self.table_widget.setColumnWidth(4, 60)
        self.table_widget.setColumnWidth(5, 60)
        self.table_widget.setColumnWidth(6, 60)
        self.table_widget.setColumnWidth(7, 530)

        main_window.setCentralWidget(self.central_widget)

        self.menu_bar = QtWidgets.QMenuBar(main_window)
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menu_bar.setObjectName("menu_bar")

        self.menu_file = QtWidgets.QMenu(self.menu_bar)
        self.menu_file.setObjectName("menu_file")

        self.menu_help = QtWidgets.QMenu(self.menu_bar)
        self.menu_help.setObjectName("menu_help")

        main_window.setMenuBar(self.menu_bar)

        self.status_bar = QtWidgets.QStatusBar(main_window)
        self.status_bar.setObjectName("status_bar")

        main_window.setStatusBar(self.status_bar)

        self.action_add_info_from_html = QtWidgets.QAction(main_window)
        self.action_add_info_from_html.setObjectName("action_add_info_from_html")
        self.action_add_info_from_html.triggered.connect(self.add_info_from_html)

        self.action_save_info_to_am = QtWidgets.QAction(main_window)
        self.action_save_info_to_am.setObjectName("action_save_info_to_am")
        self.action_save_info_to_am.triggered.connect(self.NOT_REALIZED)

        self.action_load_info_from_am = QtWidgets.QAction(main_window)
        self.action_load_info_from_am.setObjectName("action_load_info_from_am")
        self.action_load_info_from_am.triggered.connect(self.NOT_REALIZED)

        self.action_exit = QtWidgets.QAction(main_window)
        self.action_exit.setObjectName("action_exit")
        self.action_exit.triggered.connect(self.NOT_REALIZED)

        self.action_about = QtWidgets.QAction(main_window)
        self.action_about.setObjectName("action_about")
        self.action_about.triggered.connect(self.NOT_REALIZED)

        self.menu_file.addAction(self.action_add_info_from_html)
        self.menu_file.addAction(self.action_save_info_to_am)
        self.menu_file.addAction(self.action_load_info_from_am)
        self.menu_file.addAction(self.action_exit)
        self.menu_help.addAction(self.action_about)
        self.menu_bar.addAction(self.menu_file.menuAction())
        self.menu_bar.addAction(self.menu_help.menuAction())

        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(translate("main_window", "Airlines manager"))

        item = self.table_widget.horizontalHeaderItem(0)
        item.setText(translate("main_window", "HUB"))
        item = self.table_widget.horizontalHeaderItem(1)
        item.setText(translate("main_window", "TAG"))
        item = self.table_widget.horizontalHeaderItem(2)
        item.setText(translate("main_window", "CATEGORY"))
        item = self.table_widget.horizontalHeaderItem(3)
        item.setText(translate("main_window", "DISTANCE"))
        item = self.table_widget.horizontalHeaderItem(4)
        item.setText(translate("main_window", "E"))
        item = self.table_widget.horizontalHeaderItem(5)
        item.setText(translate("main_window", "B"))
        item = self.table_widget.horizontalHeaderItem(6)
        item.setText(translate("main_window", "F"))
        item = self.table_widget.horizontalHeaderItem(7)
        item.setText(translate("main_window", "COUNTRY"))

        self.menu_file.setTitle(translate("main_window", "File"))
        self.menu_help.setTitle(translate("main_window", "Help"))
        self.action_add_info_from_html.setText(translate("main_window", "Add info from .html"))
        self.action_save_info_to_am.setText(translate("main_window", "Save info to .am"))
        self.action_load_info_from_am.setText(translate("main_window", "Load info from .am"))
        self.action_exit.setText(translate("main_window", "Exit"))
        self.action_about.setText(translate("main_window", "About"))

    def NOT_REALIZED(self):
        print('This feature has not been realized yet!')

    def add_info_from_html(self):
        print('Input file names via space:')
        airports_list = parser.html_parser(input().split())
        self.table_widget.setRowCount(len(airports_list))
        row_counter = 0

        for airport in airports_list:
            self.table_widget.setItem(row_counter, 0, QtWidgets.QTableWidgetItem(airport['HUB']))
            self.table_widget.setItem(row_counter, 1, QtWidgets.QTableWidgetItem(airport['TAG']))
            self.table_widget.setItem(row_counter, 2, QtWidgets.QTableWidgetItem(str(airport['CATEGORY'])))
            self.table_widget.setItem(row_counter, 3, QtWidgets.QTableWidgetItem(str(airport['DISTANCE'])))
            self.table_widget.setItem(row_counter, 4, QtWidgets.QTableWidgetItem(str(airport['E'])))
            self.table_widget.setItem(row_counter, 5, QtWidgets.QTableWidgetItem(str(airport['B'])))
            self.table_widget.setItem(row_counter, 6, QtWidgets.QTableWidgetItem(str(airport['F'])))
            self.table_widget.setItem(row_counter, 7, QtWidgets.QTableWidgetItem(airport['COUNTRY']))
            row_counter += 1

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = Ui_main_window()
    ui.setupUi(main_window)
    main_window.show()
    sys.exit(app.exec_())
