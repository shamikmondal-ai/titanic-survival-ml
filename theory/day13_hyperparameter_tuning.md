# Day 13 – Hyperparameter Tuning in Machine Learning

---

## 🎯 What Are Hyperparameters?

- **Hyperparameters** are settings you define **before** training a model.
- They are not learned from the data — you choose them manually or via search.
- Examples:
  - `n_estimators`, `max_depth` in Random Forest
  - `C` (regularization) in Logistic Regression
  - Learning rate in Gradient Boosting or Neural Networks

These directly affect:
- Model performance
- Overfitting / underfitting
- Training time and resource usage

---

## 🛠 Why Tuning Is Important

You can build the right model **and still get poor results** if your hyperparameters are suboptimal.

Proper tuning:
- Boosts model accuracy and F1 score
- Reduces overfitting
- Can make the difference between a “meh” model and a “production-ready” model

---

## 🔍 Grid Search vs Random Search

| Method | How It Works | Pros | Cons |
|--------|---------------|------|------|
| **Grid Search** | Try **every** combination in a predefined grid | Exhaustive, thorough | Slow on large grids |
| **Random Search** | Try **random** combinations from the same grid | Faster, often nearly as good | May miss ideal combo |
| **Bayesian/Optuna** | Uses prior results to choose next params | Efficient, scalable | More complex to set up |

---

## 🧪 Example: Random Forest Parameters to Tune

| Hyperparameter       | Meaning |
|----------------------|---------|
| `n_estimators`       | Number of trees |
| `max_depth`          | Max depth of each tree |
| `min_samples_split`  | Minimum samples to split a node |
| `max_features`       | How many features each tree sees |

---

## 🧠 PM Implications

- Tuning isn't just a “tech detail” — it's the difference between:
  - Launching a model that performs well everywhere
  - Or one that crashes under real-world load

As a PM, ask:
- “Did we tune this model?”
- “Which parameters had the biggest impact?”
- “Are we using the best model *for our use case* or just the fastest to train?”

---

## 🧮 Metric Selection During Tuning

Choose your scoring metric based on business priority:

| Goal | Scoring Metric |
|------|----------------|
| Maximize overall accuracy | `scoring='accuracy'` |
| Balance precision/recall | `scoring='f1'` |
| Avoid false positives | `scoring='precision'` |
| Avoid false negatives | `scoring='recall'` |

---

## ✅ Summary

- **Hyperparameter tuning** improves performance, robustness, and confidence
- **Grid Search** tests all combinations → great for small parameter sets
- **Random Search** is better for large grids or time-limited cases
- PMs must know:
  - Which parameters were tuned
  - Why those were chosen
  - How the tuning impacted model and business metrics

**A model that’s not tuned is like a race car with flat tires.**
