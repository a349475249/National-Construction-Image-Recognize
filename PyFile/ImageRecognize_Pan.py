from PyQt5.Qt import *
from PIL import Image
import sys
import os
from ImageRecognize import Ui_Form
from Result_Pan import ResultPan
from RecognizeModule import Recognize


class ImageRecognizePan(QWidget, Ui_Form):
    return_ui_signal = pyqtSignal()

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setWindowState(Qt.WindowMaximized)
        self.setupUi(self)
        self.result_pan = ResultPan(self)
        self.result_pan.hide()

    def select_image(self):
        result = QFileDialog.getOpenFileName(self, '选择图片', 'C:\\Users\Administrator\Desktop', 'Images(*.jpg)')
        img_path = result[0]
        if img_path != '':
            save_path = 'F:\keti\Minzu_IR\\venv\Minzu_IR\Application\Resource\ImageData\PredictImage\Predicting\predict.jpg'
            self.Img_label.setPixmap(QPixmap(img_path))
            self.Img_label.setScaledContents(True)
            img = Image.open(img_path)
            img.save(save_path)
        else:
            self.show()

    def recognize_image(self):
        img_path = 'F:\keti\Minzu_IR\\venv\Minzu_IR\Application\Resource\ImageData\PredictImage\Predicting\predict.jpg'
        if os.path.exists(img_path):
            self.pred = Recognize().predict()

            self.result_pan.Img_label.setPixmap(QPixmap(img_path))
            self.result_pan.Img_label.setScaledContents(True)
            self.result_pan.Result_label.setText(self.pred)
            if self.pred == "苗族":
                self.result_pan.IntroduceText.setPlainText(
                    "    苗族建筑有吊脚楼和落地式房屋。吊脚楼一般以四排三间为一幢，有的除了正房外，还搭了一两个“偏厦”。每排木柱一般9根，即五柱四瓜。每幢木楼，一般分三层，上层储谷，中层住人，下层楼脚围栏成圈，作堆放杂物或关养牲畜。住人的一层，旁有木梯与楼上层和下层相接，该层设有走廊通道，约1米宽。堂屋是迎客间，两侧各间则隔为二三小间为卧室或厨房。房间宽敞明亮，门窗左右对称。有的苗家还在侧间设有火坑，冬天就在这烧火取暖。中堂前有大门，门是两扇，两边各有一窗。中堂的前檐下，都装有靠背栏杆，称“美人靠”。落地式房屋多分布在黔东湘西的一些平坦地区，中柱直接建立在平坦的地上，没有吊脚。房屋为五柱七瓜三排、七柱九瓜三排的不等，以三层为主，第一层即落地层，左右两排为日常生活之用，进伸二或三间，中间排为中堂，后为神龛。左后一间通常为茶中，为向火、煮饭之用，前两间为主人卧室或客房。平地房的厨房一般设在正房的一边，另起一小偏房。二楼前面的全为客房，后面的全为储存谷物等储藏室。三楼为放置一些杂物之用。一般家禽都在离正房屋几米的周围，而牛圈羊舍则更远些。")
            elif self.pred == "侗族":
                self.result_pan.IntroduceText.setPlainText(
                    "    侗族地区的民居具有鲜明的地方特点和浓郁的民族特色，建筑多为木质结构，贵州侗族分为“北侗”、“南侗”两个部分。北侗地区的民居与当地汉族的民居极为相似，一般都是一楼一底、四榀三间的木结构楼房。屋面覆盖小青瓦，四周安装木板壁，或者垒砌土坯墙。有些侗族民居在正房前二楼下，横腰加建一披檐，此作增加檐下使用空间，形成宽敞前廊，便于小憩纳凉。南部侗族地区盛产杉木，民居建筑体积较大，房屋高度很不一般。在竹木掩映的侗寨中,面阔五间.高三四层的庞然大物比比皆是，至今仍保留着古代越人的“干栏”式木楼。如果有高大宽敞的楼房，房东特别贤惠，又有能歌善舞、聪明过人的“姑娘头”，便自然而然地成为青年男女谈情说爱、“行歌坐月”的理想场所，侗胞称其为“月堂”。")
            elif self.pred == "布依族":
                self.result_pan.IntroduceText.setPlainText(
                    "    布依族民居多为干栏式楼房或半边楼（前半部正面看是楼，后半部背面看是平方）式的石板房。贵州的镇宁、安顺等布依族地区盛产优质石料，当地布依族因地制宜，就地取材，用石料修造出一幢幢颇具民族特色的石板房。石板房以石条或石块砌墙，墙可垒至5至6米高；以石板盖顶，风雨不透。总之，除檩条、椽子是木料外，其余全是石料，甚至家用的桌、凳、灶、钵都是石头凿的。一切都朴实无华，固若金汤。这种房屋冬暖夏凉，防潮放火，只是采光较差。")
            elif self.pred == "黎族":
                self.result_pan.IntroduceText.setPlainText(
                    "    黎族主要有船形茅屋和金字形茅屋两种样式。船形屋是黎族最传统也是最具代表性的住宅。它以木条、竹子、红白藤和茅草为建筑材料，房屋的骨架用竹木构成，十分原始和简单，属于传统竹木结构建筑。船形屋有高脚船形屋与低脚船形屋之分，外形像倒扣的船篷，屋架用红、白藤扎紧，上盖茅草或葵叶。金字形茅屋是黎族人民在与周边民族交往时吸收过来的住宅类型，20世纪50年代后普遍出现于黎族社会。它以树干作为支架，竹木编墙，用稻草与泥混合后抹成泥墙。")
            self.show_result_pan()
        else:
            mb = QMessageBox(QMessageBox.Information, '提示信息', '请先选择图片！', parent=self)
            mb.open()

    def clear(self):
        self.Img_label.clear()
        file_path = 'F:\keti\Minzu_IR\\venv\Minzu_IR\Application\Resource\ImageData\PredictImage\Predicting\predict.jpg'
        if os.path.exists(file_path) == True:
            os.remove(file_path)
        else:
            mb = QMessageBox(QMessageBox.Information, '提示信息', '请不要重复清空！', parent=self)
            mb.open()

    def return_ui(self):
        self.return_ui_signal.emit()

    def resizeEvent(self, evt):
        x = self.result_area.x()
        y = self.result_area.y()
        width = self.result_area.width()
        height = self.result_area.height()
        self.result_pan.resize(width, height)
        self.result_pan.move(x, y)

    def show_result_pan(self):
        x = self.result_area.x()
        y = self.result_area.y()
        width = self.result_area.width()
        height = self.result_area.height()
        self.result_pan.resize(width, height)
        self.result_pan.move(x, y)
        self.result_pan.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ImageRecognizePan()
    window.show()
    sys.exit(app.exec_())
