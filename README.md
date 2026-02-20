# ornamental-plant-selection
Hybrid CNN–Morphometric Fusion Framework for Ornamental Plant Selection
# Hybrid CNN–Morphometric Fusion Framework for Ornamental Plant Selection

This repository contains the inference pipeline supporting the study:

"A Hybrid CNN–Morphometric Fusion Framework for Automated Commercial Categorization of Ornamental Plants"

## Overview

The system integrates:

- Dual-view CNN processing (front & top images)
- Morphometric feature preprocessing
- Feature alignment to trained model structure (92 features)
- Expert-weighted score fusion
- Category-based commercial ranking

## Model Inputs

1. Front view RGB image (224×224)
2. Top view RGB image (224×224)
3. 92-dimensional aligned morphometric feature vector

## Reproducibility

The model expects:

- One-hot encoded categorical variables
- Z-score normalized numerical variables
- Exact feature alignment using model_columns.csv

## Code Availability

This repository provides the inference and preprocessing pipeline used in the published study.
Model weights are available upon request.
