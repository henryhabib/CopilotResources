#!/usr/bin/env python3
"""
ROI / Business Case Calculator
Used by the business-case-roi skill.

Works out ROI, payback period, NPV and IRR for a proposed investment.
Standard library only, so no installs are needed.

Usage examples:
  # Same benefit every year
  python roi_calculator.py --investment 120000 --annual-benefit 60000 --annual-cost 12000 --years 3

  # Different benefit each year (e.g. a ramp-up)
  python roi_calculator.py --investment 120000 --benefits 30000,60000,70000 --annual-cost 12000

  # Custom discount rate (default is 8%)
  python roi_calculator.py --investment 50000 --annual-benefit 25000 --years 3 --discount-rate 0.10
"""

import argparse
import sys

VERSION = "1.0"


def npv(rate, cashflows):
    """Net present value. cashflows[0] is year 0 (today)."""
    return sum(cf / (1 + rate) ** year for year, cf in enumerate(cashflows))


def irr(cashflows, low=-0.99, high=10.0, tolerance=1e-7, max_iter=500):
    """Internal rate of return using bisection. Returns None if there's no IRR."""
    f_low, f_high = npv(low, cashflows), npv(high, cashflows)
    if f_low * f_high > 0:
        return None
    for _ in range(max_iter):
        mid = (low + high) / 2
        f_mid = npv(mid, cashflows)
        if abs(f_mid) < tolerance:
            return mid
        if f_low * f_mid < 0:
            high, f_high = mid, f_mid
        else:
            low, f_low = mid, f_mid
    return (low + high) / 2


def payback_months(investment, net_benefits):
    """Months until cumulative net benefit covers the investment (linear within a year)."""
    cumulative = 0.0
    for year, benefit in enumerate(net_benefits, start=1):
        if benefit > 0 and cumulative + benefit >= investment:
            remaining = investment - cumulative
            return round((year - 1) * 12 + remaining / benefit * 12, 1)
        cumulative += benefit
    return None  # never pays back within the period


def money(x):
    sign = "-" if x < 0 else ""
    return f"{sign}${abs(x):,.0f}"


def main():
    p = argparse.ArgumentParser(description="ROI / business case calculator")
    p.add_argument("--investment", type=float, required=True, help="Upfront cost (year 0)")
    p.add_argument("--annual-benefit", type=float, help="Benefit per year (same every year)")
    p.add_argument("--benefits", type=str, help="Comma-separated benefit per year, e.g. 30000,60000,70000")
    p.add_argument("--annual-cost", type=float, default=0.0, help="Ongoing cost per year (licences, support)")
    p.add_argument("--years", type=int, help="Number of years (needed with --annual-benefit)")
    p.add_argument("--discount-rate", type=float, default=0.08, help="Discount rate as a decimal (default 0.08)")
    a = p.parse_args()

    if a.benefits:
        benefits = [float(b.strip()) for b in a.benefits.split(",") if b.strip()]
    elif a.annual_benefit is not None and a.years:
        benefits = [a.annual_benefit] * a.years
    else:
        sys.exit("Error: give either --benefits OR both --annual-benefit and --years")

    net = [b - a.annual_cost for b in benefits]
    cashflows = [-a.investment] + net

    total_benefit = sum(benefits)
    total_cost = a.investment + a.annual_cost * len(benefits)
    net_gain = total_benefit - total_cost
    roi_pct = net_gain / total_cost * 100 if total_cost else 0.0
    npv_value = npv(a.discount_rate, cashflows)
    irr_value = irr(cashflows)
    payback = payback_months(a.investment, net)

    print(f"=== ROI CALCULATION (roi_calculator.py v{VERSION}) ===")
    print(f"Years analysed:      {len(benefits)}")
    print(f"Discount rate:       {a.discount_rate:.1%}")
    print("")
    print("Year-by-year cash flow:")
    print(f"  Year 0: {money(-a.investment)} (investment)")
    for i, n in enumerate(net, start=1):
        print(f"  Year {i}: {money(n)} (benefit {money(benefits[i-1])} - cost {money(a.annual_cost)})")
    print("")
    print(f"Total benefit:       {money(total_benefit)}")
    print(f"Total cost:          {money(total_cost)}")
    print(f"Net gain:            {money(net_gain)}")
    print(f"ROI:                 {roi_pct:.1f}%")
    print(f"{'NPV @ ' + format(a.discount_rate, '.0%') + ':':<21}{money(npv_value)}")
    print(f"IRR:                 {'n/a' if irr_value is None else f'{irr_value:.1%}'}")
    print(f"Payback period:      {'Does not pay back in period' if payback is None else f'{payback} months'}")
    print("")
    print("VERIFIED_BY_SCRIPT=true")


if __name__ == "__main__":
    main()
