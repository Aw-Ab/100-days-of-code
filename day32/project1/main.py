import smtplib
import datetime as dt
import random


current_date = dt.datetime.now()

my_email = "someone@outlook.com"
my_password = "***********"
rec_email = "someone@yahoo.com"
print(current_date.weekday())
if current_date.weekday() == 1 :
    with open("quotes.txt", 'r') as file:
        quotes = file.readlines()
        today_quote = random.choice(quotes)
    with smtplib.SMTP("smtp-mail.outlook.com") as connection:
        connection.starttls()
        connection.login(user=rec_email , password= my_password)
        connection.sendmail(from_addr=rec_email ,to_addrs=my_email ,msg=f"Subject:Monday's quote\n\n{today_quote}")

