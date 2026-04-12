# tasks

This file is the task list for Freeclaw's task timer.

## Format
- Each enabled task is one line: `<minutes>-<task>`
  - Example: `30-check weather` (runs about every 30 minutes).
- `minutes` is the repeat interval (dotime) in minutes.
- Disable a task by commenting it out: `# 30-check weather`
- Log results under a task as Markdown bullet lines starting with `- `.
  - This avoids log lines being misread as tasks.

## How It Works
- Interval minutes (config): 0
- Every tick, the task timer checks which tasks are due (based on dotime + elapsed time since last run).
- It runs only due tasks; it does NOT run everything every tick.
- The agent will be told which tasks are due (with elapsed minutes).

## Tasks
1440-Journal your activites for today in a dated .md file in the Journal directory
<!-- Add tasks below -->

