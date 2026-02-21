# Ornamental Plant Selection  
## Hybrid CNN–Morphometric Fusion Framework

This repository contains the inference pipeline supporting the study:

"A Hybrid CNN–Morphometric Fusion Framework for Automated Commercial Categorization of Ornamental Plants"

---

## Overview

This system implements a hybrid decision framework that integrates:

- Dual-view CNN processing (front and top plant images)
- Morphometric feature preprocessing
- Structured feature alignment
- Expert-weighted score fusion
- Category-based commercial ranking

The framework combines deep learning predictions with domain-based botanical scoring to support automated ornamental plant categorization.

---

## Model Inputs

The trained model expects:

- Front view RGB image (224 × 224)
- Top view RGB image (224 × 224)
- 92-dimensional aligned morphometric feature vector

---

## Preprocessing Requirements

To ensure reproducibility, the pipeline requires:

- One-hot encoded categorical variables
- Z-score normalized numerical variables
- Exact feature alignment using `model_training_columns.csv`

---

## Output

The system produces:

- Category-level classification
- Weighted ranking scores
- Excel-based export of final commercial categorization

---

## Code Availability

This repository provides the inference and preprocessing pipeline used in the published study.

Pre-trained model weights are not included in this repository due to intellectual property considerations. They may be available upon reasonable request.

---

## License

This project is licensed under the Apache License 2.0.
