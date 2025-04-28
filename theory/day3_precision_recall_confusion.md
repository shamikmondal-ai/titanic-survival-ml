# Day 3 – Confusion Matrix, Precision, and Recall

---

## 📊 What Is a Confusion Matrix?

A confusion matrix is a summary table used to evaluate the performance of a classification model.

|                  | Predicted Positive | Predicted Negative |
|------------------|--------------------|--------------------|
| **Actual Positive** | True Positive (TP)  | False Negative (FN) |
| **Actual Negative** | False Positive (FP) | True Negative (TN)  |

---

## 📐 Key Metrics

### 🎯 Accuracy
Accuracy = (TP + TN) / Total  
Measures overall correctness.

---

### 🔍 Precision
Precision = TP / (TP + FP)  
Among predicted positives, how many were correct?  
High precision = few false positives.

---

### 🧲 Recall (Sensitivity)
Recall = TP / (TP + FN)  
Among actual positives, how many did the model catch?  
High recall = few false negatives.

---

## ⚖️ Precision vs Recall Trade-off

| Metric | Focus | Real-World Priority |
|--------|-------|---------------------|
| **Precision** | Avoiding false alarms | Spam filters, recommender quality |
| **Recall** | Catching all positives | Fraud detection, cancer diagnosis |

You often can't maximize both — improving one can reduce the other.

---

## 🧠 PM Implications

- Always ask: “**What matters more — missing a case, or triggering false ones?**”
- Prioritize **precision** when false alarms damage UX or trust.
- Prioritize **recall** when missing a case is costly or dangerous.
- Accuracy can be misleading in imbalanced datasets.

---

## 🚨 Example: Fraud Detection

You build a fraud detection model for 10,000 transactions:
- 100 are truly fraudulent

Model flags 80 transactions:
- 60 are actual fraud (TP)
- 20 are false alarms (FP)
- 40 frauds were missed (FN)

### Metrics:
- **Precision** = 60 / (60 + 20) = 0.75
- **Recall** = 60 / (60 + 40) = 0.60
- **Accuracy** = (60 + 9,880) / 10,000 = 99.4% → misleading

✅ As a PM, you'd focus on **recall** — better to catch more fraud, even with some false alarms.

---

## ✅ Summary

- **Confusion matrix** explains how your model is really behaving
- **Precision** = quality of positive predictions
- **Recall** = ability to capture true positives
- **Accuracy** ≠ reliability, especially in imbalanced data
- PMs must align model metrics with **user risk**, **business cost**, and **experience quality**
