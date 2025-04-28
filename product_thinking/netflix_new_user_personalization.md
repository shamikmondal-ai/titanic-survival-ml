# Day 2 – Netflix Use Case: Personalization for New Users

---

## 🎯 Problem Statement

New Netflix users often land on the homepage and are shown default, non-personalized content. This can lead to:
- High bounce rate
- Low session time
- Poor early engagement
- Missed opportunity to capture user interest immediately

As a PM, the goal is to improve **first-session content relevance** using ML-driven personalization.

---

## 📊 Available Signals (at Signup or First Session)

- Country, region, language
- Time of day / day of week
- Device type (TV, mobile, desktop)
- Referral source (email, ads, direct)
- Genre preferences (if explicitly selected)
- First few clicks or scrolls (if tracked in real time)

---

## ⚙️ Non-ML Baseline Options

- Show globally trending titles
- Show regional top 10
- Default layout by genre (e.g., top picks in Action, Drama, Comedy)
- Manual curation by editorial team
- Rule-based recommendations (e.g., if India → suggest local content first)

These are easy to implement but don’t personalize for the **individual user context**.

---

## 🤖 ML Techniques (and Their Trade-offs)

| Technique | Use | Trade-Offs |
|----------|-----|------------|
| **Collaborative Filtering** | Recommend based on similar users’ preferences | Needs historical user data (not great for cold start) |
| **Content-Based Filtering** | Recommend based on metadata: genre, language, actors | Works better with limited user info; but less “serendipity” |
| **Hybrid Models** | Combine content + collaborative filtering | More accurate but more complex to implement |
| **Contextual Bandits / RL** | Learn from first few clicks in real time | Needs strong infra; can adapt quickly |
| **Embedding Models** | Map users and titles to latent space for similarity | Can support multi-dimensional personalization but requires compute + training data

---

## 📈 Key Product Metrics

- **Time to first stream**
- **Session length** (first 24 hours)
- **First 7-day retention**
- **Click-through rate (CTR)** on homepage rows
- **Genre diversity in first sessions**

---

## ⚠️ PM Considerations / Risks

- **Cold start problem** — limited data on new users
- **Cultural sensitivity** — content preferences vary by region/language
- **Latency vs experience** — ML model scoring must be fast for homepage
- **Bias in training data** — may reflect dominant user preferences (over-personalization risk)
- **Measurement difficulty** — personalization impact must be isolated from content changes

---

## 🧠 Strategic PM Questions

- Can we build personalization off **minimal signals** (region, time, device)?
- How do we test ML vs. rule-based approaches? (A/B test design)
- What’s our definition of a successful first session?
- How do we avoid recommending the same things to everyone?
- What’s the fallback when ML fails or is uncertain?

---

## ✅ Summary

Personalizing the first-time user experience on Netflix is a high-impact opportunity. ML can help tailor content **even in early stages**, but must be approached with thoughtful use of limited data, fallback logic, and experimentation strategy.

The right balance between **rule-based scaffolding and ML-driven adaptation** is key to driving engagement and retention for new users.

