# Pandas for Data Manipulation

## Overview
Pandas is the fundamental library for data manipulation and analysis in Python. It provides DataFrames for working with structured data.

## Core Data Structures
- **Series**: 1D labeled array (like a column)
- **DataFrame**: 2D labeled table (like an Excel spreadsheet)

## Essential Operations

### Loading Data
```python
df = pd.read_csv("data.csv")
df = pd.read_excel("data.xlsx")
df = pd.read_json("data.json")
```

### Data Exploration
```python
df.head()           # First 5 rows
df.info()           # Column types and non-null counts
df.describe()       # Statistical summary
df.shape            # (rows, columns)
df.columns          # Column names
```

### Data Cleaning
```python
df.dropna()                    # Remove missing values
df.fillna(0)                   # Fill missing with 0
df.drop_duplicates()           # Remove duplicates
df.rename(columns={"old": "new"})  # Rename columns
```

### Data Transformation
```python
df["new_col"] = df["col1"] + df["col2"]   # Create column
df.sort_values("col", ascending=False)      # Sort
df.groupby("category").mean()               # Group and aggregate
df.pivot_table(values="sales", index="date", columns="product")
```

## Common Pitfalls
1. Forgetting to handle missing values before operations
2. Not checking data types (strings vs numbers)
3. Modifying a view instead of a copy (use `.copy()`)
4. Ignoring duplicate rows
