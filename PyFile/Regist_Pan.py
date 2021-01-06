from PyQt5.Qt import *
import sys
from Regist import Ui_Form

class RegistPan(QWidget,Ui_Form):
    return_pan_signal=pyqtSignal()
    regist_signal=pyqtSignal(str,str,str)
    def __init__(self,parent=None,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)
        self.setAttribute(Qt.WA_StyledBackground,True)
        self.setWindowFlag(Qt.WindowMinMaxButtonsHint,False)
        self.setupUi(self)
        self.animation_targets=[self.about_btn,self.reset_btn,self.return_btn]
        self.animation_targets_pos=[target.pos() for target in self.animation_targets]

    def hide_show_menu(self,checked):
        animation_group=QSequentialAnimationGroup(self)
        for idx,target in enumerate(self.animation_targets):
            animation=QPropertyAnimation()
            animation.setTargetObject(target)
            animation.setPropertyName(b"pos")
            animation.setStartValue(self.menu_btn.pos())
            animation.setEndValue(self.animation_targets_pos[idx])
            animation.setDuration(200)
            animation_group.addAnimation(animation)
        if not checked:
            animation_group.setDirection(QAbstractAnimation.Forward)
        else:
            animation_group.setDirection(QAbstractAnimation.Backward)
        animation_group.start(QAbstractAnimation.DeleteWhenStopped)

    def about(self):
        QMessageBox.about(self, "注册提示", "请在用户界面注册您的账号！")

    def regist(self):
        name = self.account_le.text()
        password = self.password_le.text()
        confirm_pwd = self.confirm_le.text()
        f = open("F:\keti\Minzu_IR\\venv\Minzu_IR\Application\Resource\\UserData\\act_pwd_data.txt", 'r+')
        users = eval(f.read())
        if len(name.strip()) != 0 and name not in users and len(password.strip()) != 0 and password == confirm_pwd:
            if len(password) <6:
                QMessageBox.about(self, "提示消息", "密码最小为6为位")
            else:
                users[name] = {'pwd': password, 'role': 1}
                f.seek(0)
                f.truncate()
                f.writelines(str(users))
                QMessageBox.about(self, "提示消息", "注册成功！")
                f.close()
        elif name in users:
            QMessageBox.about(self, "提示消息", "该用户名已注册，请重新输入！")
        elif confirm_pwd != password:
            QMessageBox.about(self, "提示消息", "两次输入的密码不一致，请重新输入！")

    def return_pan(self):
        self.return_pan_signal.emit()

    def reset(self):
        self.account_le.clear()
        self.password_le.clear()
        self.confirm_le.clear()

    def enable_regist_btn(self):
        account_txt = self.account_le.text()
        password_txt = self.password_le.text()
        confirm_txt = self.confirm_le.text()
        if len(account_txt) > 0 and len(password_txt) > 0 and len(confirm_txt) > 0:
            self.regist_btn.setEnabled(True)
        else:
            self.regist_btn.setEnabled(False)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RegistPan()
    window.show()
    sys.exit(app.exec_())