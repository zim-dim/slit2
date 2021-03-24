#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging
from telegram     import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler,CallbackQueryHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


LINK = https://github.com/zim-dim/slit2/tree/main/data/


def read_content_from_url(file):
    url_file = LINK +file
    f = urllib.request.urlopen(url_file)
    text =f.read().decode(encoding = 'utf-8') 
    return text





# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    content ='Привіт! Цей чат-бот допоможе тобі познайомитися з кафедрою ближче. \
              Ти дізнаєшся про викладачів, спеціальності, додаткові можливості для студентів та умови вступу. \
              Обери, будь-ласка, теми, які тобі цікаві'
    kb_start = [
        [InlineKeyboardButton('Кафедра КМАД' ,callback_data ='kafedra_kmad')],
        [InlineKeyboardButton('Можливості студенту', callback_data ='moglivosti_studenta')],
        [InlineKeyboardButton('Умови вступу' ,callback_data ='umovy_vstupu')]
        ]
    reply = InlineKeyboardMarkup(kb_start)

    update.message.reply_text(content, reply_markup=reply)

    

def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)










#KAFEDRA_KMAD ФУНКЦИИ

def vykladach(update,context):
    content = read_content_from_url('vykladach.txt')
    update.callback_query.message.reply_text(content, parse_mode='Markdown')

def vidmin_kaf(update,context):
    content = read_content_from_url('vidmin_kaf.txt')
    update.callback_query.message.reply_text(content, parse_mode='Markdown')

def hist_kaf(update,context):
    content = read_content_from_url('hist_kaf.txt')
    update.callback_query.message.reply_text(content, parse_mode='Markdown')

def aud_kaf(update,context):
    content = read_content_from_url('aud_kaf.txt')
    update.callback_query.message.reply_text(content, parse_mode='Markdown')

def n_vypuskniki(update,context):
    content = read_content_from_url('n_vypuskniki.txt')
    update.callback_query.message.reply_text(content, parse_mode='Markdown')





#EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEND......................












#MOGLIVOSTI_STUDENTA ФУНКЦИИИ

def prokt_study(update,context):
    content = read_content_from_url('prokt_study.txt')
    update.callback_query.message.reply_text(content, parse_mode='Markdown')

def dual_osv(update,context):
    content = read_content_from_url('dual_osv.txt')
    update.callback_query.message.reply_text(content, parse_mode='Markdown')

def praq_vlascht(update,context):
    content = read_content_from_url('praq_vlascht.txt')
    update.callback_query.message.reply_text(content, parse_mode='Markdown')

def prakt(update,context):
    content = read_content_from_url('prakt.txt')
    update.callback_query.message.reply_text(content, parse_mode='Markdown')



#EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEND.......................................














#UMOVY_VSTUPU ФУНКЦИИ

def konk_pred_ZNO(update,context):
    content =  read_content_from_url('konk_pred_ZNO.txt')
    update.callback_query.message.reply_text(content, parse_mode='Markdown')

def pozp_konk_bal(update,context):
    content =  read_content_from_url('pozp_konk_bal.txt')
    update.callback_query.message.reply_text(content, parse_mode='Markdown')

def etap_vstup_komp(update,context):
    content = read_content_from_url('etap_vstup_komp.txt')
    update.callback_query.message.reply_text(content, parse_mode='Markdown')

def kor_pos(update,content):
    content = read_content_from_url('kor_pos.txt')
    update.callback_query.message.reply_text(content, parse_mode='Markdown')

def mt_budj_kont_mt_vstup(update,context):
    content = read_content_from_url('mt_budj_kont_mt_vstup.txt')
    update.callback_query.message.reply_text(content, parse_mode='Markdown')


#EEEEEEEEEEEEEEEEEEEEEND......................











def kafedra_kmad(update, context):
    content ='З чого почнемо?'

    kaf_start=[
        [InlineKeyboardButton('Викладачі',callback_data='vykladach')],
        [InlineKeyboardButton('Відмінності кафедри',callback_data='vidmin_kaf')],
        [InlineKeyboardButton('Історія кафедри (фото)',callback_data='hist_kaf')],
        [InlineKeyboardButton('Аудиторії кафедри(фото)',callback_data='aud_kaf')],
        [InlineKeyboardButton('Наші випускники(Картинка с лого компаний как в ролике)',callback_data='n_vypuskniki')]
        ]
    replud = InlineKeyboardMarkup(kaf_start)

    update.callback_query.message.reply_text(content, reply_markup = replud)






def moglivosti_studenta(update,context):
    content ='У нас є багато можливостей для студентів. З чого почнемо?'

    mog_start=[
        [InlineKeyboardButton('Проєктне навчання',callback_data='prokt_study')],
        [InlineKeyboardButton('Дуальна освіта (Картинка с лого компаний-партнеров',callback_data='dual_osv')],
        [InlineKeyboardButton('Працевлаштування',callback_data='praq_vlascht')],
        [InlineKeyboardButton('Практика',callback_data='prakt')]
        ]
    rexud = InlineKeyboardMarkup(mog_start)

    update.callback_query.message.reply_text(content, reply_markup = rexud)








def umovy_vstupu(update,context):
    content ='Обери підпункт, який тобі цікавий'

    um_start =[
        [InlineKeyboardButton('Конкурсні предмети ЗНО',callback_data='konk_pred_ZNO')],
        [InlineKeyboardButton('Розрахунок конкурсного балу',callback_data='pozp_konk_bal')],
        [InlineKeyboardButton('Етапи вступної кампанії',callback_data='etap_vstup_komp')],
        [InlineKeyboardButton('Корисні посилання',callback_data='kor_pos')],
        [InlineKeyboardButton('Кількість бюджетних та контрактних місць для вступників',callback_data='mt_budj_kont_mt_vstup')]
        ]
    replied = InlineKeyboardMarkup(um_start)

    update.callback_query.message.reply_text(content, reply_markup = replied)



def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("1696273550:AAFRj9BxWQHbYrfXeyYNIZoZ1CLsZyCW2hQ", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CallbackQueryHandler(kafedra_kmad,
                                        pattern = 'kafedra_kmad'))
    dp.add_handler(CallbackQueryHandler(moglivosti_studenta,
                                        pattern ='moglivosti_studenta')) 
    dp.add_handler(CallbackQueryHandler(umovy_vstupu,
                                        pattern ='umovy_vstupu'))




    #kafedra_kmad
    dp.add_handler(CallbackQueryHandler(vykladach,
                                        pattern ='vykladach'))

    dp.add_handler(CallbackQueryHandler(vidmin_kaf,
                                        pattern ='vidmin_kaf'))

    dp.add_handler(CallbackQueryHandler(hist_kaf,
                                        pattern ='hist_kaf'))

    dp.add_handler(CallbackQueryHandler(aud_kaf,
                                        pattern ='aud_kaf'))

    dp.add_handler(CallbackQueryHandler(n_vypuskniki,
                                        pattern ='n_vypuskniki'))


    #djfdsfusdu

    #moglivosti_studenta
    dp.add_handler(CallbackQueryHandler(prokt_study,
                                        pattern ='prokt_study'))

    dp.add_handler(CallbackQueryHandler(dual_osv,
                                        pattern ='dual_osv'))

    dp.add_handler(CallbackQueryHandler(praq_vlascht,
                                        pattern ='praq_vlascht'))

    dp.add_handler(CallbackQueryHandler(prakt,
                                        pattern ='prakt'))




    #cmvisndvndvu



    #umovy_vstupu
    dp.add_handler(CallbackQueryHandler(konk_pred_ZNO,
                                        pattern ='konk_pred_ZNO'))
    dp.add_handler(CallbackQueryHandler(pozp_konk_bal,
                                        pattern ='pozp_konk_bal'))
    dp.add_handler(CallbackQueryHandler(etap_vstup_komp,
                                        pattern ='etap_vstup_komp'))
    dp.add_handler(CallbackQueryHandler(kor_pos,
                                        pattern ='kor_pos'))
    dp.add_handler(CallbackQueryHandler(mt_budj_kont_mt_vstup,
                                        pattern ='mt_budj_kont_mt_vstup'))

     #dfdua
    
    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
