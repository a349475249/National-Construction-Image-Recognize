# coding:utf-8
import os
import torch
import torchvision.transforms as transforms
import torch.nn as nn
import skimage.data
import skimage.io
import skimage.transform
import numpy as np
import torchvision.models as models
import cv2
from PIL import Image
import matplotlib.pyplot as plt


class FeatureExtractor(nn.Module):
    def __init__(self, submodule, extracted_layers):
        super(FeatureExtractor, self).__init__()
        self.submodule = submodule
        self.extracted_layers = extracted_layers

    def forward(self, x):
        outputs = {}
        for name, module in self.submodule._modules.items():
            if "fc" in name:
                x = x.view(x.size(0), -1)

            x = module(x)
            print(name)
            if self.extracted_layers is None or name in self.extracted_layers and 'fc' not in name:
                outputs[name] = x

        return outputs


class FeatureMap():

    def get_picture(self, pic_name, transform):
        img = skimage.io.imread(pic_name)
        img = skimage.transform.resize(img, (256, 256))
        img = np.asarray(img, dtype=np.float32)
        # skimage.io.imshow(img)
        # plt.show()
        return transform(img)

    def make_dirs(self, path):
        if os.path.exists(path) is False:
            os.makedirs(path)

    def get_feature(self):
        self.pic_dir = 'F:\keti\Minzu_IR\\venv\Minzu_IR\Application\Resource\ImageData\FeatureMapImage\selected.jpg'
        transform = transforms.Compose([
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                 std=[0.229, 0.224, 0.225])
        ])
        img = self.get_picture(self.pic_dir, transform)
        # 插入维度
        img = img.unsqueeze(0)

        img = img

        net = models.resnet18(pretrained=True)
        net.fc = nn.Sequential(nn.Dropout(p=0.2),
                               nn.Linear(512, 4))
        net.eval()
        net.load_state_dict(torch.load('F:\keti\Minzu_IR\\venv\Minzu_IR\Application\Resource\\UserData\\result_model.mdl'))
        exact_list = None
        dst = 'F:\keti\Minzu_IR\\venv\Minzu_IR\Application\Resource\ImageData\FeatureMapImage'
        therd_size = 256

        myexactor = FeatureExtractor(net, exact_list)
        outs = myexactor(img)
        for k, v in outs.items():
            features = v[0]
            iter_range = features.shape[0]
            for i in range(iter_range):
                # plt.imshow(x[0].data.numpy()[0,i,:,:],cmap='jet')
                if 'fc' in k:
                    continue

                feature = features.data.numpy()
                feature_img = feature[i, :, :]
                feature_img = np.asarray(feature_img * 255, dtype=np.uint8)

                dst_path = os.path.join(dst, k)

                self.make_dirs(dst_path)
                feature_img = cv2.applyColorMap(feature_img, cv2.COLORMAP_JET)
                if feature_img.shape[0] < therd_size:
                    tmp_file = os.path.join(dst_path, str(i) + '_' + str(therd_size) + '.png')
                    tmp_img = feature_img.copy()
                    tmp_img = cv2.resize(tmp_img, (therd_size, therd_size), interpolation=cv2.INTER_NEAREST)
                    cv2.imwrite(tmp_file, tmp_img)

                # dst_file = os.path.join(dst_path, str(i) + '.png')
                # cv2.imwrite(dst_file, feature_img)

if __name__ == '__main__':
    FeatureMap().get_feature()