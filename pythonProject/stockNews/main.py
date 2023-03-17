import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHA_KEY = "8QXFR0EOWOR22QAJ"
RATES_URL = "https://www.alphavantage.co/query"
NEWS_API_KEY = "d95fde7c3c5e4127b7b2bd345883019b"

stocks_parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": ALPHA_KEY
}


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#READY

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

def get_daily_values():
    response =requests.get(url=RATES_URL, params=stocks_parameters)
    response.raise_for_status()
    values = response.json()["Time Series (Daily)"]
    values_list = list(values.items())[:2]
    yesterday_close = float(values_list[0][1]['4. close'])
    day_before_close = float(values_list[1][1]['4. close'])
    print(values_list[0][0])
    delta = round((yesterday_close/day_before_close - 1) * 100, 2)
    if delta < 0:
        result = f"🔻{abs(delta)}%"
    else:
        result = f"🔺{abs(delta)}%"
    send_message(result)
    if abs(delta) >= 5:
        get_news(values_list[1][0])

def get_news(yesterday_date):
    url = f"https://newsapi.org/v2/everything?" \
           f"q={STOCK}&" \
           f"from={yesterday_date}&" \
           f"pageSize=3&" \
           f"apiKey={NEWS_API_KEY}"
    print(url)
    response = requests.get(url=url)
    response.raise_for_status()
    news = response.json()["articles"]
    for article in news:
        message = f"Title: {article['title']}\n" \
                  f"Description: {article['description']}\n" \
                  f"Link: {article['url']}"
        send_message(message)

def send_message(bot_message):
    bot_token = '5946329067:AAGqI1azQNi_aTxiV-BzhWWaVPPew7-epSw'
    bot_chatID = '172133786'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)

get_daily_values()
