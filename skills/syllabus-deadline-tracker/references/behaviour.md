# What the generated app does (spec and constraints)

## Screens
- **Today**: today's target in hours, the lessons or tasks to cover (with resources), a large "I hit today's target" checkbox (undoable), "Log hours" for partial credit, "Re-plan today", a status chip (On track / Ahead / Behind / Infeasible with options), prompts for past work days with no check-in (Missed or Day off), a daily motivation card, and progress and streak.
- **Plan**: next 10 work days with lesson titles, weekly targets, monthly targets.
- **Syllabus**: every task with progress, expandable lessons, and "I already know this".
- **Phases**: only if the config has phases; projected start and end dates that shift automatically.
- **Settings**: deadline (date input, slider from 12 weeks earlier to 24 weeks later, and +/- week buttons), hours per day, maximum hours per day, buffer, weekly days off, extra days off, live before/after preview (planning days, daily, weekly, monthly targets), a what-if table for shifted deadlines, and backup as copy-and-paste text.

## Scheduling rules (summary)
- Work days exclude off weekdays and custom days off. Planning days are work days to the deadline minus the buffer. Required pace P = remaining hours / planning days; the daily target is P in 15-minute steps with remainders carried.
- Today's target is frozen when first opened. Missed hours stay in the remaining total, so targets recompute automatically. Ticking the box applies the day's hours to the queue; unticking reverses it.
- If P exceeds the maximum hours per day the plan is infeasible: the app offers a later deadline (the earliest that fits the planned hours) and never changes it without a click.
- Settings changes are previewed and applied only on confirmation; only future days change.

## Persistence and updating
- Progress lives in the viewer's `localStorage` under `<id>.v1`. On each load, tasks are re-synced from the config by title (hours and order update, completed hours are kept, new tasks appear, removed ones disappear). If the task list changed, pending day records are cleared so targets recompute. Deadline and other settings stay as the user set them in the app.
- Keep `id` and task titles stable between versions. Renaming a task resets its progress.
- Backups are shown as text to copy; browsers can clear local data.

## Platform constraints (published pages)
Single self-contained HTML file; no external scripts, fonts, images or network requests; downloads and file saves do not work, so there is no .ics or file export; storage is per browser, so progress does not sync between devices.

## Not implemented (say so if asked)
Per-task check boxes within a day, burn-up chart, drag-to-pin tasks, pinning later phases to fixed dates, adaptive estimates, calendar export, cross-device sync.

## Additions
- Resources written as `[Label](https://...)` render as links (opened in a new tab). Only http(s) links are linked.
- With `examDate`, Today shows a days-to-exam countdown. With `sources` or `notes`, the Syllabus tab shows a "Sources and assumptions" card with the check date.
