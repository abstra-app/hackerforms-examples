from hackerforms import *
from abstra import *
from datetime import datetime
import os

#Here you can add your company's authentication.
#user = get_user()
#if not user.email.endswith('@mycompany.com'):
  #exit()

# This form uses an environment variable. To make it work properly, add your database API Key to your workspace's environment variables in the sidebar.
tables = Tables(api_key=os.environ.get("TABLES_ERP_TOKEN"))

def preprocessing_date(date):
    if date != None:
        date = datetime(date.year, date.month, date.day)
        date = date.replace(tzinfo=None)
        date = date.strftime("%Y/%m/%d, %H:%M:%S")
    return date

travel = Page().display("Hello! To register a new travel, please add the information required in the fields below:")\
            .read("Travel purpose")\
            .read_date("Date of travel")\
            .read("Country of travel")\
            .read("City of travel")\
            .run("Send")

purpose, travel_date, country, city = travel.values()

travel_date = preprocessing_date(travel_date)

# Here you'll need to set your database's query statement in order to properly update it
# We'll continue this example without doing so to keep the data stable

#travel_statement = tables.statement(id="my_statement_id")

#result = travel_statement.run(params={"purpose": purpose, "created_at": travel_date,\
                                    #"country": country, "city": city})

display("All good! Your travel has been registered.")
