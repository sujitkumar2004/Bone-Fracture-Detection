import torch
import torch.nn as nn
from torch.utils.data import DataLoader
import torchvision.datasets as datasets

from config.config import Config
from data.transforms import get_train_transform, get_eval_transform
from models.cnn import BoneFractureCNN
from train.trainer import Trainer
from utils.visualization import plot_training_history, visualize_predictions
from utils.metrics import calculate_metrics

def main():
    # Set device
    Config.DEVICE = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
    
    # Load datasets
    train_dataset = datasets.ImageFolder(
        root=Config.TRAIN_DIR,
        transform=get_train_transform()
    )
    
    test_dataset = datasets.ImageFolder(
        root=Config.TEST_DIR,
        transform=get_eval_transform()
    )
    
    # Create dataloaders
    train_loader = DataLoader(
        train_dataset,
        batch_size=Config.BATCH_SIZE,
        shuffle=True
    )
    
    test_loader = DataLoader(
        test_dataset,
        batch_size=Config.BATCH_SIZE
    )
    
    # Initialize model, loss, and optimizer
    model = BoneFractureCNN().to(Config.DEVICE)
    criterion = nn.BCEWithLogitsLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=Config.LEARNING_RATE)
    
    # Initialize trainer
    trainer = Trainer(
        model=model,
        train_loader=train_loader,
        val_loader=test_loader,
        criterion=criterion,
        optimizer=optimizer,
        device=Config.DEVICE
    )
    
    # Training loop
    history = {
        'train_acc': [], 'train_loss': [],
        'val_acc': [], 'val_loss': []
    }
    
    for epoch in range(Config.EPOCHS):
        train_acc, train_loss = trainer.train_epoch()
        val_acc, val_loss = trainer.validate()
        
        history['train_acc'].append(train_acc)
        history['train_loss'].append(train_loss)
        history['val_acc'].append(val_acc)
        history['val_loss'].append(val_loss)
        
        print(f'Epoch {epoch+1}/{Config.EPOCHS}:')
        print(f'Train Acc: {train_acc:.2f}%, Loss: {train_loss:.4f}')
        print(f'Val Acc: {val_acc:.2f}%, Loss: {val_loss:.4f}')
    
    # Plot training history
    plot_training_history(history)
    
    # Calculate and display metrics
    calculate_metrics(model, test_loader, Config.DEVICE)
    
    # Visualize predictions
    visualize_predictions(model, test_loader, test_dataset.classes, Config.DEVICE)

if __name__ == '__main__':
    main()