# Power BI Row Level Security (RLS)

**Date:** 2026-06-30

## What is Row Level Security?

RLS restricts which data rows a user can see in a Power BI report — different users see different subsets of the same report.

```
Admin user    → sees ALL data
Regional manager → sees only their region's data
Sales rep     → sees only their own data
```

---

## Setting Up RLS

### Step 1 — Create a Role

```
Power BI Desktop → Modeling tab → Manage Roles → Create role
```

### Step 2 — Add a DAX Filter

```dax
-- Role: "SouthRegion"
-- Filter on Region table:
[Region] = "South"

-- Dynamic RLS (user sees their own data):
[Email] = USERPRINCIPALNAME()
```

`USERPRINCIPALNAME()` returns the logged-in user's email — powerful for dynamic filtering.

### Step 3 — Test the Role

```
Modeling → View As → select role → report filters automatically
```

### Step 4 — Publish and Assign

```
Publish to Power BI Service →
Dataset → Security → assign users/groups to roles
```

---

## Static vs Dynamic RLS

| | Static RLS | Dynamic RLS |
|--|-----------|------------|
| Filter | Hardcoded value | Based on logged-in user |
| Maintenance | Update role for each region | Self-managing |
| Example | `[Region] = "South"` | `[Email] = USERPRINCIPALNAME()` |
| Best for | Few fixed groups | Many users with own data |

---

## DAX for Dynamic RLS

```dax
-- Users table has Email column matching login emails
-- Filter: show only rows matching logged-in user
[SalesRepEmail] = USERPRINCIPALNAME()
```

---

## Key Takeaway

> RLS is essential for enterprise Power BI reports — you build one report but different users see different data. Use static RLS for regional filters and dynamic RLS with USERPRINCIPALNAME() for user-specific data. Always test roles before publishing.
