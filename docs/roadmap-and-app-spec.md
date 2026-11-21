# Physics & Maths to the Frontier: Master Roadmap and Tracker App Spec

> **Note:** this is the original study plan and app design spec, written before the apps were built. The apps in `apps/` implement a subset of the spec; see the "Status and limitations" section of the top-level README for what is and is not implemented. Resource availability and exam-related details change over time, so verify links before relying on them.

*Prepared 4 October 2026. Sections 1–5 are the study plan: Checkpoint 1 (physics as it stood in the 1920s, 6–7 months) is detailed in sections 2–4, and the checkpoints that follow, toward the final goal, are in section 5. Section 6 is the toolkit. Sections 7–13 are the design spec for the progress-tracker app (design only; another agent will implement it).*

## 1. The final goal, and how this plan is structured

Your final goal is to learn physics and maths deeply enough to work on frontier problems: quantum gravity, string theory and a theory of everything, plus the Millennium Problems (Riemann Hypothesis, P vs NP, Yang–Mills mass gap, Navier–Stokes, Hodge conjecture, Birch and Swinnerton-Dyer). This document plans the whole journey as a chain of **checkpoints**. Physics as it stood in the 1920s is **Checkpoint 1**: a milestone on the way, not the destination.

**An honest picture of the distance.** Checkpoint 1 is a bounded project you can finish in 6–7 months. Getting to the point where you can read current research (Checkpoints 2–4) is more like 3–3.5 years of steady work at this pace. Making an original contribution to a Millennium Problem or a theory of everything cannot be scheduled, because nobody knows how long it takes or whether it can be done. This plan's job is to give you the strongest possible foundation and a real chance to try. Dates after Checkpoint 1 are estimates, and you re-plan at each checkpoint review.

**Checkpoints at a glance**

| # | Goal | Estimated duration | Running total |
| --- | --- | --- | --- |
| 1 | Physics as of the 1920s: classical foundations, quantum mechanics, special and general relativity | 7 months (target 6–7) | 7 months |
| 2 | Rigorous maths plus graduate-level quantum, statistical and electromagnetic physics | about 8 months | about 15 months |
| 3 | Quantum field theory, the Standard Model, advanced GR and cosmology | about 9 months | about 2 years |
| 4 | Frontier entry: string theory, supersymmetry, CFT, quantum gravity, and the maths behind the Millennium Problems | 12–18 months | about 3–3.5 years |
| 5 | Research frontier: choose a problem, read the literature, write, find mentors | open-ended | n/a |

**Starting point.** You have high-school single-variable calculus and basic classical physics, a few years rusty. Month 1 of Checkpoint 1 is a reboot. In week 1 you take a diagnostic, and any module you pass can be marked 'already know' in the app, which removes its hours.

**Three rules that decide success:**

1. At least half your hours go to solving problems, not watching videos.
2. A month-end mastery gate (≥70% on a timed self-test) before moving on. Failing adds review days, not shame.
3. Consistency beats intensity. The app's rescheduling exists so a bad day costs a few hours, not your motivation.

## 2. Checkpoint 1: time budget and daily rhythm

- **Window:** start Monday 5 Oct 2026, deadline Friday 30 Apr 2027 (30 weeks, about 7 months). The last two weeks are capstone and buffer, so on pace you finish the content in week 28 (about 6.5 months).
- **A 6-month version:** about 845 hours of work (content plus gates and capstone) fit into 26 weeks only at about 6.5 hours a day with no buffer. The app's compress feature shows the exact numbers before you commit.
- **Schedule:** Monday to Friday, about 6 hours a day (30 hours a week). Weekends are holidays. Both are configurable.
- **Daily template (6h):** 2h new material in the main module, 1.5h new material in the parallel module, 1.5h problem solving, 30 min Anki/spaced review, 30 min notes and error log. On Fridays, swap some new material for a weekly problem set, review and history reading.
- **Minimum viable day (2h):** on a bad day, do one problem block. It keeps the habit alive, and the app logs it as partial.
- **Method:** pause videos and predict the next step; attempt problems before reading solutions; keep an error log; explain each topic aloud in plain words; make Anki cards for definitions, key equations and derivation outlines.

**Hour budget** (30 weeks × 30 h = 900 h: about 765 content, about 80 for gates, review and capstone, and about 55 buffer):

| Subject | Depth | Hours |
| --- | --- | --- |
| Single-variable calculus completion + vectors | Core | 50 |
| Multivariable and vector calculus | Core | 50 |
| Linear algebra (including complex vector spaces) | Core | 60 |
| Complex numbers and functions | Compressed | 20 |
| Ordinary differential equations | Core | 30 |
| Fourier analysis and PDEs | Core | 35 |
| Probability and special functions | Compressed | 20 |
| Tensor calculus and differential geometry | Core | 40 |
| **Maths subtotal** |  | **305** |
| Newtonian mechanics refresh | Core | 30 |
| Oscillations and waves | Core | 15 |
| Electromagnetism | Core | 60 |
| Thermodynamics and statistical mechanics | Compressed | 30 |
| Lagrangian and Hamiltonian mechanics | Core | 45 |
| Special relativity | Core | 35 |
| Old quantum theory and key experiments | Core | 20 |
| Quantum mechanics | Core | 125 |
| General relativity and early cosmology | Core | 90 |
| History and primary sources | Survey | 10 |
| **Physics subtotal** |  | **460** |

*Depth key:* **Core** = full course depth with problem sets. **Compressed** = a focused lecture series, notes and selected problems. **Survey** = read and watch for orientation.

## 3. Checkpoint 1: month-by-month roadmap

**Month 1 (weeks 1–4): Reboot with calculus, vectors and Newtonian mechanics**

- Week 1: diagnostic using Khan Academy unit tests (Calculus 1 and 2, mechanics). Mark modules you clearly pass as 'already know'. Set up Anki, a notes system and Python (Harvard's CS50P covers the basics, about 10h spread over the first months).
- Maths: 3Blue1Brown *Essence of Calculus*, then MIT OCW 18.01SC for what you have not seen (integration techniques, sequences and series, Taylor series). Vectors, dot and cross products on Khan Academy. Start MIT 18.02SC (multivariable calculus).
- Physics: MIT 8.01 (Walter Lewin's lectures) or OpenStax University Physics Vol. 1: kinematics, Newton's laws, energy, momentum, rotation. Do the end-of-chapter problems.
- Gate 1.

**Month 2 (weeks 5–8): Multivariable calculus finished, linear algebra, oscillations and waves**

- Maths: finish 18.02SC (gradients, multiple integrals, line and surface integrals, Green/Stokes/divergence theorems). Linear algebra in full: 3Blue1Brown *Essence of Linear Algebra*, then MIT 18.06 (Gilbert Strang), with emphasis on eigenvalues, orthogonality, complex vector spaces, Hermitian matrices and diagonalisation (the language of quantum mechanics). Complex numbers and Euler's formula begin (Khan Academy).
- Physics: simple harmonic motion, damped and driven oscillations, the wave equation (selected lectures from MIT 8.03).
- Gate 2.

**Month 3 (weeks 9–12): ODEs, complex numbers, electromagnetism**

- Maths: ODEs via MIT 18.03SC and 3Blue1Brown's differential equations series; finish complex numbers (early lectures of MIT 18.04, or the free text by Beck et al., *A First Course in Complex Analysis*); start Fourier series with 3Blue1Brown's Fourier videos.
- Physics: MIT 8.02 (Lewin) and the Feynman Lectures Vol. II (free online): electrostatics, Gauss's law, potential, circuits, magnetism, induction, Maxwell's equations and electromagnetic waves. Tong's Electromagnetism notes as a stretch. Notice how Maxwell's equations hint at relativity.
- Gate 3.

**Month 4 (weeks 13–16): Fourier analysis and PDEs, probability, thermal physics, Lagrangian mechanics begins**

- Maths: finish Fourier series and transforms (Steve Brunton's Fourier/PDE lectures); wave, heat and Laplace equations by separation of variables (late units of 18.03SC); basic probability and distributions (Khan Academy, selected MIT 18.05 lectures).
- Physics: thermodynamics and statistical mechanics up to the Boltzmann distribution, equipartition and the black-body radiation problem (Susskind's *Statistical Mechanics*, selected Tong notes, Feynman Vol. I). Begin analytical mechanics: calculus of variations and the Euler–Lagrange equations (Susskind's *Classical Mechanics*, Tong's Classical Dynamics notes).
- Gate 4. Friday history reading starts this month.

**Month 5 (weeks 17–20): Hamiltonian mechanics, special relativity, the old quantum theory**

- Physics: finish analytical mechanics (Noether's theorem, Hamilton's equations, Poisson brackets, which become quantum commutators). Special relativity: Michelson–Morley, Lorentz transformations, spacetime diagrams, four-vectors, relativistic energy and momentum (Susskind's *Special Relativity and Classical Field Theory*, Feynman Vol. I, MIT 8.033 problems, and Einstein's *Relativity: The Special and General Theory*, free on Project Gutenberg). Old quantum theory: Planck's radiation law, the photoelectric effect, Compton scattering, the Bohr atom, de Broglie waves, Davisson–Germer, Stern–Gerlach (first lectures of MIT 8.04, Feynman Vol. III opening chapters).
- Maths: special functions the quantum mechanics needs (Legendre, Hermite, spherical harmonics), learned just in time. Wave mechanics begins: the Schrödinger equation.
- Gate 5.

**Month 6 (weeks 21–24): Quantum mechanics completed, tensors begin**

- Quantum mechanics: wells, tunnelling, the harmonic oscillator and hydrogen atom; Hilbert space and Dirac notation; Heisenberg's matrix mechanics as the equivalent formulation; commutators and the uncertainty principle; angular momentum and spin (Pauli matrices); identical particles and the exclusion principle; basic perturbation theory; a survey of the Dirac equation (1928). Resources: Susskind's *Quantum Mechanics*, MIT 8.04 and selected 8.05 lectures (Zwiebach), Tong's QM notes, Feynman Vol. III.
- Maths: start tensor calculus with eigenchris *Tensors for Beginners* and *Tensor Calculus*.
- Gate 6.

**Month 7 (weeks 25–28): Differential geometry and general relativity**

- Maths: finish tensors (metric, covariant derivative, Christoffel symbols, geodesics, Riemann and Ricci curvature) with Sean Carroll's free GR lecture notes; Frederic Schuller's lectures as a stretch.
- Physics: the equivalence principle, curved spacetime, the Einstein field equations, the Schwarzschild solution, the classic tests (Mercury's perihelion, 1919 eclipse light bending, gravitational redshift), weak-field gravitational waves (survey), and early cosmology (Friedmann 1922, Lemaître 1927, Hubble 1929). Use Susskind's *General Relativity* and *Cosmology*, Tong's GR notes and MIT 8.286 (Alan Guth) for the cosmology.
- Gate 7.

**Weeks 29–30: capstone, buffer and Checkpoint 1 review.** Pick two capstones: (1) simulate Mercury's perihelion precession or light bending in Python using Schwarzschild geodesics; (2) solve the 1D Schrödinger equation numerically for several potentials and compare with the analytic results; (3) write 'The 1900–1930 story, explained to my past self' (about 3,000 words) and record a 20-minute talk. Any slipped work lands here too. Then run the checkpoint review (section 10): compare actual versus planned hours, and re-plan Checkpoint 2.

## 4. Checkpoint 1 checklist: how you know you have a firm grip

Use these as gate questions. If you can do the item cold, on paper, the module is done.

| Area | You can… |
| --- | --- |
| Mechanics | derive the equations of motion of a double pendulum from a Lagrangian; write Hamilton's equations; explain how energy conservation follows from Noether's theorem |
| Electromagnetism | use Gauss's and Ampère's laws on symmetric setups; derive the wave equation from Maxwell's equations and the speed of light |
| Thermal physics | derive the Boltzmann distribution; explain equipartition and why classical physics fails for black-body radiation |
| Special relativity | solve time dilation, length contraction and velocity-addition problems; use four-vectors and energy–momentum conservation in collisions |
| Quantum mechanics | solve the infinite well, the oscillator and hydrogen's energy levels; compute commutators; predict spin-1/2 measurement sequences; explain the Born rule and the uncertainty principle |
| General relativity | compute Christoffel symbols for a simple metric; write the geodesic equation; derive light bending and perihelion precession in the Schwarzschild metric; state the Friedmann equations |
| History | give a dated timeline: Planck 1900, Einstein 1905, Bohr 1913, general relativity 1915, Eddington's eclipse 1919, de Broglie 1924, Heisenberg and Pauli 1925, Schrödinger and Born 1926, uncertainty and the Solvay conference 1927, Hubble 1929 |

## 5. Checkpoints 2–5: the road to the frontier

*These are estimates. At the end of each checkpoint, run the review (section 10): compare actual with planned hours, pick the next branch, adjust hours per day, then let the app generate the next checkpoint's tasks. Free-resource availability changes, so verify links when you get there.*

**Checkpoint 2: rigorous foundations and graduate-level physics (about 8 months, about 1,000 h)**

- Maths (about 550 h): real analysis (MIT 18.100, Trench's free *Introduction to Real Analysis*); linear algebra at proof level (Hefferon's free *Linear Algebra*); abstract algebra (Matthew Macauley's lectures, MIT 18.701); point-set topology (MIT 18.901); complex analysis in full (MIT 18.04); manifolds and differential forms (Schuller's lectures); measure and probability basics (Terence Tao's free 245A notes).
- Physics (about 450 h): graduate-level quantum mechanics (MIT 8.05 and 8.06, Tong's *Topics in Quantum Mechanics* and *Applications of Quantum Mechanics*: perturbation theory, scattering, density matrices); electrodynamics and radiation (MIT 8.07, Tong); full statistical physics (MIT 8.044, Kardar's MIT 8.333); classical field theory and relativistic wave equations (Susskind, Tong).
- Gate: prove standard theorems on paper (Cauchy's theorem, Lagrange's theorem, Heine–Borel) and solve graduate problem sets at ≥70%.

**Checkpoint 3: quantum field theory, the Standard Model, advanced GR (about 9 months, about 1,150 h)**

- Quantum field theory: Tong's QFT notes, Sidney Coleman's Harvard lectures (YouTube, with typed-up notes on arXiv), Srednicki's free textbook draft; the Standard Model and gauge theory (Tong's notes); Lie groups and representations.
- Gravity and cosmology: Carroll's GR notes, Harvey Reall's Cambridge black-hole notes, Baumann's and Tong's cosmology notes.
- Maths: functional analysis (MIT 18.102), fibre bundles and the geometry of gauge theory (Schuller), algebraic topology begins (Hatcher's free book).
- Gate: compute tree-level scattering amplitudes, derive the Higgs mechanism, derive the Schwarzschild and expanding-universe results, and outline cosmological perturbations.

**Checkpoint 4: frontier entry (12–18 months, about 1,500–2,300 h)**

Choose a branch first, or alternate in blocks. The app lets you split this checkpoint into a physics part and a maths part.

- Physics branch: supersymmetry (Martin's *Supersymmetry Primer* on arXiv); conformal field theory (Ginsparg's notes on arXiv); string theory (Tong's notes, Zwiebach's MIT 8.251, then Polchinski or Becker–Becker–Schwarz if you can access them); AdS/CFT (McGreevy's and Maldacena's lecture notes on arXiv); black-hole information (Harlow's lectures on arXiv); loop quantum gravity for contrast (Rovelli's introductory papers). The theory of everything and quantum gravity are research programmes rather than single problems, so this checkpoint is about understanding their motivations, tools and open issues.
- Maths branch, by problem:

| Problem | Core prerequisites | Free starting points |
| --- | --- | --- |
| P vs NP | algorithms, logic, complexity | MIT 18.404 and 6.045, the Arora–Barak draft, Aaronson's survey. The most accessible entry; consider starting it as a side thread during Checkpoint 2 |
| Riemann Hypothesis | complex analysis, analytic number theory | Checkpoint 2 complex analysis, then free analytic number theory lecture notes, Terence Tao's blog, Keith Conrad's notes; Bombieri's Clay description |
| Yang–Mills mass gap | QFT, gauge theory, differential geometry, functional analysis | Checkpoint 3 material, then the constructive QFT literature; Jaffe and Witten's Clay description |
| Navier–Stokes | PDE, functional analysis, fluid dynamics | MIT 18.152, Tong's fluid mechanics notes, Tao's blog; Fefferman's Clay description |
| Birch and Swinnerton-Dyer | elliptic curves, algebraic number theory | MIT 18.783, Milne's free notes; Wiles's Clay description |
| Hodge conjecture | algebraic geometry, complex manifolds, algebraic topology | Vakil's *Rising Sea* notes, Hatcher; Deligne's Clay description |

**Checkpoint 5: research frontier (open-ended)**

Narrow to a specific question. Read arXiv regularly, write expository notes, work through lists of open problems, take part in communities (MathOverflow, Physics Stack Exchange, recorded seminars), and contact researchers. Original results in these areas usually come from people with years of specialised training, and a formal graduate programme is the usual route. The tracker will keep your progress honest either way.

## 6. Study toolkit

- **Tools:** Anki (spaced repetition), Obsidian or a paper notebook with an error log, Python with Jupyter/NumPy/SymPy/Matplotlib, LaTeX via Overleaf, Desmos or GeoGebra.
- **Resource hubs:** MIT OpenCourseWare, Class Central (search and audit-mode edX/Coursera courses), Khan Academy, Stanford's Susskind Theoretical Minimum, Harvard CS50P, Tong's lecture notes, 3Blue1Brown, the Feynman Lectures online. Brilliant has limited free content, so treat it as optional; Learn Anything is handy for finding curated link lists.
- **Primary sources:** search archive.org and Wikisource for English translations of key papers (Einstein 1905 and 1915–16, Bohr 1913, de Broglie 1924, Heisenberg 1925 and 1927, Schrödinger 1926). Availability varies, so treat them as enrichment, not required reading.
- **Discipline:** choose one primary source per topic and finish it. Collecting playlists is not learning.

## 7. App overview and goals

Working title: **FrontierPath** (rename freely). A personal, offline-first planner that turns a content roadmap plus a deadline into daily, weekly and monthly targets, and rebalances automatically when life happens.

**Goals**

1. Generate concrete daily, weekly and monthly targets from the roadmap and the deadline.
2. One-tap daily check-in: tick 'I hit today's target'. If it is not ticked, the plan rebalances.
3. Change the deadline (or hours per day, or days off) at any time. All targets recalculate, with a preview before committing.
4. Honest progress: percent complete, projected finish date, ahead/behind status.
5. Free, private, works offline, no account.

**Long-horizon journey (core requirement):** the plan is a chain of checkpoints toward the final goal of frontier physics and maths. Checkpoint 1 (1920s physics, 6–7 months) is the first of five. Each checkpoint has its own deadline, targets and gate. Only the active checkpoint is scheduled day by day; later checkpoints are provisional and are projected at weekly and monthly granularity. A slip or a deadline change in one checkpoint must visibly shift the projected dates of the later ones.

**Non-goals (v1):** hosting course content (it links out), social features, native apps, accounts or cloud sync.

## 8. Recommended stack (implementer may substitute)

- Installable, mobile-first PWA that works offline. TypeScript; React or Svelte; IndexedDB via Dexie; Vite PWA plugin; Recharts or Chart.js; date-fns; Vitest for tests.
- Free hosting (GitHub Pages or Cloudflare Pages). Backup via JSON export/import. Sync can come later.
- The scheduler is a pure TypeScript module with no UI or storage imports, so it is easy to test.
- Store dates as local calendar strings (YYYY-MM-DD), never timestamps, to avoid timezone and DST bugs.

**Free-only rule (hard requirement for v1)**

- No paid APIs, SDKs or services, and no AI/LLM calls inside the app. All logic, including rescheduling, is local deterministic code.
- No backend, accounts or server database. All data lives on the device (IndexedDB), so there are no running costs and no free-tier limits to hit.
- Host the built files on a free static host (GitHub Pages or Cloudflare Pages free tier). A free subdomain is enough.
- Use only open-source libraries (MIT, Apache or BSD licences). Use system fonts or self-hosted open-licence fonts. No paid icon sets, maps, analytics or tracking.
- Reminders: browsers cannot reliably fire scheduled notifications while the app is closed without a push server. So the app shows an on-open check-in prompt, optional notifications while it is open, and exports recurring daily and weekly reminders as an .ics file that you import into Google Calendar or your phone's calendar (free).
- Data safety: request persistent storage (navigator.storage.persist) so the browser does not evict the data, and show a weekly 'download backup' prompt that saves the JSON export to the device.
- If cross-device sync is ever added, it must be optional and use a free tier only. The app must work fully without it.

## 9. Data model

- **Settings:** startDate, masterTargetDate (optional, for the final goal), dailyHours (default 6), maxDailyHours (default 8), offWeekdays (default Sat, Sun), customOffDays (dates and ranges), bufferDays (default 10 working days at the end), catchUpPolicy (even-spread | buffer-first | use-weekend), trackMix (default maths 40% / physics 60%), planMode (even-pace | front-load), adaptiveEstimates (bool), reminderTime.
- **Module:** id, title, checkpointId, track (maths | physics | history | gate | capstone), order, description.
- **Task:** id, moduleId, title, estHours (sized 1–3h so replanning is fine-grained), tier (core | stretch | optional), prerequisiteIds, resources \[title, url, kind: video | notes | book | problems\], status (todo | in-progress | done | skipped), hoursLogged, completedOn, pinnedDate (optional manual override).
- **Gate:** id, moduleIds, passThreshold (70%), attempts \[date, scorePct\]. A failed attempt injects review tasks before the next module.
- **DayRecord:** date, kind (work | off), plannedHours, slices \[taskId, hours\], targetAchieved (bool), hoursLogged, status (pending | achieved | partial | missed | excused), note.
- **EventLog (append-only):** taskCompleted, dayChecked, dayMissed, deadlineChanged, settingsChanged, gateAttempted. Powers undo and lets the app explain why any target changed.

* **Checkpoint:** id, title, order, status (active | upcoming | done), deadline, deadlineMode (fixed | flowing), bufferDays, plannedHours, provisional (true until the checkpoint is activated and broken into tasks), gateId (the checkpoint exam), reviewNotes. A fixed deadline is a date the user chose. A flowing deadline is derived: it starts when the previous checkpoint ends and lasts plannedHours ÷ pace. Every Module and Task belongs to exactly one checkpoint through checkpointId.

**Core rule:** past DayRecords are history and are never rewritten by the scheduler. Future days are always derived. Daily, weekly and monthly targets are never stored as authoritative values; they are computed from remaining work and remaining working days.

## 10. Scheduling engine (the heart of the app)

**Definitions**

- Working day: a date between today and the active checkpoint's deadline that is not an off weekday and not a custom day off.
- Planning days: working days minus the last bufferDays (the buffer is unscheduled slack).
- R (remaining hours): the sum of (estHours − hoursLogged) over incomplete in-scope tasks. Scope is all core tasks plus any stretch/optional tasks the user keeps.
- P (required pace): R divided by the number of remaining planning days.

**Rules**

1. **Even-pace mode (default):** each remaining planning day's target is P hours, rounded to 15 minutes with remainders carried forward so totals are preserved. Front-load mode fills each day to dailyHours until work runs out.
2. **Filling a day:** take tasks from the ordered queue (topological order by prerequisites, interleaved by trackMix). A task may be split across days. Pinned tasks take their day first.
3. **Weekly target:** the sum of that week's day targets plus the module milestone due. **Monthly target:** per calendar month, listing modules to finish and the gate.
4. **Feasibility:** if P exceeds maxDailyHours the plan is infeasible. Show options with exact numbers: (a) extend the deadline to date X, the earliest date where P ≤ dailyHours; (b) raise hours per day to Y; (c) defer these stretch/optional tasks, lowest priority first. Never change the deadline or scope without confirmation.
5. **Missed day:** on first open after a work day ends (or when the user taps 'End day'), an unticked day becomes a prompt: Done late / Partial (enter hours) / Missed / Excused (sick or travel, converted to a holiday). Missed and unfinished slices return to the queue and the plan regenerates from today forward, so P rises automatically.
6. **Catch-up policy:** even-spread (default) spreads the extra over all remaining days; buffer-first shifts work into buffer days before raising P; use-weekend schedules catch-up on off days. No day may exceed 125% of its normal target unless the user allows it. If that cap blocks the plan, report the new projected finish date instead.
7. **Ahead of schedule:** finishing tasks early lowers R, so targets shrink automatically. Show 'ahead by N days' and offer 'keep pace' or 'lighter days'.
8. **Changing deadline, hours or days off:** show a live preview (before → after for daily, weekly and monthly targets and remaining buffer), then Confirm. Only future days change.
9. **Gates:** a score below 70% inserts review tasks, which raises R. It is just another reschedule.
10. **Adaptive estimates (optional):** velocity = actual hours ÷ estimated hours over the last 10 completed tasks, applied to remaining estimates.
11. **Determinism:** plan = f(settings, tasks, history, today). The same input always yields the same output.

**Pseudocode**

```
function buildPlan(state, today):
  days = workingDays(today, state.deadline, state.offWeekdays, state.customOffDays)
  planDays = dropLast(days, state.bufferDays)
  if planDays is empty: return Infeasible(reason = NO_DAYS)
  queue = orderTasks(incompleteTasks(state), state.trackMix)   # respects prerequisites
  R = sum(remainingHours(t) for t in queue)
  P = R / length(planDays)
  if P > state.maxDailyHours:
    return Infeasible(extendTo = earliestDeadlineFor(R, state), raiseTo = P, defer = lowestPriorityTasksToCut(R, state))
  for day in planDays:
    budget = P - hours(pinnedTasks(day))      # front-load mode uses dailyHours
    day.slices = pinnedSlices(day) + takeHours(queue, budget)   # may split a task
  return Plan(planDays, weekly = groupByWeek(planDays), monthly = groupByMonth(planDays), projectedFinish = lastDayWithWork(planDays))
```

**Worked example (use as a unit test).** 600h remaining over 100 planning days gives 6.00 h/day. Two missed days leave 612h over 98 days, which is 6.24 h/day. Extending the deadline to 108 planning days gives 5.67 h/day. Shortening to 90 planning days gives 6.80 h/day; if maxDailyHours is 6.5, the plan is infeasible and the engine offers: extend to 102 planning days (612 ÷ 6), or raise hours to 6.8, or defer tasks.

**Compressing or extending the timeline**

- **Where:** Settings → Deadline, plus quick buttons 'Extend by N weeks' and 'Compress by N weeks' on the Today and Plan screens. Hours per day and days off use the same flow.
- **Extend (later deadline):** more planning days, so P drops. The preview shows the new daily, weekly and monthly targets, for example 6.24 → 5.67 h/day. The user then picks 'Lighter days' (lower the pace) or 'Add stretch content' (keep the pace and add optional tasks).
- **Compress (earlier deadline):** fewer planning days, so P rises. Up to dailyHours it applies directly. Between dailyHours and maxDailyHours it applies with a warning ('this needs 6.8 h/day'). Above maxDailyHours it is infeasible, and the engine proposes a scope trim: first defer optional tasks, then stretch tasks, then (with explicit confirmation) Compressed-depth modules, showing the exact hours cut and the resulting pace. Core tasks are never cut automatically.
- **What-if view:** a small table of candidate deadlines (−4, −2, +2, +4, +8 weeks) with the required hours per day for each, without committing anything.
- **After confirming:** targets update everywhere at once (Today, Plan, Roadmap, Insights). Past days are untouched, the change is logged as a deadlineChanged event, and a one-tap Undo restores the previous settings.
- **Month boundaries:** monthly targets are per calendar month, so partial first and last months are pro-rated.

**Planning across checkpoints**

- **Detail levels:** the daily scheduler (buildPlan, above) runs on the active checkpoint only; in the pseudocode, state.deadline means the active checkpoint's deadline. Upcoming checkpoints are projected by a separate pure function, projectJourney, using hours only: remaining plannedHours ÷ recent average pace (trailing 14-day actual, falling back to dailyHours), converted to working days with the same calendar.
- **Fixed versus flowing deadlines:** Checkpoint 1 is fixed (default Friday 30 Apr 2027). Later checkpoints default to flowing, so a slip in Checkpoint 1 pushes their projected start and end dates automatically. The user can pin any checkpoint to a fixed date; then, instead of its dates moving, the app reports the pace that checkpoint would now need.
- **Cascade preview:** changing any checkpoint's deadline or hours per day shows a journey preview: each later checkpoint's projected start and end, before → after, plus the status of the master target date. Confirm applies it.
- **Provisional checkpoints:** their tasks are not generated until they activate. Until then they hold module-level hour estimates that the user may edit.
- **Checkpoint review (on completion or at the deadline):** a short wizard covering the gate result, actual versus planned hours per module (velocity), carry-over of unfinished tasks (move into the next checkpoint or drop), the choice of branch where one exists (for example physics-first or maths-first in Checkpoint 4), a check of hours per day, and then generation of the next checkpoint's tasks from its template.
- **Unfinished work at a deadline:** the engine never silently extends a fixed deadline. It offers: extend by N working days (showing the cascade), carry the leftover tasks into the next checkpoint, or defer them.
- **Worked example (unit test):** Checkpoint 2 has 1,000h planned at 6 h/day with a flowing deadline, so it takes about 167 working days. If Checkpoint 1 slips by 10 working days, Checkpoint 2's projected start and end both move by 10 working days. If Checkpoint 2 is pinned instead, its required pace rises accordingly.

## 11. Screens and interactions

- **Today (home):** date, a status chip ('On track', '2 days behind', 'Ahead 1 day'), and projected finish versus deadline. Shows today's target in hours and a checklist of task slices (title, hours, resource link buttons, per-slice checkbox). A large **'I hit today's target'** checkbox ticks every slice and can be undone. Also: log hours, a note field, 'Re-plan today' and 'Take a day off'. Weekends and holidays show a calm rest-day view with a preview of the next working day and no guilt messaging.
- **Plan:** week and month calendar. Off days are shaded; each day shows its target and tasks, coloured by status. Drag a task to another day to pin it. A 'Why did this change?' panel reads from the event log.
- **Roadmap:** tree of track → module → task with progress bars. Toggle core/stretch/optional tiers (this changes scope and recomputes the plan). Gate cards with score entry. Edit task hours and resources, add or remove tasks.
- **Insights:** burn-up chart (scope, completed, ideal, projected), weekly hours bars, streak (off days never break it), hours by track, estimate accuracy, and a forecast finish date from the trailing 14-day average pace.
- **Settings:** deadline, hours per day, off weekdays, custom days off (range picker), buffer, catch-up policy, track mix, reminders, import/export, reset. Any change that affects the plan goes through the preview-and-confirm dialog.
- **Onboarding:** set start date and deadline (default about 30 May 2027), hours per day and days off; load the seed roadmap; optionally mark modules as 'already know' to remove their hours from R.
- **Reminders (in-app prompts and .ics calendar export):** an evening 'Did you hit today's target?', a Friday weekly review, and a Monday preview.

* **Journey (new tab):** a horizontal timeline of the checkpoints with status (done, active, upcoming), start and end dates (fixed dates marked with a pin), hours remaining, and overall progress toward the final goal. Tapping a checkpoint shows its modules; tapping an upcoming one lets the user edit its provisional estimates or pin its date. It shows the master target date status ('on track', 'N weeks late').
* **Today and Roadmap:** show the active checkpoint's name in the header chip and the progress summary. Insights adds a journey-level burn-up chart.
* **Checkpoint review wizard:** as described in section 10; also launchable manually from the Journey tab.

## 12. Edge cases

- **Away for days:** on reopen, prompt once for the whole gap: mark as missed, vacation, or done offline.
- **Retroactive check-ins:** allowed for recent days, always logged as events.
- **Invalid deadlines:** a deadline before today, or one leaving zero working days, is blocked with a clear message.
- **New holidays added later:** future targets recompute.
- **Out-of-order tasks:** allowed; unmet prerequisites only warn.
- **Estimate edits mid-task:** change R, never history.
- **Tiny remainders (under 15 min):** roll to the next day.
- **Timezone and DST changes:** handled by local date strings.
- **Everything finished early:** show completion and offer stretch content.

* **Checkpoint finished early:** offer to activate the next checkpoint immediately, or to spend the spare time deepening weak modules.
* **Moving modules between checkpoints:** allowed in the Roadmap editor; hours move with the module and the journey projection recomputes.
* **Adding, splitting or removing a checkpoint:** allowed (for example splitting Checkpoint 4 into a physics part and a maths part).
* **Long breaks (exams, travel, illness):** a 'pause journey' option adds a custom off range and shifts all flowing deadlines.
* **Lost browser data mid-journey:** the journey may last years, so the weekly backup prompt matters more; offer an annual full export as well.

## 13. Seed roadmap, build order and acceptance tests

**Seed template.** Convert section 3 into an importable, versioned JSON template: one module per course or topic, each split into 1–3h tasks with real links, tier, track and prerequisites. Task hours must sum to the section 2 budget (about 765h content plus about 80h gates, review and capstone, for Checkpoint 1). Users can edit and re-import it.

**Journey template.** The same template file also contains Checkpoints 2–5 as provisional modules with hour estimates taken from section 5, and no tasks yet. When a checkpoint is activated, a template update supplies its detailed tasks; the implementer does not need to author them up front. The importer must therefore accept a template that adds tasks to an existing provisional checkpoint without disturbing progress elsewhere.

**Suggested build order**

1. Scheduler library with unit tests (including the worked example).
2. Storage layer and event log.
3. Today screen and check-in flow.
4. Settings with preview and confirm.
5. Plan and Roadmap screens.
6. Insights.
7. PWA install, offline mode, reminders and .ics export.
8. Seed template and onboarding.

Note: build the checkpoint model and the pure projectJourney function, with unit tests, immediately after step 1, since the Journey tab and the cascade preview depend on them.

**Acceptance criteria**

- Changing the deadline recalculates all future daily, weekly and monthly targets within a second, shows a preview first, and leaves past days untouched.
- An unticked work day triggers the prompt, and unfinished hours return to the queue and spread per the catch-up policy.
- The worked example numbers reproduce exactly.
- Weekends and custom days off never receive targets, and never break streaks.
- Scheduled hours across planning days equal R (within 15 minutes).
- An infeasible plan shows its options and changes nothing until the user confirms.
- The app works fully offline, and export followed by import restores identical state.
- Identical inputs always produce identical plans.

* Changing Checkpoint 1's deadline shows a journey preview, and on confirm shifts every flowing later checkpoint by the right number of working days.
* A pinned checkpoint does not move; the app shows its required pace instead.
* Completing a checkpoint launches the review wizard and activates the next one; unfinished tasks are carried over only with the user's confirmation.
* Provisional checkpoints never produce daily targets.

**Later ideas (v2):** auto-generated spaced-review tasks, a Pomodoro timer, optional sync via a free tier (never required), a reading-group mode.
