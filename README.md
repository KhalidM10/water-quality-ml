# Water Potability Prediction using Machine Learning

## Project Overview
This project aims to predict water potability using machine learning models based on physicochemical water quality indicators.

The goal is to determine whether water is safe for human consumption using measurable chemical properties.

## Dataset
The dataset contains 3276 samples with the following features:

- pH
- Hardness
- Solids
- Chloramines
- Sulfate
- Conductivity
- Organic Carbon
- Trihalomethanes
- Turbidity

Target variable:
- Potability (0 = Not Safe, 1 = Safe)

## Data Preprocessing
- Missing values were handled using median imputation.
- Dataset was split into training (80%) and testing (20%) sets.
- Feature scaling was applied for linear models.

## Models Implemented
- Logistic Regression
- Random Forest Classifier
- Gradient Boosting Classifier

## Results

| Model | Accuracy |
|-------|----------|
| Logistic Regression | 62.8% |
| Random Forest | 67.4% |
| Gradient Boosting | 66.9% |

Random Forest achieved the best performance.

## Key Insights
Feature importance analysis revealed that Sulfate, pH, and Hardness were the most influential predictors of water potability. However, similar importance scores across all features suggest that water safety is determined by complex interactions between multiple chemical indicators.

## Future Improvements
- Hyperparameter tuning
- Cross-validation
- Handling class imbalance using SMOTE
- Deployment as a web application