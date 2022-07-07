"""
This example shows how to easily create your own marketplace with Forms.
Use requests to your fav database to populate multiple choices and cards, and send everything right back. You're good to go!
"""

from hackerforms import *
import requests
import json
import os

if not 'AIRTABLE_MARKETPLACE_API_KEY' in os.environ:
    Page().display("Hmmm seems like you forgot to set your API key. An error will appear on the log tab.") \
          .display_link("https://www.abstracloud.com/examples/dev-marketplace", link_text="Click here to see the working example") \
          .run("Next")
    raise ValueError("Try adding your API key for this script to work")
    exit()

# This form uses an environment variable. To make it work properly, add an Airtable API Key to your workspace's environment variables in the sidebar.
api_key = os.environ['AIRTABLE_MARKETPLACE_API_KEY']
devs_endpoint = os.environ['AIRTABLE_MARKETPLACE_DEVS_URL']
jobs_endpoint = os.environ['AIRTABLE_MARKETPLACE_JOBS_URL']

def who():
    who = read_multiple_choice("What are you looking for today?", [
        {"label": "I'm a dev, looking for a job opening", "value": "dev"},
        {"label": "I'm looking for a dev for my company.", "value": "business"},
    ])

    if who == "dev":
        dev()
    elif who == "business":
        business()


def dev():
    action = read_multiple_choice("Very cool. What do you need?", [
        {"label": "I'd like to check out the job board.", "value": "view"},
        {"label": "I want to list my services.", "value": "create"},
    ])

    if action == "view":
        view_job_board()

    elif action == "create":
        list_services()


def list_services():
    display("Let's start by authenticating your email.")
    auth_info = get_user()
    email = auth_info.email

    name = read("What is your full name?")
    seniority = read_dropdown("What is your seniority?", [
                              "Intern/Trainee", "Junior", "Mid-level", "Senior", "Leader"])
    rate = read_number("What is your hourly rate?")
    availability = read_number(
        "What many available hours do you have per week?")
    skills = read_textarea("What are your main skills?")

    endpoint = devs_endpoint
    head = {"Authorization": "Bearer " + api_key,
            "Content-Type": "application/json"}
    info = {"records": [
            {
                "fields": {
                    "Name": name,
                    "Email address": email,
                    "Seniority": seniority,
                    "Hourly rate": rate,
                    "Available hours per week": availability,
                    "Skills": skills
                }}],
            "typecast": True
            }
    response = requests.post(url=endpoint, json=info, headers=head)

    display(f"Perfect {name}, your services have been listed! Now anyone searching for a dev can find you in our Dev Board. I'm sure you'll receive a proposal in no time.",
            button_text="Woohoo!")

    display_link("https://meetings.hubspot.com/sophia-faria/abstra-cloud-onboarding",
                 link_text="If you have any questions, get in touch with us here.",
                 button_text="See you soon"
                 )


def view_job_cards(endpoint):
    head = {"Authorization": "Bearer " + api_key,
            "Content-Type": "application/json"}
    res = requests.get(url=endpoint, headers=head)
    data = res.json()
    data_records = data['records']

    cards = []
    for record in range(len(data_records)):
        job_title = data_records[record]['fields']['Job title']
        seniority = data_records[record]['fields']['Seniority needed']
        hourly_rate = str(data_records[record]['fields']['Hourly rate'])
        hours_needed = str(data_records[record]
                           ['fields']['Hours needed per week'])
        skills = data_records[record]['fields']['Skills required']

        cards.append({
            'title': data_records[record]['fields']['Company name'],
            'description': f"{job_title}, Seniority: {seniority}, ${hourly_rate}/per hour, {hours_needed} hours per week, Ideal skills: {skills}"
        })

    read_cards('Select your desired job to get in touch with the company:', cards)
    # Just insert your desired email server settings here.

    display("Love to see it. We're sending an email to connect you and the company right now. Be sure to check your inbox in the next few minutes.",
            button_text="Woohoo!")

    display_link("https://meetings.hubspot.com/sophia-faria/abstra-cloud-onboarding",
                 link_text="If you have any questions, you can get in touch with us here.",
                 button_text="See you soon"
                 )


def view_job_board():
    action = read_multiple_choice("Do you want to view the whole board or add a filter?", [
        {"label": "Show me everything", "value": "everything"},
        {"label": "Add a filter", "value": "filtered"},
    ])

    if action == "everything":
        endpoint = jobs_endpoint
        view_job_cards(endpoint)

    elif action == "filtered":
        filter_choice = read_multiple_choice("What would you like to filter by?",
                                             ["Seniority needed", "Hourly rate"])

        if filter_choice == "Seniority needed":
            seniority_filter = read_dropdown("What is your seniority?", [
                                             "Intern/Trainee", "Junior", "Mid-level", "Senior", "Leader"])
            endpoint = jobs_endpoint + '?filterByFormula=Seniority+needed+%3D+' + seniority_filter
            view_job_cards(endpoint)

        elif filter_choice == "Hourly rate":
            hourly_rate_filter = read(
                "What's the minimum hourly rate you want?")
            endpoint = jobs_endpoint + '?filterByFormula=Hourly+rate+%3D+' + hourly_rate_filter
            view_job_cards(endpoint)


def business():
    action = read_multiple_choice("Very cool. What do you need?", [
        {"label": "I'd like to check out available devs.", "value": "view"},
        {"label": "I want to post a job.", "value": "create"},
    ])

    if action == "view":
        view_dev_board()

    elif action == "create":
        list_job()


def list_job():
    display("Let's start by authenticating the email where you'd like to be reached.")
    auth_info = get_user()
    email = auth_info.email

    company_name = read("What is your company's name?")
    job_title = read("What is the job title?")
    seniority = read_dropdown("What is the seniority needed?", [
                              "Intern/Trainee", "Junior", "Mid-level", "Senior", "Leader"])
    rate = read_number("What is the hourly rate offered?")
    availability = read_number("How many hours are needed per week?")
    skills = read_textarea("What the main skills required?")

    endpoint = jobs_endpoint
    head = {"Authorization": "Bearer " + api_key,
            "Content-Type": "application/json"}
    info = {"records": [
            {
                "fields": {
                    "Company name": company_name,
                    "Job title": job_title,
                    "Email address": email,
                    "Seniority needed": seniority,
                    "Hourly rate": rate,
                    "Hours needed per week": availability,
                    "Skills required": skills
                }}],
            "typecast": True
            }
    response = requests.post(url=endpoint, json=info, headers=head)

    display("Perfect, your job offer has been listed! Now any qualified dev can find you in our Job Board. I'm sure you'll get a candidate in no time.",
            button_text="Woohoo!")

    display_link("https://meetings.hubspot.com/sophia-faria/abstra-cloud-onboarding",
                 link_text="If you have any questions, you can get in touch with us here.",
                 button_text="See you soon"
                 )


def view_dev_cards(endpoint):
    head = {"Authorization": "Bearer " + api_key,
            "Content-Type": "application/json"}
    res = requests.get(url=endpoint, headers=head)
    data = res.json()
    data_records = data['records']

    cards = []
    for record in range(len(data_records)):
        name = data_records[record]['fields']['Name']
        seniority = data_records[record]['fields']['Seniority']
        hourly_rate = str(data_records[record]['fields']['Hourly rate'])
        available_hours = str(
            data_records[record]['fields']['Available hours per week'])
        skills = data_records[record]['fields']['Skills']

        cards.append({
            'title': name,
            'description': f"{seniority} dev, ${hourly_rate}/per hour, {available_hours} available hours per week, Skills: {skills}"
        })

    read_cards('Select a dev to get in touch with:', cards)
    # Just insert your desired email server settings here.

    display("Love to see it. We're sending an email to get your company and your selected pro in touch right now. Be sure to check your inbox in the next few minutes.",
            button_text="Woohoo!")

    display_link("https://meetings.hubspot.com/sophia-faria/abstra-cloud-onboarding",
                 link_text="If you have any questions, you can get in touch with us here.",
                 button_text="See you soon"
                 )


def view_dev_board():
    action = read_multiple_choice("Do you want to view the whole board or add a filter?", [
        {"label": "Show me everything", "value": "everything"},
        {"label": "Add a filter", "value": "filtered"},
    ])

    if action == "everything":
        endpoint = devs_endpoint
        view_dev_cards(endpoint)

    elif action == "filtered":
        filter_choice = read_multiple_choice("What would you like to filter by?",
                                             ["Seniority", "Hourly rate"])

        if filter_choice == "Seniority":
            seniority_filter = read_dropdown("What is the seniority needed?", [
                                             "Intern/Trainee", "Junior", "Mid-level", "Senior", "Leader"])
            endpoint = devs_endpoint + '?filterByFormula=Seniority+needed+%3D+' + seniority_filter
            view_dev_cards(endpoint)

        elif filter_choice == "Hourly rate":
            hourly_rate_filter = read(
                "What's the maximum hourly rate you're willing to pay?")
            endpoint = devs_endpoint + '?filterByFormula=Hourly+rate+%3D+' + hourly_rate_filter
            view_dev_cards(endpoint)


display("Hey there. Welcome to our marketplace.",
        button_text="Nice to see you")

who()
