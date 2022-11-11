from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from bot_commands import *


updater = Updater('Token')


updater.dispatcher.add_handler(CommandHandler('menu', menu_command))
updater.dispatcher.add_handler(CommandHandler('sum_poly', sum_poly_command))


print('server start')
updater.start_polling()
updater.idle()