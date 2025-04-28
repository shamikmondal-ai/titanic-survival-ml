# Day 6 – First ML Model: Titanic Survival Prediction

---

## 🎯 Goal

Train and evaluate a basic classification model to predict Titanic passenger survival using the cleaned dataset.

---

## 🛠 Model Summary

- **Model Used**: Logistic Regression
- **Dataset**: Titanic cleaned dataset (`titanic_cleaned.csv`)
- **Features**: Age, Fare, Passenger Class, Gender (encoded), Embarkation Port (encoded), etc.
- **Target**: Survived (1 = survived, 0 = did not survive)

---

## 📈 Evaluation Metrics Collected

| Metric     | Meaning                                 |
|------------|-----------------------------------------|
| **Accuracy** | Overall percentage of correct predictions |
| **Precision** | Correct positive predictions over total predicted positives |
| **Recall** | Correct positive predictions over all actual positives |
| **F1 Score** | Harmonic mean of precision and recall (balance metric) |

---

## 📊 Sample Output



Accuracy: 0.8044692737430168
Precision: 0.7746478873239436
Recall: 0.7432432432432432
F1 Score: 0.7586206896551724


---

## 🧠 Observations

- **Accuracy** is decent (~78%), but recall is a bit lower (~66%).
- **Recall** matters more in Titanic because **missing true survivors is worse** than mistakenly predicting survival.
- **F1 Score** gives a balanced view, and here it's ~69%, indicating reasonable but improvable performance.

---

## 🧩 Next Steps (Future Thinking)

- Try other models like Random Forest, XGBoost to improve recall.
- Perform hyperparameter tuning.
- Balance bias vs variance to generalize better on unseen passengers.

---

## ✅ PM-Level Takeaway

In real-world ML products:
- **Accuracy alone can be misleading.**
- **Prioritize metrics** based on **user harm, business goals**, and **risk tolerance**.
- For Titanic (life-or-death), **Recall** is the key metric over just accuracy.

Choosing the right metric = Building the right product behavior.
