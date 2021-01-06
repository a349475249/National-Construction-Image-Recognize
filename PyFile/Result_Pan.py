from PyQt5.Qt import *
import sys
from Result import Ui_Form


class ResultPan(QWidget, Ui_Form):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setWindowFlag(Qt.WindowMinMaxButtonsHint, False)
        self.setupUi(self)

    def close_result_pan(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ResultPan()
    window.show()
    sys.exit(app.exec_())
