# Day 10 – Lead Scoring ML Use Case (B2B SaaS Sales Enablement)

---

## 🎯 Problem Statement

Sales reps in B2B SaaS companies (e.g., Salesforce, HubSpot, Zoho) receive hundreds or thousands of inbound leads — but not all are equal.

Without prioritization, reps waste time on cold leads while hot, high-intent leads go untouched.

The goal is to build a lead scoring system using machine learning that predicts **which leads are most likely to convert**, allowing sales teams to focus efforts and maximize revenue.

---

## 📊 Available Data Signals

- Lead source (organic, referral, ad campaign)
- Company size / industry
- Title / role of lead (e.g., VP vs Analyst)
- Website engagement (pages viewed, downloads, time on site)
- Trial sign-up or product usage metrics
- CRM data (e.g., opened sales emails, clicked links)
- Past purchase history or renewal intent
- Country / time zone

---

## 🤖 ML-Based Approach

### Model Type:
- **Binary classifier** → Predict whether a lead will convert (1) or not (0)

### Features:
- Derived engagement scores (e.g., high-engagement session flag)
- Job seniority encoded into tiers
- Product activity recency (last 7 days usage)
- Categorical variables one-hot encoded (industry, source, tier)

### Output:
- Probability score (0 to 1) → interpreted as lead quality

---

## 📈 Metrics and Evaluation Strategy

| Metric | Why It Matters |
|--------|----------------|
| **Precision** | Sales teams must trust that high scores = high-quality leads |
| **Recall** | Don't miss promising leads who might convert |
| **F1 Score** | Balanced metric for calibration of triage thresholds |
| **Lift over random** | Shows how much better the model performs than guesswork |
| **Revenue generated from scored leads** | Ultimate business outcome metric |

---

## ⚖️ Precision vs Recall Trade-Off

- **Precision-first** approach: Avoid sending low-quality leads to reps
- **Recall second**: Improve over time to capture more good leads, but not at the cost of spamming reps
- Use **tiered lead routing**:
  - High score → route to sales
  - Medium → email nurture
  - Low → drop or delay outreach

---

## 🛡️ Product Risks and Mitigations

| Risk | Mitigation |
|------|------------|
| False positives (bad leads marked high) | Limit reps to “Top 5” leads/day, track lead-to-conversion ratio |
| False negatives (good leads dropped) | Use fallback campaigns (email nurture), re-evaluate periodically |
| Biased training data (from legacy behavior) | Retrain with new campaigns, balance features, check fairness across industries or company sizes |
| Model trust | Show score drivers (e.g., “High engagement, job seniority = Director+”) to sales team |

---

## 🧭 PM Strategy

- **Phase 1: Shadow Mode** — Model scores leads silently, no impact on sales routing
- **Phase 2: Assistive Mode** — Show scores + reasons in CRM, reps choose manually
- **Phase 3: Automated Routing** — High-confidence leads auto-assigned to sales reps
- Monitor feedback loop → sales accepts/rejects lead → retrain model monthly

Success = Increased conversion rate per rep + shorter sales cycles + higher ROI per campaign

---

## ✅ Summary

Lead scoring is a high-leverage ML use case that **increases revenue without adding headcount**.

As an ML PM:
- Focus on **precision**, especially early in rollout
- Treat your model as an **assistant**, not an absolute decision-maker
- Use scores as part of a **prioritization system**, not a binary gate

The most impactful models are those that **augment humans**, not just automate choices.
