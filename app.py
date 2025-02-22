import streamlit as st

# App Title
st.title("📝 To-Do List App")

# Initialize Session State
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# Function to Add Task
def add_task():
    if new_task:
        st.session_state.tasks.append(new_task)
        st.success(f"Task Added: {new_task}")

# Function to Remove Task
def remove_task(index):
    del st.session_state.tasks[index]
    st.success("Task Removed!")

# Function to Update Task
def update_task(index, updated_task):
    st.session_state.tasks[index] = updated_task
    st.success("Task Updated!")

# Input Field for New Task
new_task = st.text_input("Enter a new task:")
if st.button("Add Task"):
    add_task()

# Display Tasks
st.subheader("Your Tasks:")
for i, task in enumerate(st.session_state.tasks):
    col1, col2, col3 = st.columns([4, 1, 1])

    # Show Task
    with col1:
        updated_task = st.text_input(f"Task {i+1}", task, key=f"task_{i}")

    # Update Button
    with col2:
        if st.button("✏️", key=f"update_{i}"):
            update_task(i, updated_task)

    # Remove Button
    with col3:
        if st.button("❌", key=f"remove_{i}"):
            remove_task(i)

# Clear All Button
if st.button("Clear All"):
    st.session_state.tasks = []
    st.success("All Tasks Cleared!")
