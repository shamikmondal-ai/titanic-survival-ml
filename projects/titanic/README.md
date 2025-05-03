# Titanic Survival Prediction – Machine Learning Project

---

## 🎯 Project Overview

This project explores machine learning techniques to predict passenger survival using the Titanic dataset.  
It focuses on model training, feature importance, model evaluation beyond accuracy, and improving generalization.

Key models implemented:
- Logistic Regression
- Random Forest (Full features)
- Random Forest (Pruned features)
- Random Forest with K-Fold Cross-Validation

---

## 🧰 Technologies and Libraries

- Python 3.x
- Pandas, NumPy
- Scikit-learn
- Matplotlib (later stages)

---

## 🛠 Project Structure

```bash
titanic-survival-ml/
├── data/
│   └── titanic_cleaned.csv
├── load_data.py
├── train_model.py                 # Logistic Regression
├── train_random_forest.py        # Random Forest (full features)
├── train_rf_pruned.py            # Random Forest with fewer features
├── cross_validate_rf.py          # Random Forest with 5-Fold CV
├── README.md
├── theory_notes/
│   ├── day6_first_model_evaluation.md
│   ├── day8_decision_trees_random_forests.md
│   └── day10_cross_validation_generalization.md
└── product_thinking/
    ├── fraud_system_architecture.md
    └── lead_scoring_use_case.md



Absolutely — here’s your updated README.md content for the Titanic project after completing Day 10.

This version includes:

K-Fold Cross-Validation

Model performance comparison

Signal pruning

Portfolio polish-level presentation

📁 File Path:
bash
Copy
Edit
ml_product_leader_2025/projects/titanic/README.md
📄 Full Updated README.md Content:
markdown
Copy
Edit
# Titanic Survival Prediction – Machine Learning Project

---

## 🎯 Project Overview

This project explores machine learning techniques to predict passenger survival using the Titanic dataset.  
It focuses on model training, feature importance, model evaluation beyond accuracy, and improving generalization.

Key models implemented:
- Logistic Regression
- Random Forest (Full features)
- Random Forest (Pruned features)
- Random Forest with K-Fold Cross-Validation

---

## 🧰 Technologies and Libraries

- Python 3.x
- Pandas, NumPy
- Scikit-learn
- Matplotlib (later stages)

---

## 🛠 Project Structure

```bash
titanic-survival-ml/
├── data/
│   └── titanic_cleaned.csv
├── load_data.py
├── train_model.py                 # Logistic Regression
├── train_random_forest.py        # Random Forest (full features)
├── train_rf_pruned.py            # Random Forest with fewer features
├── cross_validate_rf.py          # Random Forest with 5-Fold CV
├── README.md
├── theory_notes/
│   ├── day6_first_model_evaluation.md
│   ├── day8_decision_trees_random_forests.md
│   └── day10_cross_validation_generalization.md
└── product_thinking/
    ├── fraud_system_architecture.md
    └── lead_scoring_use_case.md




---

## 📈 Results

| Model                   | Accuracy | Precision | Recall | F1 Score |
|-------------------------|----------|-----------|--------|----------|
| Logistic Regression     | ~78%     | ~73%      | ~66%   | ~69%     |
| Random Forest (Full)    | ~81%     | ~76%      | ~72%   | ~74%     |
| Random Forest (Pruned)  | ~80%     | ~75%      | ~71%   | ~73%     |
| Random Forest (5-Fold CV Avg) | ~79–81% | ~74–77% | ~70–73% | ~72–75% |

*Note: Numbers may vary slightly due to data splits.*

---

## 🧠 Key Learnings

- ML metrics beyond accuracy: **Precision, Recall, F1 Score, AUC**
- Signal pruning and feature selection using **feature importances**
- Model generalization via **K-Fold Cross-Validation**
- Aligning model behavior with product goals (e.g., survival prediction = recall-sensitive)
- Product thinking applied to ML: **fraud detection, lead scoring**

---

## 🧪 Advanced Evaluation Techniques

This project uses **5-Fold Cross-Validation** to validate generalization and avoid overfitting to a single test split.



