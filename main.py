import bot_messages as b_m
import config
import correct_message_checker as cms
import phraze_synthesizer
import telebot
import time
import wiki_parser


bot = telebot.TeleBot(config.secrets["tg"]["token"])


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, b_m.welcome_message)


@bot.message_handler(content_types=['text'])
def get_text_message(message):
    text = message.text.lower()
    if cms.check_message(text):
        f = wiki_parser.get_date_fact(text)
        phraze_synthesizer.make_voice_file(f)
        with open('speech.ogg', "rb") as audio:
            bot.send_audio(message.chat.id, audio)
    else:
        bot.send_message(message.chat.id, b_m.bad_input_message)


if __name__ == '__main__':
    while True:
        try:
            bot.polling()
        except Exception as e:
            print(e)
            time.sleep(5)

