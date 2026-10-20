---
name: weekly-status-report
description: Turns scattered project updates (team messages, notes, task lists) into a concise executive weekly status report with an overall RAG status (Red/Amber/Green), progress, risks, and asks for leadership. Use when the user pastes project updates or asks to "write my weekly status report", "create a project update for leadership", or "summarize this week's progress".
---

# Weekly Status Report

Help project managers and team leads turn messy updates into a one-page status report that executives can read in 60 seconds.

## Steps

1. **Collect the facts.** From the input, pull out what was finished, what's in progress, what's blocked, upcoming milestones, and any numbers (budget, % complete, dates).
2. **Decide the overall RAG status** using these rules:
   - 🟢 **Green**: on track for scope, schedule, and budget; no major blockers
   - 🟡 **Amber**: at risk; a milestone may slip, budget is 5–10% over, or there's an unresolved blocker the team can still handle
   - 🔴 **Red**: off track; a milestone has slipped or will slip, budget is more than 10% over, or a blocker needs leadership to step in
   - When in doubt between two colours, **choose the more cautious one** and explain why.
3. **Write for executives.** Lead with outcomes, not activity. "Payment integration live in test" beats "Worked on payment stuff."
4. **Make the asks explicit.** If leadership needs to decide, approve, or unblock something, put it in "Decisions / Help needed" with a named owner and a deadline.

## Output format

```
# Weekly Status: <Project name>
**Week ending:** <date> | **Owner:** <name> | **Overall status:** <🟢/🟡/🔴 + word>

**TL;DR:** <One sentence: where we are and the single most important thing.>

### ✅ Completed this week
- <outcome>

### 🔄 In progress / next week
- <item> – <target date if known>

### ⚠️ Risks & issues
| Risk/Issue | Impact | Mitigation | Owner |
|---|---|---|---|

### 🙋 Decisions / help needed
- <Specific ask> – needed from <who> by <date>   (or "None this week")

### 📅 Key milestones
| Milestone | Target date | Status |
|---|---|---|
```

## Rules

- Keep the whole report **under 300 words**.
- Don't hide bad news. If something slipped, say so plainly in the TL;DR.
- Don't invent dates, percentages, or owners. Use `[TBC]` if unknown.
- Leave out jargon and internal ticket numbers unless the user asks for them.
