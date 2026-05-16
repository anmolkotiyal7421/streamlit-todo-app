import streamlit as st
import json
import os

# -----------------------------
# FILE NAME
# -----------------------------
FILE_NAME = "tasks.json"

# -----------------------------
# LOAD TASKS FROM FILE
# -----------------------------
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r") as file:
        tasks = json.load(file)
else:
    tasks = []

# -----------------------------
# SAVE FUNCTION
# -----------------------------
def save_tasks():
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file)

# -----------------------------
# TITLE
# -----------------------------
st.title("📝 Smart To-Do App")

# -----------------------------
# INPUT
# -----------------------------
new_task = st.text_input("Enter a new task")

# -----------------------------
# ADD BUTTON
# -----------------------------
if st.button("Add Task"):
    if new_task:
        tasks.append({
            "task": new_task,
            "done": False
        })

        save_tasks()

        st.success("Task added!")
        st.rerun()

    else:
        st.warning("Please enter a task!")

# -----------------------------
# SHOW TASKS
# -----------------------------
st.subheader("Your Tasks")

for i, task in enumerate(tasks):

    col1, col2 = st.columns([5, 1])

    with col1:

        checked = st.checkbox(
            task["task"],
            value=task["done"],
            key=i
        )

        tasks[i]["done"] = checked

    with col2:

        if st.button("❌", key=f"delete_{i}"):

            tasks.pop(i)

            save_tasks()

            st.rerun()

# -----------------------------
# SAVE CHECKBOX CHANGES
# -----------------------------
save_tasks()