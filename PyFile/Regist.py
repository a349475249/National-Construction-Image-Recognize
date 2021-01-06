# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Regist.ui'
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
        Form.setStyleSheet("QWidget#Form{\n"
"    border-image:url(:/BackgroundIMG/ImageFile/IMG/bgi3.jpg)\n"
"}")
        self.menu_btn = QtWidgets.QPushButton(Form)
        self.menu_btn.setGeometry(QtCore.QRect(20, 20, 60, 30))
        self.menu_btn.setStyleSheet("QPushButton{\n"
"    border-radius:10px;\n"
"    background-color:rgba(255, 255, 255,150);\n"
"    font: 12pt \"楷体\";\n"
"    color: rgb(57, 57, 57);\n"
"    border:2px solid rgb(53, 122, 165)\n"
"}\n"
"QPushButton:hover {\n"
"    border:4px solid rgb(255, 95, 74);\n"
"}\n"
"QPushButton:checked{\n"
"    background-color:rgba(33, 174, 250,250)\n"
"}")
        self.menu_btn.setCheckable(True)
        self.menu_btn.setObjectName("menu_btn")
        self.about_btn = QtWidgets.QPushButton(Form)
        self.about_btn.setGeometry(QtCore.QRect(20, 60, 60, 30))
        self.about_btn.setStyleSheet("QPushButton{\n"
"    border-radius:10px;\n"
"    background-color:rgba(255, 255, 255,150);\n"
"    font: 12pt \"楷体\";\n"
"    color: rgb(57, 57, 57);\n"
"    border:2px solid rgb(53, 122, 165)\n"
"}\n"
"QPushButton:hover {\n"
"    border:4px solid rgb(255, 95, 74);\n"
"}\n"
"QPushButton:checked{\n"
"    background-color:rgb(216, 48, 79)\n"
"}")
        self.about_btn.setCheckable(False)
        self.about_btn.setObjectName("about_btn")
        self.reset_btn = QtWidgets.QPushButton(Form)
        self.reset_btn.setGeometry(QtCore.QRect(20, 100, 60, 30))
        self.reset_btn.setStyleSheet("QPushButton{\n"
"    border-radius:10px;\n"
"    background-color:rgba(255, 255, 255,150);\n"
"    font: 12pt \"楷体\";\n"
"    color: rgb(57, 57, 57);\n"
"    border:2px solid rgb(53, 122, 165)\n"
"}\n"
"QPushButton:hover {\n"
"    border:4px solid rgb(255, 95, 74);\n"
"}\n"
"QPushButton:checked{\n"
"    background-color:rgb(216, 48, 79)\n"
"}")
        self.reset_btn.setCheckable(False)
        self.reset_btn.setObjectName("reset_btn")
        self.return_btn = QtWidgets.QPushButton(Form)
        self.return_btn.setGeometry(QtCore.QRect(20, 140, 60, 30))
        self.return_btn.setStyleSheet("QPushButton{\n"
"    border-radius:10px;\n"
"    background-color:rgba(255, 255, 255,150);\n"
"    font: 12pt \"楷体\";\n"
"    color: rgb(57, 57, 57);\n"
"    border:2px solid rgb(53, 122, 165)\n"
"}\n"
"QPushButton:hover {\n"
"    border:4px solid rgb(255, 95, 74);\n"
"}\n"
"QPushButton:checked{\n"
"    background-color:rgb(216, 48, 79)\n"
"}")
        self.return_btn.setCheckable(False)
        self.return_btn.setObjectName("return_btn")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(130, 210, 242, 163))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.account_le = QtWidgets.QLineEdit(self.layoutWidget)
        self.account_le.setMinimumSize(QtCore.QSize(240, 35))
        self.account_le.setStyleSheet("QLineEdit{\n"
"background-color:rgba(255, 255, 255,170);\n"
"color:rgb(0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid lightgray;\n"
"border-radius:10px;\n"
"font: 12pt \"楷体\";\n"
"font-color:rgb(62, 62, 62);\n"
"}\n"
"QLineEdit:focus{\n"
"border-bottom:3px solid rgb(0, 182, 218);\n"
"}")
        self.account_le.setText("")
        self.account_le.setMaxLength(11)
        self.account_le.setFrame(True)
        self.account_le.setClearButtonEnabled(True)
        self.account_le.setObjectName("account_le")
        self.verticalLayout.addWidget(self.account_le)
        self.password_le = QtWidgets.QLineEdit(self.layoutWidget)
        self.password_le.setMinimumSize(QtCore.QSize(240, 35))
        self.password_le.setStyleSheet("QLineEdit{\n"
"background-color:rgba(255, 255, 255,170);\n"
"color:rgb(0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid lightgray;\n"
"border-radius:10px;\n"
"font: 12pt \"楷体\";\n"
"font-color:rgb(62, 62, 62);\n"
"}\n"
"QLineEdit:focus{\n"
"border-bottom:3px solid rgb(0, 182, 218);\n"
"}")
        self.password_le.setMaxLength(11)
        self.password_le.setFrame(True)
        self.password_le.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_le.setClearButtonEnabled(True)
        self.password_le.setObjectName("password_le")
        self.verticalLayout.addWidget(self.password_le)
        self.confirm_le = QtWidgets.QLineEdit(self.layoutWidget)
        self.confirm_le.setMinimumSize(QtCore.QSize(240, 35))
        self.confirm_le.setStyleSheet("QLineEdit{\n"
"background-color:rgba(255, 255, 255,170);\n"
"color:rgb(0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid lightgray;\n"
"border-radius:10px;\n"
"font: 12pt \"楷体\";\n"
"font-color:rgb(62, 62, 62);\n"
"}\n"
"QLineEdit:focus{\n"
"border-bottom:3px solid rgb(0, 182, 218);\n"
"}")
        self.confirm_le.setMaxLength(11)
        self.confirm_le.setFrame(True)
        self.confirm_le.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirm_le.setClearButtonEnabled(True)
        self.confirm_le.setObjectName("confirm_le")
        self.verticalLayout.addWidget(self.confirm_le)
        self.regist_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.regist_btn.setEnabled(False)
        self.regist_btn.setMinimumSize(QtCore.QSize(240, 35))
        self.regist_btn.setStyleSheet("QPushButton{    \n"
"    background-color: rgb(33, 174, 250);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius:10px;    \n"
"    font: 16pt \"楷体\";\n"
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
"")
        self.regist_btn.setCheckable(False)
        self.regist_btn.setObjectName("regist_btn")
        self.verticalLayout.addWidget(self.regist_btn)
        self.about_btn.raise_()
        self.reset_btn.raise_()
        self.return_btn.raise_()
        self.layoutWidget.raise_()
        self.menu_btn.raise_()

        self.retranslateUi(Form)
        self.menu_btn.clicked['bool'].connect(Form.hide_show_menu)
        self.about_btn.clicked.connect(Form.about)
        self.regist_btn.clicked.connect(Form.regist)
        self.reset_btn.clicked.connect(Form.reset)
        self.account_le.textChanged['QString'].connect(Form.enable_regist_btn)
        self.password_le.textChanged['QString'].connect(Form.enable_regist_btn)
        self.confirm_le.textChanged['QString'].connect(Form.enable_regist_btn)
        self.return_btn.clicked.connect(Form.return_pan)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "民族建筑识别系统注册"))
        self.menu_btn.setText(_translate("Form", "菜单"))
        self.about_btn.setText(_translate("Form", "关于"))
        self.reset_btn.setText(_translate("Form", "重置"))
        self.return_btn.setText(_translate("Form", "返回"))
        self.account_le.setPlaceholderText(_translate("Form", "请输入账号"))
        self.password_le.setPlaceholderText(_translate("Form", "请输入密码"))
        self.confirm_le.setPlaceholderText(_translate("Form", "请确认密码"))
        self.regist_btn.setText(_translate("Form", "注册"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
