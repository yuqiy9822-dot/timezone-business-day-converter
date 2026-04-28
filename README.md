# Timezone Business Day Converter

## Author
Yuqi Yang

## What this skill does

This skill converts a given timestamp into multiple time zones and determines whether it is a business day. It also calculates the next business day.

## Why I chose this

Time zone conversion and date calculation require precise and deterministic logic. These tasks cannot be reliably handled by language models alone, so a Python script is necessary.

## How to use

Run the script:

cd .agents/skills/timezone-business-day-converter
python scripts/convert.py

## What the script does

- Converts time across different time zones
- Checks if the date is a business day
- Computes the next business day

## What worked well

The script provides accurate and reproducible results for time and date calculations.

## Limitations

- Only supports a fixed set of time zones
- Assumes correct input format

## Demo Video

(Paste your video link here)