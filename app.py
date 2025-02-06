import streamlit as st
import pandas as pd
from datetime import datetime

st.title("To-Do List App📋")
st.write("Organize and prioritize your tasks efficiently.")

if 'tasks' not in st.session_state:
    st.session_state.tasks = []

def add_task(description, due_date, priority):
    task = {
        "description": description,
        "due_date": due_date,
        "priority": priority,
        "completed": False
    }
    st.session_state.tasks.append(task)

def display_tasks(filter_status):
    filtered_tasks = [task for task in st.session_state.tasks if (task["completed"] == filter_status or filter_status == "All")]

    if filtered_tasks:
        for index, task in enumerate(filtered_tasks):
            col1, col2, col3, col4, col5 = st.columns([0.05, 0.6, 0.18, 0.1, 0.1])

            with col1:
                if st.checkbox(
                    label="",
                    key=f"complete_{index}",
                    value=task["completed"],
                    label_visibility="collapsed"
                ):
                    task["completed"] = not task["completed"]


            with col2:
                st.write(task["description"])

            with col3:
                st.write(f"📅 {task['due_date'].strftime('%d-%m-%Y')}")

            with col4:
                st.write(f"{task['priority']}")

            with col5:
                if st.button("❌", key=f"delete_{index}"):
                    st.session_state.tasks.pop(index)
    else:
        st.write("No tasks to show.")

st.subheader("Add New Task")
with st.form("new_task_form", clear_on_submit=True):
    description = st.text_input("Task Description")
    due_date = st.date_input("Due Date", min_value=datetime.today())
    priority = st.selectbox("Priority Level", ["Low", "Medium", "High"])
    submit = st.form_submit_button("Add Task")

    if submit:
        if description:
            add_task(description, due_date, priority)
            st.success("Task added successfully!")
        else:
            st.warning("Please enter a task description.")

st.subheader("To-Do List")
filter_status = st.radio("Filter by Status:", ("All", "Pending", "Completed"))

if filter_status == "Pending":
    display_tasks(False)
elif filter_status == "Completed":
    display_tasks(True)
else:
    display_tasks("All")