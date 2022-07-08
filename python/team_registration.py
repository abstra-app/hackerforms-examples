import os
from hackerforms import *
from abstra import *
from datetime import datetime

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
    
registration = read_multiple_choice("Hello! What would you like to do?",\
[{"label": "Register a new member of team", "value":"new_member"},\
{"label":"Update a member information", "value":"update_member"}])

if registration == "new_member":
    member = Page().display("Ok, to register a new member please fill in the following information:")\
                .read("Full name")\
                .read_email("Personal Email")\
                .read_date("Start date at company")\
                .read("Position")\
                .read_date("Birth date")\
                .read_phone("Phone Number")\
                .read("National ID number")\
                .read("ID number emited by")\
                .read("Social Security/ Individual Taxpayer Registration")\
                .read_email("Company email")\
                .read("Country")\
                .read("State")\
                .read("City")\
                .read("Address")\
                .read("Address number")\
                .read("Address Complement", required=False)\
                .read("District")\
                .read("Zip code")\
                .read("Bank Name")\
                .read("Bank account number")\
                .read("Bank branch code")\
                .read("Legal entities number", required=False)\
                .read("Company name", required=False)\
                .read("Company state", required=False)\
                .read("Company city", required=False)\
                .read("Company address", required=False)\
                .read("Company address number", required=False)\
                .read("Company address complement", required=False)\
                .read("Company district", required=False)\
                .read("Company zip code", required=False)\
                .read("Shirt size")\
                .read("Dietary restrictions", required=False)\
                .run("Send")

    name, personal_email, start_date, position, birth_date, phone_number, id_number,\
    id_emited_by, id_taxpayer, company_email, country, state, city, address, number_address,\
    complement_address, district, zip_code, bank_name, bank_account_number, bank_branch_code, legal_entity_number,\
    name_company, state_company, city_company, company_address, company_number_address,\
    company_complement_address, company_district, company_zip_code, shirt_size, dietary_restrictions = member.values()

    start_date = preprocessing_date(start_date)
    birth_date = preprocessing_date(birth_date)
    phone_number = phone_number.raw

    # Here you'll need to set your database's query statement in order to properly update it
    # We'll continue this example without doing so to keep the data stable

    # team_statement = tables.statement(id="your_statement_id")

    # result = team_statement.run(params={"name": name, "email": personal_email, "created_at": start_date,\
    #                                     "position": position, "birth_date": birth_date, "phone_number": phone_number,\
    #                                     "identification_number": id_number, "id_emited_by": id_emited_by,\
    #                                     "taxpayer_id": id_taxpayer, "company_email": company_email, "country": country,\
    #                                     "state": state, "city": city, "address": address, "number_address": number_address,\
    #                                     "complement_address": complement_address, "district": district, "zip_code": zip_code,\
    #                                     "shirt_size": shirt_size, "dietary_restrictions": dietary_restrictions})


    # bank_statement = tables.statement(id="your_statement_id")
    # bank_statement.run(params={"bank_name": bank_name, "number": bank_account_number,\
    #                            "branch_code": bank_branch_code, "team_id": result[0]["id"]})

    # if name_company is not None:
    #     entity_statement = tables.statement(id="your_statement_id")
    #     entity_statement.run(params={"entity_number": legal_entity_number, "name_company": name_company,\
    #                                 "state_company": state_company, "city_company": city_company,\
    #                                 "company_address": company_address, "company_number_address": company_number_address,\
    #                                 "company_complement_address": company_complement_address, "company_district": company_district,\
    #                                 "company_zip_code": company_zip_code, "team_id": result[0]["id"]})
                            
    display("Congrats on the new team member! Their info has added to your database.", button_text = "See you next time")

elif registration == "update_member":

    team_informations = convert_db_to_dropdown_format("name", "id", "9952fc39-7f93-470d-b2a4-2f846d0d290a")
    
    team_member_id = read_dropdown("Which member of team do you want to update data on?", team_informations)

    member = Page().display("Perfect. Please update the information you need below:")\
                .read_email("Personal Email", required=False)\
                .read_date("Start date at company", required=False)\
                .read("Position", required=False)\
                .read_date("Birth date", required=False)\
                .read_phone("Phone Number", required=False)\
                .read("National ID number", required=False)\
                .read("ID number emited by", required=False)\
                .read("Social Security/ Individual Taxpayer Registration", required=False)\
                .read_email("Company email", required=False)\
                .read("Country", required=False)\
                .read("State", required=False)\
                .read("City", required=False)\
                .read("Address", required=False)\
                .read("Address number", required=False)\
                .read("Address Complement", required=False)\
                .read("District", required=False)\
                .read("Zip code", required=False)\
                .read("Bank Name", required=False)\
                .read("Bank account number", required=False)\
                .read("Bank branch code", required=False)\
                .read("Legal entities number", required=False)\
                .read("Company name", required=False)\
                .read("Company state", required=False)\
                .read("Company city", required=False)\
                .read("Company address", required=False)\
                .read("Company address number", required=False)\
                .read("Company address Complement", required=False)\
                .read("Company district", required=False)\
                .read("Company zip code", required=False)\
                .read("Shirt size", required=False)\
                .read("Dietary restrictions", required=False)\
                .read_date("Departure date", required=False)\
                .run("Send")


    personal_email, start_date, position, birth_date, phone_number, id_number,\
    id_emited_by, id_taxpayer, company_email, country, state, city, address, number_address,\
    complement_address, district, zip_code, bank_name, bank_account_number, bank_branch_code, legal_entity_number,\
    name_company, state_company, city_company, company_address, company_number_address,\
    company_complement_address, company_district, company_zip_code, shirt_size, dietary_restrictions, departure_date = member.values()

    start_date = preprocessing_date(start_date)
    birth_date = preprocessing_date(birth_date)
    if phone_number != None:
        phone_number = phone_number.raw
    departure_date = preprocessing_date(departure_date)

    # Here you'll need to set your database's query statement in order to properly update it
    # We'll continue this example without doing so to keep the data stable

    # statement = tables.statement(id="your_statement_id")

    # result = statement.run(params={"email": personal_email, "created_at": start_date, "position": position,\
    #                                "birth_date": birth_date, "phone_number": phone_number, "identification_number": id_number,\
    #                                "id_emited_by": id_emited_by, "taxpayer_id": id_taxpayer, "company_email": company_email,\
    #                                "country": country, "state": state, "city": city, "address": address,\
    #                                "number_address": number_address, "complement_address": complement_address,\
    #                                "district": district, "zip_code": zip_code, "shirt_size": shirt_size,\
    #                                "dietary_restrictions": dietary_restrictions,\
    #                                "exit_date":departure_date, "team_member_id": team_member_id})
    
    # bank_statement = tables.statement(id="your_statement_id")
    # bank_statement.run(params={"name": bank_name, "number": bank_account_number,\
    #                                 "branch_code": bank_branch_code, "team_member_id": team_member_id})


    # entity_statement = tables.statement(id="your_statement_id")
    # entity_statement.run(params={"entity_number": legal_entity_number, "name": name_company,\
    #                              "state": state_company, "city": city_company,\
    #                              "address": company_address, "number_address": company_number_address,\
    #                              "complement_address": company_complement_address, "district": company_district,\
    #                              "zip_code": company_zip_code, "team_member_id": team_member_id})

    display("Great! The team member's info has been updated.", button_text = "See you next time")
