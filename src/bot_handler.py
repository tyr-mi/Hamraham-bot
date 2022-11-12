from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import sqlite3
import os
import random
from helpers.poem_repository import PoemRepository

updater = Updater("5583347821:AAHrlqHXfyIMJ880PRqFUvX-b8WXh6jt6-k",
                  use_context=True)
  
def start(update: Update, context: CallbackContext):
    repository = PoemRepository()
    poem = repository.retrieve_poem()
    update.message.reply_text(poem)

updater.dispatcher.add_handler(CommandHandler('start', start))

updater.start_polling()