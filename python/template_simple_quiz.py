from hackerforms import *

# use Output widgets to display texts, images, tables, graphs and much more
display("Hey, there. Right now, you're navigating through a web app built entirely on Python.", button_text = "Oh, cool... but how?")

# use Input widgets to get user inputs
you = read("Hang on a sec, I'll get to that. But first, how shall I refer to *you*?")

feeling = read_multiple_choice(f"Sup, {you}. How's your day going?",["pretty good","ugh"])

# ifs, elses, whiles, etc: all of Python's logic can be used in your Forms!
if feeling == "ugh":
  display(f"Oh. I'm also kinda {feeling} today. We'll get through it together.", 
          button_text = "Uh. Ok.")
else:
  display("Nice! Mine's only gotten better since you showed up.",
         button_text = "Awkward")

x = read("Now that we're besties, let's do some math. First up, set a value for x")

y = read("Cool, now set a value for y")

operation = read_multiple_choice(f"Interesting choices there, {you}. Now choose what you want me to do with x and y.", ["add", "subtract", "multiply","divide"])

# make calculations within your Forms flow
if operation == "add":
  display(f"Let's go! {x} + {y} = {int(x)+int(y)}",button_text = "Right on")

if operation == "subtract":
  display(f"Alrighty then. {x} - {y} = {int(x)-int(y)}", button_text = "So smart")

if operation == "multiply":
  display(f"Then, you mean {x} * {y} = {int(x)*int(y)}", button_text = "Pretty much")

if operation == "divide":
  display(f"Tricky. Let me give it my best shot: {x} / {y} = {int(x)/int(y)}", button_text = "I guess?")

ans2 = read_number("Now one for you. Find the sum of the numbers between 1 and 10 (1 and 10 included).")
    
rightans2 = 55

if int(ans2) == rightans2:
  display(
    "I see you, smarty-pants!", 
    button_text = "Crushed it"),
else:
  display(
    "Don't think so. The right answer is 55.", 
    button_text = "Oh man..."
  )

display(f"Isn't this fun, {you}?" , button_text = "Hell yeah!")

display_link("https://abstracloud.com/examples", link_text = "Check out all sorts of things you can build with Abstra Cloud right now", button_text = "On my way")
