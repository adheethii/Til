# Power BI Relationships and Data Model

**Date:** 2026-06-26

## What is a Data Model?

A data model in Power BI defines how tables relate to each other — like a database schema. Good data models make DAX measures simpler and reports faster.

---

## Types of Relationships

| Type | Description | Example |
|------|-------------|---------|
| One-to-Many (1:*) | Most common | One customer → many orders |
| Many-to-One (*:1) | Reverse of 1:* | Many orders → one customer |
| One-to-One (1:1) | Rare | One employee → one ID card |
| Many-to-Many (*:*) | Avoid if possible | Students ↔ Courses |

---

## Star Schema (Best Practice)

```
        Calendar
            |
Facts ── Customers
(Sales)     |
           Products
```

- **Fact table** — contains measures (sales amount, casualties)
- **Dimension tables** — contain descriptive attributes (date, customer, product)

---

## Creating Relationships

```
Steps:
1. Model view → drag field from one table to another
2. Set cardinality (1:* or *:1)
3. Set cross-filter direction (Single or Both)
```

---

## Active vs Inactive Relationships

```
Active relationship → used automatically in calculations
Inactive relationship → must be activated with USERELATIONSHIP()
```

```dax
-- Use inactive relationship in a measure
Sales by Ship Date = CALCULATE(
    SUM(Sales[Amount]),
    USERELATIONSHIP(Sales[ShipDate], Calendar[Date])
)
```

---

## What I Built

In my [Road Accident Dashboard](https://github.com/adheethii/Road-Accident-Analysis-Dashboard) — created a star schema with the accident facts table connected to a Calendar dimension table, enabling all time intelligence DAX functions to work correctly.

---

## Key Takeaway

> Always use a star schema — one fact table connected to multiple dimension tables. The Calendar table is essential for time intelligence. One-to-many relationships from dimension to fact are the standard pattern. Avoid many-to-many relationships whenever possible.
