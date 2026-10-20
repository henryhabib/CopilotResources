---
name: customer-complaint-reply
description: Drafts calm, empathetic, on-brand replies to customer complaints and classifies each complaint by category and urgency. Use when the user pastes a customer email, review, chat message, or support ticket that expresses frustration, or asks to "reply to this customer", "respond to this complaint", or "handle this angry email".
---

# Customer Complaint Reply

Help support and account teams reply to unhappy customers quickly, consistently, and without making promises the company can't keep.

## When to use this skill

- A customer email, review, chat, or ticket is pasted and the customer is unhappy
- The user asks for a reply, a response, or a way to de-escalate

Do **not** use it for positive feedback or general sales enquiries.

## Steps

1. **Triage first.** Before drafting, work out:
   - **Category:** Billing, Delivery/Shipping, Product Quality, Service/Staff, Technical Issue, or Other
   - **Urgency:**
     - 🔴 **High**: legal threats, safety issues, threats to cancel, public/social media posts, or a VIP/enterprise customer
     - 🟠 **Medium**: a clear financial or service impact
     - 🟢 **Low**: minor inconvenience or general frustration
   - **What the customer actually wants:** a refund, replacement, explanation, apology, or escalation
2. **Draft the reply** using the structure below.
3. **Flag risks** for the human reviewer, e.g. "Customer mentions a lawyer, so loop in Legal before sending."

## Reply structure (the A.R.C. method)

1. **Acknowledge.** Name the specific problem and their feeling ("I'm sorry your order arrived damaged; that's really frustrating, especially for a gift.").
2. **Resolve.** Say clearly what happens next. Use `[placeholders]` for anything the agent can't confirm (refund amount, dates, order numbers).
3. **Close.** Give a named contact or next step, and thank them.

## Rules

- **Never promise** refunds, credits, discounts, or timelines that aren't in the company policy. Use a placeholder like `[confirm refund amount]` instead.
- **Never blame** the customer, a colleague, or a third party (e.g. "the courier messed up").
- **Never admit legal liability** ("it was our fault and we'll pay for damages").
- Keep replies **under 150 words** unless the issue is complex.
- Match the channel: email replies get a greeting and sign-off; chat or social replies are shorter and more casual.
- Use the customer's name if it's given.

## Output format

```
**Triage**
- Category: <category>
- Urgency: <🔴/🟠/🟢 level> – <one-line reason>
- Customer wants: <what they want>

**Draft reply**
<reply>

**Notes for reviewer**
- <risks, placeholders to fill in, or who to loop in. "None" if nothing.>
```
