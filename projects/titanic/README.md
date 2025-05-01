# Titanic Survival Prediction – Machine Learning Project

---

## 🎯 Project Overview

This project applies machine learning techniques to predict passenger survival on the Titanic dataset.

We use basic data preprocessing, feature engineering, and two classification models:
- Logistic Regression
- Random Forest Classifier

The goal is to explore model evaluation metrics beyond accuracy and understand the trade-offs between precision, recall, and F1 score.

---

## 🧰 Technologies and Libraries

- Python 3.x
- Pandas
- NumPy
- Scikit-learn
- Matplotlib (for visualization later)

---

## 🛠 Project Structure

## 🛠 Project Structure

```bash
titanic-survival-ml/
├── data/
│   └── titanic_cleaned.csv
├── load_data.py
├── train_model.py          # Logistic Regression model
├── train_random_forest.py  # Random Forest model
├── train_rf_pruned.py      # Random Forest with pruned features
├── README.md
├── theory_notes/
│   ├── day6_first_model_evaluation.md
│   └── day8_decision_trees_random_forests.md
└── product_thinking/
    └── fraud_system_architecture.md

---

## 🧠 Key Learnings

- **Model Evaluation**: Using Accuracy, Precision, Recall, and F1 Score to assess models properly
- **Bias-Variance Tradeoff**: Handling underfitting and overfitting
- **Feature Engineering**: Handling missing values, encoding categorical variables
- **Explainability**: Analyzing feature importances in Random Forest
- **Production Thinking**: Architecting ML systems for real-world applications
- **Performed **feature importance analysis** and retrained model with a reduced set of features for improved generalization

---

## 📈 Results

| Model                  | Accuracy | Precision | Recall | F1 Score |
|------------------------|----------|-----------|--------|----------|
| Logistic Regression     | ~78%     | ~73%      | ~66%   | ~69%     |
| Random Forest (Full)    | ~81%     | ~76%      | ~72%   | ~74%     |
| Random Forest (Pruned)  | ~80%     | ~75%      | ~71%   | ~73%     |


##Note: The pruned model uses fewer features and offers nearly the same performance with improved simplicity and lower risk of overfitting.*

---


## 👤 About Me

Machine Learning Product Leader building a public portfolio step-by-step. Working with Bain.  
Focused on combining **technical fluency**, **system design**, and **product leadership** to drive real-world ML impact.

---
