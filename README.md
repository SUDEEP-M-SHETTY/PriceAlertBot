# Telegram Price Alert Bot for Flipkart Products

This Telegram bot helps you monitor the price of Flipkart products and sends notifications when the price drops below a specified threshold.

## Features

- **Real-time Price Monitoring:** Continuously checks the price of a specified Flipkart product.
- **Customizable Alerts:** Set a minimum price threshold to receive notifications when the price drops below that value.
- **Error Handling:** Handles errors gracefully and retries after a delay to ensure continuous monitoring.

## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library
- `telebot` library

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/sudeep-m-shetty/PriceAlertBot.git
   cd PriceAlertBot
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Obtain a Telegram Bot Token:
   - Create a new bot using [BotFather](https://core.telegram.org/bots#botfather).
   - Copy the token and replace `TELEGRAM_TOKEN` in the `bot.py` file.

4. Get your Telegram Chat ID:
   - Send a message to your bot from Telegram.
   - Replace `TELEGRAM_CHAT_ID` in the `bot.py` file with your chat ID.

## Usage

1. Start the bot:
   ```bash
   python bot.py
   ```

2. Use the bot:
   - Send the complete Flipkart product URL to the bot.
   - Enter the minimum price (in ₹) you want to be notified for.
   - The bot will start monitoring the price and notify you when it drops below the specified threshold.

## Contributing

Contributions are welcome! If you find any issues or want to enhance the bot, feel free to open an issue or create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
