# -------------------------------
# Day 10 - Pandas Basics
# -------------------------------

# Series

students = pd.Series(["Aman", "Vanshika", "Rahul"])

print("Series:")
print(students)

print()


# DataFrame

data = {
    "Name": ["Aman", "Vanshika", "Rahul"],
    "Age": [20, 21, 22],
    "Marks": [85, 91, 88]
}

df = pd.DataFrame(data)

print("DataFrame:")
print(df)

print()


# Grabbing Columns

print("Name Column:")
print(df["Name"])

print()


# Grabbing Rows

print("First Row:")
print(df.loc[0])

print()


# Adding New Column

df["City"] = ["Delhi", "Ludhiana", "Chandigarh"]

print(df)

print()


# Deleting Column

new_df = df.drop("City", axis=1)

print(new_df)

print()


# Conditional Selection

print(df[df["Marks"] > 85])

print()


# Setting an Index

indexed_df = df.set_index("Name")

print(indexed_df)

print()


# Missing Values

sample = pd.DataFrame({
    "A": [10, 20, None],
    "B": [5, None, 8]
})

print(sample)

print()

print(sample.fillna(0))

print()


# Grouping

employees = pd.DataFrame({
    "Department": ["IT", "IT", "HR", "HR"],
    "Salary": [50000, 55000, 40000, 45000]
})

print(employees.groupby("Department").mean())

print()


# Custom Function

def grade(mark):

    if mark >= 90:
        return "A"

    return "B"


df["Grade"] = df["Marks"].apply(grade)

print(df)

print()


# Reading CSV File

# Uncomment after creating students.csv

# csv_data = pd.read_csv("students.csv")
# print(csv_data)

# ---------------------------------
# Day 11 - Pandas Practice Questions
# ---------------------------------

import pandas as pd
import numpy as np

# Create a Series with custom index

series = pd.Series([10, 20, 30, 40], index=["A", "B", "C", "D"])
print(series)

print()


# Create a DataFrame

students = {
    "Name": ["Aman", "Vanshika", "Rahul", "Priya", "Simran"],
    "Age": [20, 21, 22, 20, 23],
    "Marks": [85, 91, 78, 88, 95]
}

df = pd.DataFrame(students)

print(df)

print()


# Read CSV File

# csv_data = pd.read_csv("data.csv")
# print(csv_data)


# Select Age column

print(df["Age"])

print()


# First three rows

print(df.head(3))

print()


# Add Grade column

df["Grade"] = ["B", "A", "C", "B", "A"]

print(df)

print()


# Delete Marks column

new_df = df.drop("Marks", axis=1)

print(new_df)

print()


# Filter rows

print(df[df["Age"] > 20])

print()


# Group By

group = pd.DataFrame({
    "Class": ["A", "A", "B", "B"],
    "Marks": [80, 90, 70, 85]
})

print(group.groupby("Class")["Marks"].mean())

print()


# Merge DataFrames

df1 = pd.DataFrame({
    "Student_ID": [1, 2, 3],
    "Name": ["Aman", "Rahul", "Vanshika"]
})

df2 = pd.DataFrame({
    "Student_ID": [1, 2, 3],
    "Marks": [80, 75, 95]
})

print(pd.merge(df1, df2, on="Student_ID"))

print()


# Replace Missing Values

data = pd.DataFrame({
    "Marks": [80, np.nan, 90, np.nan]
})

data["Marks"] = data["Marks"].fillna(data["Marks"].mean())

print(data)

print()


# Sort Data

sorted_df = df.sort_values(
    by=["Age", "Marks"],
    ascending=[True, False]
)

print(sorted_df)

print()


# Apply Custom Function

def double_marks(mark):
    return mark * 2

df["Double Marks"] = df["Marks"].apply(double_marks)

print(df)