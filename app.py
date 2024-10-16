import streamlit as st
import math

# Calculator functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    else:
        return x / y

def square(x):
    return x ** 2

def square_root(x):
    if x < 0:
        return "Error: Square root of a negative number!"
    else:
        return math.sqrt(x)

def power(x, y):
    return x ** y

def logarithm(x):
    if x <= 0:
        return "Error: Logarithm of non-positive number!"
    else:
        return math.log(x)

def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))

def factorial(x):
    if x < 0:
        return "Error: Factorial of a negative number!"
    else:
        return math.factorial(x)

# Streamlit app layout
st.title("Scientific Calculator")

# Select an operation from a dropdown menu
operation = st.selectbox("Select an operation:",
                         ['Add', 'Subtract', 'Multiply', 'Divide', 'Square', 
                          'Square Root', 'Power', 'Logarithm', 
                          'Sine', 'Cosine', 'Tangent', 'Factorial'])

# Input for operations requiring two numbers
if operation in ['Add', 'Subtract', 'Multiply', 'Divide', 'Power']:
    num1 = st.number_input("Enter the first number:", format="%.2f")
    num2 = st.number_input("Enter the second number:", format="%.2f")

# Input for single number operations
else:
    num = st.number_input("Enter the number:", format="%.2f")

# Perform the calculation when the "Calculate" button is pressed
if st.button("Calculate"):
    if operation == 'Add':
        st.write(f"Result: {add(num1, num2)}")
    elif operation == 'Subtract':
        st.write(f"Result: {subtract(num1, num2)}")
    elif operation == 'Multiply':
        st.write(f"Result: {multiply(num1, num2)}")
    elif operation == 'Divide':
        st.write(f"Result: {divide(num1, num2)}")
    elif operation == 'Square':
        st.write(f"Result: {square(num)}")
    elif operation == 'Square Root':
        st.write(f"Result: {square_root(num)}")
    elif operation == 'Power':
        st.write(f"Result: {power(num1, num2)}")
    elif operation == 'Logarithm':
        st.write(f"Result: {logarithm(num)}")
    elif operation == 'Sine':
        st.write(f"Result: {sine(num)}")
    elif operation == 'Cosine':
        st.write(f"Result: {cosine(num)}")
    elif operation == 'Tangent':
        st.write(f"Result: {tangent(num)}")
    elif operation == 'Factorial':
        st.write(f"Result: {factorial(int(num))}")
