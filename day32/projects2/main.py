##################### Extra Hard Starting Project ######################
import pandas
import datetime as dt
import random
import smtplib
# 1. Update the birthdays.csv

my_email = "someone@outlook.com"
my_password = "***********"
outlook_smtp = "smtp-mail.outlook.com"

birthdays = pandas.read_csv("birthdays.csv")
birthdays = birthdays.to_dict("records")

# 2. Check if today matches a birthday in the birthdays.csv
today = dt.datetime.today()
for person in birthdays :
    print(today.year , today.month , today.day)
    if today.month == person['month'] and today.day == person['day'] :
        num = random.randint(1,3)
        with open(f"letter_templates/letter_{num}.txt") as text :
            letter = text.read()
            letter = letter.replace(f"\n\n" , f"\n")
            letter = letter.replace("[NAME]" ,person['name'])
            print(letter)
        with   smtplib.SMTP(outlook_smtp) as connection :
            connection.starttls()
            connection.login(user=my_email , password=my_password)
            connection.sendmail(from_addr=my_email , to_addrs=person['email'] , msg=letter)




