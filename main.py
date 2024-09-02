import streamlit as st

st.title("Simple To-Do List App")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

new_task = st.text_input("Enter a task")
if st.button("Add Task"):
    if new_task:
        st.session_state.tasks.append(new_task)
        st.success(f"Task '{new_task}' added!")
    else:
        st.warning("Please enter a task.")

st.write("## Your Tasks")
if st.session_state.tasks:
    for i, task in enumerate(st.session_state.tasks, 1):
        st.write(f"{i}. {task}")
else:
    st.write("No tasks yet!")

if st.button("Clear All Tasks"):
    st.session_state.tasks = []
    st.warning("All tasks cleared!")
