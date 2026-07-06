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

