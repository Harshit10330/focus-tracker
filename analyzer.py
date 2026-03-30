import pandas as pd

# Load data
df = pd.read_csv("data.csv", names=["time", "window"])

# Categorization logic
def categorize(window):
    window = str(window).lower()

    if "youtube" in window or "instagram" in window or "facebook" in window or "whatsapp" in window:
        return "Distracting"
    elif "code" in window or "pycharm" in window or "notepad" in window:
        return "Productive"
    else:
        return "Neutral"

# Apply categorization
df["category"] = df["window"].apply(categorize)

# Each row = 5 seconds
df["seconds"] = 5

# Group by category
time_spent = df.groupby("category")["seconds"].sum()

print("\n Time Spent (in seconds):")
print(time_spent)

# Calculate Focus Score
productive = time_spent.get("Productive", 0)
total = time_spent.sum()

focus_score = (productive / total) * 100 if total > 0 else 0

print(f"\n Focus Score: {focus_score:.2f}%")

#Graph 
import matplotlib.pyplot as plt

# taking labels and values from earlier result
labels = list(time_spent.index)
values = list(time_spent.values)

# basic pie chart
plt.figure()

plt.pie(values, labels=labels, autopct='%1.1f%%')

plt.title("How my time was spent")

plt.show()