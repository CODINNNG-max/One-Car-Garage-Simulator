# Car & Electric Car Manager

A simple Python program that lets you create a car (gas or electric),
interact with it (turn it on/off, check status, view info), and swap
it out for a new one whenever you like.

## How to run
python class.py

## What it does
- Choose to create a Gas car or an Electric car
- Enter a brand (validated against a fixed list), model, and year
- Electric cars also ask for battery size (kWh)
- Once created, you can: turn the car on/off, check its status,
  view its info, or create a replacement car
- The "garage" always holds exactly one car — creating a new one
  replaces the current one, it doesn't add to a list

## Classes
- 'Car' — base class: make, model, year, on/off state,display info, status
- 'Electric' — inherits from Car, adds battery size and charging
- 'Garage' — holds the single active car and displays it

## Notes
Input is validated throughout (invalid brands, non-numeric years/
battery sizes, out-of-range years, invalid menu choices) — the
program re-prompts rather than crashing on bad input.
