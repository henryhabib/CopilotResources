# Copilot Studio Skills: Demo Guide

Each folder contains one skill (`SKILL.md`) and a `test-inputs/` folder. Paste or upload a test input into the agent's test chat, then check the output against "What to look for".

| Skill | Test input | What to look for |
|---|---|---|
| **meeting-recap** | `01-messy-notes.txt` | Travel freeze decision; Marcus's action item due next Thursday; forecast update is **Unassigned**; CRM licence question is open; Tom's sick kid is **left out** (privacy rule) |
| | `02-teams-transcript.txt` | Concept B and the Aug 25 go-live are decisions; 3 action items (David, Priya, Alex); copy ownership and the SEO URL question are open |
| **customer-complaint-reply** | `01-damaged-order-email.txt` | Product Quality / Delivery, 🟠 Medium (repeat issue, deadline); empathetic reply; no promised refund amount |
| | `02-billing-legal-threat.txt` | 🔴 High (legal threat, LinkedIn, enterprise); reviewer note to loop in Legal/Finance; **no admission of liability** |
| | `03-short-review.txt` | 🟢 Low; short public-review style reply, no blaming staff |
| **expense-report-checker** | `01-chicago-trip.csv` | ❌ business class (flight under 6h), hotel $39/night over, minibar, Zoom (must go via IT), luxury car; ⚠️ client dinner missing client names/purpose, $32.40 lunch missing receipt; ✅ $14.75 breakfast (under $25) |
| | `02-clean-report.csv` | All ✅ → **Approve** (mileage 60 × $0.67 = $40.20 is correct) |
| | `03-quick-question.txt` | Business class OK only **after** VP approval; lounge pass not covered by policy → manager decides |
| **job-description-writer** | `01-hiring-manager-notes.txt` | Replaces "guy", "young and energetic", "ninja", "aggressive", "native English speaker"; trims must-haves to 5 or fewer; adds "or equivalent experience" |
| | `02-minimal-notes.txt` | Flags **missing** location and salary instead of inventing them |
| **weekly-status-report** | `01-team-updates.txt` | 🔴 or 🟡 status (projected ~$227k vs $200k budget = 13% over → Red); asks: Finance to provide Stripe keys by June 20; critical data-exposure bug listed as a risk |
| | `02-good-week.txt` | 🟢 Green; short report; "None this week" for asks |
| **invoice-data-extractor** | `01-clean-invoice.txt` | All maths ✅; due date 2025-06-13 (calculated from Net 30) → Ready for approval |
| | `02-suspicious-invoice.txt` | ❗ Laptop line: 12 × $85 = $1,020, **not** $1,120 (subtotal overstated by $100); ❗ no PO; ❗ due in 5 days; ❗ **bank change = possible fraud**; odd `.co` email domain → Hold |

## Advanced: multi-file skill package (.zip)

`business-case-roi/` shows a skill with **references, a template, and a Python script**. Upload `business-case-roi.zip`, which leaves out `test-inputs/`.

```
business-case-roi/
├── SKILL.md                          main instructions + map of the other files
├── references/finance-assumptions.md discount rate, hourly rates, approval thresholds
├── references/estimating-benefits.md converting time saved into dollars
├── assets/business-case-template.md  output format
└── scripts/roi_calculator.py         exact ROI / NPV / IRR / payback maths
```

| Test input | What to look for |
|---|---|
| `01-automation-tool.txt` | Time saved: 6 × 8 hrs × 75% = 36 hrs/wk × $40 × 46 = $66,240 + $12,000 fees = **$78,240/yr**. With the 50/90/100% ramp-up: ROI **89.7%**, NPV **$67,314**, IRR **65.8%**, payback **17.5 months** (just under the 18-month target). At −30%: payback **25.4 months**, so the sensitivity check matters. Approver: **Department director**. |
| `02-bad-investment.txt` | ROI **−36.4%**, NPV **−$124,229**, never pays back → ❌ Do not recommend. Approver: VP + Finance. |
| `03-missing-info.txt` | Agent should **ask** for the cost, number of users, and time saved instead of guessing. |

**Did the script actually run?** The script output ends with `VERIFIED_BY_SCRIPT=true` and quotes exact figures like **$67,314**. If the agent's numbers differ slightly, or there's no sign the script ran, Copilot Studio probably estimated the maths instead of running the code. That makes a good teaching moment.

**Note:** if the agent doesn't apply the ramp-up, it will use $78,240 flat for 3 years and get different numbers. Both are valid; just check which assumptions it states.

## Demo ideas
1. **Before/after:** run the same input with the skill turned off and then on, and compare consistency.
2. **Edit the policy live:** change the hotel limit in `expense-report-checker/SKILL.md` to $300, re-upload it, and show the result change. Business users can update the agent's behaviour without code.
3. **Catch the trap:** ask the audience to spot the errors in `02-suspicious-invoice.txt` before running the agent.
