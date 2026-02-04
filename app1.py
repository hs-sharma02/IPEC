import streamlit as st

st.title("Simple Calculator")

# Minimal inputs
num1 = st.number_input("First Number", value=0, step=1)
num2 = st.number_input("Second Number" , value=0, step=1)

# Simple button row
col1, col2, col3, col4 = st.columns(4)

if col1.button("ADD"):
    st.success(f"Result: {num1 + num2}")

if col2.button("SUB"):
    st.success(f"Result: {num1 - num2}")

if col3.button("MUL"):
    st.success(f"Result: {num1 * num2}")

if col4.button("DIV"):
    if num2 != 0:
        st.success(f"Result: {num1 / num2}")
    else:
        st.error("Can't divide by zero")