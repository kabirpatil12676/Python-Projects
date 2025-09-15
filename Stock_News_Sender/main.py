import requests

from twilio.rest import Client


STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API = ""
NEWS_API = ""
account_sid = ""
auth_token = ""


params = {
    "function" : "TIME_SERIES_DAILY" ,
    "symbol" : STOCK_NAME ,
    "apikey" : STOCK_API ,

}

parameters = {
    "q" : STOCK_NAME,
    "apiKey" : NEWS_API,

}

response = requests.get(STOCK_ENDPOINT,params =params)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]

data_list = [value for (date, value) in data.items()]

#Yesturdays closing Price
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
# print(yesterday_closing_price)

#Day before Yesterday Closing price
day_before_data = data_list[1]
day_before_closing_price = day_before_data["4. close"]
# print(day_before_closing_price)


# Percentage of difference in stocks
diff = float(yesterday_closing_price) - float(day_before_closing_price)
up_down = None
if diff > 0:
    up_down = "⬆️"
else:
    up_down = "⬇️"

diff_percent = round((diff / float(yesterday_closing_price) )* 100)

if abs(diff_percent) > 5:
    parameters = {
        "qInTitle": STOCK_NAME,
        "apiKey": NEWS_API,
    }
    response  = requests.get(NEWS_ENDPOINT,params=parameters)
    articles = response.json()["articles"]
    three_articles = articles[:3]

    formatted_articles_list = [f"{STOCK_NAME}:{up_down}{diff_percent}% \nHeadline: {article ['title']}. \nBrief: {article ['description']}" for article in three_articles]
    client = Client(account_sid, auth_token)
    for article in formatted_articles_list:
        message = client.messages.create(
            messaging_service_sid='MGb56250f0394ba432376989a1dbc97500',
            body= article,
            to='+917517415161'
        )
        print(message.sid)










    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

#TODO 2. - Get the day before yesterday's closing stock price

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

    ## STEP 2: https://newsapi.org/
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number.

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio.



#Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""













# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press F9 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')


