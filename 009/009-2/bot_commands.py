import fractions
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime
from spy import *
from fractions import Fraction


def menu_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text('Введите через / выбранную функцию: ')
    update.message.reply_text(f'Рациональные числа\n/sum_rat\n/sub_rat\n/mult_rat\n/div_rat\n(пример, /sum_rat 1/2 1/2)')
    update.message.reply_text(f'Комплексные числа\n/sum_complex\n/sub_complex\n/mult_complex\n/div_complex\n(пример, /div_complex 1+2j 2+4j)')
    

def sum_rat_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg) 
    items = msg.split()  
    x = fractions.Fraction(str(items[1]))
    y = fractions.Fraction(str(items[2]))
    update.message.reply_text(f'{x} + {y}={x+y}')

def sub_rat_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = fractions.Fraction(str(items[1]))
    y = fractions.Fraction(str(items[2]))
    update.message.reply_text(f'{x} - {y}={x-y}')

def mult_rat_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = fractions.Fraction(str(items[1]))
    y = fractions.Fraction(str(items[2]))
    update.message.reply_text(f'{x} * {y}={x*y}')

def div_rat_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = fractions.Fraction(str(items[1]))
    y = fractions.Fraction(str(items[2]))
    update.message.reply_text(f'{x} / {y}={x/y}')

def sum_complex_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg) 
    items = msg.split()  
    x = complex(str(items[1]))
    y = complex(str(items[2]))
    update.message.reply_text(f'{x} + {y}={x+y}')

def sub_complex_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg) 
    items = msg.split()  
    x = complex(str(items[1]))
    y = complex(str(items[2]))
    update.message.reply_text(f'{x} - {y}={x-y}')

def mult_complex_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg) 
    items = msg.split()  
    x = complex(str(items[1]))
    y = complex(str(items[2]))
    update.message.reply_text(f'{x} * {y}={x*y}')

def div_complex_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg) 
    items = msg.split()  
    x = complex(str(items[1]))
    y = complex(str(items[2]))
    update.message.reply_text(f'{x} / {y}={x/y}')






