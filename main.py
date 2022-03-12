import datetime as dt
import pandas
import random
import smtplib

email = "sajidhasan23955@gmail.com"
password = "sajid1999"


today = (dt.datetime.now().month, dt.datetime.now().day)

data = pandas.read_csv("birthdays.csv")

birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open (file_path) as letter:
        text_file = letter.read()
        text_file = text_file.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(email, password)
        connection.sendmail(from_addr=email,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday\n\n{text_file}")



