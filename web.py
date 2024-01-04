import streamlit as st
import Functions

todos = Functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"#session state is a type of dictionary
    todos.append(todo)
    Functions.write_todos(todos)



st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)#creates a dictionary of multiple pairs
    if checkbox:
        todos.pop(index)
        Functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()#just needed for chek boxes
st.text_input(label="Enter a todo:",
              placeholder="Add a new todo...",
              on_change=add_todo, key="new_todo")#on change is a call abck function
            #the key is what id


print("Hello")
