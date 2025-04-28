# Day 4 – ROC-AUC and Class Imbalance in ML Evaluation

---

## 🎯 What Is ROC-AUC?

- **ROC** = Receiver Operating Characteristic
- **AUC** = Area Under the Curve
- It’s a performance metric for classification models that shows the **model’s ability to distinguish between classes** across all classification thresholds.

---

## 📈 ROC Curve – Axes Explained

- **X-axis:** False Positive Rate (FPR) = FP / (FP + TN)
- **Y-axis:** True Positive Rate (TPR) = Recall = TP / (TP + FN)

Each point on the ROC curve represents a **different threshold** applied to the model's prediction probability.

---

## 📐 Interpreting AUC Scores

| AUC Score | Meaning |
|-----------|---------|
| **0.5**   | Random guessing |
| **0.6–0.7** | Poor model |
| **0.7–0.8** | Fair model |
| **0.8–0.9** | Good model |
| **0.9–1.0** | Excellent to perfect |

---

## 🧪 Real-World Example

Imagine you're predicting **fraud**, which occurs in just 0.5% of transactions.

- Accuracy may be **99.5%**, simply because the model always predicts “no fraud”
- But **ROC-AUC = 0.72** shows the model does somewhat discriminate between fraudulent and legit transactions
- Better than guessing, but not yet production-grade

---

## ⚖️ Why ROC-AUC > Accuracy (in many cases)

| Metric | Weakness |
|--------|----------|
| **Accuracy** | Misleading in imbalanced datasets |
| **Precision/Recall** | Sensitive to a single threshold |
| **ROC-AUC** | Looks at **model performance across all thresholds** — more reliable view |

---

## 🧠 PM Implications

- Don’t rely on accuracy alone, especially in **imbalanced use cases** like:
  - Fraud detection
  - Churn prediction
  - Disease classification
- ROC-AUC helps you understand:
  - “Is the model good at separating positives from negatives?”
  - “Does it rank riskier cases higher than safe ones?”

As a PM, choose:
- **ROC-AUC** for **overall model quality**
- **Precision/Recall/F1** for **business actionability**
- **Accuracy** only when data is balanced and both errors matter equally

---

## 📊 Class Imbalance – What It Is

In many real-world cases, one class is much rarer than the other:
- **Example:** 0.5% of transactions are fraud → 1:199 ratio
- A model can be 99.5% accurate and still **never detect any fraud**

This is where **recall**, **precision**, and **AUC** matter more than raw accuracy.

---

## ✅ Summary

- **ROC-AUC** evaluates how well a model ranks positives over negatives across thresholds
- It’s especially valuable when working with **imbalanced datasets**
- Accuracy can be deceptive — PMs must choose evaluation metrics that reflect **business goals**, **risk tolerance**, and **real-world class distribution**
