# PhysicsMaths

A free, offline study system built around one ambitious goal: **learn physics and mathematics from scratch, all the way toward the research frontier** (quantum gravity, string theory, a theory of everything, the Millennium Prize problems), using only free resources.

**Try it now:** [open the FrontierPath tracker](https://geniusdevam.github.io/PhysicsMaths/apps/frontierpath/) in your browser. It runs entirely on your device and saves progress in that browser.

It has three parts:

1. **A realistic multi-year roadmap**, split into checkpoints, with a detailed 7-month first checkpoint (physics as it stood in the 1920s).
2. **FrontierPath**, a single-file tracker app that turns the roadmap and a deadline into daily, weekly and monthly targets, and re-plans automatically when you miss a day or move the deadline.
3. **Two Claude skills**: a personal study coach for this plan, and a generator skill (the engine FrontierPath grew into) that builds trackers like it for other syllabi and deadlines, researching the syllabus and free resources along the way.

Everything is free to run: no backend, no accounts, no paid APIs, no AI calls inside the apps. Your progress lives in your own browser.

> **Status:** working and tested with scripted checks (see [Status and limitations](#status-and-limitations)), but not yet put through a full manual pass across browsers and devices. Treat it as a solid first version.

## Contents

- [Purpose](#purpose)
- [What's in this repo](#whats-in-this-repo)
- [Quick start](#quick-start)
- [Using the tracker apps](#using-the-tracker-apps)
- [FrontierPath: the physics and maths journey](#frontierpath-the-physics-and-maths-journey)
- [Generate trackers for other syllabi](#generate-trackers-for-other-syllabi)
- [The coach skill](#the-coach-skill)
- [How the scheduling works](#how-the-scheduling-works)
- [Design constraints](#design-constraints)
- [Status and limitations](#status-and-limitations)
- [Next steps](#next-steps)
- [How this was made](#how-this-was-made)
- [License](#license)

## Purpose

Learning a huge subject alone fails in two usual ways: the plan is vague ("study physics"), and one bad week breaks it. This project tackles both.

- **A concrete plan.** The roadmap names what to study, in what order, from which free resources, with hours per topic and a pass/fail gate every month.
- **A plan that bends instead of breaking.** Targets are never stored; they are recomputed from the work still remaining and the working days still available. Miss a day and the hours spread over the days that remain. Move the deadline and every daily, weekly and monthly target updates, with a preview before you commit.
- **Honesty about the distance.** Checkpoint 1 is a bounded, achievable project. Reaching the point where you can read current research takes roughly 3 to 3.5 years at this pace. Original contributions to a Millennium Problem or a theory of everything cannot be scheduled and are never promised. The roadmap aims at the strongest possible foundation and a real chance to try.
- **Reusable.** The tracker started as a physics tool and was generalised, so the same engine now serves any syllabus and deadline.

## What's in this repo

| Path | What it is |
|---|---|
| `apps/frontierpath/index.html` | The physics and maths tracker (cosmic theme, daily equation, lessons for the first modules). Open it in a browser. |
| `skills/syllabus-deadline-tracker/` | **Generator skill.** App template, build script, pace calculator, smoke test, research and resource-vetting guides, an example config. |
| `skills/physics-maths-mastery/` | **Coach skill.** Roadmap, scheduling rules, lesson format, pace calculator, and a copy of the app. |
| `dist/*.skill` | The two skills packaged for upload to Claude. |
| `docs/roadmap-and-app-spec.md` | The full study plan (all checkpoints, resources, gate checklist) and the original app design spec. |
| `scripts/verify.sh` | One command that checks the whole repo is consistent. |

## Quick start

**Run an app.** No install, no build step, no network needed.

```bash
git clone https://github.com/GeniusDevam/PhysicsMaths.git
cd PhysicsMaths
# Option 1: open the file directly in a browser
#   apps/frontierpath/index.html
# Option 2: serve the folder locally, then visit http://localhost:8000/apps/frontierpath/
python3 -m http.server 8000
```

Your progress is saved in that browser's local storage. Browsers keep storage separate per browser and per address, so open the app the same way, in the same browser, each time.

**Check the repo.** Needs Python 3 and Node.js.

```bash
./scripts/verify.sh
```

It builds the example config, smoke-tests FrontierPath and the example app, and confirms that the app copy inside the coach skill and the packaged `.skill` files match their sources.

**Host it free.** Because each app is a single static file, any free static host works. This repository already serves FrontierPath on GitHub Pages at [https://geniusdevam.github.io/PhysicsMaths/apps/frontierpath/](https://geniusdevam.github.io/PhysicsMaths/apps/frontierpath/).

## Using the tracker apps

FrontierPath and the apps the generator builds share one engine and the same five tabs. (FrontierPath calls two of them Roadmap and Journey; generated apps call them Syllabus and Phases, and leave Phases out when there are no later stages.)

**Today**
- Shows today's target in hours and the lessons or tasks to cover, with resources.
- Tick **"I hit today's target"** when you finish. That credits the whole day's work. Untick it to undo.
- Did only part of it? Enter hours under **Log hours**. They are credited to your queue in syllabus order and the day is marked partial.
- **Re-plan today** regenerates today's target from the current state.
- A status chip says whether you are **On track**, **Ahead** or **Behind** (within about a quarter of an hour per day counts as on track).
- If the plan has become impossible within your maximum daily hours, the chip says so and offers a new deadline, the earliest date that fits your planned hours. Nothing changes until you click it.
- Work days that passed with no check-in are listed so you can mark each **Missed** or **Day off**. Missed hours are already folded back into the plan either way.
- Also shows overall progress, your streak (consecutive completed work days; days off never break it), and the projected finish date.

**Plan.** The next 10 work days with their lessons, then weekly and monthly targets.

**Roadmap or Syllabus.** Every topic with a progress bar, expandable day-by-day lessons, and an **I already know this** button that removes a topic's hours from the plan (press again to reset).

**Journey or Phases.** Later stages after the main syllabus, projected from your planned pace. They shift automatically when the earlier stage slips.

**Settings** (the timeline controls)
- Deadline: a date input, a **slider** (from 12 weeks earlier to 24 weeks later than your saved deadline), and ±2 / ±4 week buttons.
- Hours per day, maximum hours per day, and a buffer of work days kept free at the end.
- Days off each week, plus extra individual days off (holidays, exams, travel).
- A live **before → after preview** of planning days and daily, weekly and monthly targets, and a **what-if table** showing the required pace for deadlines 4 and 2 weeks earlier, and 2, 4 and 8 weeks later. Nothing is applied until you press **Apply changes**. Only future days change; history stays as it was.
- **Backup:** *Show backup* prints your data as text to copy somewhere safe; *Restore from text* loads it back.

## FrontierPath: the physics and maths journey

The goal is split into checkpoints so progress is visible and the plan can be re-planned at each one.

| # | Goal | Estimate |
|---|---|---|
| 1 | Physics as of the 1920s: classical foundations, quantum mechanics, special and general relativity | 7 months (target 6 to 7) |
| 2 | Rigorous maths plus graduate-level quantum, statistical and electromagnetic physics | about 8 months |
| 3 | Quantum field theory, the Standard Model, advanced GR and cosmology | about 9 months |
| 4 | Frontier entry: string theory, supersymmetry, CFT, quantum gravity, and the maths behind the Millennium Problems | 12 to 18 months |
| 5 | Research frontier: pick a problem, read the literature, write, find mentors | open-ended |

**Checkpoint 1 in the app:** 27 tasks totalling 837 hours (content, seven monthly gates and a capstone), planned over 207 days (about 7 months) starting the day you first open the app, at 6 hours per weekday, weekends off, with a 10-work-day buffer. The original plan ran from 5 Oct 2026 to 30 Apr 2027; change the deadline and hours in Settings. Day-by-day lessons with exact resources are written for the first four modules (diagnostic and setup, calculus and vectors, Newtonian mechanics, multivariable calculus, 135 hours in total). Later modules show their resource list until their lessons are written. The Journey tab projects Checkpoints 2 to 5 from their estimated hours.

The app has a deep-space look (pulsar, black hole, multiverse bubbles, real equations drawn faintly in the background) and a "north star" equation card each day, tied to the checkpoint where you will be able to read it fluently.

The full plan, with month-by-month resources, the Checkpoint 1 competency checklist (used as gate questions) and what each Millennium Problem demands, is in [`docs/roadmap-and-app-spec.md`](docs/roadmap-and-app-spec.md).

## Generate trackers for other syllabi

Beyond the physics plan, the generator skill produces an app like FrontierPath for any other syllabus and deadline. It is optional; FrontierPath works without it.

### With Claude (the intended way)

1. Add the skill to Claude. In Claude Code, copy `skills/syllabus-deadline-tracker/` into `.claude/skills/` (project) or `~/.claude/skills/` (personal). In the Claude apps, upload `dist/syllabus-deadline-tracker.skill` where Claude lets you add skills; the exact menu may change, so check Anthropic's current instructions.
2. Ask in plain language, for example:
   > Make me a tracker for the SSC CGL tier 1 exam on 2027-03-10. I can study 4 hours a day, Sundays off.
3. The skill then:
   - researches the exam (official notice, dates, pattern, marks, syllabus) and records its sources and the date it checked;
   - turns the syllabus into hour-weighted tasks with timed mock tests and a buffer, and checks the plan fits the deadline;
   - searches for free resources per topic, vets them (free, relevant, current, legitimate), and links only URLs it actually saw;
   - writes day-by-day lessons where it can do so accurately;
   - builds and checks the app, and delivers it (as a published page when Claude can publish one, otherwise as an HTML file).
4. Any exam or deadline works. If you already have the syllabus, paste it and the research step is skipped.

### Without Claude

Write a config and build it yourself. Needs Python 3.

```bash
python3 skills/syllabus-deadline-tracker/scripts/build_app.py my-config.json -o my-app.html
node skills/syllabus-deadline-tracker/scripts/smoke_test.js my-app.html   # optional render check
```

A minimal config:

```json
{
  "id": "my-exam",
  "title": "My Exam",
  "start": "2026-12-01",
  "deadline": "2027-02-28",
  "examName": "My Exam",
  "examDate": "2027-03-01",
  "hoursPerDay": 4,
  "maxHoursPerDay": 6,
  "bufferDays": 5,
  "offWeekdays": [0, 6],
  "theme": "midnight",
  "tasks": [
    {"title": "Topic one", "kind": "subject", "hours": 20, "hint": "[Free course](https://example.com)"},
    {"title": "Mock test 1", "kind": "gate", "hours": 3, "hint": "Timed past paper"}
  ]
}
```

The build script validates the config (unique task titles, lesson hours that sum to their task, dates in order), prints total hours, planning days and the required pace, and warns when the plan is infeasible, has lots of slack, or has few verified resource links. The full schema, including lessons, phases, sources, themes, background art and daily motivation entries, is in [`skills/syllabus-deadline-tracker/references/config.md`](skills/syllabus-deadline-tracker/references/config.md). The app's behaviour is described in `references/behaviour.md`, and the research and resource-vetting method in `references/research.md` and `references/resources.md`.

**Updating a published app:** keep the config's `id` and the task titles the same. On load the app re-syncs its task list by title, keeps your completed hours, and recomputes targets. Renaming a task resets its progress.

## The coach skill

`skills/physics-maths-mastery/` is a personal coaching skill for this exact plan. Once installed it responds to things like "what should I study tomorrow", "I missed three days", "compress my timeline", or "write the next module's syllabus". It holds the learner's constraints (free resources only, weekdays, about 6 hours a day), the roadmap, the scheduling rules, the lesson format, and the app source. It also covers gate tests, checkpoint reviews and, if you get near research-level material, rigorous brainstorming.

Its pace calculator can be run on its own:

```bash
python3 skills/physics-maths-mastery/scripts/pace.py --remaining 837 --deadline 2027-04-30 --from 2026-10-05
# Remaining 837 h, 140 planning days (buffer 10 kept free) to 2027-04-30
# Required pace 5.98 h/day vs plan 6 h/day -> on track
```

Useful options: `--hpd` (planned hours per day), `--max`, `--buffer`, `--off` (weekday numbers, 0 = Sunday), `--custom` (extra days off), `--shifts` (what-if weeks).

This skill is written for one learner, so adapt its constraints before reusing it for someone else.

## How the scheduling works

- A **work day** is any date that is not an off weekday and not an extra day off.
- **Planning days** are the work days from today to the deadline, minus the buffer.
- **Required pace** = remaining hours ÷ planning days. Each day's target is that pace in 15-minute steps, with remainders carried so the totals add up.
- Today's target is frozen when first opened, so it does not shift under you. Tomorrow's target reflects whatever happened today.
- Missed hours stay in the remaining total, so the required pace rises automatically. Finishing early lowers it.
- If the pace exceeds your maximum hours per day, the plan is **infeasible**. The app never silently changes the deadline or drops content; it offers a later deadline and you decide.

Worked example (also used as a test case in the spec): 600 h over 100 planning days is 6.00 h/day. After two missed days, 612 h over 98 days is 6.24 h/day. Extending to 108 planning days brings it to 5.67 h/day; shortening to 90 planning days raises it to 6.80 h/day, which is infeasible if your maximum is 6.5.

Full rules are in `skills/physics-maths-mastery/references/scheduling.md`.

## Design constraints

- **Free and private.** No paid APIs or services, no accounts, no analytics, no AI calls inside the apps. All logic, including rescheduling, is local and deterministic.
- **Single file.** Each app is one self-contained HTML file with no external scripts, fonts, images or network requests.
- **Local storage.** Progress is stored in the browser under the key `<id>.v1` (`frontierpath.v1` for FrontierPath). Clearing site data erases it, so use the backup text in Settings regularly.
- **Dates as calendar days.** Dates are handled as local calendar days rather than timestamps, to avoid timezone and daylight-saving bugs.

## Status and limitations

**What was checked.** `scripts/verify.sh` validates and builds the example configs, renders every screen of FrontierPath and the example app against a stub DOM, exercises the daily tick-box and its undo when run on a working day, and confirms that the app copy inside the coach skill and the packaged skills match their sources. During development it was also checked once, by hand and outside the script, that re-syncing a changed syllabus keeps completed hours. The apps have not been used in real browsers or on phones by hand, so expect rough edges.

**Known limitations**
- **Storage is per browser.** There is no sync between devices, and clearing site data loses progress unless you saved a backup.
- **Lessons are partial.** FrontierPath has lessons for its first four modules only. Later modules fall back to a resource list.
- **Resources age.** Links were checked when written. Some will break or change over time.
- **Generated trackers need checking.** If you use the generator skill on an exam or course, re-confirm dates, patterns and syllabus on the official site before relying on them.
- **No downloads or calendar export.** Backups are copy-and-paste text.

**Designed in the spec but not implemented yet**
- Per-task check boxes within a day
- Burn-up chart and a full Insights screen
- Drag a task to pin it to a date
- Pinning later checkpoints to fixed dates (they currently flow from the previous one)
- Adaptive time estimates
- Calendar (`.ics`) reminders and notifications
- An onboarding flow, and cross-device sync

## Next steps

1. Write day-by-day lessons for the remaining FrontierPath modules, starting with linear algebra.
2. Test the apps by hand in common browsers and on phones; fix what turns up.
3. Add the unimplemented features above, starting with per-task check boxes and a burn-up chart.
4. Write detailed tasks for Checkpoints 2 to 5 when you reach them, using your real pace from Checkpoint 1.

## How this was made

Designed and built in a long working session with Claude (Anthropic): the roadmap and app spec first, then the app, then the generator skill. The commit history is short because the repository was assembled from the finished files.

## License

Free for non-commercial use under the [PolyForm Noncommercial License 1.0.0](LICENSE.md): personal projects, study, research, hobby use, and use by charities, schools and public bodies. If you share this project or build on it, keep the `Required Notice` line from the license and credit GeniusDevam with a link to this repository.

Commercial use needs a separate licence. To arrange one, open an issue titled "Commercial licence" in this repository or contact [@GeniusDevam](https://github.com/GeniusDevam) on GitHub.
