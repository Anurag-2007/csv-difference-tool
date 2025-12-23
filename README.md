# CSV Row Filter

A Python utility to compare two CSV files and remove rows from one file
based on matching values in a specified column from another file.

The cleaned data is saved as a new CSV file.

---

## 📌 Use Case

- Remove duplicate records
- Filter users based on a reference list
- Clean datasets using IDs, usernames, emails, or any key column
- Subtract one CSV dataset from another

---

## 📂 Folder Structure

│── filter.py
│── file1.csv
│── file2.csv
│── output.csv

---
🚀 Usage

Place both CSV files in the same directory as the script

Ensure both files contain a common column (key column)

Update the column name in the script

Run: python filter.py


---

👨‍💻 How It Works

Loads both CSV files into memory

Normalizes values in the chosen column

Removes rows from File 2 where the key value exists in File 1

Writes the filtered data to a new CSV file
