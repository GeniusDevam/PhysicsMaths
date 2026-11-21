---
name: syllabus-deadline-tracker
description: Build a free, self-contained progress-tracker web app for ANY exam, course, certification or goal and ANY deadline. Given just an exam name (or a pasted syllabus) plus a date, it researches the official pattern, dates and syllabus, finds and vets free study resources for each daily target, and generates an app with daily, weekly and monthly targets, a tick-box check-in, automatic rescheduling when days are missed, a deadline slider with before/after preview, days off, day-by-day lessons with clickable links, an exam countdown and a themed look. Use this skill whenever the user wants a study planner, exam countdown, syllabus tracker, "plan to finish X by date Y", free resources for an exam, or to update, extend, retheme or republish such an app, for competitive and government exams, university finals, certifications, language tests or self-study goals, even if they never say "skill" or "tracker".
---

# Syllabus Deadline Tracker

Generates a single-file web app (no backend, no paid services) from a short config. The hard parts (the scheduler, missed-day rebalancing, deadline preview, persistence) live in `assets/template.html`; your job is the content: a good syllabus, honest hour estimates, accurate resources, and a fitting look.

## Workflow

1. **Understand the target.** The user may give an exam name and date, a pasted syllabus, or just a goal. Any exam or deadline works. Ask only what you cannot find or infer (hours per day, days off, which post or stage if it matters); otherwise state assumptions in one line.
2. **Research (when given a name, not a syllabus).** Follow `references/research.md`: find the official notice, dates, pattern, marks and syllabus by searching and fetching pages, prefer official sources, flag tentative dates, and record sources.
3. **Draft the syllabus as tasks.** Follow `references/config.md`: tasks from the official syllabus sections, learning order, hours weighted by marks, timed mocks as `gate` tasks, a buffer, and a capacity check (total hours near 85-90% of work days x hours per day). If it does not fit, show the trade-offs; `scripts/pace.py` does the arithmetic.
4. **Find free resources and write lessons.** Follow `references/resources.md`: search per subject, vet each resource (free, relevant, current, legitimate), and add verified `[Label](url)` links to task hints and lesson resources. Write day-by-day lessons from the syllabus structure; lesson hours must sum to their task. Never invent a link or chapter; name unverified resources in plain text and say so.
5. **Choose the look.** `theme` (midnight, paper, forest, cosmic), optional `colors`, `bgSvg`, and `motivation` entries that fit the user and the subject.
6. **Build.** Write `config.json` and run `python scripts/build_app.py config.json -o app.html`. It validates, prints total hours, planning days, required pace and link coverage, and warns about problems. Fix warnings. Optionally `node scripts/smoke_test.js app.html`.
7. **Deliver.** Publish `app.html` as a page if an Artifact tool exists, otherwise present the file. Reply briefly: what was built, the assumptions (target stage, dates, hours, days off), which resources are verified, which tasks lack lessons, and that dates should be re-confirmed on the official site.
8. **Maintain.** Edit the config and rebuild, then republish to the same page so progress is kept (keep `id` and task titles stable). Deeper changes: small targeted edits to `assets/template.html`.

## Files

- `assets/template.html`: the app template. The config is injected at `/*__CONFIG__*/{}`.
- `scripts/build_app.py`: validate and build. `scripts/pace.py`: pace, extension and what-if arithmetic. `scripts/smoke_test.js`: render check.
- `references/research.md`: researching an exam from its name. `references/resources.md`: finding and vetting free resources. Read both whenever the user names an exam or goal.
- `references/config.md`: schema, sizing a syllabus, lessons, exam fields, themes, backgrounds. Read before writing a config.
- `references/behaviour.md`: what the app does, scheduling rules, persistence and platform limits. Read before changing the template or answering questions about the app.
- `examples/example-config.json`: a small complete config to copy from.

## Principles

- Honesty over flattery: if the plan cannot fit the deadline, say so and offer options with numbers. Never silently drop content or move a deadline.
- Free by default: no paid APIs or services, local storage only; prefer free learning resources unless the user says otherwise.
- Accuracy of resources matters more than quantity of lessons; partial coverage is fine if the rest falls back to hints, and say which tasks lack lessons.
- Keep the app calm and motivating: no guilt messaging for missed days; missed hours are simply rescheduled.
