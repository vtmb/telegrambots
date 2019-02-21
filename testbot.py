import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove

updater = Updater(token="das token vom bot")
dispatcher = updater.dispatcher

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

GENDER = range(1)

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Bot wurde gestartet!")


def info(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Infos folgen")


def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)


def caps(bot, update, args):
    text_caps = "".join(args).upper()
    bot.send_message(chat_id=update.message.chat_id, text=text_caps)


# creating handlers
start_handler: CommandHandler = CommandHandler("start", start)
info_handler: CommandHandler = CommandHandler("info", info)
message_handler: MessageHandler = MessageHandler(Filters.text, echo)
caps_handler: CommandHandler = CommandHandler("caps", caps, pass_args=True)

# adding closures to dispatcher
dispatcher.add_handler(start_handler)
dispatcher.add_handler(info_handler)
dispatcher.add_handler(message_handler)
dispatcher.add_handler(caps_handler)

# start bot

updater.start_polling()
