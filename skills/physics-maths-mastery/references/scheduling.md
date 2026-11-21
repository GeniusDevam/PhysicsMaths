# Scheduling reference

## Definitions
- Work day: a date not on an off weekday (default Saturday and Sunday) and not a custom day off.
- Planning days: work days from today to the active checkpoint's deadline, minus the last `buffer` days (default 10 work days; the buffer is unscheduled slack).
- R: remaining hours = sum of (hours - hours done) over incomplete in-scope tasks.
- P (required pace) = R / planning days. Daily target = P, rounded to 15 minutes with remainders carried so totals are preserved.
- Weekly average = P x work days per week. Monthly average = weekly x 52/12.
- Status: ahead if P < plan - 0.25 h/day; on track within +/- 0.25; behind if P > plan; infeasible if P > max hours per day (default 8).

## Rules
1. **Missed days**: unfinished hours return to the remaining total, so P rises automatically. Catch-up policy: spread evenly over remaining days (default); use the buffer first; or use weekends if the learner opts in. No day exceeds 125% of its normal target unless the learner agrees.
2. **Infeasible**: offer (a) extend the deadline to the earliest date where P is at most the planned hours (the n-th work day with n = ceil(R / planned hours) + buffer), (b) raise hours per day to P, (c) defer stretch or optional tasks (lowest priority first; compressed modules only with explicit consent). Core content is never dropped automatically. Never change the deadline without confirmation.
3. **Ahead**: targets shrink; offer "keep pace and finish early" or "lighter days".
4. **Compress or extend**: show a before/after table (planning days, daily, weekly, monthly) and a what-if table (-4, -2, +2, +4, +8 weeks). Past days are history; only future days change. Up to planned hours: apply. Between planned and max: apply with a warning. Above max: infeasible, propose a scope trim.
5. **Journey**: only the active checkpoint is planned day by day. Later checkpoints are projected from hours at the planned pace. A fixed deadline is a chosen date; a flowing deadline starts when the previous checkpoint ends. A slip in one checkpoint shifts every flowing later one; a pinned one reports its required pace instead.
6. **Gates**: below 70% inserts review tasks, which raises R. It is just another reschedule.
7. **Checkpoint review** (at completion or deadline): gate result; actual versus planned hours per module (velocity); carry-over (move or drop); branch choice where one exists; hours-per-day check; then write the next checkpoint's syllabi.
8. **Bad day**: a 2-hour minimum viable day (one problem block) keeps the habit; log it as partial.

## Worked examples (unit-test these)
- 600 h over 100 planning days = 6.00 h/day. Two missed days leave 612 h over 98 days = 6.24 h/day. Extending to 108 planning days = 5.67 h/day. Shortening to 90 planning days = 6.80 h/day; with max 6.5 it is infeasible and the options are: extend to 102 planning days (612 / 6), raise hours to 6.8, or defer tasks.
- Checkpoint 2: 1,000 h at 6 h/day (flowing) takes about 167 work days. If Checkpoint 1 slips by 10 work days, Checkpoint 2's projected start and end both move by 10 work days.
- Checkpoint 1 default: about 837 h (770 content + 42 gates + 25 capstone) over 140 planning days = 5.98 h/day.

Use `scripts/pace.py` instead of hand arithmetic.
