# Power BI DAX Time Intelligence Functions

**Date:** 2026-06-26

## What is Time Intelligence?

Time intelligence DAX functions calculate values across time periods — YTD, month-over-month, same period last year — automatically.

**Requirement:** A dedicated Calendar/Date table connected to your data.

---

## Creating a Calendar Table

```dax
Calendar = CALENDAR(DATE(2021,1,1), DATE(2023,12,31))
```

---

## Core Functions

```dax
-- Year to Date
CY Casualties = TOTALYTD(SUM(Data[Number_of_Casualties]), 'Calendar'[Date])

-- Same Period Last Year
PY Casualties = CALCULATE(
    SUM(Data[Number_of_Casualties]),
    SAMEPERIODLASTYEAR('Calendar'[Date])
)

-- YoY % Change
YoY % Change = DIVIDE([CY Casualties] - [PY Casualties], [PY Casualties])

-- Previous Month
PM Casualties = CALCULATE(
    SUM(Data[Number_of_Casualties]),
    PREVIOUSMONTH('Calendar'[Date])
)

-- Running Total
Running Total = CALCULATE(
    SUM(Data[Number_of_Casualties]),
    DATESYTD('Calendar'[Date])
)
```

---

## What I Built

Used these in my [Road Accident Dashboard](https://github.com/adheethii/Road-Accident-Analysis-Dashboard) — showing CY vs PY casualties with YoY % change on KPI cards. Fatal casualties dropped 33.3% year-over-year.

---

## Key Takeaway

> Always create a Calendar table first. TOTALYTD for running yearly total, SAMEPERIODLASTYEAR for previous year, DIVIDE for safe percentage calculations. These 3 measures power most KPI cards in Power BI dashboards.
