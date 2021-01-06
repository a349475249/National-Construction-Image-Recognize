from PyFile.Regist_Pan import RegistPan
from PyFile.Login_Pan import LoginPan
from PyFile.ImageRecognize_Pan import ImageRecognizePan
from PyFile.UserInterface_Pan import UserInterfacePan
from PyFile.FeatureMap_Pan import FeatureMapPan
from PyQt5.Qt import *
import sys


class GUI():
    def __init__(self):
        app = QApplication(sys.argv)
        self.login_pan = LoginPan()
        self.regist_pan = RegistPan(self.login_pan)
        self.userinterface_pan = UserInterfacePan()
        self.ir_pan = ImageRecognizePan(self.userinterface_pan)
        self.ir_pan.hide()
        self.fm_pan = FeatureMapPan(self.userinterface_pan)
        self.fm_pan.hide()
        self.regist_pan.move(0, self.login_pan.height())
        self.regist_pan.show()
        self.login_pan.show_regist_pan_signal.connect(self.show_regist_pan)
        self.login_pan.login_info_signal.connect(self.check_login_info)
        self.regist_pan.return_pan_signal.connect(self.return_login_pan)
        self.userinterface_pan.show_ir_pan_signal.connect(self.show_ir_pan)
        self.userinterface_pan.show_fm_pan_signal.connect(self.show_fm_pan)
        self.ir_pan.return_ui_signal.connect(self.return_ui_pan_from_ir_pan)
        self.fm_pan.return_ui_signal.connect(self.return_ui_pan_from_fm_pan)
        self.userinterface_pan.ir_pan_size_signal.connect(self.ir_pan_resize)
        self.userinterface_pan.fm_pan_size_signal.connect(self.fm_pan_resize)

        self.login_pan.show()
        sys.exit(app.exec_())

    def show_ir_pan(self):
        self.fm_pan.hide()
        self.fm_pan.Img_label.clear()
        self.fm_pan.Result_label.clear()
        x = self.userinterface_pan.function_area.x()
        y = self.userinterface_pan.function_area.y()
        height = self.userinterface_pan.function_area.height()
        width = self.userinterface_pan.function_area.width()
        self.ir_pan.resize(width, height)
        self.ir_pan.move(0, self.userinterface_pan.height())
        self.ir_pan.show()
        animation = QPropertyAnimation(self.ir_pan)
        animation.setTargetObject(self.ir_pan)
        animation.setPropertyName(b"pos")
        animation.setStartValue(QPoint(x, height))
        animation.setEndValue(QPoint(x, y))
        animation.setDuration(300)
        animation.start(QAbstractAnimation.DeleteWhenStopped)

    def show_fm_pan(self):
        self.ir_pan.hide()
        self.ir_pan.Img_label.clear()
        x = self.userinterface_pan.function_area.x()
        y = self.userinterface_pan.function_area.y()
        height = self.userinterface_pan.function_area.height()
        width = self.userinterface_pan.function_area.width()
        self.fm_pan.resize(width, height)
        self.fm_pan.move(0, self.userinterface_pan.height())
        self.fm_pan.show()
        animation = QPropertyAnimation(self.fm_pan)
        animation.setTargetObject(self.fm_pan)
        animation.setPropertyName(b"pos")
        animation.setStartValue(QPoint(x, height))
        animation.setEndValue(QPoint(x, y))
        animation.setDuration(300)
        animation.start(QAbstractAnimation.DeleteWhenStopped)

    def show_regist_pan(self):
        self.login_pan.setWindowTitle('注册账号')
        animation = QPropertyAnimation(self.regist_pan)
        animation.setTargetObject(self.regist_pan)
        animation.setPropertyName(b"pos")
        animation.setStartValue(QPoint(0, self.login_pan.height()))
        animation.setEndValue(QPoint(0, 0))
        animation.setDuration(500)
        animation.setEasingCurve(QEasingCurve.OutBounce)
        animation.start(QAbstractAnimation.DeleteWhenStopped)

    def return_login_pan(self):
        self.login_pan.setWindowTitle('民族建筑图像识别系统登录')
        animation = QPropertyAnimation(self.regist_pan)
        animation.setTargetObject(self.regist_pan)
        animation.setPropertyName(b"pos")
        animation.setStartValue(QPoint(0, 0))
        animation.setEndValue(QPoint(self.login_pan.width(), 0))
        animation.setDuration(500)
        animation.setEasingCurve(QEasingCurve.InBounce)
        animation.start(QAbstractAnimation.DeleteWhenStopped)

    def return_ui_pan_from_ir_pan(self):
        x = self.userinterface_pan.function_area.x()
        y = self.userinterface_pan.function_area.y()
        # animation = QPropertyAnimation(self.ir_pan)
        # animation.setTargetObject(self.ir_pan)
        # animation.setPropertyName(b"pos")
        # animation.setStartValue(QPoint(x, y))
        # animation.setEndValue(QPoint(x, self.userinterface_pan.height()))
        # animation.setDuration(300)
        # animation.start(QAbstractAnimation.DeleteWhenStopped)
        self.ir_pan.Img_label.clear()
        self.ir_pan.close()

    def return_ui_pan_from_fm_pan(self):
        x = self.userinterface_pan.function_area.x()
        y = self.userinterface_pan.function_area.y()
        animation = QPropertyAnimation(self.fm_pan)
        animation.setTargetObject(self.fm_pan)
        animation.setPropertyName(b"pos")
        animation.setStartValue(QPoint(x, y))
        animation.setEndValue(QPoint(x, self.userinterface_pan.height()))
        animation.setDuration(300)
        animation.start(QAbstractAnimation.DeleteWhenStopped)
        self.fm_pan.Img_label.clear()
        self.fm_pan.Result_label.clear()
        self.fm_pan.close()

    def check_login_info(self, account, pwd):
        self.userinterface_pan.show()
        self.login_pan.hide()
        # f = open('F:\keti\Minzu_IR\\venv\Minzu_IR\Application\Resource\\UserData\\act_pwd_data.txt', 'r',
        #          encoding='utf8')
        # users = eval(f.read())
        # name = account
        # password = pwd
        # if name in users and password == users[name]['pwd']:
        #     self.userinterface_pan.show()
        #     self.login_pan.hide()
        # else:
        #     self.login_pan.error_check()
        # f.close()

    def ir_pan_resize(self, x, y, height, width):
        x = x
        y = y
        height = height
        width = width
        self.ir_pan.move(x, y)
        self.ir_pan.resize(width, height)

    def fm_pan_resize(self, x, y, height, width):
        x = x
        y = y
        height = height
        width = width
        self.fm_pan.move(x, y)
        self.fm_pan.resize(width, height)


if __name__ == '__main__':
    app = GUI()
