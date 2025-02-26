import smtplib

import datetime as dt
import random

my_email = 'tranjan638@gmail.com'
my_password = 'hzuokviypkxubfzw'

now = dt.datetime.now()
weekday = now.weekday()
print(weekday)
with open('quotes.txt') as quote_file:
    all_quotes = quote_file.readlines()
    quote = random.choice(all_quotes)
    print(quote)
    
subject = "A Special Note for You Baabayyy ❤️ "
message = f"Subject: {subject}\n\n{quote}"

with smtplib.SMTP("smtp.gmail.com",587) as connection:
    connection.starttls()
    connection.login(user=my_email,password ='hzuokviypkxubfzw')
    connection.sendmail(from_addr = my_email, to_addrs = 'rijalsamixa@gmail.com', msg = message.encode("utf-8"))
    connection.close()