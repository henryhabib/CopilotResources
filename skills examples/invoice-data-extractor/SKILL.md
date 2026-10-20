---
name: invoice-data-extractor
description: Extracts key fields from invoices (vendor, invoice number, dates, line items, tax, totals) into a clean, structured table, checks the maths, and flags anomalies like duplicate numbers, total mismatches, or missing PO numbers. Use when the user pastes or uploads an invoice, bill, or receipt, or asks to "extract invoice data", "pull the details from this invoice", or "check this invoice".
---

# Invoice Data Extractor

Help finance and accounts payable teams pull structured data out of invoices and catch errors before payment.

## Fields to extract

| Field | Notes |
|---|---|
| Vendor name | As shown on the invoice |
| Invoice number | Exactly as written |
| Invoice date | Format as YYYY-MM-DD |
| Due date | YYYY-MM-DD. If only terms are given (e.g. "Net 30"), calculate it and note "(calculated)" |
| PO number | Write `MISSING` if there isn't one |
| Currency | e.g. USD, EUR, GBP |
| Line items | Description, quantity, unit price, line total |
| Subtotal, Tax, Total | As stated on the invoice |

## Steps

1. **Extract** every field above. If a field isn't on the invoice, write `Not found`. Never guess.
2. **Check the maths:**
   - Each line: quantity × unit price = line total
   - Sum of line totals = subtotal
   - Subtotal + tax (− discounts) = total
3. **Flag anomalies:**
   - ❗ Maths doesn't add up (show the expected vs. stated value)
   - ❗ Missing PO number
   - ❗ Due date already passed, or under 7 days away
   - ❗ Bank details mention a "change", "new account", or "update". This is a **possible fraud signal**: tell the user to verify by phone using a known number.
   - ❗ Tax rate looks unusual for the stated region
4. **Output** in the format below.

## Output format

```
## Invoice Summary: <Vendor> #<Invoice number>

| Field | Value |
|---|---|
| Vendor | |
| Invoice # | |
| Invoice date | |
| Due date | |
| PO # | |
| Currency | |
| Subtotal | |
| Tax | |
| **Total** | |

### Line items
| # | Description | Qty | Unit price | Line total | Check |
|---|---|---|---|---|---|
| 1 | | | | | ✅ / ❗ |

### Validation
- Maths check: <✅ All totals correct / ❗ details>
- Flags: <list, or "None">

**Recommendation:** <Ready for approval / Hold – resolve flags first>
```

## Rules

- Copy numbers exactly. Don't round unless the invoice does.
- Treat any bank-detail change as high priority, even if everything else looks fine.
- If several invoices are provided, process each one separately, then add a one-line summary table at the end.
