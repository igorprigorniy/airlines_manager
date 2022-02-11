import sys
import PyQt5
import main_window

def application():
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    win = PyQt5.QtWidgets.QMainWindow()

    main_window_ui = main_window.Ui_main_window()
    main_window_ui.setupUi(win)

    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':

    application()
