# Day 7 – Customer Retention Prediction Use Case (Subscription Business)

---

## 🎯 Problem Statement

In a subscription-based platform (e.g., Netflix, Spotify, Duolingo), losing paying customers (churn) reduces lifetime value (LTV) and increases the cost of customer acquisition.

The goal is to build an ML model that predicts **which users are likely to cancel their subscription within the next 30 days**, enabling the business to proactively intervene with offers, nudges, or content personalization to retain them.

---

## 📊 Available Data Signals

- Login frequency (logins per week)
- Average session duration
- Content engagement (shows watched, songs played, lessons completed)
- Payment history and renewal attempts
- Days since last activity
- Customer support tickets opened
- Device or platform type (mobile vs desktop)
- Account age (tenure)
- Historical discounts or promotions used

---

## ⚙️ ML-Based Approach

### Model Type:
- **Binary classifier** → "Likely to Churn" vs "Likely to Stay"

### Feature Ideas:
- Recent session drop-off rate
- Engagement ratio (last 30 days vs lifetime average)
- Payment delays or declines
- Customer service complaint severity

---

## 📈 Metrics and Evaluation Strategy

| Metric | Why It Matters |
|--------|----------------|
| **Recall (Primary)** | Must catch as many real churners as possible to maximize retention actionability |
| **Precision (Secondary)** | Important to minimize unnecessary targeting of loyal users |
| **F1 Score** | Balanced view of how well recall and precision are working together |

PM Guidance:
- Initially optimize for **high recall** → catch most at-risk users
- Gradually improve **precision** through better segmentation and personalized targeting

---

## ⚖️ Product Risks

| Risk | Mitigation |
|------|------------|
| False positives (flagging loyal users) | Soft offers first (non-intrusive nudges), build tiered intervention plans |
| False negatives (missing real churners) | Conservative model thresholds, multi-signal escalation |
| Data drift (new content trends, seasonality) | Retrain models every 3–6 months |
| Privacy compliance (GDPR/CCPA) | Use anonymized behavioral signals, get clear consent for personalized messaging |

---

## 🧭 PM Strategy

- Phase 1: Silent evaluation — model predicts churn risk, no interventions yet
- Phase 2: Pilot interventions for medium/high-risk users (discounts, premium content offers)
- Phase 3: Full-scale retention program, personalized based on user risk tier
- Phase 4: Continuous model monitoring, A/B testing of intervention effectiveness

Success = Lower churn rate, higher LTV, increased customer satisfaction through smarter retention efforts.

---

## ✅ Summary

Predicting customer churn is a **high-ROI ML application** for subscription businesses.

As a PM:
- Prioritize **recall** initially to maximize churn prevention.
- Build user-friendly, trust-preserving intervention strategies.
- Treat the ML model as a **decision support tool** embedded in proactive user engagement programs — not as an isolated score.
