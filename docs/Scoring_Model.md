# AI Product Readiness Scoring Model

## Objective

The scoring model translates launch readiness into a consistent and transparent decision framework.

The score is intended to support—not replace—product judgment.

---

## Gate Weighting

Every gate contributes equally.

| Gate | Maximum Score |
|------|--------------:|
| Customer Value | 20 |
| AI Quality | 20 |
| Trust & Safety | 20 |
| Operational Readiness | 20 |
| Business Readiness | 20 |

Maximum Overall Score = 100

---

## Question Scoring

| Answer | Points |
|--------|-------:|
| Yes | 5 |
| Partial | 3 |
| No | 0 |

---

## Critical Questions

Some questions automatically prevent a Production recommendation.

Critical examples:

- Human evaluation completed
- Rollback plan documented
- Security review completed
- Legal approval completed

These are known as **Launch Blockers**.

---

## Recommendation Logic

Ready for Production

Requirements:

- Score ≥ 90
- No launch blockers

---

Ready for Beta

Requirements:

- Score ≥ 75
- No critical safety blockers

---

Additional Review Required

Requirements:

- Score between 60–74
OR
- One or more launch blockers

---

Not Ready

Requirements:

- Score below 60
OR
- Multiple critical blockers

---

## Output

The application generates:

- Overall Readiness Score
- Gate Scores
- Launch Recommendation
- Missing Critical Items
- Recommended Next Actions
