# How Power BI DAX Measures Work

**Date:** 2026-05-30

## What is DAX?

**DAX = Data Analysis Expressions** — a formula language used in Power BI to create custom calculations, KPIs, and aggregations that go beyond basic drag-and-drop visuals.

---

## Calculated Column vs Measure

| | Calculated Column | Measure |
|--|------------------|---------|
| Computed | Row by row | On demand (at query time) |
| Stored | In the table | Not stored |
| Use for | Row-level values | Aggregations & KPIs |
| Example | `Full Name = [First] & " " & [Last]` | `Total Sales = SUM(Sales[Amount])` |

**Always prefer Measures over Calculated Columns** for aggregations — they're faster and more memory efficient.

---

## Basic Measure Syntax

```dax
Measure Name = FUNCTION(Table[Column])
```

### Common Functions

```dax
-- Aggregations
Total Casualties = SUM(Data[Number_of_Casualties])
Avg Casualties   = AVERAGE(Data[Number_of_Casualties])
Accident Count   = COUNT(Data[Accident_Index])

-- Conditional
Fatal Only = CALCULATE(SUM(Data[Number_of_Casualties]),
                       Data[Accident_Severity] = "Fatal")
```

---

## Time Intelligence (Most Powerful DAX Feature)

```dax
-- Current Year total
CY Casualties = TOTALYTD(SUM(Data[Number_of_Casualties]), 'Calendar'[Date])

-- Previous Year total
PY Casualties = CALCULATE([CY Casualties],
                SAMEPERIODLASTYEAR('Calendar'[Date]))

-- Year-over-Year % change
YoY % Change = DIVIDE([CY Casualties] - [PY Casualties],
                       [PY Casualties])
```

These 3 measures power the **KPI cards** showing ▼ -11.9% change in dashboards.

---

## CALCULATE — The Most Important DAX Function

`CALCULATE` changes the **filter context** of a measure.

```dax
-- Without CALCULATE (uses whatever filter is on the visual)
Urban Casualties = SUM(Data[Number_of_Casualties])

-- With CALCULATE (forces Urban filter regardless of slicer)
Urban Only = CALCULATE(SUM(Data[Number_of_Casualties]),
                       Data[Urban_or_Rural_Area] = "Urban")
```

---

## Filter Context vs Row Context

```
Filter Context → What CALCULATE and slicers control
Row Context    → What calculated columns see (current row)

Measures always run in Filter Context.
Calculated Columns always run in Row Context.
```

---

## What I Built

Used these DAX measures in my [Road Accident Analysis Dashboard](https://github.com/adheethii/Road-Accident-Analysis-Dashboard):
- `CY Casualties` and `PY Casualties` for KPI cards
- `YoY % Change` to show year-on-year improvement
- `CALCULATE` with severity filters for Fatal / Serious / Slight breakdowns

---

## Key Takeaway

> DAX measures are calculated at query time in filter context — not stored. `CALCULATE` is the most powerful function because it lets you override filters. Time intelligence functions like `TOTALYTD` and `SAMEPERIODLASTYEAR` make YoY comparisons effortless.
