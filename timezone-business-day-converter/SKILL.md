---
name: timezone-business-day-converter
description: Convert a timestamp across time zones and determine business day status including next business day calculation.
---

# Timezone Business Day Converter

## When to use this skill

Use this skill when:
- A user provides a date and time
- Timezone conversion is required
- Business day calculation is needed

## When NOT to use

Do not use this skill:
- If no time input is provided
- If the task is purely descriptive

## Expected inputs

- datetime string (e.g. 2026-04-26 15:00)
- timezone (e.g. US/Eastern)

## What the script does

- Converts time into multiple time zones
- Checks if the date is a business day
- Calculates the next business day

## Why code is required

Time calculations must be precise and deterministic. Language models alone cannot reliably perform timezone conversion and date arithmetic.

## Step-by-step instructions

1. Parse the input datetime
2. Convert to target time zones
3. Check if it is a weekday
4. Compute the next business day

## Output format

- Converted times
- Business day status (True/False)
- Next business day

## Limitations

- Supports a fixed set of time zones
- Assumes correct input format