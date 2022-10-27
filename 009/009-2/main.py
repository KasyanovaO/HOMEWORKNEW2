from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from bot_commands import *


updater = Updater('Token')


updater.dispatcher.add_handler(CommandHandler('menu', menu_command))
updater.dispatcher.add_handler(CommandHandler('sum_rat', sum_rat_command))
updater.dispatcher.add_handler(CommandHandler('sub_rat', sub_rat_command))
updater.dispatcher.add_handler(CommandHandler('mult_rat', mult_rat_command))
updater.dispatcher.add_handler(CommandHandler('div_rat', div_rat_command))
updater.dispatcher.add_handler(CommandHandler('sum_complex', sum_complex_command))
updater.dispatcher.add_handler(CommandHandler('sub_complex', sub_complex_command))
updater.dispatcher.add_handler(CommandHandler('mult_complex', mult_complex_command))
updater.dispatcher.add_handler(CommandHandler('div_complex', div_complex_command))

print('server start')
updater.start_polling()
updater.idle()