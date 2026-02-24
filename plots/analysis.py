import pandas as pd

path = "/content/drive/MyDrive/Agentic AI/task_completion_matrix.xlsx"  
df = pd.read_excel(path)

TASKS = ["T1","T2","T3","T4","T5","T6","T7"]

for t in TASKS:
    df[t] = pd.to_numeric(df[t], errors="coerce").fillna(0).astype(int)

df["tasks_completed_calc"] = df[TASKS].sum(axis=1)

if "tasks_completed" in df.columns:
    df["tasks_completed"] = pd.to_numeric(df["tasks_completed"], errors="coerce")
    mism = df[df["tasks_completed"] != df["tasks_completed_calc"]][["participant_id","file","tasks_completed","tasks_completed_calc"]]
    print("Mismatches (fix these rows in Excel or just trust calc):")
    print(mism.to_string(index=False))
else:
    df["tasks_completed"] = df["tasks_completed_calc"]


df["tasks_completed"] = df["tasks_completed_calc"]
df.drop(columns=["tasks_completed_calc"], inplace=True)

df.head(20)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid", context="paper", font_scale=1.2)

path = "/content/drive/MyDrive/Agentic AI/task_completion_matrix.xlsx"
df = pd.read_excel(path)

TASKS = ["T1","T2","T3","T4","T5","T6","T7"]

for t in TASKS:
    df[t] = pd.to_numeric(df[t], errors="coerce").fillna(0).astype(int)

df["tasks_completed"] = df[TASKS].sum(axis=1)

print("Loaded rows:", len(df))
df.head()

import seaborn as sns
import matplotlib.pyplot as plt

sns.set(
    style="whitegrid",
    context="paper",
    font_scale=1.2,
    rc={
        "axes.edgecolor": "0.2",
        "grid.color": "0.5"
    }
)

# palette = sns.color_palette("Set1", n_colors=len(TASKS))
palette = sns.color_palette("mako", n_colors=len(TASKS))

plt.figure(figsize=(7,4))
sns.barplot(
    x=TASKS,
    y=df[TASKS].mean().values * 100,
    palette=palette
)
plt.ylabel("Participants completing task (%)")
plt.xlabel("Task")
plt.ylim(0,100)
plt.tight_layout()
plt.savefig("/content/drive/MyDrive/Agentic AI/fig1_taskwise_completion.png", dpi=300)
plt.show()

coverage = df["tasks_completed"].value_counts().sort_index()

plt.figure(figsize=(7,4))
sns.barplot(
    x=coverage.index,
    y=(coverage.values/len(df))*100,
    color=sns.color_palette("dark")[2]
)
plt.xlabel("Number of Tasks Completed")
plt.ylabel("Participants (%)")
plt.tight_layout()
plt.savefig("/content/drive/MyDrive/Agentic AI/fig2_participant_coverage.png", dpi=300)
plt.show()

categories = {
    "Tool-grounded (T1–T3)": ["T1","T2","T3"],
    "Reasoning (T4–T6)": ["T4","T5","T6"],
    "Failure-mode (T7)": ["T7"],
}

cat_df = pd.DataFrame({
    "Category": list(categories.keys()),
    "Completion Rate (%)": [df[v].mean().mean()*100 for v in categories.values()]
})

labels = cat_df["Category"]
sizes = cat_df["Completion Rate (%)"]
colors = ["#4C956C", "#F4A261", "#C44536"]

plt.figure(figsize=(6,6))
plt.pie(
    sizes,
    labels=labels,
    autopct="%1.1f%%",
    startangle=140,
    colors=colors,
    wedgeprops={"edgecolor": "white", "linewidth": 1}
)

plt.tight_layout()
plt.savefig(
    "/content/drive/MyDrive/Agentic AI/fig3_category_completion_pie.png",
    dpi=300
)
plt.show()

plt.show()
