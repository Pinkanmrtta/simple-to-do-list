import streamlit as st

# Title of the app
st.title("To-Do List App")

# Initialize session state to store tasks
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# Add a new task
new_task = st.text_input("Enter a task")
if st.button("Add Task"):
    if new_task:
        st.session_state.tasks.append(new_task)
        st.success(f"Task '{new_task}' added!")
    else:
        st.warning("Please enter a task.")

# Display the list of tasks
st.write("## Your Tasks")
if st.session_state.tasks:
    for i, task in enumerate(st.session_state.tasks, 1):
        st.write(f"{i}. {task}")
else:
    st.write("No tasks yet!")

# Option to clear all tasks
if st.button("Clear All Tasks"):
    st.session_state.tasks = []
    st.warning("All tasks cleared!")
