import pandas as pd

file1 = pd.read_csv("file1.csv")
file2 = pd.read_csv("file2.csv")

file1["email"] = file1["email"].str.strip().str.lower()
file2["email"] = file2["email"].str.strip().str.lower()

filtered_file2 = file2[~file2["email"].isin(file1["email"])]

filtered_file2.to_csv("new_file2.csv", index=False)

print("Done! new_file2.csv created.")
