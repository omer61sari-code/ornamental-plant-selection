# Ornamental Plant Selection  
## Hybrid CNN–Morphometric Fusion Framework

This repository contains the inference and preprocessing pipeline supporting the study:

"A Hybrid CNN–Morphometric Fusion Framework for Automated Commercial Categorization of Ornamental Plants"

---

## Abstract

This study proposes a hybrid decision framework that integrates deep convolutional neural networks with structured morphometric features for automated ornamental plant categorization. The system combines image-based representation learning with expert-informed botanical scoring to improve commercial classification reliability.

---

## Methodological Framework

The proposed framework integrates:

- Dual-view CNN processing (front and top RGB images)
- Morphometric feature preprocessing and normalization
- Feature-space alignment to trained model structure
- Expert-weighted score fusion mechanism
- Category-based ranking and selection

This hybrid approach enables structured feature fusion between visual and morphometric domains.

---

## Model Inputs

The trained model requires:

- Front-view RGB image (224 × 224)
- Top-view RGB image (224 × 224)
- 92-dimensional aligned morphometric feature vector

---

## Reproducibility Requirements

To ensure consistent inference results, the pipeline assumes:

- One-hot encoded categorical variables  
- Z-score normalization of numerical variables  
- Exact feature alignment using `model_training_columns.csv`
-Feature names remain in their original language to preserve exact alignment with the trained model structure.  
-Modifying feature names may invalidate model alignment and inference consistency.

---

## Output

The system produces:

- Predicted commercial category  
- Weighted fusion score  
- Excel-based ranked output  

---

## Code Availability

This repository provides the preprocessing and inference pipeline used in the study.

Pre-trained model weights and dataset are not included due to intellectual property considerations. They may be made available upon reasonable academic request.

---

## License

This project is licensed under the Apache License 2.0.
