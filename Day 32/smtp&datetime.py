# import smtplib
# my_email = 'gghabade@gmail.com'
# password = 'inlf ubab tkbc ybwi'
#
# connection = smtplib.SMTP('smtp.gmail.com')
# connection.starttls()
# connection.login(user=my_email, password=password)
# connection.sendmail(
#     from_addr=my_email,
#     to_addrs='adityaghabade26@gmail.com',
#     msg="Subject:Hello\n\nThis is the body of the email")
# connection.close()

# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)
#
# dob = dt.datetime(year=1995,month = 11,day = 16,hour = 9,minute = 48,second = 59)
# print(dob)

import smtplib
import datetime as dt
import random

my_email = 'gghabade@gmail.com'
password = 'inlf ubab tkbc ybwi'

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 5:
    with open('quotes.txt') as quotes:
        all_quotes = quotes.readlines()
        quote = random.choice(all_quotes)
    print(quote)
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,to_addrs=my_email,msg=f"Subject:Hello World!\n\n{quote}")