import torch
from tqdm import tqdm
import numpy as np
from config.config import Config

class Trainer:
    def __init__(self, model, train_loader, val_loader, criterion, optimizer, device):
        self.model = model
        self.train_loader = train_loader
        self.val_loader = val_loader
        self.criterion = criterion
        self.optimizer = optimizer
        self.device = device
        
    def train_epoch(self):
        self.model.train()
        batch_acc = []
        batch_loss = []
        
        for X, y in tqdm(self.train_loader, desc='Training'):
            X, y = X.to(self.device), y.to(self.device, dtype=torch.float)
            
            self.optimizer.zero_grad()
            yHat = self.model(X).squeeze()
            loss = self.criterion(yHat, y)
            
            loss.backward()
            self.optimizer.step()
            
            # Calculate accuracy
            yHat = yHat.cpu()
            y = y.cpu()
            batch_acc.append(torch.mean(((yHat > 0.0) == y).float()) * 100)
            batch_loss.append(loss.item())
            
        return np.mean(batch_acc), np.mean(batch_loss)
    
    def validate(self):
        self.model.eval()
        batch_acc = []
        batch_loss = []
        
        with torch.no_grad():
            for X, y in self.val_loader:
                X, y = X.to(self.device), y.to(self.device, dtype=torch.float)
                yHat = self.model(X).squeeze()
                loss = self.criterion(yHat, y)
                
                yHat = yHat.cpu()
                y = y.cpu()
                batch_acc.append(torch.mean(((yHat > 0.0) == y).float()) * 100)
                batch_loss.append(loss.item())
        
        return np.mean(batch_acc), np.mean(batch_loss)