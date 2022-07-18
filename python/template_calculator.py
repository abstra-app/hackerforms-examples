from hackerforms import *

# define functions and make calculations: all of Python's logic can be used in your Forms
def tax_calculator(value, tax1, tax2, tax3):
    tax = 100 - (tax1 + tax2 + tax3)
    tax1_usd = round(tax1 * (value / tax), 2)
    tax2_usd = round(tax2 * (value / tax), 2)
    tax3_usd = round(tax3 * (value / tax), 2)
    invoice_value = round(value / (tax / 100), 2)
    if (tax1_usd+tax2_usd+tax3_usd) < 10:
      tax1_usd = 0
      tax2_usd = 0
      tax3_usd = 0
      invoice_value = value
    return tax1_usd, tax2_usd, tax3_usd, invoice_value

# use Input widgets to get user inputs
invoice_data = Page().display("Hello! Fill in the data below:")\
                    .read("Invoice value without taxes (usd)")\
                    .read("Tax 1 (%)")\
                    .read("Tax 2 (%)")\
                    .read("Tax 3 (%)")\
                    .run("Send")

amount_usd, tax1_usd, tax2_usd, tax3_usd = [float(x) for x in invoice_data.values()]

tax1, tax2, tax3, invoice_value = tax_calculator(amount_usd, tax1_usd, tax2_usd, tax3_usd)

# use Output widgets to display texts, images, tables, graphs and much more
# the Page class allows you to display multiple widgets on the same screen
Page().display("Invoice value with taxes: R$ {}".format(invoice_value))\
      .display("Tax 1 = $ {}".format(tax1))\
      .display("Tax 2 = $ {}".format(tax2))\
      .display("Tax 3 = $ {}".format(tax3))\
      .run("Ok, got it!")
