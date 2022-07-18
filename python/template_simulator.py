from hackerforms import *

# choose between lists, tuples, dictionaries and sets to store your data
department_budget = {
    "Engineering": 1000,
    "Product": 800,
    "Sales": 500,
    "Marketing": 500,
    "Operations": 300
}

# use Output widgets to display texts, images, tables, graphs and much more
display("Hi! Welcome to our Budget Checker.", button_text = "Let's get started")

# use Input widgets to get user inputs
department_name = read_multiple_choice("Firstly, to which department does this expense belong?",
 ["Product", "Engineering", "Marketing", "Sales", "Operations"]
)

value = read_number("Cool. How much was this expense?")

# ifs, elses, whiles, etc: all of Python's logic can be used in your Forms!
if value < department_budget[department_name]:
    display("All clear! You've got the cash 😎", button_text = "Go ahead")
else:
    display("Sorry, your department's budget is not sufficient to cover this expense. Please speak to your manager.", button_text = "See you next time")
