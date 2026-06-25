# Power BI Visuals and Filters

**Date:** 2026-06-25

## Types of Visuals in Power BI

Power BI has built-in visuals for every use case:

| Visual | Best For |
|--------|----------|
| Bar/Column Chart | Comparing categories |
| Line Chart | Trends over time |
| Pie/Donut Chart | Part-to-whole relationships |
| Card | Single KPI value |
| Table/Matrix | Detailed data |
| Map | Geographic data |
| Scatter Plot | Correlation between two measures |
| Slicer | Interactive filtering |

---

## KPI Cards

```
Card visual → drag your measure → shows single value
KPI visual  → shows value + target + trend arrow
```

Used in Road Accident Dashboard for:
- Total Casualties: 195.7K
- Total Accidents: 144.4K
- Fatal Casualties: 2.9K ▼ -33.3%

---

## Slicers (Interactive Filters)

Slicers let users filter all visuals on a page interactively:

```
Steps:
1. Insert → Slicer
2. Drag field to slicer (e.g. Road_Surface)
3. All visuals on page filter automatically when slicer is clicked
```

Types of slicers:
- Dropdown
- List
- Between (for date ranges)
- Relative date

---

## Cross-Filtering

When you click on one visual, it automatically filters others:

```
Click "Urban" in donut chart
→ Bar chart shows only urban casualties
→ Map highlights only urban areas
→ Line chart shows only urban trend
```

This happens automatically — no extra setup needed.

---

## Drill-Through

Right-click a data point → Drill through → See detailed page for that item:

```
Steps:
1. Create a detail page
2. Add "Drill through" field to that page
3. Right-click any data point in main page → Drill through
```

---

## Filters Pane

Three levels of filtering:
- **Visual level** → affects only one chart
- **Page level** → affects all visuals on current page
- **Report level** → affects all pages

---

## What I Built

Used slicers for Road Surface (Dry/Wet/Snow) and Weather Conditions in my [Road Accident Dashboard](https://github.com/adheethii/Road-Accident-Analysis-Dashboard) — all 7 visuals filter simultaneously when a slicer is clicked.

---

## Key Takeaway

> Power BI's power is in interactivity — slicers, cross-filtering, and drill-through let users explore data without writing queries. Always add slicers for your most important dimensions. Cross-filtering is automatic and makes dashboards feel alive.
