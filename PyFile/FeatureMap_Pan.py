#coding:utf-8
from PyQt5.Qt import *
from PIL import Image
import sys
from FeatureMap import Ui_Form
import os
from FeatureMapModule import FeatureMap
from CreateFMModule import Combine

class FeatureMapPan(QWidget,Ui_Form):
    return_ui_signal=pyqtSignal()

    def __init__(self,parent=None,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)
        self.setAttribute(Qt.WA_StyledBackground,True)
        self.setWindowState(Qt.WindowMaximized)
        self.setupUi(self)

    def select_image(self):
        self.Result_label.setText('')
        self.Img_label.clear()
        result = QFileDialog.getOpenFileName(self, '选择图片', 'C:\\Users\Administrator\Desktop', 'Images(*.jpg)')
        img_path = result[0]
        if img_path != '':
            save_path = 'F:\keti\Minzu_IR\\venv\Minzu_IR\Application\Resource\ImageData\FeatureMapImage\selected.jpg'
            self.Img_label.setPixmap(QPixmap(img_path))
            self.Img_label.setScaledContents(True)
            img = Image.open(img_path)
            img.save(save_path)
        else:
            self.show()

    def createfm(self):
        self.Result_label.setText('')
        if os.path.exists(
                'F:\keti\Minzu_IR\\venv\Minzu_IR\Application\Resource\ImageData\FeatureMapImage\selected.jpg'):
            self.featuremap = FeatureMap().get_feature()
            mb = QMessageBox(QMessageBox.Information, '提示信息', '特征图已生成，请点击对应网络层查看！', parent=self)
            mb.open()
        else:
            mb = QMessageBox(QMessageBox.Information, '提示信息', '请先选择图片！', parent=self)
            mb.open()

    def conv1(self):
        if os.path.exists(
                'F:\keti\Minzu_IR\\venv\Minzu_IR\Application\Resource\ImageData\FeatureMapImage\selected.jpg'):
            self.Result_label.setText('第一卷积层特征图')
            self.Img_label.setMaximumSize(900,900 )
            Combine().image_compose(
                'F:\keti\Minzu_IR\\venv\Minzu_IR\Application\Resource\ImageData\FeatureMapImage\\conv1\\',
                'F:\keti\Minzu_IR\\venv\Minzu_IR\Application\Resource\ImageData\FeatureMapImage\\conv1\\conv1.jpg', 8,
                8)
            self.Img_label.setPixmap(
                QPixmap(
                    'F:\keti\Minzu_IR\\venv\Minzu_IR\Application\Resource\ImageData\FeatureMapImage\\conv1\\conv1.jpg'))
            self.Img_label.setScaledContents(True)
        else:
            mb = QMessageBox(QMessageBox.Information, '提示信息', '请先选择图片！', parent=self)
            mb.open()

    def bn1(self):
        if os.path.exists(
                'F:\keti\Minzu_IR\\venv\Minzu_IR\Application\Resource\ImageData\FeatureMapImage\selected.jpg'):
            self.Result_label.setText('批正则化层特征图')
            self.Img_label.setMaximumSize(900,900 )
            Combine().image_compose(
                'F:\keti\Minzu_IR\\venv\Minzu_IR\Application\Resource\ImageData\FeatureMapImage\\bn1\\',
                'F:\keti\Minzu_IR\\venv\Minzu_IR\Application\Resource\ImageData\FeatureMapImage\\bn1\\bn1.jpg', 8, 8)
            self.Img_label.setPixmap(
                QPixmap('F:\keti\Minzu_IR\\venv\Minzu_IR\Application\Resource\ImageData\FeatureMapImage\\bn1\\bn1.jpg'))
            self.Img_label.setScaledContents(True)
        else:
            mb = QMessageBox(QMessageBox.Information, '提示信息', '请先选择图片！', parent=self)
            mb.open()

    def maxpool(self):
        if os.path.exists(
                'F:\keti\Minzu_IR\\venv\Minzu_IR\Application\Resource\ImageData\FeatureMapImage\selected.jpg'):
            self.Result_label.setText('最大池化层特征图')
            self.Img_label.setMaximumSize(900,900 )
            Combine().image_compose(
                'F:\keti\Minzu_IR\\venv\Minzu_IR\Application\Resource\ImageData\FeatureMapImage\\maxpool\\',
                'F:\keti\Minzu_IR\\venv\Minzu_IR\Application\Resource\ImageData\FeatureMapImage\\maxpool\\maxpool.jpg',
                8, 8)
            self.Img_label.setPixmap(
                QPixmap(
                    'F:\keti\Minzu_IR\\venv\Minzu_IR\Application\Resource\ImageData\FeatureMapImage\\maxpool\\maxpool.jpg'))
            self.Img_label.setScaledContents(True)
        else:
            mb = QMessageBox(QMessageBox.Information, '提示信息', '请先选择图片！', parent=self)
            mb.open()

    def resblock1(self):
        if os.path.exists(
                'F:\keti\Minzu_IR\\venv\Minzu_IR\Application\Resource\ImageData\FeatureMapImage\selected.jpg'):
            self.Result_label.setText('第一残差块特征图')
            self.Img_label.setMaximumSize(900,900 )
            Combine().image_compose(
                'F:\keti\Minzu_IR\\venv\Minzu_IR\Application\Resource\ImageData\FeatureMapImage\\layer1\\',
                'F:\keti\Minzu_IR\\venv\Minzu_IR\Application\Resource\ImageData\FeatureMapImage\\layer1\\layer1.jpg', 8,
                8)
            self.Img_label.setPixmap(
                QPixmap(
                    'F:\keti\Minzu_IR\\venv\Minzu_IR\Application\Resource\ImageData\FeatureMapImage\\layer1\\layer1.jpg'))
            self.Img_label.setScaledContents(True)
        else:
            mb = QMessageBox(QMessageBox.Information, '提示信息', '请先选择图片！', parent=self)
            mb.open()

    def resblock2(self):
        if os.path.exists(
                'F:\keti\Minzu_IR\\venv\Minzu_IR\Application\Resource\ImageData\FeatureMapImage\selected.jpg'):
            self.Result_label.setText('第二残差块特征图')
            self.Img_label.setMaximumSize(1400,700)
            Combine().image_compose(
                'F:\keti\Minzu_IR\\venv\Minzu_IR\Application\Resource\ImageData\FeatureMapImage\\layer2\\',
                'F:\keti\Minzu_IR\\venv\Minzu_IR\Application\Resource\ImageData\FeatureMapImage\\layer2\\layer2.jpg', 8,
                16)
            self.Img_label.setPixmap(
                QPixmap(
                    'F:\keti\Minzu_IR\\venv\Minzu_IR\Application\Resource\ImageData\FeatureMapImage\\layer2\\layer2.jpg'))
            self.Img_label.setScaledContents(True)
        else:
            mb = QMessageBox(QMessageBox.Information, '提示信息', '请先选择图片！', parent=self)
            mb.open()

    def resblock3(self):
        if os.path.exists(
                'F:\keti\Minzu_IR\\venv\Minzu_IR\Application\Resource\ImageData\FeatureMapImage\selected.jpg'):
            self.Result_label.setText('第三残差块特征图')
            self.Img_label.setMaximumSize(900,900)
            Combine().image_compose(
                'F:\keti\Minzu_IR\\venv\Minzu_IR\Application\Resource\ImageData\FeatureMapImage\\layer3\\',
                'F:\keti\Minzu_IR\\venv\Minzu_IR\Application\Resource\ImageData\FeatureMapImage\\layer3\\layer3.jpg',
                16, 16)
            self.Img_label.setPixmap(
                QPixmap(
                    'F:\keti\Minzu_IR\\venv\Minzu_IR\Application\Resource\ImageData\FeatureMapImage\\layer3\\layer3.jpg'))
            self.Img_label.setScaledContents(True)
        else:
            mb = QMessageBox(QMessageBox.Information, '提示信息', '请先选择图片！', parent=self)
            mb.open()

    def resblock4(self):
        if os.path.exists(
                'F:\keti\Minzu_IR\\venv\Minzu_IR\Application\Resource\ImageData\FeatureMapImage\selected.jpg'):
            self.Result_label.setText('第四残差块特征图')
            self.Img_label.setMaximumSize(1400,700)
            Combine().image_compose(
                'F:\keti\Minzu_IR\\venv\Minzu_IR\Application\Resource\ImageData\FeatureMapImage\\layer4\\',
                'F:\keti\Minzu_IR\\venv\Minzu_IR\Application\Resource\ImageData\FeatureMapImage\\layer4\\layer4.jpg',
                16, 32)
            self.Img_label.setPixmap(
                QPixmap(
                    'F:\keti\Minzu_IR\\venv\Minzu_IR\Application\Resource\ImageData\FeatureMapImage\\layer4\\layer4.jpg'))
            self.Img_label.setScaledContents(True)
        else:
            mb = QMessageBox(QMessageBox.Information, '提示信息', '请先选择图片！', parent=self)
            mb.open()

    def relu(self):
        if os.path.exists(
                'F:\keti\Minzu_IR\\venv\Minzu_IR\Application\Resource\ImageData\FeatureMapImage\selected.jpg'):
            self.Result_label.setText('激活函数特征图')
            self.Img_label.setMaximumSize(900,900)
            Combine().image_compose(
                'F:\keti\Minzu_IR\\venv\Minzu_IR\Application\Resource\ImageData\FeatureMapImage\\relu\\',
                'F:\keti\Minzu_IR\\venv\Minzu_IR\Application\Resource\ImageData\FeatureMapImage\\relu\\relu.jpg', 8, 8)
            self.Img_label.setPixmap(
                QPixmap(
                    'F:\keti\Minzu_IR\\venv\Minzu_IR\Application\Resource\ImageData\FeatureMapImage\\relu\\relu.jpg'))
            self.Img_label.setScaledContents(True)
        else:
            mb = QMessageBox(QMessageBox.Information, '提示信息', '请先选择图片！', parent=self)
            mb.open()

    def save_pic(self):
        if self.Result_label.text() == '':
            mb = QMessageBox(QMessageBox.Information, '提示信息', '请先选择对应网络层！', parent=self)
            mb.open()
        elif self.Result_label.text() == '第一卷积层特征图':
            img=Image.open('F:\keti\Minzu_IR\\venv\Minzu_IR\Application\Resource\ImageData\FeatureMapImage\\conv1\\conv1.jpg')
            img.save('C:\\Users\Administrator\Desktop\conv1.jpg')
            mb = QMessageBox(QMessageBox.Information, '提示信息', '图片已保存至桌面！', parent=self)
            mb.open()
        elif self.Result_label.text() == '批正则化层特征图':
            img=Image.open('F:\keti\Minzu_IR\\venv\Minzu_IR\Application\Resource\ImageData\FeatureMapImage\\bn1\\bn1.jpg')
            img.save('C:\\Users\Administrator\Desktop\\bn1.jpg')
            mb = QMessageBox(QMessageBox.Information, '提示信息', '图片已保存至桌面！', parent=self)
            mb.open()
        elif self.Result_label.text() == '最大池化层特征图':
            img=Image.open('F:\keti\Minzu_IR\\venv\Minzu_IR\Application\Resource\ImageData\FeatureMapImage\\maxpool\\maxpool.jpg')
            img.save('C:\\Users\Administrator\Desktop\\maxpool.jpg')
            mb = QMessageBox(QMessageBox.Information, '提示信息', '图片已保存至桌面！', parent=self)
            mb.open()
        elif self.Result_label.text() == '第一残差块特征图':
            img = Image.open(
                'F:\keti\Minzu_IR\\venv\Minzu_IR\Application\Resource\ImageData\FeatureMapImage\\layer1\\layer1.jpg')
            img.save('C:\\Users\Administrator\Desktop\\resblock1.jpg')
            mb = QMessageBox(QMessageBox.Information, '提示信息', '图片已保存至桌面！', parent=self)
            mb.open()
        elif self.Result_label.text() == '第二残差块特征图':
            img = Image.open(
                'F:\keti\Minzu_IR\\venv\Minzu_IR\Application\Resource\ImageData\FeatureMapImage\\layer2\\layer2.jpg')
            img.save('C:\\Users\Administrator\Desktop\\resblock2.jpg')
            mb = QMessageBox(QMessageBox.Information, '提示信息', '图片已保存至桌面！', parent=self)
            mb.open()
        elif self.Result_label.text() == '第三残差块特征图':
            img = Image.open(
                'F:\keti\Minzu_IR\\venv\Minzu_IR\Application\Resource\ImageData\FeatureMapImage\\layer3\\layer3.jpg')
            img.save('C:\\Users\Administrator\Desktop\\resblock3.jpg')
            mb = QMessageBox(QMessageBox.Information, '提示信息', '图片已保存至桌面！', parent=self)
            mb.open()
        elif self.Result_label.text() == '第四残差块特征图':
            img = Image.open(
                'F:\keti\Minzu_IR\\venv\Minzu_IR\Application\Resource\ImageData\FeatureMapImage\\layer4\\layer4.jpg')
            img.save('C:\\Users\Administrator\Desktop\\resblock4.jpg')
            mb = QMessageBox(QMessageBox.Information, '提示信息', '图片已保存至桌面！', parent=self)
            mb.open()
        elif self.Result_label.text() == '激活函数特征图':
            img = Image.open(
                'F:\keti\Minzu_IR\\venv\Minzu_IR\Application\Resource\ImageData\FeatureMapImage\\relu\\relu.jpg')
            img.save('C:\\Users\Administrator\Desktop\\relu.jpg')
            mb = QMessageBox(QMessageBox.Information, '提示信息', '图片已保存至桌面！', parent=self)
            mb.open()

    def return_ui(self):
        self.return_ui_signal.emit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FeatureMapPan()
    window.show()
    sys.exit(app.exec_())