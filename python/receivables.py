from hackerforms import *
from abstra import *
from datetime import datetime
import os

#Here you can add your company's authentication.
#user = get_user()

#if not user.email.endswith('@mycompany.com'):
  #exit()

tables = Tables(api_key=os.environ.get("TABLES_ERP_TOKEN"))

def preprocessing_date(date):
    if date != None:
        date = datetime(date.year, date.month, date.day)
        date = date.replace(tzinfo=None)
        date = date.strftime("%Y/%m/%d, %H:%M:%S")
    return date

def convert_db_to_dropdown_format(label, value, statement_id):
    dict = tables.run_statement(id=statement_id)
    for d in dict:
        d["label"] = d.pop(label)
        d["value"] = d.pop(value)
    return dict

def get_receivable():
    customers = convert_db_to_dropdown_format("name", "id", "499da0c9-5df8-42ca-a2f3-987d41e74a30")
    entities = convert_db_to_dropdown_format("name", "id", "855fa423-d4dd-4733-bc76-c36aee941af2")
    currencies =  [{"label": "USD", "value": "usd"},{"label": "BRL", "value": "brl"}]
    receivable = Page().display("Hello. To insert a receivable, please fill in the information below:")\
                       .read("Description")\
                       .read("Amount")\
                       .read_dropdown("Currency", currencies)\
                       .read_dropdown("Customer", customers)\
                       .read_dropdown("Legal entity", entities)\
                       .read_date("Receivable date")\
                       .run("Send")

    return receivable.values()

def insert_receivables_db():
    description, amount, currency, customer_id, legal_entity_id, receivable_date = get_receivable()
    amount = float(amount)
    receivable_date = preprocessing_date(receivable_date)

    # Here you'll need to set your database's query statement in order to properly update it
    # We'll continue this example without doing so to keep the data stable
    # tables.run_statement(id="your_statement_id",\
    #                     params={
    #                         "description": description, "amount": amount,
    #                         "currency": currency, "customer_id": customer_id,
    #                         "legal_entity_id": legal_entity_id, "created_at": receivable_date
    #                     })

insert_receivables_db()
display("All clear, boss. Receivable added to your database.", button_text = "👍")
