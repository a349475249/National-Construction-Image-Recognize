# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 450)
        Form.setMinimumSize(QtCore.QSize(500, 450))
        Form.setMaximumSize(QtCore.QSize(500, 450))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icon/ImageFile/Icon/AppIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.login_gif = QtWidgets.QLabel(self.widget)
        self.login_gif.setStyleSheet("")
        self.login_gif.setText("")
        self.login_gif.setObjectName("login_gif")
        self.horizontalLayout_2.addWidget(self.login_gif)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setStyleSheet("")
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 10)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.register_account_btn = QtWidgets.QPushButton(self.widget_2)
        self.register_account_btn.setFlat(True)
        self.register_account_btn.setObjectName("register_account_btn")
        self.horizontalLayout.addWidget(self.register_account_btn, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.login_module = QtWidgets.QWidget(self.widget_2)
        self.login_module.setStyleSheet("")
        self.login_module.setObjectName("login_module")
        self.formLayout = QtWidgets.QFormLayout(self.login_module)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setContentsMargins(0, 30, 0, 0)
        self.formLayout.setHorizontalSpacing(10)
        self.formLayout.setVerticalSpacing(25)
        self.formLayout.setObjectName("formLayout")
        self.account_icon = QtWidgets.QLabel(self.login_module)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.account_icon.sizePolicy().hasHeightForWidth())
        self.account_icon.setSizePolicy(sizePolicy)
        self.account_icon.setMinimumSize(QtCore.QSize(35, 35))
        self.account_icon.setMaximumSize(QtCore.QSize(100, 100))
        self.account_icon.setAutoFillBackground(False)
        self.account_icon.setStyleSheet("border-image: url(:/Icon/ImageFile/Icon/UserIcon.png);")
        self.account_icon.setText("")
        self.account_icon.setObjectName("account_icon")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.account_icon)
        self.account_input = QtWidgets.QLineEdit(self.login_module)
        self.account_input.setMinimumSize(QtCore.QSize(0, 35))
        self.account_input.setStyleSheet("QLineEdit {    \n"
"    font-size:30px;\n"
"    border: none;\n"
"    border-bottom: 2px solid lightgray;\n"
"    background-color: transparent;\n"
"}\n"
"QLineEdit:hover {\n"
"    border-bottom: 2px solid gray;\n"
"}\n"
"QLineEdit:focus {\n"
"    border-bottom: 3px solid rgb(18, 183, 245);\n"
"}\n"
"")
        self.account_input.setText("")
        self.account_input.setMaxLength(11)
        self.account_input.setClearButtonEnabled(True)
        self.account_input.setObjectName("account_input")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.account_input)
        self.password_icon = QtWidgets.QLabel(self.login_module)
        self.password_icon.setMinimumSize(QtCore.QSize(35, 35))
        self.password_icon.setStyleSheet("border-image: url(:/Icon/ImageFile/Icon/Password.png);")
        self.password_icon.setText("")
        self.password_icon.setObjectName("password_icon")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.password_icon)
        self.password_input = QtWidgets.QLineEdit(self.login_module)
        self.password_input.setMinimumSize(QtCore.QSize(0, 35))
        self.password_input.setStyleSheet("QLineEdit {    \n"
"    font-size:15px;\n"
"    border: none;\n"
"    border-bottom: 2px solid lightgray;\n"
"    background-color: transparent;\n"
"}\n"
"QLineEdit:hover {\n"
"    border-bottom: 2px solid gray;\n"
"}\n"
"QLineEdit:focus {\n"
"    border-bottom: 3px solid rgb(18, 183, 245);\n"
"}\n"
"")
        self.password_input.setText("")
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_input.setClearButtonEnabled(True)
        self.password_input.setObjectName("password_input")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.password_input)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.remember_pwd_cb = QtWidgets.QCheckBox(self.login_module)
        self.remember_pwd_cb.setEnabled(False)
        self.remember_pwd_cb.setMaximumSize(QtCore.QSize(90, 16777215))
        self.remember_pwd_cb.setCheckable(True)
        self.remember_pwd_cb.setObjectName("remember_pwd_cb")
        self.horizontalLayout_3.addWidget(self.remember_pwd_cb)
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.SpanningRole, self.horizontalLayout_3)
        self.login_btn = QtWidgets.QPushButton(self.login_module)
        self.login_btn.setEnabled(False)
        self.login_btn.setMinimumSize(QtCore.QSize(0, 50))
        self.login_btn.setMaximumSize(QtCore.QSize(300, 16777215))
        self.login_btn.setStyleSheet("QPushButton{    \n"
"    background-color: rgb(33, 174, 250);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius:10px;    \n"
"    font: 14pt \"宋体\";\n"
"}\n"
"QPushButton:hover{    \n"
"    background-color: rgb(78, 196, 250);    \n"
"}\n"
"QPushButton:pressed{    \n"
"    background-color: rgb(24, 131, 188);\n"
"}\n"
"QPushButton:disabled{    \n"
"    background-color: rgb(135, 135, 135);\n"
"}\n"
"    \n"
"\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Icon/ImageFile/Icon/Shield.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.login_btn.setIcon(icon1)
        self.login_btn.setIconSize(QtCore.QSize(35, 35))
        self.login_btn.setObjectName("login_btn")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.login_btn)
        self.horizontalLayout.addWidget(self.login_module)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 6)
        self.horizontalLayout.setStretch(2, 2)
        self.verticalLayout.addWidget(self.widget_2)
        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 3)

        self.retranslateUi(Form)
        self.password_input.textChanged['QString'].connect(Form.enabel_login_btn)
        self.login_btn.clicked.connect(Form.login_btn_clicked)
        self.remember_pwd_cb.clicked['bool'].connect(Form.remember_pwd)
        self.register_account_btn.clicked.connect(Form.show_regist_pan)
        self.account_input.textChanged['QString'].connect(Form.enabel_login_btn)
        self.account_input.textChanged['QString'].connect(Form.enable_remember_cb)
        self.password_input.textChanged['QString'].connect(Form.enable_remember_cb)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "民族建筑图像识别系统登录"))
        self.register_account_btn.setText(_translate("Form", "注册账号"))
        self.remember_pwd_cb.setText(_translate("Form", "记住密码"))
        self.login_btn.setText(_translate("Form", "登录"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
