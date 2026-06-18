# import pandas as pd

# students = pd.Series(["Nazmul", "Rahim", "Karim"])

# print(students)

import pandas as pd

students = {
    "Name": ["Nazmul", "Rahim", "Karim", "Sakib"],
    "Age": [22, 23, 21, 24],
    "Marks": [85, 75, 90, 80]
}

df = pd.DataFrame(students)

print("Student Information")
print(df)

print("\nAverage Marks:", df["Marks"].mean())
print("Highest Marks:", df["Marks"].max())

top_students = df[df["Marks"] >= 80]

print("\nTop Students:")
print(top_students)