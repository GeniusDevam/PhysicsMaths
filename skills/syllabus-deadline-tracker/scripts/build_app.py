#!/usr/bin/env python3
"""Build a syllabus tracker app from a config JSON.
Usage: python build_app.py config.json -o app.html [--template ../assets/template.html]
Validates the config, prints a feasibility summary, and injects the config into the template."""
import argparse, datetime as dt, json, math, os, sys

ap = argparse.ArgumentParser()
ap.add_argument('config'); ap.add_argument('-o', '--out', required=True)
ap.add_argument('--template', default=os.path.join(os.path.dirname(__file__), '..', 'assets', 'template.html'))
a = ap.parse_args()
cfg = json.load(open(a.config, encoding='utf-8'))
errs, warns = [], []
for k in ('title', 'start', 'deadline', 'tasks'):
    if k not in cfg: errs.append(f'missing required key: {k}')
if errs: sys.exit('\n'.join(errs))
try: start, dl = dt.date.fromisoformat(cfg['start']), dt.date.fromisoformat(cfg['deadline'])
except ValueError as e: sys.exit(f'bad date: {e}')
if dl <= start: errs.append('deadline must be after start')
titles = [t.get('title') for t in cfg['tasks']]
if len(set(titles)) != len(titles): errs.append('task titles must be unique (they are used as keys)')
for t in cfg['tasks']:
    if not t.get('title') or not isinstance(t.get('hours'), (int, float)) or t['hours'] <= 0:
        errs.append(f'task needs a title and positive hours: {t}')
hours = {t['title']: t['hours'] for t in cfg['tasks'] if t.get('title')}
for name, ls in (cfg.get('lessons') or {}).items():
    if name not in hours: errs.append(f'lessons key not a task title: {name}'); continue
    tot = sum(l[1] for l in ls)
    if abs(tot - hours[name]) > 0.01: errs.append(f'lessons for "{name}" sum to {tot} h but the task is {hours[name]} h')
    if any(len(l) != 4 for l in ls): errs.append(f'every lesson needs [title, hours, description, resources]: {name}')
if cfg.get('theme', 'midnight') not in ('midnight', 'paper', 'forest', 'cosmic'): errs.append('theme must be midnight, paper, forest or cosmic')
off = set(cfg.get('offWeekdays', [0, 6])); custom = {dt.date.fromisoformat(x) for x in cfg.get('daysOff', [])}
if cfg.get('examDate'):
    try:
        if dl > dt.date.fromisoformat(cfg['examDate']): errs.append('deadline must not be after examDate')
    except ValueError: errs.append('bad examDate')
for src in cfg.get('sources', []):
    if len(src) < 2 or not str(src[1]).startswith(('http://', 'https://')): errs.append(f'source must be [label, http(s) url, note?]: {src}')
if cfg.get('sources') and not cfg.get('verifiedOn'): warns.append('sources given but verifiedOn (date you checked them) is missing')
if len(off) > 5: errs.append('offWeekdays can list at most 5 days')
if errs: sys.exit('CONFIG ERRORS:\n  ' + '\n  '.join(errs))
days, d = [], start
while d <= dl:
    if ((d.weekday() + 1) % 7) not in off and d not in custom: days.append(d)
    d += dt.timedelta(days=1)
buf = cfg.get('bufferDays', 10); plan = max(0, len(days) - buf); total = sum(hours.values())
hpd = cfg.get('hoursPerDay', 6); mx = cfg.get('maxHoursPerDay', 8); P = total / plan if plan else math.inf
print(f'{len(cfg["tasks"])} tasks, {total:g} h total; {len(days)} work days, {plan} planning days (buffer {buf})')
print(f'Required pace {P:.2f} h/day vs plan {hpd} (max {mx}); lessons for {len(cfg.get("lessons") or {})} of {len(hours)} tasks')
if P > mx: warns.append('INFEASIBLE as configured: trim scope, extend the deadline, or raise hours per day')
elif P > hpd + .25: warns.append('behind the planned pace from day one: consider trimming or extending')
elif P < hpd * .6: warns.append('plenty of slack: consider adding content or reducing hours per day')
res = [l[3] for ls in (cfg.get('lessons') or {}).values() for l in ls] + [x.get('hint', '') for x in cfg['tasks']]
linked = sum('](http' in r for r in res)
print(f'Resources with clickable links: {linked} of {len(res)}')
if res and linked < len(res) / 2: warns.append('fewer than half of the resource lines have verified links; search and add them')
for w in warns: print('WARNING:', w)
tpl = open(a.template, encoding='utf-8').read()
assert tpl.count('/*__CONFIG__*/{}') == 1, 'template placeholder missing'
blob = json.dumps(cfg, ensure_ascii=False).replace('</', '<\\/')
open(a.out, 'w', encoding='utf-8').write(tpl.replace('/*__CONFIG__*/{}', blob))
print('Wrote', a.out, f'({os.path.getsize(a.out)//1024} KB)')
