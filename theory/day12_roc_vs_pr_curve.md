# Day 12 – ROC vs PR Curve: When to Use Which and Why

---

## 🎯 What Are ROC and PR Curves?

Both are tools to evaluate **binary classification models**, especially in **threshold-sensitive** and **high-stakes** applications.

---

### 🔹 ROC Curve (Receiver Operating Characteristic)

- Plots **True Positive Rate (Recall)** vs **False Positive Rate**
- Shows how well the model **separates classes**
- Used when:
  - Classes are **balanced**
  - You care about **overall ranking performance**
  - You're comparing models, not tuning thresholds yet

**AUC-ROC**: Area under this curve  
→ 1.0 = perfect, 0.5 = random

---

### 🔸 PR Curve (Precision-Recall)

- Plots **Precision** vs **Recall** at different thresholds
- Focuses on **positive class** (usually rare or high-risk events)
- Used when:
  - Dataset is **imbalanced**
  - You care more about **positive predictions being right**
  - You want to **tune for action thresholds**

**AUC-PR**: Area under the PR curve  
→ More informative than ROC when positive class is rare

---

## 🧠 Key Differences

| Feature              | ROC Curve                         | PR Curve                        |
|----------------------|-----------------------------------|---------------------------------|
| X-axis               | False Positive Rate               | Recall                          |
| Y-axis               | True Positive Rate (Recall)       | Precision                       |
| Class Imbalance      | Hides issues with imbalance       | Highlights issues with imbalance |
| Business Focus       | Ranking models broadly            | Optimizing for decision-making  |
| Visual Interpretation| Stable across all classes         | Focused on quality of positive class predictions |

---

## 🧪 Example: Titanic Survival Prediction

- Classes are relatively balanced (around 60% did not survive, 40% survived)
- ROC Curve gives a general sense of **model power**
- PR Curve helps decide **threshold** to **trigger alerts or actions**

---

## 🧠 PM Implications

| Situation | Curve to Use |
|-----------|--------------|
| Detecting rare diseases | **PR Curve** — Precision and Recall matter more |
| Flagging spam content | **PR Curve** — Class imbalance is high |
| General model benchmarking | **ROC Curve** |
| Explaining decision thresholds to stakeholders | **PR Curve** |
| Fraud, moderation, churn, default | Start with ROC, then optimize with **PR Curve** |

As a PM:
- Ask for both curves in model evaluations
- Use **PR for tuning**, **ROC for comparison**
- Don’t rely on a single number (AUC); always understand the **trade-offs**

---

## 📊 Visual Examples (You May Have Plotted)

| Curve | What It Tells You |
|-------|--------------------|
| **ROC Curve** is high and smooth | Model ranks well — good separation of classes |
| **PR Curve** drops quickly | Model may only perform well for top predictions; tune threshold carefully |
| **ROC AUC is high, but PR AUC is low** | Model is misleading on rare classes — don’t trust the ROC blindly |

---

## ✅ Summary

- **ROC Curves** are best for comparing models
- **PR Curves** are best for evaluating **real-world decisions**
- AUC is useful, but **interpretation is more important**
- As a PM, use curves to:
  - Understand model risk
  - Choose thresholds
  - Communicate decisions clearly to stakeholders

**Better evaluation = better decisions = better products.**
