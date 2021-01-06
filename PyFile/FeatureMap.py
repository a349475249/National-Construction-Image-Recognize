# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FeatureMap.ui'
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
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Option_area = QtWidgets.QWidget(Form)
        self.Option_area.setStyleSheet("")
        self.Option_area.setObjectName("Option_area")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.Option_area)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.ImgSelect_btn = QtWidgets.QPushButton(self.Option_area)
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
        self.verticalLayout.addWidget(self.ImgSelect_btn)
        self.CreateFM_btn = QtWidgets.QPushButton(self.Option_area)
        self.CreateFM_btn.setMinimumSize(QtCore.QSize(0, 40))
        self.CreateFM_btn.setStyleSheet("QPushButton{    \n"
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
        self.CreateFM_btn.setObjectName("CreateFM_btn")
        self.verticalLayout.addWidget(self.CreateFM_btn)
        self.Conv1 = QtWidgets.QPushButton(self.Option_area)
        self.Conv1.setMinimumSize(QtCore.QSize(0, 40))
        self.Conv1.setStyleSheet("QPushButton{    \n"
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
        self.Conv1.setFlat(False)
        self.Conv1.setObjectName("Conv1")
        self.verticalLayout.addWidget(self.Conv1)
        self.pushButton = QtWidgets.QPushButton(self.Option_area)
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
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.Maxpool_btn = QtWidgets.QPushButton(self.Option_area)
        self.Maxpool_btn.setMinimumSize(QtCore.QSize(0, 40))
        self.Maxpool_btn.setStyleSheet("QPushButton{    \n"
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
        self.Maxpool_btn.setObjectName("Maxpool_btn")
        self.verticalLayout.addWidget(self.Maxpool_btn)
        self.ResBlock1_btn = QtWidgets.QPushButton(self.Option_area)
        self.ResBlock1_btn.setMinimumSize(QtCore.QSize(0, 40))
        self.ResBlock1_btn.setStyleSheet("QPushButton{    \n"
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
        self.ResBlock1_btn.setObjectName("ResBlock1_btn")
        self.verticalLayout.addWidget(self.ResBlock1_btn)
        self.ResBlock2_btn = QtWidgets.QPushButton(self.Option_area)
        self.ResBlock2_btn.setMinimumSize(QtCore.QSize(0, 40))
        self.ResBlock2_btn.setStyleSheet("QPushButton{    \n"
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
        self.ResBlock2_btn.setObjectName("ResBlock2_btn")
        self.verticalLayout.addWidget(self.ResBlock2_btn)
        self.ResBlock3_btn = QtWidgets.QPushButton(self.Option_area)
        self.ResBlock3_btn.setMinimumSize(QtCore.QSize(0, 40))
        self.ResBlock3_btn.setStyleSheet("QPushButton{    \n"
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
        self.ResBlock3_btn.setFlat(False)
        self.ResBlock3_btn.setObjectName("ResBlock3_btn")
        self.verticalLayout.addWidget(self.ResBlock3_btn)
        self.ResBlock4_btn = QtWidgets.QPushButton(self.Option_area)
        self.ResBlock4_btn.setMinimumSize(QtCore.QSize(0, 40))
        self.ResBlock4_btn.setStyleSheet("QPushButton{    \n"
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
        self.ResBlock4_btn.setFlat(False)
        self.ResBlock4_btn.setObjectName("ResBlock4_btn")
        self.verticalLayout.addWidget(self.ResBlock4_btn)
        self.Relu_btn = QtWidgets.QPushButton(self.Option_area)
        self.Relu_btn.setMinimumSize(QtCore.QSize(0, 40))
        self.Relu_btn.setStyleSheet("QPushButton{    \n"
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
        self.Relu_btn.setObjectName("Relu_btn")
        self.verticalLayout.addWidget(self.Relu_btn)
        self.Save_btn = QtWidgets.QPushButton(self.Option_area)
        self.Save_btn.setMinimumSize(QtCore.QSize(0, 40))
        self.Save_btn.setStyleSheet("QPushButton{    \n"
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
        self.Save_btn.setObjectName("Save_btn")
        self.verticalLayout.addWidget(self.Save_btn)
        self.Return_btn = QtWidgets.QPushButton(self.Option_area)
        self.Return_btn.setMinimumSize(QtCore.QSize(0, 40))
        self.Return_btn.setStyleSheet("QPushButton{    \n"
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
        self.Return_btn.setObjectName("Return_btn")
        self.verticalLayout.addWidget(self.Return_btn)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_2.addWidget(self.Option_area)
        self.Result_area = QtWidgets.QWidget(Form)
        self.Result_area.setObjectName("Result_area")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.Result_area)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Img_label = QtWidgets.QLabel(self.Result_area)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Img_label.sizePolicy().hasHeightForWidth())
        self.Img_label.setSizePolicy(sizePolicy)
        self.Img_label.setMinimumSize(QtCore.QSize(300, 300))
        self.Img_label.setStyleSheet("")
        self.Img_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Img_label.setText("")
        self.Img_label.setScaledContents(True)
        self.Img_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Img_label.setObjectName("Img_label")
        self.verticalLayout_2.addWidget(self.Img_label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.Result_label = QtWidgets.QLabel(self.Result_area)
        self.Result_label.setStyleSheet("    font: 16pt \"楷体\";\n"
"")
        self.Result_label.setText("")
        self.Result_label.setObjectName("Result_label")
        self.verticalLayout_2.addWidget(self.Result_label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout_2.setStretch(0, 9)
        self.verticalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.addWidget(self.Result_area)
        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 8)

        self.retranslateUi(Form)
        self.Return_btn.clicked.connect(Form.return_ui)
        self.ImgSelect_btn.clicked.connect(Form.select_image)
        self.Save_btn.clicked.connect(Form.save_pic)
        self.Conv1.clicked.connect(Form.conv1)
        self.Maxpool_btn.clicked.connect(Form.maxpool)
        self.ResBlock1_btn.clicked.connect(Form.resblock1)
        self.ResBlock2_btn.clicked.connect(Form.resblock2)
        self.ResBlock3_btn.clicked.connect(Form.resblock3)
        self.ResBlock4_btn.clicked.connect(Form.resblock4)
        self.Relu_btn.clicked.connect(Form.relu)
        self.CreateFM_btn.clicked.connect(Form.createfm)
        self.pushButton.clicked.connect(Form.bn1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.ImgSelect_btn.setText(_translate("Form", "图片选择"))
        self.CreateFM_btn.setText(_translate("Form", "生成特征图"))
        self.Conv1.setText(_translate("Form", "第一卷积层"))
        self.pushButton.setText(_translate("Form", "批正则化层"))
        self.Maxpool_btn.setText(_translate("Form", "最大池化层"))
        self.ResBlock1_btn.setText(_translate("Form", "第一残差块"))
        self.ResBlock2_btn.setText(_translate("Form", "第二残差块"))
        self.ResBlock3_btn.setText(_translate("Form", "第三残差块"))
        self.ResBlock4_btn.setText(_translate("Form", "第四残差块"))
        self.Relu_btn.setText(_translate("Form", "激活函数"))
        self.Save_btn.setText(_translate("Form", "保存图片"))
        self.Return_btn.setText(_translate("Form", "返回"))
import Application_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
