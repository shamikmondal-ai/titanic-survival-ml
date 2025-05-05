# Day 12 – ML-Based Risk Scoring Use Case (Lending / Insurance)

---

## 🎯 Problem Statement

In industries like lending and insurance, incorrect risk assessment leads to significant financial loss.  
- **False positives** → approving high-risk applicants → defaults, claims, fraud  
- **False negatives** → rejecting low-risk applicants → missed revenue, poor UX

We aim to build a machine learning model that assigns a **risk score (0–1)** to each applicant, enabling smarter decision-making:  
**Approve**, **Review Manually**, or **Reject**.

---

## 📊 Available Data Signals

- Credit score or credit bureau data
- Transaction history (bank statements, spending patterns)
- Demographics: age, income, employment type, location
- Historical defaults or claims
- Loan/insurance product type
- Repayment history or claims history
- Application metadata: device type, session behavior, velocity

---

## 🤖 ML-Based Approach

### Model Type:
- **Binary classifier** (Default vs No Default, or High-risk vs Low-risk)
- Output: **Risk probability score (0–1)**

### Model Options:
- Logistic Regression for explainability (regulators)
- Random Forest or XGBoost for performance
- Calibrated models for probability output reliability

### Routing Logic:
| Score Range | Action |
|-------------|--------|
| 0.00–0.50   | Approve |
| 0.51–0.75   | Manual Review |
| 0.76–1.00   | Reject or Escalate |

---

## 📈 Evaluation Metrics

| Metric | Why It Matters |
|--------|----------------|
| **ROC AUC** | Measures ranking power — ability to separate good vs bad risk |
| **Precision (for low-risk approvals)** | Ensure those we approve are truly safe |
| **Recall (for high-risk detection)** | Catch all real defaults or claims |
| **False Positive Rate** | Mistaken approvals — expensive |
| **False Negative Rate** | Missed good customers — opportunity cost |

---

## ⚖️ ROC vs PR Trade-Offs

- Use **ROC AUC** early to compare models (how well they rank overall)
- Use **PR Curve** to fine-tune threshold:  
  - **Precision-focus** = fewer false approvals  
  - **Recall-focus** = fewer missed risks

Choose threshold based on business appetite for risk.

---

## 🛡️ Product Risks and Mitigations

| Risk | Mitigation |
|------|------------|
| Approving bad-risk applicants | Set conservative thresholds, manual override |
| Rejecting good applicants | Soft declines, appeal process, human-in-the-loop |
| Model bias | Audit by region, gender, income band |
| Model drift (e.g., after economic changes) | Retrain on latest data monthly or quarterly |
| Regulatory compliance | Explainable models, audit logs, score breakdowns |

---

## 🧭 PM Strategy

- **Phase 1**: Deploy in shadow mode → compare predictions with actual repayment/claim behavior
- **Phase 2**: Use model scores for routing (review vs auto-approve)
- **Phase 3**: Integrate with pricing, limits, and offer personalization
- Build **explainability dashboard**: show why a score was assigned (top features)

Monitor:
- Default rate by score tier
- Approval volume vs business goals
- Regulatory readiness (model cards, version tracking)

---

## ✅ Summary

Risk scoring is a **core use case** for ML in financial systems.

As a PM:
- Balance **precision, recall, and regulatory safety**
- Choose the right **thresholds and feedback loops**
- Deliver value through **safer decisions**, **faster approvals**, and **revenue protection**

A great risk model doesn’t just reduce fraud —  
it protects trust, ensures fairness, and powers scalable growth.
