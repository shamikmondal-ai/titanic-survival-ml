# Day 11 – Precision-Recall Trade-Off in ML

---

## 🎯 What Is Precision-Recall Trade-Off?

In classification tasks, especially when detecting **rare or high-risk events**, we care deeply about two competing goals:

- **Precision**: Of all the positive predictions the model made, how many were actually correct?
- **Recall**: Of all the actual positives in the dataset, how many did the model catch?

The trade-off is about **choosing where to set the threshold** that decides if a prediction is considered “positive”.

---

## 📐 Definitions

| Metric     | Formula                            | Goal |
|------------|------------------------------------|------|
| **Precision** | TP / (TP + FP)                      | Avoid false alarms |
| **Recall**    | TP / (TP + FN)                      | Don’t miss real cases |
| **F1 Score**  | 2 × (Precision × Recall) / (P + R) | Balance both |

---

## 🔄 How the Trade-Off Works

- Lowering the threshold = **more recall, less precision**
  - You catch more real cases (good), but you get more false alarms (bad).
- Raising the threshold = **more precision, less recall**
  - You avoid false alarms, but you miss more true cases.

---

## 🧠 Real-World Examples

| Use Case                  | Priority       | Why |
|---------------------------|----------------|-----|
| Cancer detection          | **Recall**     | Missing a case is life-threatening |
| Spam filter               | **Precision**  | False spam hurts UX and trust |
| Fraud detection           | Recall → Precision | First catch all fraud, then reduce false positives |
| ML alerts for ops/infra   | **Precision**  | Too many false alerts = alert fatigue |
| Customer churn prediction | **Recall**     | Catch at-risk users early to intervene |
| Resume screening (recruiting) | **Precision** | Avoid sending junk profiles to hiring teams |

---

## 📈 PM Implications

- This is **not just a modeling decision** — it impacts **user trust, cost, and actionability**
- As a PM, you must ask:
  - “What’s the business cost of a false positive vs false negative?”
  - “Do we want to be conservative or aggressive with triggering this feature?”
- You should **guide threshold tuning**, not delegate it blindly

---

## 🧪 Precision-Recall Curve

- A Precision-Recall (PR) curve shows the trade-off at all threshold levels.
- Ideal models have **high area under PR curve (AUC-PR)**.
- Helps justify your decision to **alert**, **block**, or **escalate**.

---

## 🛠 Threshold Tuning

In production, the model may output a **probability score** (e.g., 0.87)  
You set a threshold (e.g., 0.75) to convert it into an actual **yes/no prediction**

Choose threshold based on:
- Business priority (cost of errors)
- Regulatory requirements
- Feedback from ops/users
- Model monitoring metrics

---

## ✅ Summary

- Precision and recall **pull in opposite directions**
- Every ML product has to pick the **right balance based on use case**
- PMs must:
  - Define **what matters most**
  - Guide **threshold decisions**
  - Design the **UX around false positives and negatives**

**Trade-offs are not technical problems — they are product decisions.**
