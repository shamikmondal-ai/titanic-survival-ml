# Day 1 – Spotify Use Case (ML Product Thinking Warm-Up)

---

## 🎯 Goal

Increase user engagement using AI — specifically by improving the music recommendation experience on the home page.

---

## 📊 Existing Signals Available

- Listening history
- Skip rate
- Time spent per session
- Time of day / day of week
- Device type (mobile/desktop/speaker)
- Likes, dislikes, saves
- Playlist follows and unfollows
- User location, language, subscription tier

---

## 🤕 User Problems Identified

- Music recommendations are repetitive over time
- Users aren't discovering new content
- Workout/Focus playlists often miss mood or energy level
- New users don’t get meaningful personalization quickly
- Personalized playlists feel stale after a few weeks

---

## 🚫 Non-ML Alternatives (Baselines)

- Rule-based playlist curation (e.g., sort by popularity + genre)
- Time-of-day based manual scheduling
- Predefined “editorial” recommendation blocks
- Recently played & popular artists shown statically

---

## 🤖 If ML is Used — What Kind and Why?

| ML Technique             | Use Case |
|--------------------------|----------|
| Collaborative Filtering  | Leverage patterns from similar users |
| Content-Based Filtering  | Recommend based on track metadata (genre, tempo, mood) |
| Embedding Models         | Capture similarity between songs, users, playlists |
| Sequential Models (RNNs) | Predict next likely song in session |
| Bandits / Reinforcement Learning | Optimize playlist ordering in real-time based on interactions |

---

## 📈 Key Product Metrics to Track

- Daily active time spent listening
- Skip rate per session
- # of new artists discovered per user/week
- Retention over 30 days
- Satisfaction score (via survey or feedback prompts)

---

## 🧠 PM Thinking Summary

Before choosing an ML model, validate:
- Is the user problem clearly defined?
- Is there enough signal in the data to personalize meaningfully?
- Can a simpler solution work well enough?
- How will we evaluate model effectiveness from a user and business perspective?

