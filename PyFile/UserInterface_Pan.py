from PyQt5.Qt import *
import sys
from UserInterface import Ui_UserInterface


class UserInterfacePan(QWidget,Ui_UserInterface):
    show_ir_pan_signal=pyqtSignal()
    show_fm_pan_signal=pyqtSignal()
    ir_pan_size_signal=pyqtSignal(int,int,int,int)
    fm_pan_size_signal=pyqtSignal(int,int,int,int)
    def __init__(self,parent=None,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)
        self.setAttribute(Qt.WA_StyledBackground,True)
        self.setWindowState(Qt.WindowMaximized)
        self.setupUi(self)
    def ir_pan_show(self):
        self.show_ir_pan_signal.emit()

    def fm_pan_show(self):
        self.show_fm_pan_signal.emit()

    def resizeEvent(self, evt):
        x=self.function_area.x()
        y=self.function_area.y()
        height=self.function_area.height()
        width=self.function_area.width()
        self.ir_pan_size_signal.emit(x,y,height,width)
        self.fm_pan_size_signal.emit(x,y,height,width)

    def exit_ui(self):
        self.close()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = UserInterfacePan()
    window.show()
    sys.exit(app.exec_())