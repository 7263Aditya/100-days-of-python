import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

account_sid = 'AC3ae0ca724d3eadd91b6dae7e2944676'
auth_token = 'c6d04c5158b439ffa5ffec758a8e12f'

STOCK_API_KEY = '3CJW8DIRH3FBR8HW'
NEWS_API_KEY = '8ac69aca08224f5eac16ef1bef3d0041'

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": '3CJW8DIRH3FBR8HW',
}
response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

# Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_closing_price = day_before_yesterday_data["4. close"]
print(day_before_closing_price)

# Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20
difference = float(yesterday_closing_price) - float(day_before_closing_price)
print(abs(difference))

up_down = None
if difference > 0:
    up_down = '🔺'
else:
    up_down = '🔻'
    
# Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percent = round((difference / float(yesterday_closing_price)) * 100)
print(diff_percent)

# Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
if abs(diff_percent) > 4:
    news_params = {
        'apiKey': NEWS_API_KEY,
        'qInTitle': COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]

# Use Python slice operator to create a list that contains the first 3 articles.
    three_articles = articles[:3]
    print(three_articles)

# Create a new list of the first 3 article's headline and description using list comprehension.
    formatted_articles = [f"{STOCK_NAME}: {up_down}{abs(diff_percent)}% \nHeadline:{articles['title']}. \nBrief: {articles['description']}" for articles in three_articles]

# Send each article as a separate message via Twilio.
    client = Client(account_sid, auth_token)
    
    def send_alert(message_body):
        message = client.messages.create(
            from_='whatsapp:+14155238886',  # Use your specific Sandbox number
            body=message_body,
            to='whatsapp:+917263970149'  # Your verified WhatsApp number
        )
        print(f"Message Sent! SID: {message.sid}")

    for article in formatted_articles:
        send_alert(article)