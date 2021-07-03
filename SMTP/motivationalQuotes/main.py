import smtplib
import datetime as dt
import random

# objective 1
NOW = dt.datetime.now()
weekday = NOW.weekday()
print(weekday)

# objective 2
a = 5
quotation = []
with open("quotes.txt", "r") as quote:
    for i in quote:
        quotation.append(i)

    if weekday == 5:
        Random_quote = random.choice(quotation)
        my_email = "nallidenny.pip@gmail.com"
        my_password = "DK.python100"
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="nallidenny@gmail.com",
                            msg=f"subject:MOTIVATIONAL QUOTATION\n\n{Random_quote}")
        connection.close()
