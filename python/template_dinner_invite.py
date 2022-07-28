from hackerforms import *

display("Hey there. Glad you're coming to our dinner!")

suggestion = read("Do you have any restaurant suggestions?")

email = read_email("Great. What's your email?", button_text="Confirm")

# Add your event's link
url = "https://calendar.google.com/event?action=TEMPLATE&tmeid=NGlybjhjcDlkcWc0azZqZTBzN2ltbmIzOG4gY19tOW9oZGMzdm43dnN2bGx0bnU4MDJvMnFkY0Bn&tmsrc=c_m9ohdc3vn7vsvlltnu802o2qdc%40group.calendar.google.com"

# Register suggestion
f = open("dinner.txt", "a").write("\n" + email + "\t" + suggestion)

display("Your suggestion has been registered! \
        On the next page you'll be redirected to add the event to your calendar.")

# Redirect
execute_js("location.href = $context.url", context={'url': url})
