# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ImageRecognize.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1172, 778)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icon/ImageFile/Icon/AppIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setWindowOpacity(0.5)
        Form.setStyleSheet("QWidget#Form{\n"
"border:4px solid rgb(255, 95, 74);\n"
"border-radius:30px;\n"
"background-color: rgba(255, 255, 255,150);\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(13, 13, 13, 13)
        self.verticalLayout.setSpacing(13)
        self.verticalLayout.setObjectName("verticalLayout")
        self.result_area = QtWidgets.QWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.result_area.sizePolicy().hasHeightForWidth())
        self.result_area.setSizePolicy(sizePolicy)
        self.result_area.setObjectName("result_area")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.result_area)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Img_label = QtWidgets.QLabel(self.result_area)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Img_label.sizePolicy().hasHeightForWidth())
        self.Img_label.setSizePolicy(sizePolicy)
        self.Img_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Img_label.setText("")
        self.Img_label.setScaledContents(True)
        self.Img_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Img_label.setObjectName("Img_label")
        self.horizontalLayout_3.addWidget(self.Img_label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout.addWidget(self.result_area)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(7)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.ImgSelect_btn = QtWidgets.QPushButton(Form)
        self.ImgSelect_btn.setMinimumSize(QtCore.QSize(0, 40))
        self.ImgSelect_btn.setStyleSheet("QPushButton{    \n"
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
"}")
        self.ImgSelect_btn.setFlat(False)
        self.ImgSelect_btn.setObjectName("ImgSelect_btn")
        self.horizontalLayout_2.addWidget(self.ImgSelect_btn, 0, QtCore.Qt.AlignBottom)
        self.Recognize_btn = QtWidgets.QPushButton(Form)
        self.Recognize_btn.setMinimumSize(QtCore.QSize(0, 40))
        self.Recognize_btn.setStyleSheet("QPushButton{    \n"
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
"}")
        self.Recognize_btn.setFlat(False)
        self.Recognize_btn.setObjectName("Recognize_btn")
        self.horizontalLayout_2.addWidget(self.Recognize_btn, 0, QtCore.Qt.AlignBottom)
        self.Clean_btn = QtWidgets.QPushButton(Form)
        self.Clean_btn.setMinimumSize(QtCore.QSize(0, 40))
        self.Clean_btn.setStyleSheet("QPushButton{    \n"
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
"}")
        self.Clean_btn.setFlat(False)
        self.Clean_btn.setObjectName("Clean_btn")
        self.horizontalLayout_2.addWidget(self.Clean_btn, 0, QtCore.Qt.AlignBottom)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton.setStyleSheet("QPushButton{    \n"
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
"}")
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton, 0, QtCore.Qt.AlignBottom)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 1)
        self.horizontalLayout_2.setStretch(3, 1)
        self.horizontalLayout_2.setStretch(4, 1)
        self.horizontalLayout_2.setStretch(5, 2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.setStretch(0, 10)

        self.retranslateUi(Form)
        self.ImgSelect_btn.clicked.connect(Form.select_image)
        self.Recognize_btn.clicked.connect(Form.recognize_image)
        self.Clean_btn.clicked.connect(Form.clear)
        self.pushButton.clicked.connect(Form.return_ui)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.ImgSelect_btn.setText(_translate("Form", "图片选择"))
        self.Recognize_btn.setText(_translate("Form", "识别"))
        self.Clean_btn.setText(_translate("Form", "清空"))
        self.pushButton.setText(_translate("Form", "返回"))
import Application_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
