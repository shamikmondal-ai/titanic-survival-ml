# Day 9 – Customer Support Triage ML Use Case

---

## 🎯 Problem Statement

In high-volume support environments (e.g., SaaS platforms like Freshdesk, Zendesk, or Salesforce), not all tickets are created equal.

Critical issues (e.g., “Payment failed” or “System down”) must be prioritized over general inquiries (“How do I reset my password?”).

Today, tickets are often handled **in the order they arrive**, creating delays and breaching SLAs for enterprise customers.

We aim to build an ML-based triage system that **automatically classifies support tickets by priority** so that high-impact issues are surfaced first.

---

## 📊 Available Signals

- Ticket text (title + body)
- Sentiment of the message
- Customer tier (free vs paid vs enterprise)
- Response time expectation (SLA rules)
- Channel (email, chat, phone)
- Historical ticket volume from same account
- Previous escalation history
- Product/module mentioned (if parsed)

---

## ⚙️ ML-Based Approach

### Model Type:
- **Multiclass classifier** (Low, Medium, High Priority)

### Feature Engineering Ideas:
- NLP embeddings of ticket text
- Sentiment scores
- One-hot encoding for customer tier
- Urgency keywords ("urgent", "asap", "not working")
- Time-based features (e.g., time of day sent)

---

## 📈 Metrics and Evaluation Strategy

| Metric | Why It Matters |
|--------|----------------|
| **Recall (High-priority class)** | Catching all truly urgent issues is critical |
| **Precision (High-priority class)** | Avoid alerting engineers on low-priority tickets |
| **Accuracy** | Helpful but not sufficient — class imbalance likely (few “High” tickets) |
| **Confusion Matrix** | Check how often tickets are misclassified as lower urgency |

PM Tip: Treat **high-priority recall** as your north star initially.  
Better to over-escalate than under-prioritize.

---

## 🛡️ Product Risks and Mitigation

| Risk | Mitigation |
|------|------------|
| False negatives (missed escalations) | Human-in-the-loop for borderline predictions |
| False positives (over-escalating low-priority tickets) | Use soft signals first (priority suggestions, not auto-routing) |
| Biased training data (based on past triage decisions) | Include diverse ticket examples across regions/times/tone |
| User trust | Provide override/feedback options in the agent interface |

---

## 🧭 PM Strategy

- **Phase 1: Silent Mode** – Model predicts but doesn’t affect routing
- **Phase 2: Assistive Mode** – Model suggests priority, agents can override
- **Phase 3: Partial Automation** – Auto-route clear-cut high/low priority tickets
- **Phase 4: Continuous Learning** – Use agent feedback to retrain + calibrate

Rollout should focus on **trust-building with support teams**, not just model accuracy.

---

## ✅ Summary

Triage ML systems are one of the **highest-leverage internal tools** in customer-centric orgs.

As an ML PM:
- Prioritize **recall for critical cases**
- Design your rollout to respect **agent workflows and trust**
- Define success as **improved SLAs, faster resolution, and better agent focus**

This is not just a model — it’s an **AI teammate** that helps teams prioritize what matters most.
