# Python Generators

**Date:** 2026-07-10

## What is a Generator?

A generator is a function that **yields values one at a time** instead of returning them all at once — saving memory for large datasets.

```python
# Regular function — returns all values at once (memory heavy)
def get_numbers(n):
    return [i for i in range(n)]   # stores ALL in memory

# Generator — yields one at a time (memory efficient)
def gen_numbers(n):
    for i in range(n):
        yield i                    # pauses here, resumes on next()
```

---

## How yield Works

```python
def countdown(n):
    print("Starting!")
    while n > 0:
        yield n          # pause here, return n
        n -= 1           # resume here on next call
    print("Done!")

gen = countdown(3)

print(next(gen))   # Starting! → 3
print(next(gen))   # → 2
print(next(gen))   # → 1
# next(gen)        # → StopIteration (generator exhausted)
```

---

## Iterating Generators

```python
# for loop handles StopIteration automatically
for num in countdown(5):
    print(num)   # 5, 4, 3, 2, 1

# Convert to list (loses memory benefit but useful sometimes)
numbers = list(countdown(5))
```

---

## Generator Expressions

```python
# List comprehension — stores all in memory
squares_list = [x**2 for x in range(1000000)]   # ~8MB

# Generator expression — generates on demand
squares_gen = (x**2 for x in range(1000000))    # ~200 bytes!

# Use with sum, max, min
total = sum(x**2 for x in range(1000000))
```

---

## Practical ML Examples

```python
# Reading large CSV in chunks — don't load all at once
def read_csv_chunks(filepath, chunk_size=1000):
    with open(filepath) as f:
        chunk = []
        for line in f:
            chunk.append(line)
            if len(chunk) == chunk_size:
                yield chunk
                chunk = []
        if chunk:
            yield chunk   # yield remaining

for chunk in read_csv_chunks("large_dataset.csv"):
    process(chunk)   # process 1000 rows at a time


# Data augmentation generator for ML training
def augment_images(image_paths):
    for path in image_paths:
        img = load_image(path)
        yield img                    # original
        yield flip_horizontal(img)   # augmented
        yield rotate(img, 90)        # augmented
```

---

## Generator vs List

| | List | Generator |
|--|------|-----------|
| Memory | Stores all items | One at a time |
| Speed | Faster for small data | Better for large data |
| Reusable | ✅ Multiple times | ❌ Once only |
| Syntax | `[x for x in ...]` | `(x for x in ...)` or `yield` |

---

## Key Takeaway

> Generators are Python's memory-efficient iterators — they yield values one at a time instead of storing everything. Essential for processing large datasets in ML. Use generator expressions `(x for x in ...)` for simple cases and `yield` functions for complex logic.
