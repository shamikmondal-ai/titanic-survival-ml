# Day 13 – Upsell / Cross-Sell Prediction Use Case (B2B SaaS Growth)

---

## 🎯 Problem Statement

In a B2B SaaS business, identifying which customers are likely to upgrade, buy more seats, or expand into new modules is critical for revenue growth.

Currently, sales and customer success (CS) teams often guess based on anecdotal input or manual signals.

We aim to build an ML model to **predict which accounts or users are likely to convert on upsell offers**, enabling teams to prioritize outreach, personalize campaigns, and drive expansion revenue.

---

## 📊 Key Signals

- Monthly product usage trends (e.g., seats used vs purchased)
- Feature usage depth (e.g., advanced analytics, integrations)
- Account growth indicators (e.g., more teammates invited)
- Support activity (frequency, sentiment, topic)
- CRM activity (emails opened, calls logged)
- NPS score / customer satisfaction survey response
- Trial to paid conversion time
- Recent contract engagement (renewal, expansion discussion)

---

## 🤖 ML-Based Approach

### Model Type:
- **Binary classifier** → Will upsell within 30/60/90 days: Yes (1) / No (0)

### Output:
- Probability score (0.00–1.00) for upsell likelihood
- Used for:
  - Priority queues for sales
  - In-app upsell nudges
  - Marketing automation triggers

---

## ⚖️ Precision vs Recall Strategy

| Goal | Focus |
|------|-------|
| Avoid spamming uninterested users | ✅ Precision |
| Don’t miss high-value expansion accounts | ✅ Recall |
| Balanced prioritization for sales reps | ✅ F1 Score |

Recommended: Start with **precision-first** model to maintain trust  
→ Then improve recall through data and model enrichment

---

## 📈 Business Impact Metrics

- Conversion rate of scored vs unscored leads
- Uplift in upsell revenue per rep or per segment
- Average deal size increase
- Sales team satisfaction (reps using vs ignoring scores)

---

## 🛡️ Product Risks & Mitigation

| Risk | Mitigation |
|------|------------|
| Scoring loyal but non-expanding customers as “hot” | Limit outreach frequency; layer with manual insights |
| Missing strategic upsell opportunities | Route borderline cases to CS review |
| Bias toward certain verticals or account sizes | Monitor distribution of scores; segment-level tuning |
| Loss of trust if predictions feel random | Provide transparency: “This account grew 15% last month” |

---

## 🧭 PM Strategy

- **Phase 1: Shadow Mode** — Score leads, but don’t expose to sales team
- **Phase 2: Suggestive Mode** — Show top-scoring leads as daily recommendations
- **Phase 3: Integrated Routing** — Auto-create tasks or move leads to specific cadences
- **Phase 4: Feedback Loop** — Use sales acceptance + conversion rates to retrain monthly

Use dashboards to show:
- Model performance
- Conversion attribution
- Account score distributions

---

## ✅ Summary

Upsell prediction models help align GTM teams with data, improve sales focus, and scale revenue without adding headcount.

As a PM:
- Focus on **high signal features**
- Choose the right threshold for business goals
- Optimize not just for model metrics — but for **revenue lift and rep efficiency**

**A good upsell model pays for itself. A great one powers your next growth quarter.**
