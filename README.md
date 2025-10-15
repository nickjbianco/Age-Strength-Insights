# Powerlifting Data Analysis Project

## Overview

This project analyzes powerlifting performance data to explore relationships between **age**, **weight class**, **sex**, and **strength metrics** (Total, Squat, Bench, and Deadlift).  
It includes a complete **ETL pipeline** (SQL + Python) and **visual analysis** using Pandas, SQLAlchemy, and Matplotlib.

---

## Project Structure

### ETL Scripts

- **`bench_data_import.py` / `import_top50_total.py` / `top50.py`** – Import and clean data from SQL databases into structured tables.
- **`bench_etl_pipeline.ipynb`** – Orchestrates data extraction, transformation, and loading steps for the bench dataset.

### Analysis Notebooks

- **`age_comparisons.ipynb`** – Compares youngest, oldest, and average lifter ages across weight classes and sex.
- **`strength_comparisons.ipynb`** – Examines both absolute and relative (bodyweight-adjusted) strength for each lift.
- **`squat_deadlift_pcts.ipynb`** – Studies carryover between squat and deadlift performance relative to total lift rankings.

### Visualization Output

All analysis results are visualized with Matplotlib to illustrate trends and relationships by lift type, weight class, and sex.

---

## Key Analyses & Insights

### Age Comparisons

- **Average Age:** For both men and women, lifters in heavier weight classes tend to be slightly older.
- **Youngest Competitors:** Appear in lighter weight classes (148–181 lb), especially among women.
- **Oldest Competitors:** Most common in mid-heavy classes (198–242 lb).

### Relative Strength (Total-to-Bodyweight Ratio)

- **Trend:** Relative strength decreases as body weight increases, for both men and women.
- **Peak Ratios:**
  - Men: ~10× bodyweight at 148 lb class.
  - Women: ~8× bodyweight at 148 lb class.
- This reflects how lighter athletes achieve higher proportional strength, even if total loads are smaller.

### Absolute Strength (Heaviest Totals)

- **Men:** Totals rise steadily with weight class, peaking above 2400 lbs in the Super Heavyweight division.
- **Women:** Totals range from ~1350 lbs at 148 lb to ~1600 lbs at 242 lb.
- Absolute strength increases with size, but relative strength decreases — a classic powerlifting tradeoff.

### Individual Lifts

#### Bench Press

- **Relative Strength:** Declines gradually with increasing weight class.
- **Absolute Strength:** Climbs steadily — male lifters reach over 780 lbs in the heaviest class; females ~450 lbs.
- Indicates strong correlation between body mass and pressing power.

#### Squat

- **Relative Strength:** Men: ~3.8× → 2.5× | Women: ~3.0× → 2.0× (from light to heavy classes).
- **Absolute Strength:** Continues to climb with body weight, surpassing 1000 lbs in the heaviest men’s class.
- Squat performance shows clear scaling with both weight and total strength outcomes.

#### Deadlift

- **Relative Strength:** Men: ~4.5× → 2.5× | Women: ~3.5× → 2.0×.
- **Absolute Strength:** Men: up to ~1075 lbs | Women: up to ~650 lbs.
- Reflects higher mechanical advantage in lighter classes but raw power in heavier divisions.

---

## Squat vs Deadlift Carryover to Total

### Men

- **Squat dominance:** 55–68% overlap of top squat and total lifters.
- **Deadlift overlap:** 30–50%.
- Squat performance correlates more consistently with total strength — especially in heavier weight classes.

### Women

- **Squat dominance:** Even stronger, 60–80% overlap.
- **Deadlift overlap:** 44–66%.
- Women’s total results are more strongly tied to squat performance across all classes.

---

## Technology Stack

- **Language:** Python
- **Libraries:** Pandas, SQLAlchemy, Matplotlib
- **Database:** SQL (via SQLAlchemy ORM)
- **Visualization:** Matplotlib line plots for comparative analysis

---

## How to Run the Project

1. **Run ETL Files First**

2. **Open Jupyter Notebooks**

3. **View Generated Graphs**
   - Age vs Weight Class and Sex
   - Relative and Absolute Strength per Lift
   - Squat vs Deadlift Carryover

---

## Summary

This project demonstrates how lifter demographics and biomechanics affect strength outcomes.  
It highlights universal trends:

- **Heavier lifters** achieve **higher totals** but lower relative strength.
- **Squat performance** is the most predictive of overall total success.
- **Female lifters** show higher consistency across classes, while **male lifters** show greater variability in specialization.

---

### Author

Developed by Nick B.  
Combining SQL-driven ETL pipelines and Python data analysis to explore high-performance powerlifting data trends.
