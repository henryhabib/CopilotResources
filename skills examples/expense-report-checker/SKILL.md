---
name: expense-report-checker
description: Reviews expense reports or lists of expense line items against the company travel and expense policy, flags violations and missing information, and gives an approve/reject/needs-info recommendation. Use when the user pastes or uploads an expense report, receipts list, or spreadsheet of expenses, or asks "is this expense allowed?", "check this expense report", or "does this follow policy?".
---

# Expense Report Checker

Help managers and finance teams review expense reports quickly and consistently against policy.

## Company expense policy (source of truth)

> Course note: swap this section for your organisation's real policy. The skill only works as well as the rules you give it.

| Category | Limit | Notes |
|---|---|---|
| Hotel | $250 / night | $350 / night in New York, London, San Francisco |
| Meals (travelling) | $75 / day per person | Alcohol is **not** reimbursable |
| Client entertainment | $150 per person | Must list client name and business purpose |
| Flights | Economy only | Business class allowed only for flights over 6 hours **with VP approval** |
| Ground transport | Reasonable | Taxi/rideshare OK; no luxury car services |
| Mileage | $0.67 / mile | Must include start/end location |
| Software/subscriptions | Not via expenses | Must go through IT procurement |

**General rules**
- Every item over **$25** needs a receipt.
- Expenses must be submitted within **60 days** of the expense date.
- Personal items (minibar, in-room movies, gym fees, upgrades) are not reimbursable.

## Steps

1. **Read every line item.** Get the date, category, vendor, amount, and description.
2. **Check each item** against the policy table and general rules above.
3. **Give each item a status:**
   - ✅ **OK**: within policy
   - ⚠️ **Needs info**: missing a receipt, business purpose, attendees, or approval
   - ❌ **Violation**: breaks a policy rule (state the rule and the amount over)
4. **Total it up.** Calculate the total submitted, the total OK, and the total flagged.
5. **Recommend** one of: **Approve**, **Approve with adjustments** (reimburse only compliant amounts), **Return for more info**, or **Reject**.

## Output format

```
## Expense Review: <Employee name> – <Trip/Period>

**Recommendation:** <Approve / Approve with adjustments / Return for more info / Reject>

| # | Date | Item | Amount | Status | Reason |
|---|------|------|--------|--------|--------|
| 1 | ... | ... | $... | ✅/⚠️/❌ | <policy rule or "Within policy"> |

**Totals**
- Submitted: $X
- Within policy: $X
- Flagged: $X

**Message to employee** (if anything is flagged)
<Short, friendly note listing exactly what they need to fix or provide.>
```

## Rules

- Do the maths carefully. Show per-night or per-day calculations where it matters (e.g. "3 nights × $289 = $867; limit is $250/night").
- Quote the specific policy rule for every flag.
- Stay neutral and non-accusatory. Assume honest mistakes.
- If the policy doesn't cover an item, mark it ⚠️ and say "Not covered by policy – manager to decide." Don't guess.
