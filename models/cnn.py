import torch
import torch.nn as nn
import torch.nn.functional as F
from config.config import Config

class BoneFractureCNN(nn.Module):
    def __init__(self, k=Config.CONV_KERNEL_SIZE, s=Config.CONV_STRIDE, p=Config.CONV_PADDING):
        super().__init__()
        
        self.feature_extractor = nn.Sequential(
            nn.Conv2d(3, 128, k, s, p),
            nn.BatchNorm2d(128),
            nn.MaxPool2d(k),
            nn.LeakyReLU(),
            
            nn.Conv2d(128, 256, k, s, p),
            nn.BatchNorm2d(256),
            nn.MaxPool2d(k),
            nn.LeakyReLU(),
            
            nn.Conv2d(256, 256, k, s, p),
            nn.BatchNorm2d(256),
            nn.MaxPool2d(k),
            nn.LeakyReLU(),
        )
        
        # Calculate feature dimensions
        img_size = self._calculate_feature_size(Config.IMAGE_SIZE, k, s, p)
        
        self.classifier = nn.Sequential(
            nn.Linear(img_size * img_size * 256, 256),
            nn.LeakyReLU(),
            nn.Dropout(0.5),
            
            nn.Linear(256, 256),
            nn.LeakyReLU(),
            nn.Dropout(0.5),
            
            nn.Linear(256, 256),
            nn.LeakyReLU(),
            nn.Dropout(0.5),
            
            nn.Linear(256, 256),
            nn.LeakyReLU(),
            nn.Dropout(0.5),
            
            nn.Linear(256, 1)
        )
    
    def _calculate_feature_size(self, size, k, s, p):
        """Calculate the output feature map size"""
        for _ in range(3):  # 3 conv layers
            size = ((size - k + 2*p) // s) + 1
            size = size // k  # maxpool
        return size
    
    def forward(self, x):
        x = self.feature_extractor(x)
        x = x.view(x.size(0), -1)
        return self.classifier(x)