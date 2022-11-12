import fractions
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime
from spy import *
import sympy
import re


def menu_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text('Введите через / выбранную функцию: ')
    update.message.reply_text(f'Сумма многочлена\n/sum_poly\n(пример, /sum_poly\nx^2+5*x+2\nx^2-5*x+3)')
    
    
def sum_poly_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg) 
    items = msg.split('\n') #запись через shift enter 
    poly1 = sympy.polys.polytools.poly_from_expr(str(items[1]))[0]
    poly2 = sympy.polys.polytools.poly_from_expr(str(items[2]))[0]
    polysum = poly1+poly2
    a = str(polysum.as_expr()).replace('**', '^')+' = 0'
    update.message.reply_text(f'{a}')
   
   

   