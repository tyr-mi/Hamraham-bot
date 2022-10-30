from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import sqlite3
import os
import random

updater = Updater("5583347821:AAHrlqHXfyIMJ880PRqFUvX-b8WXh6jt6-k",
                  use_context=True)
  

def get_db_connection():
    connection = sqlite3.connect("src" + os.sep + "Hafez.db")
    return connection

def start(update: Update, context: CallbackContext):
    connection = get_db_connection()
    selected_poem = random.randint(0,415)
    query = "SELECT TEXT FROM poems WHERE id = " + str(selected_poem)
    cur = connection.cursor()
    cur.execute(query)
    poem = cur.fetchone()[0]
    print(poem)
    update.message.reply_text(poem)

updater.dispatcher.add_handler(CommandHandler('start', start))

updater.start_polling()