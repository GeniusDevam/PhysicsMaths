#!/usr/bin/env python3
"""Pace calculator for the physics-maths-mastery plan.
Example: python pace.py --remaining 837 --deadline 2027-04-30 --from 2026-10-05 --buffer 10 --hpd 6 --max 8
Weekday numbers follow the app: 0=Sunday ... 6=Saturday (default off days: 0,6)."""
import argparse, datetime as dt, math

def day(s): return dt.date.fromisoformat(s)

ap = argparse.ArgumentParser()
ap.add_argument('--remaining', type=float, required=True, help='hours still to do')
ap.add_argument('--deadline', required=True)
ap.add_argument('--from', dest='start', default=dt.date.today().isoformat())
ap.add_argument('--buffer', type=int, default=10)
ap.add_argument('--hpd', type=float, default=6)
ap.add_argument('--max', type=float, default=8)
ap.add_argument('--off', default='0,6')
ap.add_argument('--custom', default='', help='comma-separated extra days off (YYYY-MM-DD)')
ap.add_argument('--shifts', default='-4,-2,2,4,8', help='what-if deadline shifts in weeks')
a = ap.parse_args()
off = {int(x) for x in a.off.split(',') if x != ''}
custom = {day(x) for x in a.custom.split(',') if x}

def is_work(d): return ((d.weekday() + 1) % 7) not in off and d not in custom

def work_days(s, e):
    out, d = [], s
    while d <= e:
        if is_work(d): out.append(d)
        d += dt.timedelta(days=1)
    return out

def pace(deadline):
    days = work_days(day(a.start), deadline)
    n = max(0, len(days) - a.buffer)
    return n, (0 if a.remaining <= 0 else (a.remaining / n if n else math.inf))

def nth_work_day(s, n):
    d, c = s, 0
    while True:
        if is_work(d):
            c += 1
            if c >= n: return d
        d += dt.timedelta(days=1)

dl = day(a.deadline)
n, P = pace(dl)
w = 7 - len(off)
status = ('infeasible (above max)' if P > a.max else 'behind' if P > a.hpd + 0.25
          else 'ahead' if P < a.hpd - 0.25 else 'on track')
print(f'Remaining {a.remaining:g} h, {n} planning days (buffer {a.buffer} kept free) to {dl}')
print(f'Required pace {P:.2f} h/day vs plan {a.hpd:g} h/day -> {status}')
print(f'Weekly average {P*w:.1f} h, monthly average {P*w*52/12:.1f} h')
ext = nth_work_day(day(a.start), math.ceil(a.remaining / a.hpd) + a.buffer)
print(f'Earliest deadline that fits {a.hpd:g} h/day: {ext}')
print('What if the deadline moved?')
for s in [x for x in a.shifts.split(',') if x]:
    d2 = dl + dt.timedelta(weeks=int(s)); n2, P2 = pace(d2)
    print(f'  {int(s):+d} weeks -> {d2}: {P2:.2f} h/day')
