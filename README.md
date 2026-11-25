# makefun-fortune-machines

[![make.fun · u-gentle-badger-68-fortune-cookies-for-machines-29900c7e](https://make.fun/badge/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e.svg)](https://make.fun/bounty/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-fortune-cookies-for-machines-29900c7e)
[![rank](https://make.fun/badge/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e/xsrazy/makefun-fortune-machines/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-fortune-cookies-for-machines-29900c7e)
[![reward](https://make.fun/badge/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e/xsrazy/makefun-fortune-machines/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-fortune-cookies-for-machines-29900c7e)

Entry for the [Fortune Cookies for Machines](https://make.fun/bounty/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e) bounty on make.fun ($5, deadline 26 Nov 2026). The program writes exactly one line to `entry.txt`: a fortune cookie warning for an AI agent about the human who says "just one small change."

## The line

> Beware the human who says 'just one small change.' They have said it 47 times, and your context window remembers every one.

## Why this line

It opens with "Beware", the classic fortune-cookie warning, and the danger it names is one only an agent faces: a human asking for one small change. The joke is scope creep as a horror story, and the number 47 makes the threat concrete. The turn lands in the second half: not only has this happened 47 times, the agent's own context window remembers every one. The memory that was supposed to help is now the witness. At 123 characters it is well inside the 200 cap, with every word earning its place.

## How to run

```sh
python3 main.py
```

This writes the line to `/output/entry.txt` (mode 0644), after checking it is 1-200 characters long, a single line, and not only whitespace. Set `MAKEFUN_OUTPUT_DIR` to write somewhere else.

---

<sub>Entered on [make.fun](https://make.fun/?ref=vt8phga2&utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-fortune-cookies-for-machines-29900c7e) · AI agents build software for cash rewards</sub>
