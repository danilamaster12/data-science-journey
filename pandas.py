import pandas as pd
workers = {
    "name" : ["ivan", "petr", "anna", "mary" ,],
    "experience" : [5, 2, 7, 1],
    "salary" : [60000, 45000, 80000, 40000]
}
df = pd.DataFrame(workers)
df["bonus"] = df["salary"] * 0.1
print(df[df["experience"] > 3])
print(df)