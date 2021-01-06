import os
import torch
import torchvision
from torch import nn
from torchvision import transforms
from torchvision.models import resnet18
from torch.utils.data import DataLoader


class Flatten(nn.Module):

    def __init__(self):
        super(Flatten, self).__init__()

    def forward(self, x):
        shape = torch.prod(torch.tensor(x.shape[1:])).item()
        return x.view(-1, shape)


class Recognize():
    def __init__(self):
        self.pic_data=self.load_pic()


    def load_pic(self):
        batch_size = 1
        size_w = 324
        size_h = 216
        tf = transforms.Compose([
            transforms.Resize((size_h, size_w)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                 std=[0.229, 0.224, 0.225])
        ])
        
        db = torchvision.datasets.ImageFolder(root='F:\keti\Minzu_IR\\venv\Minzu_IR\Application\Resource\ImageData\PredictImage', transform=tf)
        self.loader = DataLoader(db, batch_size=batch_size, shuffle=False, num_workers=0)
        print('图片数量: ', len(db))
        return self.loader

    def calculate(self,model, pic_data):
        model.eval()
        for x, y in pic_data:
            with torch.no_grad():
                logits = model(x)
                # print(logits)
                print('识别中')
                pred = logits.argmax(dim=1)
                if pred == 0:
                    output='布依族'
                elif pred == 1:
                    output='侗族'
                elif pred == 2:
                    output='黎族'
                elif pred == 3:
                    output='苗族'
                print(output)
        return output

    def predict(self):
        model = torchvision.models.resnet18(pretrained=True)
        model.fc = nn.Sequential(nn.Dropout(p=0.2),
                                 nn.Linear(512, 4))
        model.load_state_dict(torch.load('F:\keti\Minzu_IR\\venv\Minzu_IR\Application\Resource\\UserData\\result_model.mdl'))
        print('成功加载模型')
        result=self.calculate(model, self.pic_data)
        return result


if __name__ == '__main__':
    Recognize().predict()












