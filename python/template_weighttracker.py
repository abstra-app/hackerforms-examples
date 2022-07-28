from hackerforms import *
import pandas as pd
from os.path import exists
import time
import datetime
import plotly.express as px

user = get_user()
option = read_multiple_choice('What would you like to do?', ['Insert new weight', 'See progress'], button_text=None)

if not exists("weights.tsv"):
    with open("weights.tsv", "a") as f:
        f.write("email\tweight\tdate\n")


if option == 'Insert new weight':
    now = time.localtime()
    year = now.tm_year
    month = now.tm_mon
    day = now.tm_mday

    date = read_date("Add date of measurement", initial_value=datetime.date(year,month,day))

    weight = read_number("Fill your weight")

    with open("weights.tsv", "a") as f:
        f.write(f"{user.email}\t{weight}\t{date}\n")


df = pd.read_csv("weights.tsv", delimiter="\t")
df.date = df.date.astype('datetime64')
df = df.sort_values('date')
df = df[df.email == user.email]

fig = px.line(df, x='date', y='weight')
display_plotly(fig)
