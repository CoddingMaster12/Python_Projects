import streamlit as st

st.title("📝 To-Do List")

tasks = st.session_state.get("tasks", [])

new_task = st.text_input("New task")
if st.button("Add") and new_task:
    tasks.append(new_task)
    st.session_state.tasks = tasks
    st.rerun()

for i, task in enumerate(tasks):
    if st.button(f"❌ {task}", key=i):
        tasks.pop(i)
        st.session_state.tasks = tasks
        st.rerun()
