import pandas as pd 

# Load and sample
df = pd.read_csv("../data/raw/student_placement_1M.csv")
df = df.sample(n=100000, random_state=42)
df = df.rename(columns={"placed": "is_placed"})

### CGPA Bucket
def cgpa_bucket(cgpa):
    if cgpa < 6:
        return "Low"
    elif cgpa < 8:
        return "Medium"
    else:
        return "High"
    
df["cgpa_bucket"] = df["cgpa"].apply(cgpa_bucket)

### Total Skill Score
df["total_skill_score"] = (
    df["python_skill"] +
    df["c++_skill"] +
    df["java_skill"] +
    df["ml_skill"] +
    df["web_dev_skill"] +
    df["communication_skill"] +
    df["logical_reasoning"]
)

### Experience Score
df["experience_score"] = (
    df["internships"] +
    df["projects"] +
    df["hackathons"] +
    df["certifications"]
)

# Save
df.to_csv("../data/processed/student_placement_cleaned.csv", index=False)

print("Processed dataset saved succesfully")
