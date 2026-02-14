import streamlit as st
import functions as fun

def add_todo():
  todo = st.session_state['new_todo'] +"\n"
  todos = fun.get_todos()
  todos.append(todo)
  fun.write_todos(todos_arg=todos)

todos = fun.get_todos()

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

for index, todo in enumerate(todos):
  checkbox = st.checkbox(todo, key=todo)
  if checkbox:
    todos.pop(index)
    fun.write_todos(todos_arg=todos)
    del st.session_state[todo]
    st.rerun()

st.text_input(label="addTodo", label_visibility="hidden" , placeholder="Add new todo...",
              on_change=add_todo, key="new_todo")