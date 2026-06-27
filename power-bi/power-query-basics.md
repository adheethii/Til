# Power Query Basics

**Date:** 2026-06-27

## What is Power Query?

Power Query is Power BI's data transformation engine — it cleans, reshapes, and prepares your data before it reaches the data model.

```
Raw Data → Power Query (ETL) → Clean Data → Data Model → Visuals
```

Think of it as Python Pandas but with a visual interface.

---

## Accessing Power Query

```
Power BI Desktop → Home → Transform Data → Power Query Editor opens
```

---

## Common Transformations

### Remove Columns
```
Right-click column header → Remove
or: Home → Remove Columns
```

### Rename Columns
```
Double-click column header → type new name
```

### Change Data Type
```
Click data type icon (left of column name) → select type
Types: Text, Whole Number, Decimal, Date, True/False
```

### Filter Rows
```
Click dropdown on column header → filter options
e.g. Remove nulls: filter out blank values
```

### Replace Values
```
Right-click column → Replace Values
e.g. Replace "Yes" with 1, "No" with 0
```

---

## M Language (Behind the UI)

Every action generates M code automatically:

```m
let
    Source = Csv.Document(File.Contents("accidents.csv")),
    PromotedHeaders = Table.PromoteHeaders(Source),
    RemovedColumns = Table.RemoveColumns(PromotedHeaders, {"Unnamed: 0"}),
    ChangedTypes = Table.TransformColumnTypes(RemovedColumns,
        {{"Date", type date}, {"Casualties", Int64.Type}})
in
    ChangedTypes
```

---

## Merge Queries (Like SQL JOIN)

```
Home → Merge Queries → select tables + matching columns → choose join type
Left Join, Inner Join, Full Outer Join available
```

---

## What I Used

In my [Road Accident Dashboard](https://github.com/adheethii/Road-Accident-Analysis-Dashboard) — used Power Query to clean the raw accident data: removed irrelevant columns, changed data types, replaced coded values with readable labels, and filtered out null rows before building the data model.

---

## Key Takeaway

> Power Query is your data cleaning layer in Power BI — always clean data here before building visuals. Every UI action generates M code automatically. Think of it as a visual version of Pandas — same concepts (filter, rename, merge, transform) but no coding required.
