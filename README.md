# Lung Cancer Tumor Segmentation

![](Screenshots/prediction.png)

## Objective

This project aims to improve lung cancer diagnosis and treatment by automating tumor segmentation using advanced machine learning algorithms for accurate and efficient detection.

## Overview

Lung cancer, also called Bronchial Carcinoma, is a leading cause of cancer-related deaths globally, responsible for about 25% of all such deaths. Automating tumor segmentation offers two key benefits: reducing diagnostic errors by highlighting missed tumors and providing detailed tumor size and volume data, which helps in cancer staging and planning personalized treatments.

## Dataset

The project utilizes the Medical Segmentation Decathlon dataset, comprising 64 full-body CT scans with ground truth masks. The task is to generate 2D segmentation masks for each CT scan slice to identify tumor regions.

## Preprocessing

Using the nibabel library, CT scans and their corresponding labels are loaded, with slices cropped from slice 30 onward. The data is normalized to values between 0 and 1, and the preprocessed data is saved in the `../Preprocessed/` folder.

## Data Handling and Augmentation

The `dataset.py` file handles loading and augmentation. The `LungDataset` class retrieves images and labels, applying transformations such as affine and elastic distortions using the `imgaug` library. This helps increase the diversity of the training data.

## Model Architecture

The model is based on the U-Net architecture, designed for semantic segmentation tasks. It consists of four `DoubleConvBlock` layers for encoding and three `DoubleConvBlock` layers for decoding, connected via skip-connections to enhance multi-scale feature learning.

![](Screenshots/U-Net.png)

## Training

Training is carried out in the `training.ipynb` notebook using the PyTorch Lightning framework. The model is trained for 30 epochs, with early stopping based on validation loss. To handle class imbalance, a `Weighted Random Sampler` is used, and the model is optimized using Adam with a learning rate of 1e-4.

![](Screenshots/Train_loss.png)

## Evaluation

The model was evaluated using the Dice Score on the validation set, which returned a low score of 0.0247. This indicates challenges in accurately segmenting lung cancer regions, with a high rate of false negatives and positives. Additional optimization and validation with independent datasets are necessary before clinical use.

## Results and Visualization

Sample CT scan slices, along with ground truth masks and predicted segmentation, are visualized to assess the model’s performance in identifying tumor regions.

![](Screenshots/actual_vs_pred.png)

## Conclusion

The project demonstrates the use of deep learning, specifically the U-Net architecture, for lung cancer tumor segmentation. Despite the initial low Dice Score, the results emphasize the need for further refinement, larger datasets, and collaboration with medical professionals to improve diagnostic accuracy. Continued research is essential to enhance the model’s performance and ensure its clinical viability in lung cancer treatment.
