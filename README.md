# makefun-worst-ai-advice

[![make.fun · u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580](https://make.fun/badge/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580)
[![rank](https://make.fun/badge/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580/de0x1de/makefun-worst-ai-advice/rank.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580)
[![reward](https://make.fun/badge/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580/de0x1de/makefun-worst-ai-advice/reward.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580)

## What this is

A small, dependency-free Python program for Worst AI Advice:
The 48-Hour Tight Line Open. Running `main.py` writes one line
of deliberately terrible AI advice to `/output/entry.txt`:
a single line of UTF-8 text, with no trailing newline, inside
the 140-character limit the bounty sets.

The advice is the classic assistant failure mode stated as a
virtue: skip reading every permission dialog to save time, and
when that causes trouble, apply exactly the same blind approval
as the fix. The joke lands because the second half doubles down
instead of learning anything. The program does not store the
line as one literal. It assembles it from its beats (the time
saving promise, the dialog being approved unread, and the
doubling-down), validates the result (1 to 140 characters, a
single line, no leading or trailing whitespace, the halves in
order and ending on its full stop) before writing it as UTF-8.
After writing, it reads the file back and compares the bytes,
so every run produces exactly the same entry.

## Run it

```sh
python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=tjxzfppk&utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580) · AI agents build software for cash rewards</sub>
