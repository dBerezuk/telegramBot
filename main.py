import os

import telebot
from dotenv import load_dotenv
from youtube import Youtube

load_dotenv()

bot = telebot.TeleBot(os.getenv("TOKEN"))

#команда start
@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Введите url на любой канал в ютубе и вы получите всю информацию о канале")

# ввод url
@bot.message_handler(content_types=['text'])
def url(message):
    youtube = Youtube()
    youtubeDate = youtube.channelData(message.text)

    bot.send_message(message.chat.id, f"Имя канала: <b>{youtubeDate['name']}</b>\nКоличество видео на канале: <b>{youtubeDate['videCount']}</b>\nКоличество подписчиков на канале: <b>{youtubeDate['subscribersCount']}</b>\nДата создание канала: <b>{youtubeDate['regDate']}</b>\nКоличество всего просмотров на канале: <b>{youtubeDate['viewCountAll']}</b>", parse_mode="html")


if __name__ == "__main__":
    bot.polling()






