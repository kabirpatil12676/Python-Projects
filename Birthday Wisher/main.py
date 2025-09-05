##################### Normal Starting Project ######################
# import pandas
# import random
# import smtplib
# import datetime
#
# now = datetime.datetime.now()
# today = (now.month,now.day)
#
#
# data = pandas.read_csv("birthdays.csv")
# birthday_dict = {(data_row["month"],data_row["day"]):data_row for (index,data_row) in data.iterrows()}
#
#
# if today in birthday_dict:
#     birthday_person = birthday_dict[today]
#     with open(f"./letter_templates/letter_{random.randint(1,3)}.txt") as letter:
#         contents = letter.read()
#         new_letter = contents.replace("[NAME]",birthday_person["name"])
#
#     my_mail = "pythontest12676@gmail.com"
#     password = "htjsfstejqdvyvjk"
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(user=my_mail,password=password)
#         connection.sendmail(from_addr=my_mail,to_addrs=birthday_person["email"],msg=f"Subject:Happy BirthDay! \n\n {new_letter}")





































#HINT 4: Then you could compare and see if today's month/day tuple matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If there is a match, pick a random letter (letter_1.txt/letter_2.txt/letter_3.txt) from letter_templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT 1: Think about the relative file path to open each letter. 
# HINT 2: Use the random module to get a number between 1-3 to pick a randome letter.
# HINT 3: Use the replace() method to replace [NAME] with the actual name. https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT 1: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
# HINT 2: Remember to call .starttls()
# HINT 3: Remember to login to your email service with email/password. Make sure your security setting is set to allow less secure apps.
# HINT 4: The message should have the Subject: Happy Birthday then after \n\n The Message Body.



