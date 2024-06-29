import requests
from bs4 import BeautifulSoup
import time
import telebot

# Telegram bot settings
TELEGRAM_TOKEN = ''    # Replace with your Token
TELEGRAM_CHAT_ID = ''  # Replace with your chat ID
bot = telebot.TeleBot(TELEGRAM_TOKEN)

# Function to send notification to Telegram
def send_telegram_message(chat_id, message):
    bot.send_message(chat_id, message)

# Function to check price drop
def price_check(url, min_price, chat_id):
    try:
        while True:
            res = requests.get(url, timeout=5)
            content = BeautifulSoup(res.content, "html.parser")
            price_div = content.find('div', attrs={"class": ""}).text.strip()   #Add the class value in your Flipkart price div in inspect
            price = int(price_div.replace(",", "").replace("₹", "").strip())

            if price <= min_price:
                message = f"Price has dropped below ₹{min_price}. Current price is ₹{price}."
                send_telegram_message(chat_id, message)
            else:
                message = f"Price is ₹{price}. It has not dropped below ₹{min_price}."
                send_telegram_message(chat_id, message)
            
            # Wait for 30 minutes before checking again
            print("Checking again after 30 mins...")
            time.sleep(1800)
    
    except Exception as e:
        error_message = f"Error occurred while checking price: {e}"
        send_telegram_message(chat_id, error_message)
        print(error_message)
        time.sleep(1800)  # Retry after 30 minutes on error
        price_check(url, min_price, chat_id)

# Handler for the /start command
@bot.message_handler(commands=['start'])
def handle_start(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Welcome to Price Drop Alert Bot!\n\n"
                              "Please enter the complete link for the product to be monitored.")

    # Define inner handler for receiving the URL
    @bot.message_handler(func=lambda message: message.text.startswith('http'))
    def handle_url(message):
        url = message.text.strip()
        bot.send_message(chat_id, "Enter the minimum price (in ₹) to get notified for price drop:")

        # Define inner handler for receiving the minimum price
        @bot.message_handler(func=lambda message: message.text.isdigit())
        def handle_min_price(message):
            min_price = int(message.text.strip())
            bot.send_message(chat_id, f"Monitoring {url} for price drops below ₹{min_price}.")
            
            # Start price monitoring
            price_check(url, min_price, chat_id)

            # Clear handlers after use if not expecting further commands
            bot.remove_message_handler(handle_url)
            bot.remove_message_handler(handle_min_price)
    
    # Start listening for the URL input
    bot.register_next_step_handler(message, handle_url)

# Start the bot
bot.polling()
