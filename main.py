import telebot
import time
import sys
import os

bot = telebot.TeleBot('1152345546:AAH0m8CDNkNwqNlnk19EY7qZrPbZlA3kK5c')


@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    bot.send_message(message.chat.id, "Готов к работе!")


@bot.message_handler(content_types=['text'])
def start_message(message):
    print(message.text, message.chat.id)


# костыли на дисконект
while True:
    try:
        bot.polling(none_stop=True)
        print("************************************************")
    except Exception as e:
        print(e)  # или просто print(e) если у вас логгера нет,
        # или import traceback; traceback.print_exc() для печати полной инфы
        print(time)
        time.sleep(3)
        """Restarts the current program.
            Note: this function does not return. Any cleanup action (like
            saving data) must be done before calling this function."""
        python = sys.executable
        os.execl(python, python, *sys.argv)