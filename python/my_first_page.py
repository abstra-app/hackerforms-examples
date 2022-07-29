from hackerforms import *

# Change the string to greet users your way
read("Hi user!")

# Edit "num" to "number" in this question's label for clarity
num1 = read_number("Add a num")

# Change this input type to read_number() to use the answer as an int not a str
num2 = read("Add another number")

# Change this operation to subtract, multiply or divide
ans = num1 + num2

display(f"Here is your answer {ans}!")
