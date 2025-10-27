from pathlib import Path

class Config:
    # Data paths
    INPUT_DIR = Path('data/raw/Bone Fracture Detection')
    OUTPUT_DIR = Path('data/processed')
    TRAIN_DIR = OUTPUT_DIR / 'train'
    VAL_DIR = OUTPUT_DIR / 'val'
    TEST_DIR = OUTPUT_DIR / 'test'

    # Model parameters
    IMAGE_SIZE = 128
    BATCH_SIZE = 16
    EPOCHS = 30
    LEARNING_RATE = 0.001
    
    # CNN architecture
    CONV_KERNEL_SIZE = 3
    CONV_STRIDE = 1
    CONV_PADDING = 2
    
    # Training parameters
    DEVICE = 'cuda:0'  # Will be updated in main.py based on availability
    
    # Visualization
    VISUALIZATION_SAMPLES = 33
    COLOR_PALETTE = ['#faa5c7', '#eb679c', '#cc3d76', '#b3245d', '#d40457', '#8f1042', '#6e042e']