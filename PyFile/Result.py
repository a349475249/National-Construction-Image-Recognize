# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Result.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1176, 743)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icon/ImageFile/Icon/AppIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("QWidget#Form{\n"
"border:4px solid rgb(255, 95, 74);\n"
"border-radius:30px;\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.Img_label = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Img_label.sizePolicy().hasHeightForWidth())
        self.Img_label.setSizePolicy(sizePolicy)
        self.Img_label.setMinimumSize(QtCore.QSize(533, 300))
        self.Img_label.setStyleSheet("")
        self.Img_label.setObjectName("Img_label")
        self.verticalLayout_6.addWidget(self.Img_label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout.addLayout(self.verticalLayout_6)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.Result_label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(26)
        self.Result_label.setFont(font)
        self.Result_label.setObjectName("Result_label")
        self.verticalLayout_5.addWidget(self.Result_label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout.addLayout(self.verticalLayout_5)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 7)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 1)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.line = QtWidgets.QFrame(Form)
        self.line.setStyleSheet("background-color: rgb(255, 95, 74);")
        self.line.setLineWidth(5)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.IntroduceText = QtWidgets.QPlainTextEdit(Form)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        self.IntroduceText.setFont(font)
        self.IntroduceText.setStyleSheet("background-color: rgba(255, 255, 255,0);")
        self.IntroduceText.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.IntroduceText.setFrameShadow(QtWidgets.QFrame.Plain)
        self.IntroduceText.setReadOnly(True)
        self.IntroduceText.setBackgroundVisible(False)
        self.IntroduceText.setObjectName("IntroduceText")
        self.horizontalLayout.addWidget(self.IntroduceText)
        self.horizontalLayout.setStretch(0, 6)
        self.horizontalLayout.setStretch(2, 4)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.line_3 = QtWidgets.QFrame(Form)
        self.line_3.setStyleSheet("background-color: rgb(255, 95, 74);")
        self.line_3.setLineWidth(5)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_2.addWidget(self.line_3)
        self.Close_Btn = QtWidgets.QPushButton(Form)
        self.Close_Btn.setMinimumSize(QtCore.QSize(160, 40))
        self.Close_Btn.setMaximumSize(QtCore.QSize(160, 40))
        self.Close_Btn.setStyleSheet("QPushButton{    \n"
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
        self.Close_Btn.setObjectName("Close_Btn")
        self.verticalLayout_2.addWidget(self.Close_Btn, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)

        self.retranslateUi(Form)
        self.Close_Btn.clicked.connect(Form.close_result_pan)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Img_label.setText(_translate("Form", "Img_label"))
        self.Result_label.setText(_translate("Form", "Result_label"))
        self.Close_Btn.setText(_translate("Form", "关闭"))
import Application_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
