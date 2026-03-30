# Focus Tracker (BYOP Project)

## Problem
Most students spend a lot of time on laptops but don’t really know where their time goes. 
Sometimes we feel busy but end up wasting hours on distractions like YouTube or social media.

## Solution
This project tracks which application is currently active on the system and logs it over time. 
It then analyzes the data and categorizes it into productive, distracting, or neutral activities.

Based on this, it calculates a "Focus Score" to give a rough idea of productivity.

## Features
- Tracks active window every few seconds
- Stores usage data in CSV file
- Categorizes apps (productive / distracting / neutral)
- Calculates Focus Score
- Displays time distribution using a pie chart

## Tech Used
- Python
- pandas
- matplotlib
- pygetwindow

## How to Run

1. Install dependencies:

pip install -r requirements.txt

2. Run tracker:

python tracker.py

3. After collecting data, run analyzer:

python analyzer.py
