import telebot
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "🤖 Bot is live and ready! Welcome!")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.send_message(message.chat.id, f"🔁 You said: {message.text}")

if __name__ == "__main__":
    print("✅ Bot is running...")
    bot.polling(non_stop=True)
