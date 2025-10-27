# Bone Fracture Detection

A deep learning project that uses Convolutional Neural Networks (CNN) to detect bone fractures in X-ray images.

## Project Structure
```
bone_fracture_detection/
├── config/
│   └── config.py           # Configuration settings
├── data/
│   ├── __init__.py
│   ├── dataset.py          # Dataset and DataLoader implementations
│   └── transforms.py       # Image transformation pipelines
├── models/
│   ├── __init__.py
│   ├── cnn.py             # CNN model architecture
│   └── utils.py           # Model utility functions
├── utils/
│   ├── __init__.py
│   ├── visualization.py    # Visualization functions
│   └── metrics.py         # Evaluation metrics
├── train/
│   ├── __init__.py
│   ├── trainer.py         # Training loop implementation
│   └── validator.py       # Validation loop implementation
├── main.py                # Entry point
└── requirements.txt       # Project dependencies
```

## Features

- Custom CNN architecture optimized for bone fracture detection
- Comprehensive data augmentation pipeline
- Training and validation loops with progress tracking
- Visualization tools for model performance
- Modular and maintainable code structure

## Requirements

```
torch>=2.0.0
torchvision>=0.15.0
numpy>=1.21.0
tqdm>=4.65.0
matplotlib>=3.5.0
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/bone-fracture-detection.git
cd bone-fracture-detection
```

2. Install dependencies:
```bash
pipenv install
```

## Usage

### Data Preparation

1. Organize your X-ray images in the following structure:
```
data/raw/Bone Fracture Detection/
├── train/
│   ├── fracture/
│   └── normal/
├── val/
│   ├── fracture/
│   └── normal/
└── test/
    ├── fracture/
    └── normal/
```

2. Update the data paths in `config/config.py` if necessary.

### Training

To train the model:

```bash
python main.py
```

The training script will:
- Load and preprocess the dataset
- Train the CNN model
- Validate performance
- Generate visualizations
- Save the trained model

### Configuration

Key parameters can be modified in `config/config.py`:

```python
IMAGE_SIZE = 128        # Input image size
BATCH_SIZE = 16        # Batch size for training
EPOCHS = 30            # Number of training epochs
LEARNING_RATE = 0.001  # Learning rate for optimizer
```

## Model Architecture

The CNN architecture consists of:
- Three convolutional blocks with batch normalization and max pooling
- Multiple fully connected layers with dropout for regularization
- Binary classification output with sigmoid activation

## Performance Metrics

The model tracks:
- Training and validation accuracy
- Training and validation loss
- Additional metrics including precision, recall, and F1-score

## Visualization

The project includes visualization tools for:
- Training history plots
- Model predictions
- Feature maps
- Confusion matrices
