import pandas as pd

df = pd.read_csv("../data/raw/student_placement_1M.csv")
# df = pd.read_csv("../data/processed/student_placement_cleaned.csv")

# Sample
df = df.sample(n=100000, random_state=42)

# Preview
print(df.shape)
print(df.head())