#定义网络结构
import torch
import torch.nn as nn
from torchsummary import summary
from torchvision import models

net = nn.Sequential(
            nn.Conv2d(in_channels=3, out_channels=64, kernel_size=[3, 3], stride=1, padding=1),
            nn.ReLU(True),
            nn.BatchNorm2d(64),
            nn.Dropout(p=0.3),
            nn.Conv2d(in_channels=64, out_channels=64, kernel_size=[3, 3], stride=1, padding=1),
            nn.ReLU(True),
            nn.BatchNorm2d(64),
            nn.MaxPool2d(kernel_size=2),

            nn.Conv2d(in_channels=64, out_channels=128, kernel_size=[3, 3], stride=1, padding=1),
            nn.ReLU(True),
            nn.BatchNorm2d(128),
            nn.Dropout(p=0.4),
            nn.Conv2d(in_channels=128, out_channels=128, kernel_size=[3, 3], stride=1, padding=1),
            nn.ReLU(True),
            nn.BatchNorm2d(128),
            nn.MaxPool2d(kernel_size=2),

            nn.Conv2d(in_channels=128, out_channels=256, kernel_size=[3, 3], stride=1, padding=1),
            nn.ReLU(True),
            nn.BatchNorm2d(256),
            nn.Dropout(p=0.4),
            nn.Conv2d(in_channels=256, out_channels=256, kernel_size=[3, 3], stride=1, padding=1),
            nn.ReLU(True),
            nn.BatchNorm2d(256),
            nn.Dropout(p=0.4),
            nn.Conv2d(in_channels=256, out_channels=256, kernel_size=[3, 3], stride=1, padding=1),
            nn.ReLU(True),
            nn.BatchNorm2d(256),
            nn.MaxPool2d(kernel_size=2)
        )

#输出每层网络参数信息
summary(net, (3, 224, 224), batch_size=1, device="cpu")
