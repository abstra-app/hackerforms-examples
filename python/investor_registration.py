import os
from hackerforms import *
from abstra import *
from datetime import datetime

tables = Tables(api_key=os.environ.get("TABLES_ERP_TOKEN"))

def preprocessing_date(date):
    if date != None:
        date = datetime(date.year, date.month, date.day)
        date = date.replace(tzinfo=None)
        date = date.strftime("%Y/%m/%d, %H:%M:%S")
    return date

def replace_empty_list(data):
    return tuple(map(lambda x: x if x else None, data))
    
registration = read_multiple_choice("Hello! What would you like to do?",\
[{"label": "Register a new investor", "value":"first_time"},\
{"label":"Update a investor", "value":"update"}])

if registration == "first_time":

    investor = Page().read("Name")\
                    .read_email("Email")\
                    .read_multiple_choice("From the US?",\
                                        [{"label": "Yes", "value":True},\
                                        {"label":"No", "value":False}])\
                    .read_date("Signature date")\
                    .run("Send")


    name, email, from_us, signature_date = investor.values()

    created_date = preprocessing_date(signature_date)

    # Here you'll need to set your database's query statement in order to properly update it
    # We'll continue this example without doing so to keep the data stable

    #statement = tables.statement(id="my_statement_id")

    #result = statement.run(params={"name":name, "email":email,\
                                   #"from_us": from_us, "created_at":created_date})

    display("New investor has been registered! See you later.")

else:
    investors_information = tables.run_statement(id="eed30b99-6673-4994-9d12-a75d4b7a76d6")
    investors_name = list(map(lambda x: x['name'], investors_information))
    
    investor_name = read_dropdown("Which investor do you want to update data on?", investors_name)

    investor = Page().read("Name", required=False)\
                    .read_email("Email", required=False)\
                    .run("Send")

    name, email = investor.values()

    # Here you'll need to set your database's query statement in order to properly update it
    # We'll continue this example without doing so to keep the data stable

    #statement = tables.statement(id="my_statement_id")

    #result = statement.run(params={"name":name, "email":email, "investor_name":investor_name})

    display("Investor data has been updated! See you later.")
