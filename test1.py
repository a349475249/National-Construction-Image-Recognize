from PyFile.Regist_Pan import RegistPan
from PyFile.Login_Pan import LoginPan
from PyFile.ImageRecognize_Pan import ImageRecognizePan
from PyQt5.Qt import *
import sys




if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_pan = LoginPan()
    regist_pan = RegistPan(login_pan)
    ir_pan = ImageRecognizePan()
    regist_pan.move(0, login_pan.height())
    regist_pan.show()

    # 槽函数
    def show_regist_pan():
        login_pan.setWindowTitle('注册账号')
        animation=QPropertyAnimation(regist_pan)
        animation.setTargetObject(regist_pan)
        animation.setPropertyName(b"pos")
        animation.setStartValue(QPoint(0,login_pan.height()))
        animation.setEndValue(QPoint(0,0))
        animation.setDuration(500)
        animation.setEasingCurve(QEasingCurve.OutBounce)
        animation.start(QAbstractAnimation.DeleteWhenStopped)
    def return_login_pan():
        login_pan.setWindowTitle('民族建筑图像识别系统登录')
        animation = QPropertyAnimation(regist_pan)
        animation.setTargetObject(regist_pan)
        animation.setPropertyName(b"pos")
        animation.setStartValue(QPoint(0, 0))
        animation.setEndValue(QPoint(login_pan.width(), 0))
        animation.setDuration(500)
        animation.setEasingCurve(QEasingCurve.InBounce)
        animation.start(QAbstractAnimation.DeleteWhenStopped)
    def check_login_info(account,pwd):
        f = open('F:\keti\Minzu_IR\\venv\Minzu_IR\Application\Resource\\UserData\\act_pwd_data.txt', 'r', encoding='utf8')
        users = eval(f.read())
        name = account
        password = pwd
        if name in users and password == users[name]['pwd']:
            ir_pan.show()
            login_pan.hide()
        else:
            login_pan.error_check()
        f.close()
    # 信号
    login_pan.show_regist_pan_signal.connect(show_regist_pan)
    login_pan.login_info_signal.connect(check_login_info)
    regist_pan.return_pan_signal.connect(return_login_pan)

    login_pan.show()
    sys.exit(app.exec_())