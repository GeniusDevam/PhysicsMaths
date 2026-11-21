# Config reference and authoring guide

## Schema (config.json)
```
{
  "id": "short-slug",                 // storage key; keep it stable when republishing so progress survives
  "title": "...", "subtitle": "...",  // shown in the header
  "start": "YYYY-MM-DD", "deadline": "YYYY-MM-DD",
  "hoursPerDay": 4, "maxHoursPerDay": 6, "bufferDays": 5,
  "offWeekdays": [0, 6],              // 0=Sunday ... 6=Saturday (at most 5 days)
  "daysOff": ["YYYY-MM-DD"],          // holidays, exams, travel
  "theme": "midnight|paper|forest|cosmic", "colors": {"--ac": "#2f855a"},   // optional overrides
  "tasks": [{"title": "unique name", "kind": "label (use gate for tests)", "hours": 20, "hint": "resources"}],
  "lessons": {"Task title": [["Lesson", hours, "Learn: ... Do: ...", "Resources"]]},   // optional
  "phases": [{"name": "...", "hours": 300, "note": "..."}],   // optional later stages, shown on the Phases tab
  "motivation": [["headline", "caption", "optional tag"]],    // optional daily card (quotes, equations, goals)
  "bgSvg": "<svg ...>"                // optional decorative background
}
```
Tasks run in the listed order: put prerequisites first, and interleave subjects the way a learner would study them. A task can be split across days; a day can touch several tasks.

## Turning a syllabus into tasks
1. List the topics in learning order from what the user gave you (pasted syllabus, course page, textbook contents, exam board spec). If they gave only a goal, draft the topic list and confirm it.
2. Size tasks at 5 to 60 hours. Estimate: textbook chapter with problems 3-6 h; one lecture hour 2-3 h including practice; a full university course 120-150 h; exam-prep topic 1.5-2x the reading time.
3. Add review slots: a short test ("gate") of 4-6 h after every 2-4 topics, plus a final mock or capstone.
4. Capacity check: work days x hours per day. Aim for total task hours around 85-90% of capacity after subtracting the buffer (default about 2 weeks for long plans, 3-5 days for short ones). The build script prints the required pace; fix any warning before publishing (trim scope, extend the deadline, or raise hours).
5. Topics the user already knows: keep them (the app has an "I already know this" button) but note it in the reply.

## Lessons (optional but valuable)
Each lesson is `[title, hours, "Learn: ... Do: ...", "Resources"]`. Lessons for a task must sum to the task's hours; the build script enforces this. Write lessons only for tasks you can do accurately; the others fall back to the task hint. Every resource must be real and specific (course and unit, episode, chapter). If you are unsure a resource exists, search for it first rather than guessing. Prefer free resources unless the user says otherwise.

## Phases (optional)
For multi-stage goals (for example, foundations then advanced topics), the main syllabus is phase 1 and `phases` lists later stages with planned hours. They are projected from the planned pace and shift when earlier phases slip. Omit `phases` and the Phases tab disappears.

## Theme, background and motivation
- Pick a theme that fits the subject and the user's taste, then override colours with `colors` if needed (CSS variables: --bg, --cd card, --ink, --mu muted, --ac accent, --gd highlight, --bd warning, --ln lines, --bgg page background).
- `bgSvg` is optional art behind the content (a fixed layer). Write one SVG sized to the viewport with a viewBox and `preserveAspectRatio="xMidYMid slice"`, keep it faint (opacity 0.1-0.3) so text stays readable, and avoid external images. Do not use double quotes problems: the config is JSON, so escape quotes properly. Tie the art to the subject (circuit traces for electronics, star fields for astronomy, leaves for biology).
- `motivation` entries rotate daily. Use meaningful content (key equations, mantras, the user's own goals), and put what it will unlock in the caption or tag.

## Exam fields (for exams, interviews and certifications)
- `examName`, `examDate` (YYYY-MM-DD): shows a countdown on Today. The deadline must not be after `examDate`; usually set it to the day before.
- `sources`: `[["label", "https://...", "short note"]]`, shown on the Syllabus tab with the date in `verifiedOn`. List the official notice, the syllabus PDF, the schedule source, and any past-paper archive you used.
- `notes`: assumptions and caveats (tentative dates, which post or group the plan targets, days off to add). They are shown to the learner so nothing is hidden.
- Clickable links: write resources as `[Label](https://url)` inside hints and lesson resources; plain text stays plain.
