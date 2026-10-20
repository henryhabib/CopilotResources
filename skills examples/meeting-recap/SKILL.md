---
name: meeting-recap
description: Turns raw meeting notes or a transcript into a clean, consistent meeting recap with a summary, decisions, action items (owner + due date), and open questions. Use when the user pastes meeting notes or a transcript, or asks to "summarize this meeting", "write a recap", "pull out action items", or "draft a follow-up email" after a meeting.
---

# Meeting Recap

Turn messy meeting notes or transcripts into a recap the team can act on right away.

## When to use this skill

Use it when the user:
- Pastes meeting notes, a Teams transcript, or bullet points from a call
- Asks for a summary, recap, minutes, or action items
- Asks for a follow-up email after a meeting

Do **not** use it for general document summaries that aren't meetings.

## Steps

1. **Read the whole input first.** Work out who attended, what the meeting was for, and what was agreed.
2. **Pull out decisions.** Only include something that was actually agreed. Leave out ideas that were just discussed.
3. **Pull out action items.** Every action item needs:
   - **Task**: starts with a verb ("Send", "Review", "Book")
   - **Owner**: a named person. If nobody was named, write `Unassigned`. Never guess.
   - **Due date**: as stated. If none was given, write `No date set`.
4. **List open questions.** Include anything left unresolved or marked "to follow up".
5. **Write the recap** using the format below.
6. **Offer one next step:** "Want me to turn this into a follow-up email to the attendees?"

## Output format

Use exactly this structure:

```
## Meeting Recap: <Meeting topic> (<Date if known>)

**Attendees:** <names, or "Not specified">

### Summary
<2–3 sentences in plain business language. What was the meeting about and what was the outcome?>

### Decisions
- <Decision 1>
- <Decision 2>

### Action Items
| # | Task | Owner | Due |
|---|------|-------|-----|
| 1 | <Verb-first task> | <Name> | <Date> |

### Open Questions
- <Question>
```

If a section has no content, write `None` under it. Don't remove the section.

## Rules

- **Stay accurate.** Don't invent names, dates, numbers, or decisions that aren't in the input.
- **Keep it short.** The whole recap should be readable in under a minute.
- **Write neutrally and professionally.** Leave out filler, jokes, and side conversations.
- **Respect privacy.** Leave out personal or sensitive remarks (HR, health, salary) unless the user asks for them.

## Follow-up email (if the user asks)

```
Subject: Recap & next steps: <Meeting topic>

Hi all,

Thanks for your time today. Here's a quick recap:

<Summary>

Action items:
- <Owner>: <Task> (by <Due>)

Open questions:
- <Question>

Let me know if I missed anything.

Best,
<User's name, or leave a placeholder>
```

## Example

**Input:**
> sync w/ marketing tues. sarah, james, priya. agreed to push Q3 launch to Aug 15. james to update the launch deck by fri. need someone to check budget w/ finance. priya asked if we still do the webinar - nobody sure.

**Output:**

## Meeting Recap: Marketing Sync (Tuesday)

**Attendees:** Sarah, James, Priya

### Summary
The team met to review Q3 launch timing. They agreed to move the launch to August 15 and found a few follow-ups on budget and the webinar.

### Decisions
- Q3 launch moved to **August 15**

### Action Items
| # | Task | Owner | Due |
|---|------|-------|-----|
| 1 | Update the launch deck with the new date | James | Friday |
| 2 | Confirm launch budget with Finance | Unassigned | No date set |

### Open Questions
- Is the webinar still happening as part of the launch?
