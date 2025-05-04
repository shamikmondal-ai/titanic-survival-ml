# Day 11 – ML-Powered Alerting System Use Case (Anomaly Detection for Ops/Infra)

---

## 🎯 Problem Statement

Operations teams (DevOps, Cloud Infra, Security, SREs) rely on alerts to catch system anomalies — but traditional rule-based alerts create **too many false positives**.

This leads to:
- Alert fatigue
- Slower incident response
- Burnout and trust erosion

The goal is to build a machine learning–powered alerting system that detects anomalies in metrics (e.g., latency, traffic, error rates) and triggers **fewer, smarter alerts**.

---

## 📊 Available Signals

- CPU and memory usage over time
- Request/response latency
- API call volume per second
- Server error rate (4xx/5xx)
- Auth failure rate
- Deployment metadata (recent code changes)
- Time of day / business hours
- Historical incident patterns

---

## 🤖 ML-Based Approach

### Model Type:
- **Anomaly Detection (Unsupervised)**  
  - Isolation Forest  
  - Autoencoders  
  - Rolling window statistical models  
  - Prophet (for time series deviation)

### Input Features:
- Time-windowed aggregates (e.g., mean latency per 5 minutes)
- Standard deviation, deltas
- Moving average vs. baseline

### Output:
- Anomaly score (0 to 1)
- Optional: anomaly reason (e.g., “latency spike beyond 3σ”)

---

## ⚖️ Precision vs Recall Trade-Off

| Metric | Why It Matters |
|--------|----------------|
| **Precision (High priority)** | Avoid overwhelming users with false alerts |
| **Recall (Secondary)** | Missing occasional anomaly is tolerable, especially for non-critical systems |

PM Decision:  
→ Start with high-precision thresholds  
→ Gradually open up sensitivity for specific services with user feedback

---

## 🛡️ Product Risks and Mitigation

| Risk | Mitigation |
|------|------------|
| Too many alerts (false positives) | Conservative thresholds, post-processing filters, feedback loop |
| Missed anomalies (false negatives) | Human-in-the-loop for shadow alerts, log aggregation fallback |
| Alert fatigue | Grouped alerting, throttling mechanisms |
| Model drift | Retrain regularly, monitor feature distributions |
| Model mistrust | Show anomaly score + rationale + affected system |

---

## 📈 Rollout Strategy

| Phase | Details |
|-------|---------|
| **Phase 1: Shadow Mode** | Model flags anomalies silently; compare to human-labeled incidents |
| **Phase 2: Assistive Mode** | Display anomaly scores + rationale in dashboard |
| **Phase 3: Alerting Mode** | Trigger real-time alerts for high-score anomalies only |
| **Phase 4: Adaptive** | Retrain with feedback; let users tune sensitivity per service/component

---

## 🧭 Dashboard Elements

- Service name + metric affected
- Anomaly score (e.g., 0.89)
- Anomaly context (baseline vs spike)
- “Explain this alert” link (e.g., recent deployment, spike location)
- Feedback buttons: “Helpful / Not helpful”

---

## ✅ Summary

A good ML-powered alerting system doesn’t just detect spikes — it builds **trust** with engineers.

As an ML PM:
- Prioritize **precision over recall** — fewer false alarms = more confidence
- Launch gradually with **shadow and explainability**
- Treat alerts as **collaborative recommendations**, not commands

This isn’t just ML infra — it’s **user experience for on-call engineers**, and it must earn their trust to succeed.
