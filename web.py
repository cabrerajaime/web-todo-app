import streamlit as st
import functions


todos = functions.get_todos("todos.txt")


def add_todo():
    new_todo = st.session_state["new_todo"] + "\n"
    todos.append(new_todo)
    functions.write_todos(todos)


st.title("My todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    check_box = st.checkbox(todo, key=todo)
    if check_box:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun() # refrescar el script y la página


st.text_input(label="Enter todo", placeholder="Add new todo...", 
on_change=add_todo, key="new_todo")

# st.session_state