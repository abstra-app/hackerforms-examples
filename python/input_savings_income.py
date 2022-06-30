"""
With this form, you can input into your db your savings incomes info straight from an Excel file.
Since your .xlsx might be in a different format, make sure you adjust your column and query names.

You can use any Postgres db with this example, just keep an eye out for small modifications and
adjust the example's field names according to your set up.

We've set up this form (and Abstra's ERP) using Tables, our Postgres db service.
"""

from hackerforms import *
from abstra import *

import os
import pandas as pd 
from unidecode import unidecode
from datetime import datetime
import numpy as np

Page().display("Quick tip: this example involves setting up API keys and sending files. Errors will occur if you don't.") \
          .display_link("www.abstracloud.com/examples/input-savings-incomes", link_text="Click here to see the working example before continuing") \
          .run("Next")

def normalize_strings(text):
    norm_text = unidecode(text, "utf-8").lower().replace(" ", "_").replace("_$", "")
    return norm_text

"""
This date processing is needed for the db we're using.
Check the date format in your file and db of choice and edit accordingly."
"""

def preprocessing_datetime(date_str):
    date_time = datetime.strptime(date_str, '%d/%m/%Y')
    date_time = date_time.replace(tzinfo=None)
    date_str = date_time.strftime("%Y/%m/%d, %H:%M:%S")
    return date_str

display("Hey there.", button_text = "Let's jump right in.")

fileResponse = read_file("Upload your .xlsx file")
file = fileResponse.file # File object
url = fileResponse.url # Url to the file

data = pd.ExcelFile(file)
sheet_name = data.sheet_names[0] 
df = pd.read_excel(url, sheet_name, header=1, decimal=".")
normalize_columns = [normalize_strings(x) for x in df.columns]
df.columns = normalize_columns

values = list(df.query('history == "savings income"')['credit'])[::-1]
dates = list(df.query('history == "savings income"')['date'])[::-1]
currencies = list(np.repeat('USD',len(dates)))

preprocessing_dates = list(map(lambda x: preprocessing_datetime(x), dates))

input_data = list(zip(values, currencies, preprocessing_dates))


# insert data in db
tables = Tables(api_key=os.environ.get("DB_TOKEN"))
statement = tables.statement(id="DB_ID")

for data in input_data:
    value, currency, savings_date = data
    result = statement.run(params={"value": value, "currency":currency,\
                                "created_at": savings_date})

display("All your savings income info has been inputed. Simple as that", button_text = "Amazing")
