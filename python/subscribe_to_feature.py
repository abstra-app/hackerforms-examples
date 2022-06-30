from hackerforms import *
import requests
import os

if not 'HUBSPOT_API_KEY' in os.environ:
    Page().display("Hmmm seems like you forgot to set your API key. An error will appear on the log tab.") \
          .display_link("https://www.abstracloud.com/examples/subscribe-to-a-new-feature", link_text="Click here to see the working example") \
          .run("Next")
    raise ValueError("Try adding your API key for this script to work")
    exit()

# This form uses an environment variable. To make it work properly, add a Hubspot API Key to your workspace's environment variables in the sidebar.
api_key = os.environ['HUBSPOT_API_KEY']

display("Hi there. Thanks for your interest in our upcoming features!")

display("We're almost ready to launch. Let's sign you up to get the news first-hand.")

fname = read("Firstly, what is your first name?")

lname = read("What is your last name?")

email = read("Great! What's your email?")

# Create contact in Hubspot

endpoint = "https://api.hubapi.com/contacts/v1/contact"
head = {"Authorization": "Bearer " + api_key,
        "Content-Type": "application/json"}
info = json.dumps({
    "properties": [
        {
            "property": "email",
            "value": email
        },
        {
            "property": "firstname",
            "value": fname
        },
        {
            "property": "lastname",
            "value": lname
        },
    ]
})

r = requests.post(url=endpoint, data=info, headers=head)

# Add contact to list

endpoint = "https://api.hubapi.com/contacts/v1/lists/1/add"
head = {"Authorization": "Bearer " + api_key,
        "Content-Type": "application/json"}
emails = json.dumps({
    "emails": [
        email
    ]
},
)

r = requests.post(url=endpoint, data=emails, headers=head)

display(f"All set, {fname}! You'll be notified as soon as we launch 😎🚀")
