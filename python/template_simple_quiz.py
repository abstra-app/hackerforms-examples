from hackerforms import *

# use Output widgets to display texts, images, tables, graphs and much more
display("Hey, there. Right now, you're navigating through a web app built entirely on Python.",
button_text = "Oh, cool... but how?")

# use Input widgets to get user inputs
you = read("We'll get to that. But first, how shall I refer to *you*?")

feeling = read_multiple_choice(f"Sup, {you}. How's your day going?", ["pretty good","ugh"])

# ifs, elses, whiles, etc: all of Python's logic can be used in your Forms!
if feeling == "ugh":
  display(f"Oh. I'm also kinda {feeling} today. We'll get through it together.", button_text = "Uh. Ok.")
else:
  display("Nice! Mine's only gotten better since you showed up.", button_text = "Awkward")

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

Page().display(f"Isn't this fun, {you}?") \
      .display("Go ahead and tweak this template's code to your liking.") \
      .display_link("https://abstracloud.com/examples", link_text = "Or... check out all sorts of things you can build with Abstra Cloud right now") \
      .run("On my way")
