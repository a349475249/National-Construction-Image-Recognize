# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UserInterface.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_UserInterface(object):
    def setupUi(self, UserInterface):
        UserInterface.setObjectName("UserInterface")
        UserInterface.resize(1256, 720)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icon/ImageFile/Icon/AppIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        UserInterface.setWindowIcon(icon)
        UserInterface.setStyleSheet("QWidget#UserInterface\n"
"{border-image: url(:/BackgroundIMG/ImageFile/IMG/userinterface_bg.jpg);\n"
"}")
        self.horizontalLayout = QtWidgets.QHBoxLayout(UserInterface)
        self.horizontalLayout.setContentsMargins(15, 15, 15, 15)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.option_area = QtWidgets.QWidget(UserInterface)
        self.option_area.setObjectName("option_area")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.option_area)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.ir_btn = QtWidgets.QPushButton(self.option_area)
        self.ir_btn.setMinimumSize(QtCore.QSize(120, 40))
        self.ir_btn.setStyleSheet("QPushButton{    \n"
"\n"
"    background-color: rgba(33, 174, 250,150);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius:10px;    \n"
"    font: 16pt \"楷体\";\n"
"}\n"
"QPushButton:hover{    \n"
"    background-color: rgba(78, 196, 250,150);    \n"
"}\n"
"QPushButton:pressed{    \n"
"    background-color: rgba(24, 131, 188,150);\n"
"}")
        self.ir_btn.setFlat(False)
        self.ir_btn.setObjectName("ir_btn")
        self.verticalLayout.addWidget(self.ir_btn)
        self.pushButton = QtWidgets.QPushButton(self.option_area)
        self.pushButton.setMinimumSize(QtCore.QSize(120, 40))
        self.pushButton.setStyleSheet("QPushButton{    \n"
"\n"
"    background-color: rgba(33, 174, 250,150);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius:10px;    \n"
"    font: 16pt \"楷体\";\n"
"}\n"
"QPushButton:hover{    \n"
"    background-color: rgba(78, 196, 250,150);    \n"
"}\n"
"QPushButton:pressed{    \n"
"    background-color: rgba(24, 131, 188,150);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.ir_btn_2 = QtWidgets.QPushButton(self.option_area)
        self.ir_btn_2.setMinimumSize(QtCore.QSize(120, 40))
        self.ir_btn_2.setStyleSheet("QPushButton{    \n"
"\n"
"    background-color: rgba(33, 174, 250,150);\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius:10px;    \n"
"    font: 16pt \"楷体\";\n"
"}\n"
"QPushButton:hover{    \n"
"    background-color: rgba(78, 196, 250,150);    \n"
"}\n"
"QPushButton:pressed{    \n"
"    background-color: rgba(24, 131, 188,150);\n"
"}")
        self.ir_btn_2.setFlat(False)
        self.ir_btn_2.setObjectName("ir_btn_2")
        self.verticalLayout.addWidget(self.ir_btn_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout.addWidget(self.option_area)
        self.function_area = QtWidgets.QWidget(UserInterface)
        self.function_area.setStyleSheet("")
        self.function_area.setObjectName("function_area")
        self.horizontalLayout.addWidget(self.function_area)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 8)

        self.retranslateUi(UserInterface)
        self.ir_btn.clicked.connect(UserInterface.ir_pan_show)
        self.ir_btn_2.clicked.connect(UserInterface.exit_ui)
        self.pushButton.clicked.connect(UserInterface.fm_pan_show)
        QtCore.QMetaObject.connectSlotsByName(UserInterface)

    def retranslateUi(self, UserInterface):
        _translate = QtCore.QCoreApplication.translate
        UserInterface.setWindowTitle(_translate("UserInterface", "民族建筑图像识别系统"))
        self.ir_btn.setText(_translate("UserInterface", "     图像识别     "))
        self.pushButton.setText(_translate("UserInterface", "查看特征图"))
        self.ir_btn_2.setText(_translate("UserInterface", "退出"))
import Application_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UserInterface = QtWidgets.QWidget()
    ui = Ui_UserInterface()
    ui.setupUi(UserInterface)
    UserInterface.show()
    sys.exit(app.exec_())
