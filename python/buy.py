"""
This scripts is used in Abstra Cloud (https://abstracloud.com) to collect buying intentions.
This is a good example on how using Python scripts can be much simpler than forms + external automations
"""

from hackerforms import *
from requests import post
import os

if 'plan' in url_params:
  plan = url_params['plan']
else:
  plan = 'standard'

display("Thank you for showing interest in our " + plan + " plan. We need some informations to get in touch.")
name = read("Name")
email = read_email('Email')
company = read("Company name")

# This form uses an environment variable. To make it work properly, add a Slack API Key to your workspace's environment variables in the sidebar.
token = os.environ.get("SLACK_BOT_TOKEN")

res = requests.post(
        'https://slack.com/api/chat.postMessage',
    json={
        'channel': 'sales',
        'text': name + ' (' + email + ') wants to buy the ' + plan + ' plan'
    },
    headers={
        'Authorization': 'Bearer ' + token,
        'Content-type': 'application/json; charset=utf-8'
    })
