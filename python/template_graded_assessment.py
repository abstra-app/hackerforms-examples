from hackerforms import *

grade = 0

# use Output widgets to display texts, images, tables, graphs and much more
display("Welcome to the Abstra quiz! Let's see how many points you can score.", button_text = "It's on")

# use Input widgets to get user inputs
ans1 = read_dropdown("What's the best programming language ever?? (no bias at all)", ["Python", "Javascript", "C++"])

# ifs, elses, whiles, etc: all of Python's logic can be used in your Forms!
if ans1 == "Python":
    grade = grade + 1

ans2 = read_multiple_choice("What can you build with Abstra Cloud? Select all that apply.", [
 {"label": "Amazing quizzes", "value": "A"},
 {"label": "Dope internal tools", "value": "B"}, 
 {"label": "Cool calculators", "value": "C"}, 
 {"label": "Ugly, unresponsive apps", "value": "D"}, 
], multiple = True)

# choose between lists, tuples, dictionaries and sets to store your data
correct = ['A', 'B', 'C']

for x in ans2:
    if x in correct:
        grade = grade + 1

ans3 = read("To finish off, a tough one: what's 1 + 2?")

if int(ans3) == 3:
    grade = grade + 1

if grade >= 3:
    display(f"You scored {grade} sweet points.", button_text = "Congrats!")
elif grade == 1:
    display(f"Oof. You scored {grade} point.", button_text = "Better luck next time")
else:
    display(f"Oof. You scored {grade} points.", button_text = "Better luck next time")
