# Day 4 – Fraud Detection Use Case (Fintech ML Product)

---

## 🎯 Problem Statement

Fraudulent credit card transactions result in significant financial losses and impact customer trust. The business needs a system to identify and flag **suspicious transactions in real time**, ideally before money is transferred.

The key challenge is **maximizing fraud catch rate (recall)** while minimizing false alarms (precision), which could block legitimate users and create friction.

---

## 📊 Available Signals

- Transaction amount
- Transaction timestamp and frequency
- Merchant history and category
- Device fingerprint
- IP address and geolocation
- Cardholder behavior profile (usual transaction patterns)
- Past fraud history associated with card or merchant
- Velocity features (e.g., 3 transactions in 60 seconds)

---

## ⚙️ Non-ML Baseline

- Rule-based fraud scoring:
  - Block all transactions above ₹50,000 after midnight
  - Flag transactions from new devices over 3G networks
  - Disable cards if 5+ transactions happen in <2 minutes

✅ Fast and interpretable  
❌ Not adaptive, high false positives, doesn't scale with complexity

---

## 🤖 ML-Based Approach

### Model Type:
- **Binary classifier** (Fraud = 1, Legit = 0)

### Model Candidates:
- Logistic regression (baseline)
- Random Forest / XGBoost (high performance, interpretable)
- Anomaly detection for rare pattern recognition
- Time-aware models for fraud velocity

### Features:
- Manual rules → engineered features (amount z-score, geo variance)
- Session-level behavioral embeddings
- Real-time scoring with latency constraint (~100ms)

---

## 📈 Key Product Metrics

| Metric | Why It Matters |
|--------|----------------|
| **Recall (sensitivity)** | Ensure most actual fraud is flagged |
| **Precision** | Avoid blocking legitimate transactions |
| **ROC-AUC** | Overall model performance |
| **False positive rate (FPR)** | Key to keeping UX friction low |
| **Average fraud amount avoided** | Business impact in ₹₹₹ |
| **User complaints related to blocked payments** | Proxy for model quality |

---

## ⚖️ Precision vs Recall Trade-Off

| Metric Focus | Justification |
|--------------|---------------|
| **Recall**   | Better to flag a fraud than miss it. Missing costs real money. |
| **Precision**| Blocking genuine users leads to churn, complaints, regulatory issues. |

> **PM balancing act:**  
> “Don’t miss the bad guys. Don’t punish the good ones.”

---

## 🛡️ Product Risks & Mitigations

| Risk | Mitigation |
|------|------------|
| High false positives (bad UX) | Post-prediction validation rules, model tuning |
| Missed fraud | Increase recall, real-time review queue fallback |
| Model degradation (data drift) | Monitor fraud type evolution, retrain monthly |
| Latency too high for real-time scoring | Lightweight model with precomputed features |
| Bias (flagging users in certain geographies) | Fairness audits, manual review sampling |

---

## 🧭 PM Strategy

- Start with a hybrid model + rule-based fallback
- A/B test on shadow mode: model runs silently, flags reviewed manually
- Gradually move to real-time enforcement
- Build confidence with precision–recall dashboards + fraud cost saved tracker
- Integrate alerts for model confidence below threshold

---

## ✅ Summary

Fraud detection is a classic high-stakes ML use case where **recall saves money** and **precision preserves trust**.

The PM’s job is to:
- Frame the problem with clear business impact
- Balance risk and user experience
- Own both the **model decisioning layer** and **post-prediction product flow**
