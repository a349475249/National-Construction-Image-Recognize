from PyQt5.Qt import *
import sys
from Login import Ui_Form

class LoginPan(QWidget,Ui_Form):
    show_regist_pan_signal=pyqtSignal()
    login_info_signal=pyqtSignal(str,str)

    def __init__(self,parent=None,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, False)
        self.setupUi(self)
        movie = QMovie(':/BackgroundIMG/ImageFile/IMG/login_top_bg.gif')
        movie.setScaledSize(QSize(500, 180))
        self.login_gif.setMovie(movie)
        movie.start()

    def show_regist_pan(self):
        self.show_regist_pan_signal.emit()

    def enabel_login_btn(self):
        account_txt=self.account_input.text()
        password_txt=self.password_input.text()
        if len(account_txt)>0 and len(password_txt)>0:
            self.login_btn.setEnabled(True)
        else:
            self.login_btn.setEnabled(False)

    def enable_remember_cb(self):
        if len(self.account_input.text())>0:
            self.remember_pwd_cb.setEnabled(True)
        else:
            self.remember_pwd_cb.setEnabled(False)

    def login_btn_clicked(self):
        account_txt = self.account_input.text()
        password_txt = self.password_input.text()
        self.login_info_signal.emit(account_txt,password_txt)

    def remember_pwd(self,status):
        # f = open("../UserData/act_pwd_data.txt",  'r', encoding='utf8')
        # users = eval(f.read())
        # name = self.account_input.text()
        # password = users[name]['pwd']
        # if status:
        #     self.password_input.setText(password)
        pass

    def error_check(self):
        animation=QPropertyAnimation(self)
        animation.setTargetObject(self.login_module)
        animation.setPropertyName(b"pos")
        animation.setKeyValueAt(0,self.login_module.pos())
        animation.setKeyValueAt(0.25,self.login_module.pos()+QPoint(15,0))
        animation.setKeyValueAt(0.5,self.login_module.pos())
        animation.setKeyValueAt(0.75,self.login_module.pos()+QPoint(-15,0))
        animation.setKeyValueAt(1,self.login_module.pos())
        animation.setDuration(100)
        animation.setLoopCount(3)
        animation.start(QAbstractAnimation.DeleteWhenStopped)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginPan()
    window.show_regist_pan_signal.connect(lambda :print('显示注册界面'))
    window.login_info_signal.connect(lambda act,pwd:print(act,pwd))
    window.show()
    sys.exit(app.exec_())