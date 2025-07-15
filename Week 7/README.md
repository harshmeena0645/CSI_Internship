
---

### 📄 `README.md` (project root or `week7/`)

```md
# PySpark ETL Project - Customer and Order Join

## Description
This PySpark project reads customer and order data from CSV files, performs a join operation, and writes the result as a Delta table.

## Workflow
1. Read customer master files from:
   - `data/CUST_MSTR_20191112.csv`
   - `data/CUST_MSTR_20191113.csv`
2. Read order files from:
   - `data/master_child_export-20191112.csv`
   - `data/master_child_export-20191113.csv`
3. Extract date from filename and add columns.
4. Join on `id = cust_id`.
5. Write joined output to Delta format.

## Folder Structure
