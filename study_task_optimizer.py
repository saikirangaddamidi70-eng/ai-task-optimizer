# ============================================
# AI Study / Task Optimizer (Moderate Version)
# Author: Gaddamidi Sai Kiran
# ============================================

import pandas as pd
import matplotlib.pyplot as plt

# Load or create dataset
try:
    tasks = pd.read_csv("tasks.csv")
except:
    tasks = pd.DataFrame(columns=["Task", "Difficulty", "Deadline", "Priority", "Status"])

# AI rule-based priority
def assign_priority(diff, days):
    if diff == "hard" and days <= 2:
        return "Very High"
    elif diff == "medium" and days <= 4:
        return "High"
    elif diff == "easy" and days > 5:
        return "Low"
    else:
        return "Medium"

# Add task
def add_task():
    t = input("Task name: ")
    d = input("Difficulty (easy/medium/hard): ").lower()
    days = int(input("Deadline (days): "))
    p = assign_priority(d, days)
    global tasks
    tasks = pd.concat([tasks,
        pd.DataFrame([[t, d, days, p, "Pending"]], columns=tasks.columns)],
        ignore_index=True)
    print("✅ Task added")

# View tasks
def view_tasks():
    if tasks.empty:
        print("No tasks available")
        return
    order = {"Very High":1, "High":2, "Medium":3, "Low":4}
    temp = tasks.copy()
    temp["O"] = temp["Priority"].map(order)
    print(temp.sort_values("O")[tasks.columns])

# Complete task
def complete_task():
    name = input("Enter task name to complete: ")
    if name in tasks["Task"].values:
        tasks.loc[tasks["Task"] == name, "Status"] = "Completed"
        print("✅ Completed")
    else:
        print("❌ Task not found")

# Visualization
def visualize():
    if tasks.empty:
        return
    c = tasks["Status"].value_counts()
    plt.pie(c, labels=c.index, autopct="%1.1f%%")
    plt.title("Task Status")
    plt.show()

# Menu
while True:
    print("\n1.Add  2.View  3.Complete  4.Visualize  5.Exit")
    ch = input("Choice: ")
    if ch == "1":
        add_task()
    elif ch == "2":
        view_tasks()
    elif ch == "3":
        complete_task()
    elif ch == "4":
        visualize()
    elif ch == "5":
        tasks.to_csv("tasks.csv", index=False)
        print("Saved & Exit")
        break
    else:
        print("Invalid choice")

        