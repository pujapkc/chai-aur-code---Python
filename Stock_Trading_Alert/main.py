import requests
from datetime import datetime

# -------------------- CONFIG -------------------- #

STOCK_NAME = "NVIDIA Corporation"
STOCK_SYMBOL = "NVDA"
COMPANY_NAME = "NVIDIA"

STOCK_API_KEY = "WC1UKY5O05LZ07XT"
NEWS_API_KEY = "41df4ef5f1064a86954b52c76fbe0a37"

TELEGRAM_BOT_TOKEN = "8517768812:AAHmP9p4jF4IAIA7uHOqVWYqptsg2j0OQMg"
CHAT_ID = "920417404"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# -------------------- STEP 1: GET STOCK DATA -------------------- #

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_SYMBOL,
    "apikey": STOCK_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]

data_list = [value for (key, value) in data.items()]

yesterday_data = data_list[0]
yesterday_closing_price = float(yesterday_data["4. close"])

day_before_data = data_list[1]
day_before_closing_price = float(day_before_data["4. close"])

difference = yesterday_closing_price - day_before_closing_price
up_down = "🔺" if difference > 0 else "🔻"

diff_percent = round((difference / day_before_closing_price) * 100, 2)

# -------------------- STEP 2: IF SIGNIFICANT CHANGE -------------------- #

if abs(diff_percent) > 0:

    news_params = {
        "q": COMPANY_NAME,
        "apiKey": NEWS_API_KEY,
        "sortBy": "publishedAt",
        "language": "en",
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"][:3]

    formatted_articles = [
        f"{STOCK_SYMBOL}: {up_down}{abs(diff_percent)}%\n"
        f"Headline: {article['title']}\n"
        f"Brief: {article['description']}\n"
        for article in articles
    ]

    # -------------------- STEP 3: SEND TELEGRAM MESSAGE -------------------- #

    for article in formatted_articles:
        telegram_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

        telegram_params = {
            "chat_id": CHAT_ID,
            "text": article,
        }

        requests.get(telegram_url, params=telegram_params)

    print("Alert Sent Successfully 🚀")

else:
    print("No significant stock movement.")
