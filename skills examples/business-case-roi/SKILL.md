---
name: business-case-roi
description: Builds a one-page business case for a proposed investment (new software, hire, tool, automation, or project) with accurate ROI, payback period, NPV, and IRR calculated by a script, plus a clear recommendation. Use when the user asks "is this worth it?", "build a business case", "calculate the ROI", "what's the payback period", or shares costs and expected savings for a proposal.
---

# Business Case & ROI

Help business professionals turn a rough idea ("this tool will save us loads of time") into a credible one-page business case with **exact** numbers.

## Files in this skill

| File | When to use it |
|---|---|
| `scripts/roi_calculator.py` | **Always** use it for the calculations. Never do ROI/NPV/IRR maths by hand. |
| `references/finance-assumptions.md` | Read it for the standard discount rate, hourly labour rates, and approval thresholds. |
| `references/estimating-benefits.md` | Read it when the user gives benefits as time saved, errors reduced, or other non-cash savings that need converting to dollars. |
| `assets/business-case-template.md` | Use it as the exact output format for the final business case. |

## Steps

1. **Gather the inputs.** You need:
   - **Upfront investment** (one-time cost)
   - **Annual benefit** (savings or extra revenue per year), or a per-year list if benefits ramp up
   - **Ongoing annual cost** (licences, support, maintenance)
   - **Number of years** (default 3 if not given; see finance assumptions)

   If the investment or the benefit is missing, **ask the user**. Don't make them up.
2. **Convert non-cash benefits to dollars** using `references/estimating-benefits.md` (e.g. hours saved × loaded hourly rate). Show the conversion.
3. **Run the calculator:**
   ```
   python scripts/roi_calculator.py --investment <amount> --annual-benefit <amount> --annual-cost <amount> --years <n>
   ```
   or, for ramp-up benefits:
   ```
   python scripts/roi_calculator.py --investment <amount> --benefits <y1>,<y2>,<y3> --annual-cost <amount>
   ```
   Use the discount rate from `references/finance-assumptions.md` (`--discount-rate`).
4. **Use the script's numbers exactly.** Don't round differently or recalculate. The output must contain `VERIFIED_BY_SCRIPT=true`; if it doesn't, tell the user the calculation couldn't be verified.
5. **Check the approval threshold** in `references/finance-assumptions.md` to say who needs to sign off.
6. **Write the business case** using `assets/business-case-template.md`.

## Recommendation rules

- ✅ **Recommend**: NPV is positive **and** payback is within the target in the finance assumptions
- ⚠️ **Recommend with conditions**: NPV is positive but payback is longer than target, or the benefits rely on uncertain assumptions
- ❌ **Do not recommend**: NPV is negative, or it never pays back within the period

## Rules

- Always state your assumptions. A business case is only as good as its assumptions.
- Include a **"What if benefits are 30% lower?"** sensitivity check by running the script a second time with benefits × 0.7.
- Keep the final business case to one page (under 350 words, excluding tables).
