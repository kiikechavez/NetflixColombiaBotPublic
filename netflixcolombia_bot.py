#!/usr/bin/env python
# pylint: disable=W0613, C0116
# type: ignore[union-attr]
# This program is dedicated to the public domain under the CC0 license.
# Programmer: brandon.chavez@udea.edu.co

"""
First, a few callback functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Example of a bot-user conversation using ConversationHandler.
Send /start to initiate the conversation.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""
from datetime import datetime, date, time, timedelta
import calendar
import random
import logging
from typing import Pattern

from telegram import user
from telegram.files.file import File
import prueba
import time
import telegram
import os
import gspread
import gspread.exceptions
import pandas as pd
from helper2 import sheet
from flask import Flask
# import requests
# from tkinter import *
# import math
#from oauth2client.service_account import ServiceAccountCredentials
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update, InlineKeyboardButton, InlineKeyboardMarkup, ChatAction
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
    CallbackQueryHandler
)

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

logging.getLogger("requests").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)

TOKEN = "YOUR_TOKEN_BOT_FROM_TELEGRAM_PROVIDED"

bot = telegram.Bot(token=TOKEN)

MICUENTA, CORREO, DESPEDIDA, PIN_JUANGUT, PIN_DANIACEVEDO, PIN_SOPHI, PIN_MARIAIG, PIN_CINDYB, PIN_GERALD, PIN_ESTEFASIERRA, PIN_KATEHDZ, CONVERSATION, PIN_KELISUAREZ, PIN_STIVEND, PIN_FABIAND, PIN_HORACIOA, PIN_ELKINCAR, PIN_KTBETANCUR, PIN_CAMISANCHEZ, PIN_DIANASAN, PIN_JOANANGA, PIN_BRARLYNNM, PIN_KARENF,PIN_DAVIDCHA, PIN_CLAUJIMENEZ, PIN_YIMAR, PIN_CLAULOPEZ, PIN_DIANAJIMENEZ, ANSWERYES, ANSWERNOT, PIN_VIVITORO, PIN_MANUELAMON, PIN_MAUROPATINO, PIN_HENRYMOSQUERA = range(34)

def start(update: Update, context: CallbackContext) -> int:
    #query = update.callback_query
    #query.answer()
    user = update.message.from_user
    logger.info(f'El usuario {user.first_name} {user.last_name}, ha iniciado una conversaci??n.')
    id = update.message.chat_id
    context.bot.sendMessage(chat_id= id, parse_mode= "HTML",
        text= f' ??Hola {user.first_name}???? Soy <b>Luan</b>!????????, agente virtual de <b>Netflix Colombia</b>. Para m?? es un placer atenderte.\n'
        'Estoy aqu?? para ayudarte con las <u>consultas b??sicas</u> de tus servicios.\n'
        'Puedes hacerme preguntas con frases cortas utilizando <u>estos comandos</u>:\n\n'
        '/start - Inicia la conversaci??n\n'
        '/micuenta - Informaci??n de mi cuenta\n'
        '/planes - ??Quiero adquirir una cuenta!\n'
        '/ayuda - Centro de ayuda\n'
        '/pago - Detalles de pago\n'
        '/recomendaciones - Te recomiendo series y pel??culas\n'
        '/promociones - Promociones vigentes\n'
        '/preguntas - Preguntas frecuentes\n'
        '/asesor - ??Quiero hablar con un asesor!\n'
        '/about - Acerca de <b>Netflix Colombia</b>\n'
        '/cancel - Finaliza la conversaci??n\n',
    )

    return ConversationHandler.END

def inicio(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    user = query.message.from_user
    logger.info(f'El usuario {user.first_name} {user.last_name}, ha iniciado una conversaci??n.')
    id = query.message.chat_id
    query.edit_message_text(parse_mode= "HTML",
        text= f' ??Hola {user.first_name}???? Soy <b>Luan</b>!????????, agente virtual de <b>Netflix Colombia</b>. Para m?? es un placer atenderte.\n'
        'Estoy aqu?? para ayudarte con las <u>consultas b??sicas</u> de tus servicios.\n'
        'Puedes hacerme preguntas con frases cortas utilizando <u>estos comandos</u>:\n\n'
        '/start - Inicia la conversaci??n\n'
        '/micuenta - Informaci??n de mi cuenta\n'
        '/planes - ??Quiero adquirir una cuenta!\n'
        '/ayuda - Centro de ayuda\n'
        '/pago - Detalles de pago\n'
        '/recomendaciones - Te recomiendo series y pel??culas\n'
        '/promociones - Promociones vigentes\n'
        '/preguntas - Preguntas frecuentes\n'
        '/asesor - ??Quiero hablar con un asesor!\n'
        '/about - Acerca de <b>Netflix Colombia</b>\n'
        '/cancel - Finaliza la conversaci??n\n',
    )

    return ConversationHandler.END


def pago(update: Update, context: CallbackContext) -> int:

    user = update.message.from_user
    logger.info(f'El usuario {user.first_name} {user.last_name}, ha solicitado la informaci??n de pago.')
    id = update.message.chat_id
    bot.sendChatAction(chat_id=id, action=ChatAction.TYPING, timeout=None)
    time.sleep(1)
    context.bot.sendMessage(chat_id=id, parse_mode="HTML",
        text=f'Hola {user.first_name}, te comparto la informaci??n de pago habilitada:\n\n'
        '<b>Netflix Colombia Soluciones</b>\n'
        'Cuenta de ahorros Bancolombia: <a href="https://sucursalpersonas.transaccionesbancolombia.com/" target="_blank">YOUR_PAYMENT_INFORMATION</a>\n'
        'Cuenta de ahorros Nequi o Daviplata: <a href="https://transacciones.nequi.com/" target="_self">YOUR_TELEPHONE_NUMBER</a>\n\n'
    )
    bot.sendChatAction(chat_id=id, action=ChatAction.TYPING, timeout=None)
    time.sleep(1)
    context.bot.sendMessage(chat_id= id, parse_mode= "HTML", text='Recuerde que el pago puede realizarlo de manera f??sica desde un corresponsal bancario correspondiente, '
    'desde la Sucursal Virtual o App personas.\n\n'
    'Puedes enviar tu comprobante de pago una vez realizado el mismo <a href="https://t.me/netflixcolombiaoficial" target="_self">aqu??</a>. ??Saludos!'
    )
    bot.sendChatAction(chat_id=id, action=ChatAction.TYPING, timeout=None)
    time.sleep(1)
    update.message.reply_text('/start para regresar al men?? principal.',
        reply_markup=ReplyKeyboardRemove(),
    
    )
    #return START

def planes(update: Update, context: CallbackContext) -> int:

    user = update.message.from_user
    id = update.message.chat_id
    logger.info(f'El usuario {user.first_name} {user.last_name}({id}), ha ingresado el comando /planes.')
    bot.sendChatAction(chat_id=id, action=ChatAction.TYPING, timeout=None)
    update.message.reply_text(
        '??En cu??l plan est??s interesado(a)?\n\n',
        reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton(text='Plan B??sico', callback_data='b??sico')],
        [InlineKeyboardButton(text='Plan Est??ndar', callback_data='est??ndar')],
        [InlineKeyboardButton(text='Plan Premium', callback_data='premium')]
        ])
    )

def recomendaciones(update: Update, context: CallbackContext):
    user = update.message.from_user
    logger.info(f'El usuario {user.first_name} {user.last_name}, ha ingresado al comando /recomendaciones.')
    id = update.message.chat_id
    bot.sendChatAction(chat_id=id, action=ChatAction.TYPING, timeout=None)
    update.message.reply_text("??Qu?? quieres que te recomiende?\n\n",
        reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton(text='Pel??culas', callback_data='pel??culas')],
        [InlineKeyboardButton(text='Series', callback_data='series')]
    ])
    )

def peliculas_call_handler(update, context):
    
    query = update.callback_query
    query.answer()

    user = query.message.from_user
    logger.info(f'El usuario {user.first_name} {user.last_name}, ha escogido la opci??n pel??culas.')
    id = query.message.chat_id
    bot.sendChatAction(chat_id=id, action=ChatAction.TYPING, timeout=None)
    time.sleep(2)
    query.edit_message_text(
        text='??Qu?? genero buscas?\n Secci??n: pel??culas\n\n'
        '- Acci??n\n'
        '- Anime\n'
        '- Ciencia Ficci??n\n'
        '- Cl??sicas\n'
        '- Colombianos\n'
        '- Comedias\n'
        '- De Hollywood\n'
        '- Deportes\n'
        '- Documentales\n'
        '- Dramas\n'
        '- Fantas??a\n'
        '- Fe y Espiritualidad\n'
        '- Independientes\n'
        '- Infantiles y familiares\n'
        '- Internacionales\n'
        '- Latinoamericanas\n'
        '- Los favoritos de la cr??tica\n'
        '- M??sica y musicales\n'
        '- Policiales\n'
        '- Romances\n'
        '- Terror\n'
        '- Thrillers'
        )
    bot.sendChatAction(chat_id=id, action=ChatAction.TYPING, timeout=None)
    time.sleep(1)
    query.message.reply_text('\nEscr??beme lo que buscas y con mucho gusto te ayudar??. ????')
    return ConversationHandler.END

def series_call_handler(update, context):

    query = update.callback_query
    query.answer()

    user = query.message.from_user
    logger.info(f'El usuario {user.first_name} {user.last_name}, ha escogido la opci??n series.')
    id = query.message.chat_id
    bot.sendChatAction(chat_id=id, action=ChatAction.TYPING, timeout=None)
    time.sleep(2)
    query.edit_message_text(
        text='??Qu?? genero buscas?\n Secci??n: Series\n\n'
        '- Acci??n\n'
        '- Animes\n'
        '- Asi??ticos\n'
        '- Brit??nicos\n'
        '- Ciencia Ficci??n\n'
        '- Ciencia y naturaleza\n'
        '- Comedias\n'
        '- Comedias de stand up\n'
        '- De adolescentes\n'
        '- De Colombia\n'
        '- De EEUU\n'
        '- Docuseries\n'
        '- Dramas\n'
        '- Infantiles\n'
        '- Latinoamericanas\n'
        '- Misterios\n'
        '- Policiales\n'
        '- Reality TV y entrevistas\n'
        '- Romances\n'
        '- Telenovelas\n'
        '- Terror\n'
        '- Thrillers'
        )
    bot.sendChatAction(chat_id=id, action=ChatAction.TYPING, timeout=None)
    time.sleep(1)
    query.message.reply_text('\nEscr??beme lo que buscas y con mucho gusto te ayudar??. ????')
    return ConversationHandler.END

def plan_basico(update: Update, context: CallbackContext) -> int:


    query = update.callback_query
    query.answer()

    user = query.message.from_user
    logger.info(f'El usuario {user.first_name} {user.last_name}, ha escogido el plan b??sico.')
    id = query.message.chat_id
    #query.message.reply_text('Te env??o la informaci??n pertinente al Plan B??sico.\n\n')
    
    # print(id)
    query.edit_message_text(
        text='Aqu?? te env??o toda la informaci??n correspondiente al plan b??sico.'
    )
    with open('img/basicPrices.PNG','rb') as photo_file:
     bot.sendChatAction(chat_id=id, action=ChatAction.UPLOAD_PHOTO, timeout=None)
     time.sleep(1)
     bot.sendPhoto(chat_id=id, photo=photo_file, caption='Precios y descripci??n plan b??sico.')
     bot.sendChatAction(chat_id=id, action=ChatAction.TYPING, timeout=None)
    time.sleep(1)
    query.message.reply_text("La disponibilidad del contenido en Full HD (1080p), Ultra HD (4K) y HDR depende de tu servicio de internet y del dispositivo en uso. No todo el contenido est?? disponible en HD, Full HD, Ultra HD o HDR. Consulta los T??rminos de uso para obtener m??s informaci??n. "
    "Solo las personas que vivan contigo pueden usar tu cuenta. Puedes ver Netflix en 4 dispositivos distintos al mismo tiempo con el plan Premium, en 2 con el plan Est??ndar y en 1 con el plan B??sico.")
    bot.sendChatAction(chat_id=id, action=ChatAction.TYPING, timeout=None)
    time.sleep(1)
    query.message.reply_text("Recuerda que el comando /pago te brindar?? informaci??n de las cuentas bancarias habilitadas para que realices tu compra.")
    bot.sendChatAction(chat_id=id, action=ChatAction.TYPING, timeout=None)
    time.sleep(1)
    query.message.reply_text("/start para regresar al men?? principal.")
    with open('stickers/besopatito.tgs','rb') as sticker_file:
     bot.sendChatAction(chat_id=id, action=ChatAction.TYPING, timeout=None)
     time.sleep(0.5)
     bot.sendSticker(chat_id=id, sticker=sticker_file) 

    return ConversationHandler.END

def plan_estandar(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()

    user = query.message.from_user
    logger.info(f'El usuario {user.first_name} {user.last_name}, ha escogido el plan est??ndar.')
    id = query.message.chat_id

    query.edit_message_text(
        text='Aqu?? te env??o toda la informaci??n respecto al plan est??ndar.'
    )
    with open('img/StandarPrices.PNG','rb') as photo_file:
     bot.sendChatAction(chat_id=id, action=ChatAction.UPLOAD_PHOTO, timeout=None)
     time.sleep(1)
     bot.sendPhoto(chat_id=id, photo=photo_file, caption='Precios y descripci??n plan est??ndar.')
     bot.sendChatAction(chat_id=id, action=ChatAction.TYPING, timeout=None)
     time.sleep(1)
    query.message.reply_text("La disponibilidad del contenido en Full HD (1080p), Ultra HD (4K) y HDR depende de tu servicio de internet y del dispositivo en uso. No todo el contenido est?? disponible en HD, Full HD, Ultra HD o HDR. Consulta los T??rminos de uso para obtener m??s informaci??n. "
    "Solo las personas que vivan contigo pueden usar tu cuenta. Puedes ver Netflix en 4 dispositivos distintos al mismo tiempo con el plan Premium, en 2 con el plan Est??ndar y en 1 con el plan B??sico.")
    bot.sendChatAction(chat_id=id, action=ChatAction.TYPING, timeout=None)
    time.sleep(1)
    query.message.reply_text("Recuerda que el comando /pago te brindar?? informaci??n de las cuentas habilitadas para que realices tu compra.")
    bot.sendChatAction(chat_id=id, action=ChatAction.TYPING, timeout=None)
    time.sleep(1)
    query.message.reply_text("/start para regresar al men?? principal.")
    with open('stickers/besopatito.tgs','rb') as sticker_file:
     bot.sendChatAction(chat_id=id, action=ChatAction.TYPING, timeout=None)
     time.sleep(0.5)
     bot.sendSticker(chat_id=id, sticker=sticker_file) 

    return ConversationHandler.END

def plan_premium(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()

    user = query.message.from_user
    logger.info(f'El usuario {user.first_name} {user.last_name}, ha escogido el plan premium.')
    id = query.message.chat_id

    query.edit_message_text(
        text='Aqu?? te env??o toda la informaci??n respecto al plan premium.'
    )
    with open('img/PremiumPrices.PNG','rb') as photo_file:
     bot.sendChatAction(chat_id=id, action=ChatAction.UPLOAD_PHOTO, timeout=None)
     time.sleep(1)
     bot.sendPhoto(chat_id=id, photo=photo_file, caption='Precios y descripci??n plan premium.')
     bot.sendChatAction(chat_id=id, action=ChatAction.TYPING, timeout=None)
     time.sleep(1)
    query.message.reply_text("La disponibilidad del contenido en Full HD (1080p), Ultra HD (4K) y HDR depende de tu servicio de internet y del dispositivo en uso. No todo el contenido est?? disponible en HD, Full HD, Ultra HD o HDR. Consulta los T??rminos de uso para obtener m??s informaci??n. "
    "Solo las personas que vivan contigo pueden usar tu cuenta. Puedes ver Netflix en 4 dispositivos distintos al mismo tiempo con el plan Premium, en 2 con el plan Est??ndar y en 1 con el plan B??sico.")
    bot.sendChatAction(chat_id=id, action=ChatAction.TYPING, timeout=None)
    time.sleep(1)
    query.message.reply_text("Recuerda que el comando /pago te brindar?? informaci??n de las cuentas habilitadas para que realices tu compra.")
    bot.sendChatAction(chat_id=id, action=ChatAction.TYPING, timeout=None)
    time.sleep(1)
    query.message.reply_text("/start para regresar al men?? principal.")
    with open('stickers/besopatito.tgs','rb') as sticker_file:
     bot.sendChatAction(chat_id=id, action=ChatAction.TYPING, timeout=None)
     time.sleep(0.5)
     bot.sendSticker(chat_id=id, sticker=sticker_file) 

    return ConversationHandler.END

def micuenta(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    logger.info(f'El usuario {user.first_name} {user.last_name}, ha ingresado al comando /micuenta.')
    update.message.reply_text(
        'Por favor env??ame el correo electr??nico (todo en min??scula) que tienes asociado,  para validar la informaci??n.\n\n'
        'O env??a /saltar si no lo recuerdas',
        reply_markup=ReplyKeyboardRemove(),
    )

    return CORREO


def correo(update, context):

    user_name = update.effective_user['first_name']
    user_last = update.effective_user['last_name']
    user_id = update.effective_user['id']

    email = update.message.text

    logger.info("Correo que ingres?? %s %s fue %s", user_name, user_last, email)
    update.message.reply_text(
        text=f"Esta es la direcci??n de correo electr??nico que nos has proporcionado: \n{email}\n\n")
    
    for i in range(1):
        try:
            cell = sheet.find(email)

            if(email == "email_from_google_sheets_database"):
                update.message.reply_text("Por favor selecciona el nombre de tu perfil.\n\n",
                reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(text='Camila S??nchez', callback_data='cami_sanchez')],
                [InlineKeyboardButton(text='Diana S??nchez', callback_data='diana_sanchez')],
                [InlineKeyboardButton(text='Joan', callback_data='joan_angarita')],
                [InlineKeyboardButton(text='Joan Angarita 2', callback_data='joan_angarita')]
                ])
                )
            
            elif(email == "email_from_google_sheets_database"):
                update.message.reply_text("Por favor selecciona el nombre de tu perfil.\n\n",
                reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(text='Keli Su??rez', callback_data='keli_suarez')],
                [InlineKeyboardButton(text='Stiven', callback_data='stiven_duque')],
                [InlineKeyboardButton(text='Fabi??n', callback_data='fabian_duque')],
                [InlineKeyboardButton(text='Horacio Alz??te', callback_data='horacio_alzate')]
                ])
                )
            
            elif(email == "email_from_google_sheets_database"):
                update.message.reply_text("Por favor selecciona el nombre de tu perfil.\n\n",
                reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(text='Daniela Acevedo', callback_data='dani_ace')],
                [InlineKeyboardButton(text='Juan Guti??rrez', callback_data='juan_gu')],
                [InlineKeyboardButton(text='Sophia Jaramillo', callback_data='sophi_jara')],
                [InlineKeyboardButton(text='Maria Isabel Giraldo', callback_data='mariai_giraldo')]
                ])
                )
            
            elif(email == "email_from_google_sheets_database"):
                update.message.reply_text("Por favor selecciona el nombre de tu perfil.\n\n",
                reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(text='Jhon', callback_data='brarlynn_mu??oz')],
                [InlineKeyboardButton(text='Brarlynn', callback_data='brarlynn_mu??oz')],
                [InlineKeyboardButton(text='Karen Fonseca', callback_data='karen_fonseca')],
                [InlineKeyboardButton(text='David', callback_data='david_chavarriaga')]
                ])
                )
            
            elif(email == "email_from_google_sheets_database"):
                update.message.reply_text("Por favor selecciona el nombre de tu perfil.\n\n",
                reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(text='Clau Jim??nez', callback_data='clau_jimenez')],
                [InlineKeyboardButton(text='Yimar', callback_data='yimar')],
                [InlineKeyboardButton(text='Claudia L??pez', callback_data='claudia_lopez')],
                [InlineKeyboardButton(text='Diana Jim??nez', callback_data='diana_jimenez')]
                ])
                )
            
            elif(email == "email_from_google_sheets_database"):
                update.message.reply_text("Por favor selecciona el nombre de tu perfil.\n\n",
                reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(text='Cindy', callback_data='cindy_berrio')],
                [InlineKeyboardButton(text='Geral', callback_data='geral_durango')],
                [InlineKeyboardButton(text='Estefania', callback_data='estefa_sierra')],
                [InlineKeyboardButton(text='Katerine', callback_data='kate_hernandez')]
                ])
                )

            elif(email == "email_from_google_sheets_database"):
                update.message.reply_text("Por favor selecciona el nombre de tu perfil.\n\n",
                reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(text='Elkin', callback_data='elkin_carmona')],
                [InlineKeyboardButton(text='Juan', callback_data='kate_betancur')],
                [InlineKeyboardButton(text='Kate', callback_data='kate_betancur')],
                [InlineKeyboardButton(text='Vivi Toro', callback_data='viviana_toro')]
                ])
                )
            
            elif(email == "email_from_google_sheets_database"):
                update.message.reply_text("Por favor selecciona el nombre de tu perfil.\n\n",
                reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(text='Manuela', callback_data='manuela_montoya')],
                [InlineKeyboardButton(text='Berenice', callback_data='mauro_pati??o')],
                [InlineKeyboardButton(text='Henry', callback_data='henry_mosquera')]
                ])
                )

            else:
                context.bot.sendMessage(chat_id=user_id, parse_mode= "HTML", text="Esta es la informaci??n de tu cuenta: \n\n"

                        f"<b>ESTADO:</b> {sheet.cell(cell.row, cell.col-4).value}\n" 
                        f"<b>PLAN:</b> {sheet.cell(cell.row, cell.col-3).value}\n"    
                        f"<b>PRECIO:</b> ${sheet.cell(cell.row, cell.col-2).value} COP/mes\n"
                        f"<b>NOMBRE:</b> {sheet.cell(cell.row, cell.col-1).value}\n"
                        f"<b>CORREO ELECTR??NICO:</b> {sheet.cell(cell.row, cell.col).value}\n"
                        f"<b>FECHA DE PAGO OPORTUNO:</b> {sheet.cell(cell.row, cell.col+2).value}\n"
                        f"<b>FECHA DE CORTE:</b> {sheet.cell(cell.row, cell.col+3).value}"   )
                bot.sendChatAction(chat_id= user_id, action= ChatAction.TYPING, timeout= None)
                context.bot.sendMessage(chat_id= user_id, parse_mode= "HTML", text="Espero la informaci??n brindada sea de ayuda, si tienes alguna inquietud no dudes en contactarnos, el comando /asesor te puede ayudar. ??Tus amigos de <b>Netflix Colombia</b>!????????\n\n/start para regresar al men?? principal.")
        
        except gspread.CellNotFound:
            context.bot.sendMessage(chat_id=user_id, parse_mode= "HTML", text="El correo electr??nico proporcionado no fue hallado en nuestra base de datos. Recuerda ingresar tu correo en min??scula.\n\n"
            "/micuenta para intentarlo nuevamente o env??a /start para volver al men?? principal.")

    return ConversationHandler.END

def saltar_correo(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    id = update.message.from_user.id
    logger.info("Usuario %s %s no envi?? correo.", user.first_name, user.last_name)
    context.bot.sendMessage(chat_id= id, parse_mode="HTML", text=
        'Puedes intentarlo m??s tarde. El comando /asesor te puede ser ??til.\n'
        '/start para volver al men?? principal.\n\n'
        '??Tus amigos de <b>Netflix Colombia</b>????????!'
    )

    return ConversationHandler.END

def dani_acevedo(update: Update, context: CallbackContext) -> int:

    query = update.callback_query
    query.answer()
    user = query.message.from_user
    logger.info(f'El usuario {user.first_name} {user.last_name}, ha escogido el perfil Daniela Acevedo.')
    query.message.reply_text('Has ingresado el perfil "Daniela Acevedo" por motivos de seguridad para mirar la informaci??n de tu cuenta env??ame el pin de 4 d??gitos asociado a tu perfil.\n\n'
        "O env??a /saltar si no lo recuerdas.",
        reply_markup=ReplyKeyboardRemove(),
        )
    
    return PIN_DANIACEVEDO

def pin_daniace(update: Update, context: CallbackContext) -> int:
              
    while True:
        try:
            pin = int(update.message.text)
            update.message.reply_text("El pin ingresado no corresponde al del perfil seleccionado.\n"
            "Int??ntalo de nuevo o env??a /saltar si no lo recuerdas.")
            if(pin == 2201):
                #print(pin)
                cell3 = sheet.find("Daniela Acevedo")
                id = update.message.from_user.id
                bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                bot.sendMessage(chat_id= id, text="??Espera... este pin s?? lo reconozco!????")
                time.sleep(1)
                bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                bot.sendMessage(chat_id= id, text="Esta es la informaci??n de tu cuenta: \n\n")
                bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)     
                context.bot.sendMessage(chat_id= id, parse_mode= "HTML", text=
                f"<b>ESTADO:</b> {sheet.cell(cell3.row, cell3.col-3).value}\n" 
                f"<b>PLAN:</b> {sheet.cell(cell3.row, cell3.col-2).value}\n"    
                f"<b>PRECIO:</b> ${sheet.cell(cell3.row, cell3.col-1).value} COP/mes\n"
                f"<b>NOMBRE:</b> {sheet.cell(cell3.row, cell3.col).value}\n"
                f"<b>CORREO ELECTR??NICO:</b> {sheet.cell(cell3.row, cell3.col+1).value}\n"
                f"<b>FECHA DE PAGO OPORTUNO:</b> {sheet.cell(cell3.row, cell3.col+3).value}\n"
                f"<b>FECHA DE CORTE:</b> {sheet.cell(cell3.row, cell3.col+4).value}"   )
            
            time.sleep(1)
            break
            #time.sleep(1)
        except ValueError:
                update.message.reply_text("Oopss! ese no era un n??mero v??lido, por favor ingresa s??lo 4 n??meros o env??a /saltar si no lo recuerdas.")
                time.sleep(1)
                break
    #id = update.message.from_user.id
    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
    bot.sendMessage(chat_id= id, parse_mode= "HTML", text="Espero la informaci??n brindada sea de ayuda, si tienes alguna inquietud no dudes en contactarnos, el comando /asesor te puede ayudar. ??Tus amigos de <b>Netflix Colombia</b>!????????\n\n/start para regresar al men?? principal.")
    return ConversationHandler.END

def mariai_giraldo(update: Update, context: CallbackContext) -> int:

    query = update.callback_query
    query.answer()
    user = query.message.from_user
    logger.info(f'El usuario {user.first_name} {user.last_name}, ha escogido el perfil Maria Isabel Giraldo')
    query.message.reply_text('Has escogido el perfil "Maria Isabel Giraldo" por motivos de seguridad para mirar la informaci??n de tu cuenta env??ame el pin de 4 d??gitos asociado a tu perfil.\n\n'
        'O env??a /saltar si no lo recuerdas.',
        reply_markup=ReplyKeyboardRemove(),
        )
    
    return PIN_MARIAIG

def pin_mariaig(update: Update, context: CallbackContext) -> int:
              
    while True:
        try:
            pin = int(update.message.text)
            update.message.reply_text("El pin ingresado no corresponde al del perfil seleccionado.\n"
            "Int??ntalo de nuevo o env??a /saltar si no lo recuerdas.")
            if(pin == 514):
                #print(pin)
                cell3 = sheet.find("Maria Isabel Giraldo")
                id = update.message.from_user.id
                bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                bot.sendMessage(chat_id= id, text="??Espera... este pin s?? lo reconozco!????")
                time.sleep(1)
                bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                bot.sendMessage(chat_id= id, text="Esta es la informaci??n de tu cuenta: \n\n")
                bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)     
                context.bot.sendMessage(chat_id= id, parse_mode= "HTML", text=
                f"<b>ESTADO:</b> {sheet.cell(cell3.row, cell3.col-3).value}\n" 
                f"<b>PLAN:</b> {sheet.cell(cell3.row, cell3.col-2).value}\n"    
                f"<b>PRECIO:</b> ${sheet.cell(cell3.row, cell3.col-1).value} COP/mes\n"
                f"<b>NOMBRE:</b> {sheet.cell(cell3.row, cell3.col).value}\n"
                f"<b>CORREO ELECTR??NICO:</b> {sheet.cell(cell3.row, cell3.col+1).value}\n"
                f"<b>FECHA DE PAGO OPORTUNO:</b> {sheet.cell(cell3.row, cell3.col+3).value}\n"
                f"<b>FECHA DE CORTE:</b> {sheet.cell(cell3.row, cell3.col+4).value}"   )
            
            time.sleep(1)
            break
            #time.sleep(1)
        except ValueError:
                update.message.reply_text("Oopss! ese no era un n??mero v??lido, por favor ingresa s??lo 4 n??meros o env??a /saltar si no lo recuerdas.")
                time.sleep(1)
                break
    #id = update.message.from_user.id
    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
    bot.sendMessage(chat_id= id, parse_mode= "HTML", text="Espero la informaci??n brindada sea de ayuda, si tienes alguna inquietud no dudes en contactarnos, el comando /asesor te puede ayudar. ??Tus amigos de <b>Netflix Colombia</b>!????????\n\n/start para regresar al men?? principal.")
    return ConversationHandler.END

def juan_gu(update: Update, context: CallbackContext) -> int:

    query = update.callback_query
    query.answer()
    user = query.message.from_user
    logger.info(f'El usuario {user.first_name} {user.last_name}, ha escogido el perfil Juan Guti??rrez.')
    query.message.reply_text("Por motivos de seguridad para mirar la informaci??n de tu cuenta env??ame el pin de 4 d??gitos asociado a tu perfil.\n\n"
        "O env??a /saltar si no lo recuerdas.",
        reply_markup=ReplyKeyboardRemove(),
        )
    return PIN_JUANGUT

def pin_juang(update: Update, context: CallbackContext) -> int:
        #if(update.message.text.find("2612") == 0):
              
    while True:
        try:
            pin = int(update.message.text)
            update.message.reply_text("El pin ingresado no corresponde al del perfil seleccionado.\n"
            "Int??ntalo de nuevo o env??a /saltar si no lo recuerdas.")
            if(pin == 4488):
                #print(pin)
                cell3 = sheet.find("Juan Guti??rrez")
                id = update.message.from_user.id
                bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                bot.sendMessage(chat_id= id, text="??Espera... este pin s?? lo reconozco!????")
                time.sleep(1)
                bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                bot.sendMessage(chat_id= id, text="Esta es la informaci??n de tu cuenta: \n\n")
                bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)     
                context.bot.sendMessage(chat_id= id, parse_mode= "HTML", text=
                f"<b>ESTADO:</b> {sheet.cell(cell3.row, cell3.col-3).value}\n" 
                f"<b>PLAN:</b> {sheet.cell(cell3.row, cell3.col-2).value}\n"    
                f"<b>PRECIO:</b> ${sheet.cell(cell3.row, cell3.col-1).value} COP/mes\n"
                f"<b>NOMBRE:</b> {sheet.cell(cell3.row, cell3.col).value}\n"
                f"<b>CORREO ELECTR??NICO:</b> {sheet.cell(cell3.row, cell3.col+1).value}\n"
                f"<b>FECHA DE PAGO OPORTUNO:</b> {sheet.cell(cell3.row, cell3.col+3).value}\n"
                f"<b>FECHA DE CORTE:</b> {sheet.cell(cell3.row, cell3.col+4).value}"   )
            
            time.sleep(1)
            break
            #time.sleep(1)
        except ValueError:
                update.message.reply_text("Oopss! ese no era un n??mero v??lido, por favor ingresa s??lo 4 n??meros o env??a /saltar si no lo recuerdas.")
                time.sleep(1)
                break
    #id = update.message.from_user.id
    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
    bot.sendMessage(chat_id= id, parse_mode= "HTML", text="Espero la informaci??n brindada sea de ayuda, si tienes alguna inquietud no dudes en contactarnos, el comando /asesor te puede ayudar. ??Tus amigos de <b>Netflix Colombia</b>!????????\n\n/start para regresar al men?? principal.")
    return ConversationHandler.END

def sophi_jara(update: Update, context: CallbackContext) -> int:

    query = update.callback_query
    query.answer()
    user = query.message.from_user
    logger.info(f'El usuario {user.first_name} {user.last_name}, ha escogido el perfil Sophia Jaramillo.')
    query.message.reply_text("Por motivos de seguridad para mirar la informaci??n de tu cuenta env??ame el pin de 4 d??gitos asociado a tu perfil.\n\n"
        "O env??a /saltar si no lo recuerdas.",
        reply_markup=ReplyKeyboardRemove(),
        )
    return PIN_SOPHI

def pin_sophi(update: Update, context: CallbackContext) -> int:
              
    while True:
        try:
            pin = int(update.message.text)
            update.message.reply_text("El pin ingresado no corresponde al del perfil seleccionado.\n"
            "Int??ntalo de nuevo o env??a /saltar si no lo recuerdas.")
            if(pin == 926):
                #print(pin)
                cell3 = sheet.find("Sophia Jaramillo")
                id = update.message.from_user.id
                bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                bot.sendMessage(chat_id= id, text="??Espera... este pin s?? lo reconozco!????")
                time.sleep(1)
                bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                bot.sendMessage(chat_id= id, text="Esta es la informaci??n de tu cuenta: \n\n")
                bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)     
                context.bot.sendMessage(chat_id= id, parse_mode= "HTML", text=
                f"<b>ESTADO:</b> {sheet.cell(cell3.row, cell3.col-3).value}\n" 
                f"<b>PLAN:</b> {sheet.cell(cell3.row, cell3.col-2).value}\n"    
                f"<b>PRECIO:</b> ${sheet.cell(cell3.row, cell3.col-1).value} COP/mes\n"
                f"<b>NOMBRE:</b> {sheet.cell(cell3.row, cell3.col).value}\n"
                f"<b>CORREO ELECTR??NICO:</b> {sheet.cell(cell3.row, cell3.col+1).value}\n"
                f"<b>FECHA DE PAGO OPORTUNO:</b> {sheet.cell(cell3.row, cell3.col+3).value}\n"
                f"<b>FECHA DE CORTE:</b> {sheet.cell(cell3.row, cell3.col+4).value}"   )
            
            time.sleep(1)
            break
            #time.sleep(1)
        except ValueError:
                update.message.reply_text("Oopss! ese no era un n??mero v??lido, por favor ingresa s??lo 4 n??meros o env??a /saltar si no lo recuerdas.")
                time.sleep(1)
                break
    #id = update.message.from_user.id
    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
    bot.sendMessage(chat_id= id, parse_mode= "HTML", text="Espero la informaci??n brindada sea de ayuda, si tienes alguna inquietud no dudes en contactarnos, el comando /asesor te puede ayudar. ??Tus amigos de <b>Netflix Colombia</b>!????????\n\n/start para regresar al men?? principal.")
    return ConversationHandler.END

def cindy_berrio(update: Update, context: CallbackContext) -> int:

    query = update.callback_query
    query.answer()
    user = query.message.from_user
    logger.info(f'El usuario {user.first_name} {user.last_name}, ha escogido el perfil Cindy Berrio.')
    query.message.reply_text("Por motivos de seguridad para mirar la informaci??n de tu cuenta env??ame el pin de 4 d??gitos asociado a tu perfil.\n\n"
        "O env??a /saltar si no lo recuerdas.",
        reply_markup=ReplyKeyboardRemove(),
        )
    return PIN_CINDYB

def pin_cindyb(update: Update, context: CallbackContext) -> int:

    for i in range(1):          
        while True:
            try:
                pin = int(update.message.text)
                update.message.reply_text("El pin ingresado no corresponde al del perfil seleccionado.\n"
                "Int??ntalo de nuevo o env??a /saltar si no lo recuerdas.")
                if(pin == 1122): #el primer d??gito es 0 pero no aparece (cero a la izquierda)
                    #print(pin)
                    cell3 = sheet.find("Cindy Berrio")
                    id = update.message.from_user.id
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                    bot.sendMessage(chat_id= id, text="??Espera... este pin s?? lo reconozco!????")
                    time.sleep(1)
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                    bot.sendMessage(chat_id= id, text="Esta es la informaci??n de tu cuenta: \n\n")
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)     
                    context.bot.sendMessage(chat_id= id, parse_mode= "HTML", text=
                    f"<b>ESTADO:</b> {sheet.cell(cell3.row, cell3.col-3).value}\n" 
                    f"<b>PLAN:</b> {sheet.cell(cell3.row, cell3.col-2).value}\n"    
                    f"<b>PRECIO:</b> ${sheet.cell(cell3.row, cell3.col-1).value} COP/mes\n"
                    f"<b>NOMBRE:</b> {sheet.cell(cell3.row, cell3.col).value}\n"
                    f"<b>CORREO ELECTR??NICO:</b> {sheet.cell(cell3.row, cell3.col+1).value}\n"
                    f"<b>FECHA DE PAGO OPORTUNO:</b> {sheet.cell(cell3.row, cell3.col+3).value}\n"
                    f"<b>FECHA DE CORTE:</b> {sheet.cell(cell3.row, cell3.col+4).value}"   )
                
                time.sleep(1)
                break
                #time.sleep(1)
            except ValueError:
                    update.message.reply_text("Oopss! ese no era un n??mero v??lido, por favor ingresa s??lo 4 n??meros o env??a /saltar si no lo recuerdas.")
                    time.sleep(1)
                    break
        #id = update.message.from_user.id
        bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
        bot.sendMessage(chat_id= id, parse_mode= "HTML", text="Espero la informaci??n brindada sea de ayuda, si tienes alguna inquietud no dudes en contactarnos, el comando /asesor te puede ayudar. ??Tus amigos de <b>Netflix Colombia</b>!????????\n\n/start para regresar al men?? principal.")
    return ConversationHandler.END

def geral_durango(update: Update, context: CallbackContext) -> int:

    query = update.callback_query
    query.answer()
    user = query.message.from_user
    logger.info(f'El usuario {user.first_name} {user.last_name}, ha escogido el perfil Geral Durango.')
    query.message.reply_text("Por motivos de seguridad para mirar la informaci??n de tu cuenta env??ame el pin de 4 d??gitos asociado a tu perfil.\n\n"
        "O env??a /saltar si no lo recuerdas.",
        reply_markup=ReplyKeyboardRemove(),
        )
    return PIN_GERALD

def pin_gerald(update: Update, context: CallbackContext) -> int:

    for i in range(1):          
        while True:
            try:
                pin = int(update.message.text)
                update.message.reply_text("El pin ingresado no corresponde al del perfil seleccionado.\n"
                "Int??ntalo de nuevo o env??a /saltar si no lo recuerdas.")
                if(pin == 62): #los dos primeros d??gitos son 0 pero no aparece (cero a la izquierda)
                    cell3 = sheet.find("Geraldine Durango")
                    id = update.message.from_user.id
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                    bot.sendMessage(chat_id= id, text="??Espera... este pin s?? lo reconozco!????")
                    time.sleep(1)
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                    bot.sendMessage(chat_id= id, text="Esta es la informaci??n de tu cuenta: \n\n")
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)     
                    context.bot.sendMessage(chat_id= id, parse_mode= "HTML", text=
                    f"<b>ESTADO:</b> {sheet.cell(cell3.row, cell3.col-3).value}\n" 
                    f"<b>PLAN:</b> {sheet.cell(cell3.row, cell3.col-2).value}\n"    
                    f"<b>PRECIO:</b> ${sheet.cell(cell3.row, cell3.col-1).value} COP/mes\n"
                    f"<b>NOMBRE:</b> {sheet.cell(cell3.row, cell3.col).value}\n"
                    f"<b>CORREO ELECTR??NICO:</b> {sheet.cell(cell3.row, cell3.col+1).value}\n"
                    f"<b>FECHA DE PAGO OPORTUNO:</b> {sheet.cell(cell3.row, cell3.col+3).value}\n"
                    f"<b>FECHA DE CORTE:</b> {sheet.cell(cell3.row, cell3.col+4).value}"   )
                
                time.sleep(1)
                break
                #time.sleep(1)
            except ValueError:
                    update.message.reply_text("Oopss! ese no era un n??mero v??lido, por favor ingresa s??lo 4 n??meros o env??a /saltar si no lo recuerdas.")
                    time.sleep(1)
                    break
        #id = update.message.from_user.id
        bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
        bot.sendMessage(chat_id= id, parse_mode= "HTML", text="Espero la informaci??n brindada sea de ayuda, si tienes alguna inquietud no dudes en contactarnos, el comando /asesor te puede ayudar. ??Tus amigos de <b>Netflix Colombia</b>!????????\n\n/start para regresar al men?? principal.")
    return ConversationHandler.END

def estefa_sierra(update: Update, context: CallbackContext) -> int:

    query = update.callback_query
    query.answer()
    user = query.message.from_user
    logger.info(f'El usuario {user.first_name} {user.last_name}, ha escogido el perfil a nombre de Estefania Sierra.')
    query.message.reply_text('Has seleccionado el perfil "Estefania" por motivos de seguridad para mirar la informaci??n de tu cuenta env??ame el pin de 4 d??gitos asociado a tu perfil.\n\n'
        "O env??a /saltar si no lo recuerdas.",
        reply_markup=ReplyKeyboardRemove(),
        )
    return PIN_ESTEFASIERRA

def pin_estefasierra(update: Update, context: CallbackContext) -> int:

    for i in range(1):          
        while True:
            try:
                pin = int(update.message.text)
                update.message.reply_text("El pin ingresado no corresponde al del perfil seleccionado.\n"
                "Int??ntalo de nuevo o env??a /saltar si no lo recuerdas.")
                if(pin == 1808): #los dos primeros d??gitos son 0 pero no aparece (cero a la izquierda)
                    cell3 = sheet.find("Estefania Sierra")
                    id = update.message.from_user.id
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                    bot.sendMessage(chat_id= id, text="??Espera... este pin s?? lo reconozco!????")
                    time.sleep(1)
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                    bot.sendMessage(chat_id= id, text="Esta es la informaci??n de tu cuenta: \n\n")
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)     
                    context.bot.sendMessage(chat_id= id, parse_mode= "HTML", text=
                    f"<b>ESTADO:</b> {sheet.cell(cell3.row, cell3.col-3).value}\n" 
                    f"<b>PLAN:</b> {sheet.cell(cell3.row, cell3.col-2).value}\n"    
                    f"<b>PRECIO:</b> ${sheet.cell(cell3.row, cell3.col-1).value} COP/mes\n"
                    f"<b>NOMBRE:</b> {sheet.cell(cell3.row, cell3.col).value}\n"
                    f"<b>CORREO ELECTR??NICO:</b> {sheet.cell(cell3.row, cell3.col+1).value}\n"
                    f"<b>FECHA DE PAGO OPORTUNO:</b> {sheet.cell(cell3.row, cell3.col+3).value}\n"
                    f"<b>FECHA DE CORTE:</b> {sheet.cell(cell3.row, cell3.col+4).value}"   )
                
                time.sleep(1)
                break
                #time.sleep(1)
            except ValueError:
                    update.message.reply_text("Oopss! ese no era un n??mero v??lido, por favor ingresa s??lo 4 n??meros o env??a /saltar si no lo recuerdas.")
                    time.sleep(1)
                    break
        #id = update.message.from_user.id
        bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
        bot.sendMessage(chat_id= id, parse_mode= "HTML", text="Espero la informaci??n brindada sea de ayuda, si tienes alguna inquietud no dudes en contactarnos, el comando /asesor te puede ayudar. ??Tus amigos de <b>Netflix Colombia</b>!????????\n\n/start para regresar al men?? principal.")
    return ConversationHandler.END

def kate_hernandez(update: Update, context: CallbackContext) -> int:

    query = update.callback_query
    query.answer()
    user = query.message.from_user
    logger.info(f'El usuario {user.first_name} {user.last_name}, ha escogido el perfil Katerine Hern??ndez.')
    query.message.reply_text("Por motivos de seguridad para mirar la informaci??n de tu cuenta env??ame el pin de 4 d??gitos asociado a tu perfil.\n\n"
        "O env??a /saltar si no lo recuerdas.",
        reply_markup=ReplyKeyboardRemove(),
        )
    return PIN_KATEHDZ

def pin_katehdz(update: Update, context: CallbackContext) -> int:

    for i in range(1):          
        while True:
            try:
                pin = int(update.message.text)
                update.message.reply_text("El pin ingresado no corresponde al del perfil seleccionado.\n"
                "Int??ntalo de nuevo o env??a /saltar si no lo recuerdas.")
                if(pin == 1216):
                    cell3 = sheet.find("Katerine Hern??ndez")
                    id = update.message.from_user.id
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                    bot.sendMessage(chat_id= id, text="??Espera... este pin s?? lo reconozco!????")
                    time.sleep(1)
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                    bot.sendMessage(chat_id= id, text="Esta es la informaci??n de tu cuenta: \n\n")
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)     
                    context.bot.sendMessage(chat_id= id, parse_mode= "HTML", text=
                    f"<b>ESTADO:</b> {sheet.cell(cell3.row, cell3.col-3).value}\n" 
                    f"<b>PLAN:</b> {sheet.cell(cell3.row, cell3.col-2).value}\n"    
                    f"<b>PRECIO:</b> ${sheet.cell(cell3.row, cell3.col-1).value} COP/mes\n"
                    f"<b>NOMBRE:</b> {sheet.cell(cell3.row, cell3.col).value}\n"
                    f"<b>CORREO ELECTR??NICO:</b> {sheet.cell(cell3.row, cell3.col+1).value}\n"
                    f"<b>FECHA DE PAGO OPORTUNO:</b> {sheet.cell(cell3.row, cell3.col+3).value}\n"
                    f"<b>FECHA DE CORTE:</b> {sheet.cell(cell3.row, cell3.col+4).value}"   )
                
                time.sleep(1)
                break
            except ValueError:
                    update.message.reply_text("Oopss! ese no era un n??mero v??lido, por favor ingresa s??lo 4 n??meros o env??a /saltar si no lo recuerdas.")
                    time.sleep(1)
                    break
        #id = update.message.from_user.id
        bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
        bot.sendMessage(chat_id= id, parse_mode= "HTML", text="Espero la informaci??n brindada sea de ayuda, si tienes alguna inquietud no dudes en contactarnos, el comando /asesor te puede ayudar. ??Tus amigos de <b>Netflix Colombia</b>!????????\n\n/start para regresar al men?? principal.")
    return ConversationHandler.END

def keli_suarez(update: Update, context: CallbackContext) -> int:

    query = update.callback_query
    query.answer()
    user = query.message.from_user
    logger.info(f'El usuario {user.first_name} {user.last_name}, ha escogido el perfil Keli Su??rez.')
    query.message.reply_text('Has escogido el perfil "Keli Su??rez", por motivos de seguridad para mirar la informaci??n de tu cuenta env??ame el pin de 4 d??gitos asociado a tu perfil.\n\n'
        "O env??a /saltar si no lo recuerdas.",
        reply_markup=ReplyKeyboardRemove(),
        )
    return PIN_KELISUAREZ

def pin_kelisuarez(update: Update, context: CallbackContext) -> int:

    for i in range(1):          
        while True:
            try:
                pin = int(update.message.text)
                update.message.reply_text("El pin ingresado no corresponde al del perfil seleccionado.\n"
                "Int??ntalo de nuevo o env??a /saltar si no lo recuerdas.")
                if(pin == 727): #pin: 0727
                    cell3 = sheet.find("Keli Su??rez")
                    id = update.message.from_user.id
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                    bot.sendMessage(chat_id= id, text="??Espera... este pin s?? lo reconozco!????")
                    time.sleep(1)
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                    bot.sendMessage(chat_id= id, text="Esta es la informaci??n de tu cuenta: \n\n")
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)     
                    context.bot.sendMessage(chat_id= id, parse_mode= "HTML", text=
                    f"<b>ESTADO:</b> {sheet.cell(cell3.row, cell3.col-3).value}\n" 
                    f"<b>PLAN:</b> {sheet.cell(cell3.row, cell3.col-2).value}\n"    
                    f"<b>PRECIO:</b> ${sheet.cell(cell3.row, cell3.col-1).value} COP/mes\n"
                    f"<b>NOMBRE:</b> {sheet.cell(cell3.row, cell3.col).value}\n"
                    f"<b>CORREO ELECTR??NICO:</b> {sheet.cell(cell3.row, cell3.col+1).value}\n"
                    f"<b>FECHA DE PAGO OPORTUNO:</b> {sheet.cell(cell3.row, cell3.col+3).value}\n"
                    f"<b>FECHA DE CORTE:</b> {sheet.cell(cell3.row, cell3.col+4).value}"   )
                
                time.sleep(1)
                break
            except ValueError:
                    update.message.reply_text("Oopss! ese no era un n??mero v??lido, por favor ingresa s??lo 4 n??meros o env??a /saltar si no lo recuerdas.")
                    time.sleep(1)
                    break
        #id = update.message.from_user.id
        bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
        bot.sendMessage(chat_id= id, parse_mode= "HTML", text="Espero la informaci??n brindada sea de ayuda, si tienes alguna inquietud no dudes en contactarnos, el comando /asesor te puede ayudar. ??Tus amigos de <b>Netflix Colombia</b>!????????\n\n/start para regresar al men?? principal.")
    return ConversationHandler.END

def stiven_duque(update: Update, context: CallbackContext) -> int:

    query = update.callback_query
    query.answer()
    user = query.message.from_user
    logger.info(f'El usuario {user.first_name} {user.last_name}, ha escogido el perfil Keli Su??rez.')
    query.message.reply_text('Has escogido el perfil "Stiven", por motivos de seguridad para mirar la informaci??n de tu cuenta env??ame el pin de 4 d??gitos asociado a tu perfil.\n\n'
        "O env??a /saltar si no lo recuerdas.",
        reply_markup=ReplyKeyboardRemove(),
        )
    return PIN_STIVEND

def pin_stivend(update: Update, context: CallbackContext) -> int:

    for i in range(1):          
        while True:
            try:
                pin = int(update.message.text)
                update.message.reply_text("El pin ingresado no corresponde al del perfil seleccionado.\n"
                "Int??ntalo de nuevo o env??a /saltar si no lo recuerdas.")
                if(pin == 9866):
                    cell3 = sheet.find("Stiven Duque")
                    id = update.message.from_user.id
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                    bot.sendMessage(chat_id= id, text="??Espera... este pin s?? lo reconozco!????")
                    time.sleep(1)
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                    bot.sendMessage(chat_id= id, text="Esta es la informaci??n de tu cuenta: \n\n")
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)     
                    context.bot.sendMessage(chat_id= id, parse_mode= "HTML", text=
                    f"<b>ESTADO:</b> {sheet.cell(cell3.row, cell3.col-3).value}\n" 
                    f"<b>PLAN:</b> {sheet.cell(cell3.row, cell3.col-2).value}\n"    
                    f"<b>PRECIO:</b> ${sheet.cell(cell3.row, cell3.col-1).value} COP/mes\n"
                    f"<b>NOMBRE:</b> {sheet.cell(cell3.row, cell3.col).value}\n"
                    f"<b>CORREO ELECTR??NICO:</b> {sheet.cell(cell3.row, cell3.col+1).value}\n"
                    f"<b>FECHA DE PAGO OPORTUNO:</b> {sheet.cell(cell3.row, cell3.col+3).value}\n"
                    f"<b>FECHA DE CORTE:</b> {sheet.cell(cell3.row, cell3.col+4).value}"   )
                
                time.sleep(1)
                break
            except ValueError:
                    update.message.reply_text("Oopss! ese no era un n??mero v??lido, por favor ingresa s??lo 4 n??meros o env??a /saltar si no lo recuerdas.")
                    time.sleep(1)
                    break
        #id = update.message.from_user.id
        bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
        bot.sendMessage(chat_id= id, parse_mode= "HTML", text="Espero la informaci??n brindada sea de ayuda, si tienes alguna inquietud no dudes en contactarnos, el comando /asesor te puede ayudar. ??Tus amigos de <b>Netflix Colombia</b>!????????\n\n/start para regresar al men?? principal.")
    return ConversationHandler.END

def fabian_duque(update: Update, context: CallbackContext) -> int:

    query = update.callback_query
    query.answer()
    user = query.message.from_user
    logger.info(f'El usuario {user.first_name} {user.last_name}, ha escogido el perfil Stiven Duque.')
    query.message.reply_text("Por motivos de seguridad para mirar la informaci??n de tu cuenta env??ame el pin de 4 d??gitos asociado a tu perfil.\n\n"
        "O env??a /saltar si no lo recuerdas.",
        reply_markup=ReplyKeyboardRemove(),
        )
    return PIN_FABIAND

def pin_fabiand(update: Update, context: CallbackContext) -> int:

    for i in range(1):          
        while True:
            try:
                pin = int(update.message.text)
                update.message.reply_text("El pin ingresado no corresponde al del perfil seleccionado.\n"
                "Int??ntalo de nuevo o env??a /saltar si no lo recuerdas.")
                if(pin == 9866):
                    cell3 = sheet.find("Stiven Duque")
                    id = update.message.from_user.id
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                    bot.sendMessage(chat_id= id, text="??Espera... este pin s?? lo reconozco!????")
                    time.sleep(1)
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                    bot.sendMessage(chat_id= id, text="Esta es la informaci??n de tu cuenta: \n\n")
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)     
                    context.bot.sendMessage(chat_id= id, parse_mode= "HTML", text=
                    f"<b>ESTADO:</b> {sheet.cell(cell3.row, cell3.col-3).value}\n" 
                    f"<b>PLAN:</b> {sheet.cell(cell3.row, cell3.col-2).value}\n"    
                    f"<b>PRECIO:</b> ${sheet.cell(cell3.row, cell3.col-1).value} COP/mes\n"
                    f"<b>NOMBRE:</b> {sheet.cell(cell3.row, cell3.col).value}\n"
                    f"<b>CORREO ELECTR??NICO:</b> {sheet.cell(cell3.row, cell3.col+1).value}\n"
                    f"<b>FECHA DE PAGO OPORTUNO:</b> {sheet.cell(cell3.row, cell3.col+3).value}\n"
                    f"<b>FECHA DE CORTE:</b> {sheet.cell(cell3.row, cell3.col+4).value}"   )
                
                time.sleep(1)
                break
            except ValueError:
                    update.message.reply_text("Oopss! ese no era un n??mero v??lido, por favor ingresa s??lo 4 n??meros o env??a /saltar si no lo recuerdas.")
                    time.sleep(1)
                    break
        #id = update.message.from_user.id
        bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
        bot.sendMessage(chat_id= id, parse_mode= "HTML", text="Espero la informaci??n brindada sea de ayuda, si tienes alguna inquietud no dudes en contactarnos, el comando /asesor te puede ayudar. ??Tus amigos de <b>Netflix Colombia</b>!????????\n\n/start para regresar al men?? principal.")
    return ConversationHandler.END

def horacio_alzate(update: Update, context: CallbackContext) -> int:

    query = update.callback_query
    query.answer()
    user = query.message.from_user
    logger.info(f'El usuario {user.first_name} {user.last_name}, ha escogido el perfil Horacio Alzate.')
    query.message.reply_text("Por motivos de seguridad para mirar la informaci??n de tu cuenta env??ame el pin de 4 d??gitos asociado a tu perfil.\n\n"
        "O env??a /saltar si no lo recuerdas.",
        reply_markup=ReplyKeyboardRemove(),
        )
    return PIN_HORACIOA

def pin_horacioa(update: Update, context: CallbackContext) -> int:

    for i in range(1):          
        while True:
            try:
                pin = int(update.message.text)
                update.message.reply_text("El pin ingresado no corresponde al del perfil seleccionado.\n"
                "Int??ntalo de nuevo o env??a /saltar si no lo recuerdas.")
                if(pin == 4444):
                    cell3 = sheet.find("Horacio Alz??te")
                    id = update.message.from_user.id
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                    bot.sendMessage(chat_id= id, text="??Espera... este pin s?? lo reconozco!????")
                    time.sleep(1)
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                    bot.sendMessage(chat_id= id, text="Esta es la informaci??n de tu cuenta: \n\n")
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)     
                    context.bot.sendMessage(chat_id= id, parse_mode= "HTML", text=
                    f"<b>ESTADO:</b> {sheet.cell(cell3.row, cell3.col-3).value}\n" 
                    f"<b>PLAN:</b> {sheet.cell(cell3.row, cell3.col-2).value}\n"    
                    f"<b>PRECIO:</b> ${sheet.cell(cell3.row, cell3.col-1).value} COP/mes\n"
                    f"<b>NOMBRE:</b> {sheet.cell(cell3.row, cell3.col).value}\n"
                    f"<b>CORREO ELECTR??NICO:</b> {sheet.cell(cell3.row, cell3.col+1).value}\n"
                    f"<b>FECHA DE PAGO OPORTUNO:</b> {sheet.cell(cell3.row, cell3.col+3).value}\n"
                    f"<b>FECHA DE CORTE:</b> {sheet.cell(cell3.row, cell3.col+4).value}"   )
                
                time.sleep(1)
                break
            except ValueError:
                    update.message.reply_text("Oopss! ese no era un n??mero v??lido, por favor ingresa s??lo 4 n??meros o env??a /saltar si no lo recuerdas.")
                    time.sleep(1)
                    break
        #id = update.message.from_user.id
        bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
        bot.sendMessage(chat_id= id, parse_mode= "HTML", text="Espero la informaci??n brindada sea de ayuda, si tienes alguna inquietud no dudes en contactarnos, el comando /asesor te puede ayudar. ??Tus amigos de <b>Netflix Colombia</b>!????????\n\n/start para regresar al men?? principal.")
    return ConversationHandler.END

def elkin_carmona(update: Update, context: CallbackContext) -> int:

    query = update.callback_query
    query.answer()
    user = query.message.from_user
    logger.info(f'El usuario {user.first_name} {user.last_name}, ha escogido el perfil Elkin Carmona.')
    query.message.reply_text('Has escogido el perfil "Elkin" por motivos de seguridad para mirar la informaci??n de tu cuenta env??ame el pin de 4 d??gitos asociado a tu perfil.\n\n'
        "O env??a /saltar si no lo recuerdas.",
        reply_markup=ReplyKeyboardRemove(),
        )
    return PIN_ELKINCAR

def pin_elkinc(update: Update, context: CallbackContext) -> int:

    for i in range(1):          
        while True:
            try:
                pin = int(update.message.text)
                update.message.reply_text("El pin ingresado no corresponde al del perfil seleccionado.\n"
                "Int??ntalo de nuevo o env??a /saltar si no lo recuerdas.")
                if(pin == 1927):
                    cell3 = sheet.find("Elkin Carmona")
                    id = update.message.from_user.id
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                    bot.sendMessage(chat_id= id, text="??Espera... este pin s?? lo reconozco!????")
                    time.sleep(1)
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                    bot.sendMessage(chat_id= id, text="Esta es la informaci??n de tu cuenta: \n\n")
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)     
                    context.bot.sendMessage(chat_id= id, parse_mode= "HTML", text=
                    f"<b>ESTADO:</b> {sheet.cell(cell3.row, cell3.col-3).value}\n" 
                    f"<b>PLAN:</b> {sheet.cell(cell3.row, cell3.col-2).value}\n"    
                    f"<b>PRECIO:</b> ${sheet.cell(cell3.row, cell3.col-1).value} COP/mes\n"
                    f"<b>NOMBRE:</b> {sheet.cell(cell3.row, cell3.col).value}\n"
                    f"<b>CORREO ELECTR??NICO:</b> {sheet.cell(cell3.row, cell3.col+1).value}\n"
                    f"<b>FECHA DE PAGO OPORTUNO:</b> {sheet.cell(cell3.row, cell3.col+3).value}\n"
                    f"<b>FECHA DE CORTE:</b> {sheet.cell(cell3.row, cell3.col+4).value}"   )
                
                time.sleep(1)
                break
            except ValueError:
                    update.message.reply_text("Oopss! ese no era un n??mero v??lido, por favor ingresa s??lo 4 n??meros o env??a /saltar si no lo recuerdas.")
                    time.sleep(1)
                    break
        #id = update.message.from_user.id
        bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
        bot.sendMessage(chat_id= id, parse_mode= "HTML", text="Espero la informaci??n brindada sea de ayuda, si tienes alguna inquietud no dudes en contactarnos, el comando /asesor te puede ayudar. ??Tus amigos de <b>Netflix Colombia</b>!????????\n\n/start para regresar al men?? principal.")
    return ConversationHandler.END

def kate_betancur(update: Update, context: CallbackContext) -> int:

    query = update.callback_query
    query.answer()
    user = query.message.from_user
    logger.info(f'El usuario {user.first_name} {user.last_name}, ha escogido el perfil a nombre de Katerine Betancur.')
    query.message.reply_text("Por motivos de seguridad para mirar la informaci??n de tu cuenta env??ame el pin de 4 d??gitos asociado a tu perfil.\n\n"
        "O env??a /saltar si no lo recuerdas.",
        reply_markup=ReplyKeyboardRemove(),
        )
    return PIN_KTBETANCUR

def pin_ktbetancur(update: Update, context: CallbackContext) -> int:

    for i in range(1):          
        while True:
            try:
                pin = int(update.message.text)
                update.message.reply_text("El pin ingresado no corresponde al del perfil seleccionado.\n"
                "Int??ntalo de nuevo o env??a /saltar si no lo recuerdas.")
                if(pin == 7378):
                    cell3 = sheet.find("Katerine Betancur Cardona")
                    id = update.message.from_user.id
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                    bot.sendMessage(chat_id= id, text="??Espera... este pin s?? lo reconozco!????")
                    time.sleep(1)
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                    bot.sendMessage(chat_id= id, text="Esta es la informaci??n de tu cuenta: \n\n")
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)     
                    context.bot.sendMessage(chat_id= id, parse_mode= "HTML", text=
                    f"<b>ESTADO:</b> {sheet.cell(cell3.row, cell3.col-3).value}\n" 
                    f"<b>PLAN:</b> {sheet.cell(cell3.row, cell3.col-2).value}\n"    
                    f"<b>PRECIO:</b> ${sheet.cell(cell3.row, cell3.col-1).value} COP/mes\n"
                    f"<b>NOMBRE:</b> {sheet.cell(cell3.row, cell3.col).value}\n"
                    f"<b>CORREO ELECTR??NICO:</b> {sheet.cell(cell3.row, cell3.col+1).value}\n"
                    f"<b>FECHA DE PAGO OPORTUNO:</b> {sheet.cell(cell3.row, cell3.col+3).value}\n"
                    f"<b>FECHA DE CORTE:</b> {sheet.cell(cell3.row, cell3.col+4).value}"   )
                
                time.sleep(1)
                break
            except ValueError:
                    update.message.reply_text("Oopss! ese no era un n??mero v??lido, por favor ingresa s??lo 4 n??meros o env??a /saltar si no lo recuerdas.")
                    time.sleep(1)
                    break
        #id = update.message.from_user.id
        bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
        bot.sendMessage(chat_id= id, parse_mode= "HTML", text="Espero la informaci??n brindada sea de ayuda, si tienes alguna inquietud no dudes en contactarnos, el comando /asesor te puede ayudar. ??Tus amigos de <b>Netflix Colombia</b>!????????\n\n/start para regresar al men?? principal.")
    return ConversationHandler.END

def viviana_toro(update: Update, context: CallbackContext) -> int:

    query = update.callback_query
    query.answer()
    user = query.message.from_user
    logger.info(f'El usuario {user.first_name} {user.last_name}, ha escogido el perfil a nombre de Katerine Betancur.')
    query.message.reply_text('Has seleccionado el perfil "Vivi Toro" por motivos de seguridad para mirar la informaci??n de tu cuenta env??ame el pin de 4 d??gitos asociado a tu perfil.\n\n'
        "O env??a /saltar si no lo recuerdas.",
        reply_markup=ReplyKeyboardRemove(),
        )
    return PIN_VIVITORO

def pin_vivitoro(update: Update, context: CallbackContext) -> int:

    for i in range(1):          
        while True:
            try:
                pin = int(update.message.text)
                update.message.reply_text("El pin ingresado no corresponde al del perfil seleccionado.\n"
                "Int??ntalo de nuevo o env??a /saltar si no lo recuerdas.")
                if(pin == 423):
                    cell3 = sheet.find("Viviana Toro")
                    id = update.message.from_user.id
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                    bot.sendMessage(chat_id= id, text="??Espera... este pin s?? lo reconozco!????")
                    time.sleep(1)
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                    bot.sendMessage(chat_id= id, text="Esta es la informaci??n de tu cuenta: \n\n")
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)     
                    context.bot.sendMessage(chat_id= id, parse_mode= "HTML", text=
                    f"<b>ESTADO:</b> {sheet.cell(cell3.row, cell3.col-3).value}\n" 
                    f"<b>PLAN:</b> {sheet.cell(cell3.row, cell3.col-2).value}\n"    
                    f"<b>PRECIO:</b> ${sheet.cell(cell3.row, cell3.col-1).value} COP/mes\n"
                    f"<b>NOMBRE:</b> {sheet.cell(cell3.row, cell3.col).value}\n"
                    f"<b>CORREO ELECTR??NICO:</b> {sheet.cell(cell3.row, cell3.col+1).value}\n"
                    f"<b>FECHA DE PAGO OPORTUNO:</b> {sheet.cell(cell3.row, cell3.col+3).value}\n"
                    f"<b>FECHA DE CORTE:</b> {sheet.cell(cell3.row, cell3.col+4).value}"   )
                
                time.sleep(1)
                break
            except ValueError:
                    update.message.reply_text("Oopss! ese no era un n??mero v??lido, por favor ingresa s??lo 4 n??meros o env??a /saltar si no lo recuerdas.")
                    time.sleep(1)
                    break
        #id = update.message.from_user.id
        bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
        bot.sendMessage(chat_id= id, parse_mode= "HTML", text="Espero la informaci??n brindada sea de ayuda, si tienes alguna inquietud no dudes en contactarnos, el comando /asesor te puede ayudar. ??Tus amigos de <b>Netflix Colombia</b>!????????\n\n/start para regresar al men?? principal.")
    return ConversationHandler.END

def cami_sanchez(update: Update, context: CallbackContext) -> int:

    query = update.callback_query
    query.answer()
    user = query.message.from_user
    logger.info(f'El usuario {user.first_name} {user.last_name}, ha escogido el perfil a nombre de Camila S??nchez.')
    query.message.reply_text('Has escogido el perfil "Camila S??nchez" por motivos de seguridad para mirar la informaci??n de tu cuenta env??ame el pin de 4 d??gitos asociado a tu perfil.\n\n'
        "O env??a /saltar si no lo recuerdas.",
        reply_markup=ReplyKeyboardRemove(),
        )
    return PIN_CAMISANCHEZ

def pin_camisanchez(update: Update, context: CallbackContext) -> int:

    for i in range(1):          
        while True:
            try:
                pin = int(update.message.text)
                update.message.reply_text("El pin ingresado no corresponde al del perfil seleccionado.\n"
                "Int??ntalo de nuevo o env??a /saltar si no lo recuerdas.")
                if(pin == 1958):
                    cell3 = sheet.find("Camila S??nchez")
                    id = update.message.from_user.id
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                    bot.sendMessage(chat_id= id, text="??Espera... este pin s?? lo reconozco!????")
                    time.sleep(1)
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                    bot.sendMessage(chat_id= id, text="Esta es la informaci??n de tu cuenta: \n\n")
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)     
                    context.bot.sendMessage(chat_id= id, parse_mode= "HTML", text=
                    f"<b>ESTADO:</b> {sheet.cell(cell3.row, cell3.col-3).value}\n" 
                    f"<b>PLAN:</b> {sheet.cell(cell3.row, cell3.col-2).value}\n"    
                    f"<b>PRECIO:</b> ${sheet.cell(cell3.row, cell3.col-1).value} COP/mes\n"
                    f"<b>NOMBRE:</b> {sheet.cell(cell3.row, cell3.col).value}\n"
                    f"<b>CORREO ELECTR??NICO:</b> {sheet.cell(cell3.row, cell3.col+1).value}\n"
                    f"<b>FECHA DE PAGO OPORTUNO:</b> {sheet.cell(cell3.row, cell3.col+3).value}\n"
                    f"<b>FECHA DE CORTE:</b> {sheet.cell(cell3.row, cell3.col+4).value}"   )
                
                time.sleep(1)
                break
            except ValueError:
                    update.message.reply_text("Oopss! ese no era un n??mero v??lido, por favor ingresa s??lo 4 n??meros o env??a /saltar si no lo recuerdas.")
                    time.sleep(1)
                    break
        #id = update.message.from_user.id
        bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
        bot.sendMessage(chat_id= id, parse_mode= "HTML", text="Espero la informaci??n brindada sea de ayuda, si tienes alguna inquietud no dudes en contactarnos, el comando /asesor te puede ayudar. ??Tus amigos de <b>Netflix Colombia</b>!????????\n\n/start para regresar al men?? principal.")
    return ConversationHandler.END

def diana_sanchez(update: Update, context: CallbackContext) -> int:

    query = update.callback_query
    query.answer()
    user = query.message.from_user
    logger.info(f'El usuario {user.first_name} {user.last_name}, ha escogido el perfil a nombre de Diana S??nchez.')
    query.message.reply_text('Has escogido el perfil "Diana S??nchez" por motivos de seguridad para mirar la informaci??n de tu cuenta env??ame el pin de 4 d??gitos asociado a tu perfil.\n\n'
        "O env??a /saltar si no lo recuerdas.",
        reply_markup=ReplyKeyboardRemove(),
        )
    return PIN_DIANASAN

def pin_dianasanchez(update: Update, context: CallbackContext) -> int:

    for i in range(1):          
        while True:
            try:
                pin = int(update.message.text)
                update.message.reply_text("El pin ingresado no corresponde al del perfil seleccionado.\n"
                "Int??ntalo de nuevo o env??a /saltar si no lo recuerdas.")
                if(pin == 126):
                    cell3 = sheet.find("Diana S??nchez")
                    id = update.message.from_user.id
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                    bot.sendMessage(chat_id= id, text="??Espera... este pin s?? lo reconozco!????")
                    time.sleep(1)
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                    bot.sendMessage(chat_id= id, text="Esta es la informaci??n de tu cuenta: \n\n")
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)     
                    context.bot.sendMessage(chat_id= id, parse_mode= "HTML", text=
                    f"<b>ESTADO:</b> {sheet.cell(cell3.row, cell3.col-3).value}\n" 
                    f"<b>PLAN:</b> {sheet.cell(cell3.row, cell3.col-2).value}\n"    
                    f"<b>PRECIO:</b> ${sheet.cell(cell3.row, cell3.col-1).value} COP/mes\n"
                    f"<b>NOMBRE:</b> {sheet.cell(cell3.row, cell3.col).value}\n"
                    f"<b>CORREO ELECTR??NICO:</b> {sheet.cell(cell3.row, cell3.col+1).value}\n"
                    f"<b>FECHA DE PAGO OPORTUNO:</b> {sheet.cell(cell3.row, cell3.col+3).value}\n"
                    f"<b>FECHA DE CORTE:</b> {sheet.cell(cell3.row, cell3.col+4).value}"   )
                
                time.sleep(1)
                break
            except ValueError:
                    update.message.reply_text("Oopss! ese no era un n??mero v??lido, por favor ingresa s??lo 4 n??meros o env??a /saltar si no lo recuerdas.")
                    time.sleep(1)
                    break
        #id = update.message.from_user.id
        bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
        bot.sendMessage(chat_id= id, parse_mode= "HTML", text="Espero la informaci??n brindada sea de ayuda, si tienes alguna inquietud no dudes en contactarnos, el comando /asesor te puede ayudar. ??Tus amigos de <b>Netflix Colombia</b>!????????\n\n/start para regresar al men?? principal.")
    return ConversationHandler.END

def joan_angarita(update: Update, context: CallbackContext) -> int:

    query = update.callback_query
    query.answer()
    user = query.message.from_user
    logger.info(f'El usuario {user.first_name} {user.last_name}, ha escogido el perfil a nombre de Joan Angarita.')
    query.message.reply_text('Por motivos de seguridad para mirar la informaci??n de tu cuenta env??ame el pin de 4 d??gitos asociado a tu perfil.\n\n'
        "O env??a /saltar si no lo recuerdas.",
        reply_markup=ReplyKeyboardRemove(),
        )
    return PIN_JOANANGA

def pin_joanangarita(update: Update, context: CallbackContext) -> int:

    for i in range(1):          
        while True:
            try:
                pin = int(update.message.text)
                update.message.reply_text("El pin ingresado no corresponde al del perfil seleccionado.\n"
                "Int??ntalo de nuevo o env??a /saltar si no lo recuerdas.")
                if(pin == 2503):
                    cell3 = sheet.find("Joan Angarita")
                    id = update.message.from_user.id
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                    bot.sendMessage(chat_id= id, text="??Espera... este pin s?? lo reconozco!????")
                    time.sleep(1)
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                    bot.sendMessage(chat_id= id, text="Esta es la informaci??n de tu cuenta: \n\n")
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)     
                    context.bot.sendMessage(chat_id= id, parse_mode= "HTML", text=
                    f"<b>ESTADO:</b> {sheet.cell(cell3.row, cell3.col-3).value}\n" 
                    f"<b>PLAN:</b> {sheet.cell(cell3.row, cell3.col-2).value}\n"    
                    f"<b>PRECIO:</b> ${sheet.cell(cell3.row, cell3.col-1).value} COP/mes\n"
                    f"<b>NOMBRE:</b> {sheet.cell(cell3.row, cell3.col).value}\n"
                    f"<b>CORREO ELECTR??NICO:</b> {sheet.cell(cell3.row, cell3.col+1).value}\n"
                    f"<b>FECHA DE PAGO OPORTUNO:</b> {sheet.cell(cell3.row, cell3.col+3).value}\n"
                    f"<b>FECHA DE CORTE:</b> {sheet.cell(cell3.row, cell3.col+4).value}"   )
                
                time.sleep(1)
                break
            except ValueError:
                    update.message.reply_text("Oopss! ese no era un n??mero v??lido, por favor ingresa s??lo 4 n??meros o env??a /saltar si no lo recuerdas.")
                    time.sleep(1)
                    break
        #id = update.message.from_user.id
        bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
        bot.sendMessage(chat_id= id, parse_mode= "HTML", text="Espero la informaci??n brindada sea de ayuda, si tienes alguna inquietud no dudes en contactarnos, el comando /asesor te puede ayudar. ??Tus amigos de <b>Netflix Colombia</b>!????????\n\n/start para regresar al men?? principal.")
    return ConversationHandler.END

def brarlynn_mu??oz(update: Update, context: CallbackContext) -> int:

    query = update.callback_query
    query.answer()
    user = query.message.from_user
    logger.info(f'El usuario {user.first_name} {user.last_name}, ha escogido el perfil a nombre de Brarlynn Mu??oz.')
    query.message.reply_text('Por motivos de seguridad para mirar la informaci??n de tu cuenta env??ame el pin de 4 d??gitos asociado a tu perfil.\n\n'
        "O env??a /saltar si no lo recuerdas.",
        reply_markup=ReplyKeyboardRemove(),
        )
    return PIN_BRARLYNNM

def pin_brarlynnm(update: Update, context: CallbackContext) -> int:

    for i in range(1):          
        while True:
            try:
                pin = int(update.message.text)
                update.message.reply_text("El pin ingresado no corresponde al del perfil seleccionado.\n"
                "Int??ntalo de nuevo o env??a /saltar si no lo recuerdas.")
                if(pin == 4321):
                    cell3 = sheet.find("Brarlynn Mu??oz")
                    id = update.message.from_user.id
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                    bot.sendMessage(chat_id= id, text="??Espera... este pin s?? lo reconozco!????")
                    time.sleep(1)
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                    bot.sendMessage(chat_id= id, text="Esta es la informaci??n de tu cuenta: \n\n")
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)     
                    context.bot.sendMessage(chat_id= id, parse_mode= "HTML", text=
                    f"<b>ESTADO:</b> {sheet.cell(cell3.row, cell3.col-3).value}\n" 
                    f"<b>PLAN:</b> {sheet.cell(cell3.row, cell3.col-2).value}\n"    
                    f"<b>PRECIO:</b> ${sheet.cell(cell3.row, cell3.col-1).value} COP/mes\n"
                    f"<b>NOMBRE:</b> {sheet.cell(cell3.row, cell3.col).value}\n"
                    f"<b>CORREO ELECTR??NICO:</b> {sheet.cell(cell3.row, cell3.col+1).value}\n"
                    f"<b>FECHA DE PAGO OPORTUNO:</b> {sheet.cell(cell3.row, cell3.col+3).value}\n"
                    f"<b>FECHA DE CORTE:</b> {sheet.cell(cell3.row, cell3.col+4).value}"   )
                
                time.sleep(1)
                break
            except ValueError:
                    update.message.reply_text("Oopss! ese no era un n??mero v??lido, por favor ingresa s??lo 4 n??meros o env??a /saltar si no lo recuerdas.")
                    time.sleep(1)
                    break
        #id = update.message.from_user.id
        bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
        bot.sendMessage(chat_id= id, parse_mode= "HTML", text="Espero la informaci??n brindada sea de ayuda, si tienes alguna inquietud no dudes en contactarnos, el comando /asesor te puede ayudar. ??Tus amigos de <b>Netflix Colombia</b>!????????\n\n/start para regresar al men?? principal.")
    return ConversationHandler.END

def karen_fonseca(update: Update, context: CallbackContext) -> int:

    query = update.callback_query
    query.answer()
    user = query.message.from_user
    logger.info(f'El usuario {user.first_name} {user.last_name}, ha escogido el perfil a nombre de Karen Fonseca.')
    query.message.reply_text('Has escogido el perfil "Karen Fonseca" por motivos de seguridad para mirar la informaci??n de tu cuenta env??ame el pin de 4 d??gitos asociado a tu perfil.\n\n'
        "O env??a /saltar si no lo recuerdas.",
        reply_markup=ReplyKeyboardRemove(),
        )
    return PIN_KARENF

def pin_karenf(update: Update, context: CallbackContext) -> int:

    for i in range(1):          
        while True:
            try:
                pin = int(update.message.text)
                update.message.reply_text("El pin ingresado no corresponde al del perfil seleccionado.\n"
                "Int??ntalo de nuevo o env??a /saltar si no lo recuerdas.")
                if(pin == 1797):
                    cell3 = sheet.find("Karen Fonseca")
                    id = update.message.from_user.id
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                    bot.sendMessage(chat_id= id, text="??Espera... este pin s?? lo reconozco!????")
                    time.sleep(1)
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                    bot.sendMessage(chat_id= id, text="Esta es la informaci??n de tu cuenta: \n\n")
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)     
                    context.bot.sendMessage(chat_id= id, parse_mode= "HTML", text=
                    f"<b>ESTADO:</b> {sheet.cell(cell3.row, cell3.col-3).value}\n" 
                    f"<b>PLAN:</b> {sheet.cell(cell3.row, cell3.col-2).value}\n"    
                    f"<b>PRECIO:</b> ${sheet.cell(cell3.row, cell3.col-1).value} COP/mes\n"
                    f"<b>NOMBRE:</b> {sheet.cell(cell3.row, cell3.col).value}\n"
                    f"<b>CORREO ELECTR??NICO:</b> {sheet.cell(cell3.row, cell3.col+1).value}\n"
                    f"<b>FECHA DE PAGO OPORTUNO:</b> {sheet.cell(cell3.row, cell3.col+3).value}\n"
                    f"<b>FECHA DE CORTE:</b> {sheet.cell(cell3.row, cell3.col+4).value}"   )
                
                time.sleep(1)
                break
            except ValueError:
                    update.message.reply_text("Oopss! ese no era un n??mero v??lido, por favor ingresa s??lo 4 n??meros o env??a /saltar si no lo recuerdas.")
                    time.sleep(1)
                    break
        #id = update.message.from_user.id
        bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
        bot.sendMessage(chat_id= id, parse_mode= "HTML", text="Espero la informaci??n brindada sea de ayuda, si tienes alguna inquietud no dudes en contactarnos, el comando /asesor te puede ayudar. ??Tus amigos de <b>Netflix Colombia</b>!????????\n\n/start para regresar al men?? principal.")
    return ConversationHandler.END

def david_chavarriaga(update: Update, context: CallbackContext) -> int:

    query = update.callback_query
    query.answer()
    user = query.message.from_user
    logger.info(f'El usuario {user.first_name} {user.last_name}, ha escogido el perfil a nombre de David Chavarriaga Sep??lveda.')
    query.message.reply_text('Has escogido el perfil "David" por motivos de seguridad para mirar la informaci??n de tu cuenta env??ame el pin de 4 d??gitos asociado a tu perfil.\n\n'
        "O env??a /saltar si no lo recuerdas.",
        reply_markup=ReplyKeyboardRemove(),
        )
    return PIN_DAVIDCHA

def pin_davidcha(update: Update, context: CallbackContext) -> int:

    for i in range(1):          
        while True:
            try:
                pin = int(update.message.text)
                update.message.reply_text("El pin ingresado no corresponde al del perfil seleccionado.\n"
                "Int??ntalo de nuevo o env??a /saltar si no lo recuerdas.")
                if(pin == 9669):
                    cell3 = sheet.find("David Chavarriaga Sep??lveda")
                    id = update.message.from_user.id
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                    bot.sendMessage(chat_id= id, text="??Espera... este pin s?? lo reconozco!????")
                    time.sleep(1)
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                    bot.sendMessage(chat_id= id, text="Esta es la informaci??n de tu cuenta: \n\n")
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)     
                    context.bot.sendMessage(chat_id= id, parse_mode= "HTML", text=
                    f"<b>ESTADO:</b> {sheet.cell(cell3.row, cell3.col-3).value}\n" 
                    f"<b>PLAN:</b> {sheet.cell(cell3.row, cell3.col-2).value}\n"    
                    f"<b>PRECIO:</b> ${sheet.cell(cell3.row, cell3.col-1).value} COP/mes\n"
                    f"<b>NOMBRE:</b> {sheet.cell(cell3.row, cell3.col).value}\n"
                    f"<b>CORREO ELECTR??NICO:</b> {sheet.cell(cell3.row, cell3.col+1).value}\n"
                    f"<b>FECHA DE PAGO OPORTUNO:</b> {sheet.cell(cell3.row, cell3.col+3).value}\n"
                    f"<b>FECHA DE CORTE:</b> {sheet.cell(cell3.row, cell3.col+4).value}"   )
                
                time.sleep(1)
                break
            except ValueError:
                    update.message.reply_text("Oopss! ese no era un n??mero v??lido, por favor ingresa s??lo 4 n??meros o env??a /saltar si no lo recuerdas.")
                    time.sleep(1)
                    break
        #id = update.message.from_user.id
        bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
        bot.sendMessage(chat_id= id, parse_mode= "HTML", text="Espero la informaci??n brindada sea de ayuda, si tienes alguna inquietud no dudes en contactarnos, el comando /asesor te puede ayudar. ??Tus amigos de <b>Netflix Colombia</b>!????????\n\n/start para regresar al men?? principal.")
    return ConversationHandler.END

def clau_jimenez(update: Update, context: CallbackContext) -> int:

    query = update.callback_query
    query.answer()
    user = query.message.from_user
    logger.info(f'El usuario {user.first_name} {user.last_name}, ha escogido el perfil a nombre de Claudia Jim??nez')
    query.message.reply_text('Has escogido el perfil "Clau Jim??nez" por motivos de seguridad para mirar la informaci??n de tu cuenta env??ame el pin de 4 d??gitos asociado a tu perfil.\n\n'
        "O env??a /saltar si no lo recuerdas.",
        reply_markup=ReplyKeyboardRemove(),
        )
    return PIN_CLAUJIMENEZ

def pin_claujimenez(update: Update, context: CallbackContext) -> int:

    for i in range(1):          
        while True:
            try:
                pin = int(update.message.text)
                update.message.reply_text("El pin ingresado no corresponde al del perfil seleccionado.\n"
                "Int??ntalo de nuevo o env??a /saltar si no lo recuerdas.")
                if(pin == 1454):
                    cell3 = sheet.find("Claudia Jim??nez")
                    id = update.message.from_user.id
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                    bot.sendMessage(chat_id= id, text="??Espera... este pin s?? lo reconozco!????")
                    time.sleep(1)
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                    bot.sendMessage(chat_id= id, text="Esta es la informaci??n de tu cuenta: \n\n")
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)     
                    context.bot.sendMessage(chat_id= id, parse_mode= "HTML", text=
                    f"<b>ESTADO:</b> {sheet.cell(cell3.row, cell3.col-3).value}\n" 
                    f"<b>PLAN:</b> {sheet.cell(cell3.row, cell3.col-2).value}\n"    
                    f"<b>PRECIO:</b> ${sheet.cell(cell3.row, cell3.col-1).value} COP/mes\n"
                    f"<b>NOMBRE:</b> {sheet.cell(cell3.row, cell3.col).value}\n"
                    f"<b>CORREO ELECTR??NICO:</b> {sheet.cell(cell3.row, cell3.col+1).value}\n"
                    f"<b>FECHA DE PAGO OPORTUNO:</b> {sheet.cell(cell3.row, cell3.col+3).value}\n"
                    f"<b>FECHA DE CORTE:</b> {sheet.cell(cell3.row, cell3.col+4).value}"   )
                
                time.sleep(1)
                break
            except ValueError:
                    update.message.reply_text("Oopss! ese no era un n??mero v??lido, por favor ingresa s??lo 4 n??meros o env??a /saltar si no lo recuerdas.")
                    time.sleep(1)
                    break
        #id = update.message.from_user.id
        bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
        bot.sendMessage(chat_id= id, parse_mode= "HTML", text="Espero la informaci??n brindada sea de ayuda, si tienes alguna inquietud no dudes en contactarnos, el comando /asesor te puede ayudar. ??Tus amigos de <b>Netflix Colombia</b>!????????\n\n/start para regresar al men?? principal.")
    return ConversationHandler.END

def yimar(update: Update, context: CallbackContext) -> int:

    query = update.callback_query
    query.answer()
    user = query.message.from_user
    logger.info(f'El usuario {user.first_name} {user.last_name}, ha escogido el perfil a nombre de Claudia Jim??nez')
    query.message.reply_text('Has escogido el perfil "Yimar" por motivos de seguridad para mirar la informaci??n de tu cuenta env??ame el pin de 4 d??gitos asociado a tu perfil.\n\n'
        "O env??a /saltar si no lo recuerdas.",
        reply_markup=ReplyKeyboardRemove(),
        )
    return PIN_YIMAR

def pin_yimar(update: Update, context: CallbackContext) -> int:

    for i in range(1):          
        while True:
            try:
                pin = int(update.message.text)
                update.message.reply_text("El pin ingresado no corresponde al del perfil seleccionado.\n"
                "Int??ntalo de nuevo o env??a /saltar si no lo recuerdas.")
                if(pin == 1308):
                    cell3 = sheet.find("Yimar (pap?? de brayan)")
                    id = update.message.from_user.id
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                    bot.sendMessage(chat_id= id, text="??Espera... este pin s?? lo reconozco!????")
                    time.sleep(1)
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                    bot.sendMessage(chat_id= id, text="Esta es la informaci??n de tu cuenta: \n\n")
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)     
                    context.bot.sendMessage(chat_id= id, parse_mode= "HTML", text=
                    f"<b>ESTADO:</b> {sheet.cell(cell3.row, cell3.col-3).value}\n" 
                    f"<b>PLAN:</b> {sheet.cell(cell3.row, cell3.col-2).value}\n"    
                    f"<b>PRECIO:</b> ${sheet.cell(cell3.row, cell3.col-1).value} COP/mes\n"
                    f"<b>NOMBRE:</b> {sheet.cell(cell3.row, cell3.col).value}\n"
                    f"<b>CORREO ELECTR??NICO:</b> {sheet.cell(cell3.row, cell3.col+1).value}\n"
                    f"<b>FECHA DE PAGO OPORTUNO:</b> {sheet.cell(cell3.row, cell3.col+3).value}\n"
                    f"<b>FECHA DE CORTE:</b> {sheet.cell(cell3.row, cell3.col+4).value}"   )
                
                time.sleep(1)
                break
            except ValueError:
                    update.message.reply_text("Oopss! ese no era un n??mero v??lido, por favor ingresa s??lo 4 n??meros o env??a /saltar si no lo recuerdas.")
                    time.sleep(1)
                    break
        #id = update.message.from_user.id
        bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
        bot.sendMessage(chat_id= id, parse_mode= "HTML", text="Espero la informaci??n brindada sea de ayuda, si tienes alguna inquietud no dudes en contactarnos, el comando /asesor te puede ayudar. ??Tus amigos de <b>Netflix Colombia</b>!????????\n\n/start para regresar al men?? principal.")
    return ConversationHandler.END

def claudia_lopez(update: Update, context: CallbackContext) -> int:

    query = update.callback_query
    query.answer()
    user = query.message.from_user
    logger.info(f'El usuario {user.first_name} {user.last_name}, ha escogido el perfil a nombre de Claudia Jim??nez')
    query.message.reply_text('Has escogido el perfil "Claudia L??pez" por motivos de seguridad para mirar la informaci??n de tu cuenta env??ame el pin de 4 d??gitos asociado a tu perfil.\n\n'
        "O env??a /saltar si no lo recuerdas.",
        reply_markup=ReplyKeyboardRemove(),
        )
    return PIN_CLAULOPEZ

def pin_claulopez(update: Update, context: CallbackContext) -> int:

    for i in range(1):          
        while True:
            try:
                pin = int(update.message.text)
                update.message.reply_text("El pin ingresado no corresponde al del perfil seleccionado.\n"
                "Int??ntalo de nuevo o env??a /saltar si no lo recuerdas.")
                if(pin == 518):
                    cell3 = sheet.find("Claudia L??pez")
                    id = update.message.from_user.id
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                    bot.sendMessage(chat_id= id, text="??Espera... este pin s?? lo reconozco!????")
                    time.sleep(1)
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                    bot.sendMessage(chat_id= id, text="Esta es la informaci??n de tu cuenta: \n\n")
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)     
                    context.bot.sendMessage(chat_id= id, parse_mode= "HTML", text=
                    f"<b>ESTADO:</b> {sheet.cell(cell3.row, cell3.col-3).value}\n" 
                    f"<b>PLAN:</b> {sheet.cell(cell3.row, cell3.col-2).value}\n"    
                    f"<b>PRECIO:</b> ${sheet.cell(cell3.row, cell3.col-1).value} COP/mes\n"
                    f"<b>NOMBRE:</b> {sheet.cell(cell3.row, cell3.col).value}\n"
                    f"<b>CORREO ELECTR??NICO:</b> {sheet.cell(cell3.row, cell3.col+1).value}\n"
                    f"<b>FECHA DE PAGO OPORTUNO:</b> {sheet.cell(cell3.row, cell3.col+3).value}\n"
                    f"<b>FECHA DE CORTE:</b> {sheet.cell(cell3.row, cell3.col+4).value}"   )
                
                time.sleep(1)
                break
            except ValueError:
                    update.message.reply_text("Oopss! ese no era un n??mero v??lido, por favor ingresa s??lo 4 n??meros o env??a /saltar si no lo recuerdas.")
                    time.sleep(1)
                    break
        #id = update.message.from_user.id
        bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
        bot.sendMessage(chat_id= id, parse_mode= "HTML", text="Espero la informaci??n brindada sea de ayuda, si tienes alguna inquietud no dudes en contactarnos, el comando /asesor te puede ayudar. ??Tus amigos de <b>Netflix Colombia</b>!????????\n\n/start para regresar al men?? principal.")
    return ConversationHandler.END

def diana_jimenez(update: Update, context: CallbackContext) -> int:

    query = update.callback_query
    query.answer()
    user = query.message.from_user
    logger.info(f'El usuario {user.first_name} {user.last_name}, ha escogido el perfil a nombre de Claudia Jim??nez')
    query.message.reply_text('Has escogido el perfil "Diana Jim??nez" por motivos de seguridad para mirar la informaci??n de tu cuenta env??ame el pin de 4 d??gitos asociado a tu perfil.\n\n'
        "O env??a /saltar si no lo recuerdas.",
        reply_markup=ReplyKeyboardRemove(),
        )
    return PIN_DIANAJIMENEZ

def pin_dianajimenez(update: Update, context: CallbackContext) -> int:

    for i in range(1):          
        while True:
            try:
                pin = int(update.message.text)
                update.message.reply_text("El pin ingresado no corresponde al del perfil seleccionado.\n"
                "Int??ntalo de nuevo o env??a /saltar si no lo recuerdas.")
                if(pin == 3060):
                    cell3 = sheet.find("Diana Jim??nez")
                    id = update.message.from_user.id
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                    bot.sendMessage(chat_id= id, text="??Espera... este pin s?? lo reconozco!????")
                    time.sleep(1)
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                    bot.sendMessage(chat_id= id, text="Esta es la informaci??n de tu cuenta: \n\n")
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)     
                    context.bot.sendMessage(chat_id= id, parse_mode= "HTML", text=
                    f"<b>ESTADO:</b> {sheet.cell(cell3.row, cell3.col-3).value}\n" 
                    f"<b>PLAN:</b> {sheet.cell(cell3.row, cell3.col-2).value}\n"    
                    f"<b>PRECIO:</b> ${sheet.cell(cell3.row, cell3.col-1).value} COP/mes\n"
                    f"<b>NOMBRE:</b> {sheet.cell(cell3.row, cell3.col).value}\n"
                    f"<b>CORREO ELECTR??NICO:</b> {sheet.cell(cell3.row, cell3.col+1).value}\n"
                    f"<b>FECHA DE PAGO OPORTUNO:</b> {sheet.cell(cell3.row, cell3.col+3).value}\n"
                    f"<b>FECHA DE CORTE:</b> {sheet.cell(cell3.row, cell3.col+4).value}"   )
                
                time.sleep(1)
                break
            except ValueError:
                    update.message.reply_text("Oopss! ese no era un n??mero v??lido, por favor ingresa s??lo 4 n??meros o env??a /saltar si no lo recuerdas.")
                    time.sleep(1)
                    break
        #id = update.message.from_user.id
        bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
        bot.sendMessage(chat_id= id, parse_mode= "HTML", text="Espero la informaci??n brindada sea de ayuda, si tienes alguna inquietud no dudes en contactarnos, el comando /asesor te puede ayudar. ??Tus amigos de <b>Netflix Colombia</b>!????????\n\n/start para regresar al men?? principal.")
    return ConversationHandler.END

def manuela_montoya(update: Update, context: CallbackContext) -> int:

    query = update.callback_query
    query.answer()
    user = query.message.from_user
    logger.info(f'El usuario {user.first_name} {user.last_name}, ha escogido el perfil Daniela Acevedo.')
    query.message.reply_text("Has escogido el perfil Manuela, por motivos de seguridad para mirar la informaci??n de tu cuenta env??ame el pin de 4 d??gitos asociado a tu perfil.\n\n"
        "O env??a /saltar si no lo recuerdas.",
        reply_markup=ReplyKeyboardRemove(),
        )
    
    return PIN_MANUELAMON

def pin_manuelamon(update: Update, context: CallbackContext) -> int:
              
    while True:
        try:
            pin = int(update.message.text)
            update.message.reply_text("El pin ingresado no corresponde al del perfil seleccionado.\n"
            "Int??ntalo de nuevo o env??a /saltar si no lo recuerdas.")
            if(pin == 0000):
                #print(pin)
                cell3 = sheet.find("Manuela Montoya Quintero")
                id = update.message.from_user.id
                bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                bot.sendMessage(chat_id= id, text="??Espera... este pin s?? lo reconozco!????")
                time.sleep(1)
                bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                bot.sendMessage(chat_id= id, text="Esta es la informaci??n de tu cuenta: \n\n")
                bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)     
                context.bot.sendMessage(chat_id= id, parse_mode= "HTML", text=
                f"<b>ESTADO:</b> {sheet.cell(cell3.row, cell3.col-3).value}\n" 
                f"<b>PLAN:</b> {sheet.cell(cell3.row, cell3.col-2).value}\n"    
                f"<b>PRECIO:</b> ${sheet.cell(cell3.row, cell3.col-1).value} COP/mes\n"
                f"<b>NOMBRE:</b> {sheet.cell(cell3.row, cell3.col).value}\n"
                f"<b>CORREO ELECTR??NICO:</b> {sheet.cell(cell3.row, cell3.col+1).value}\n"
                f"<b>FECHA DE PAGO OPORTUNO:</b> {sheet.cell(cell3.row, cell3.col+3).value}\n"
                f"<b>FECHA DE CORTE:</b> {sheet.cell(cell3.row, cell3.col+4).value}"   )
            
            time.sleep(1)
            break
            #time.sleep(1)
        except ValueError:
                update.message.reply_text("Oopss! ese no era un n??mero v??lido, por favor ingresa s??lo 4 n??meros o env??a /saltar si no lo recuerdas.")
                time.sleep(1)
                break
    #id = update.message.from_user.id
    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
    bot.sendMessage(chat_id= id, parse_mode= "HTML", text="Espero la informaci??n brindada sea de ayuda, si tienes alguna inquietud no dudes en contactarnos, el comando /asesor te puede ayudar. ??Tus amigos de <b>Netflix Colombia</b>!????????\n\n/start para regresar al men?? principal.")
    return ConversationHandler.END

def mauro_patino(update: Update, context: CallbackContext) -> int:

    query = update.callback_query
    query.answer()
    user = query.message.from_user
    logger.info(f'El usuario {user.first_name} {user.last_name}, ha escogido el perfil Daniela Acevedo.')
    query.message.reply_text("Has escogido el perfil Berenice, por motivos de seguridad para mirar la informaci??n de tu cuenta env??ame el pin de 4 d??gitos asociado a tu perfil.\n\n"
        "O env??a /saltar si no lo recuerdas.",
        reply_markup=ReplyKeyboardRemove(),
        )
    
    return PIN_MAUROPATINO

def pin_mauropatino(update: Update, context: CallbackContext) -> int:
              
    while True:
        try:
            pin = int(update.message.text)
            update.message.reply_text("El pin ingresado no corresponde al del perfil seleccionado.\n"
            "Int??ntalo de nuevo o env??a /saltar si no lo recuerdas.")
            if(pin == 1953):
                #print(pin)
                cell3 = sheet.find("Berenice (Mauro Pati??o)")
                id = update.message.from_user.id
                bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                bot.sendMessage(chat_id= id, text="??Espera... este pin s?? lo reconozco!????")
                time.sleep(1)
                bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                bot.sendMessage(chat_id= id, text="Esta es la informaci??n de tu cuenta: \n\n")
                bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)     
                context.bot.sendMessage(chat_id= id, parse_mode= "HTML", text=
                f"<b>ESTADO:</b> {sheet.cell(cell3.row, cell3.col-3).value}\n" 
                f"<b>PLAN:</b> {sheet.cell(cell3.row, cell3.col-2).value}\n"    
                f"<b>PRECIO:</b> ${sheet.cell(cell3.row, cell3.col-1).value} COP/mes\n"
                f"<b>NOMBRE:</b> {sheet.cell(cell3.row, cell3.col).value}\n"
                f"<b>CORREO ELECTR??NICO:</b> {sheet.cell(cell3.row, cell3.col+1).value}\n"
                f"<b>FECHA DE PAGO OPORTUNO:</b> {sheet.cell(cell3.row, cell3.col+3).value}\n"
                f"<b>FECHA DE CORTE:</b> {sheet.cell(cell3.row, cell3.col+4).value}"   )
            
            time.sleep(1)
            break
            #time.sleep(1)
        except ValueError:
                update.message.reply_text("Oopss! ese no era un n??mero v??lido, por favor ingresa s??lo 4 n??meros o env??a /saltar si no lo recuerdas.")
                time.sleep(1)
                break
    #id = update.message.from_user.id
    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
    bot.sendMessage(chat_id= id, parse_mode= "HTML", text="Espero la informaci??n brindada sea de ayuda, si tienes alguna inquietud no dudes en contactarnos, el comando /asesor te puede ayudar. ??Tus amigos de <b>Netflix Colombia</b>!????????\n\n/start para regresar al men?? principal.")
    return ConversationHandler.END

def henry_mosquera(update: Update, context: CallbackContext) -> int:

    query = update.callback_query
    query.answer()
    user = query.message.from_user
    logger.info(f'El usuario {user.first_name} {user.last_name}, ha escogido el perfil Henry Mosquera.')
    query.message.reply_text("Has escogido el perfil Henry, por motivos de seguridad para mirar la informaci??n de tu cuenta env??ame el pin de 4 d??gitos asociado a tu perfil.\n\n"
        "O env??a /saltar si no lo recuerdas.",
        reply_markup=ReplyKeyboardRemove(),
        )
    
    return PIN_HENRYMOSQUERA

def pin_henrymosquera(update: Update, context: CallbackContext) -> int:
              
    while True:
        try:
            pin = int(update.message.text)
            update.message.reply_text("El pin ingresado no corresponde al del perfil seleccionado.\n"
            "Int??ntalo de nuevo o env??a /saltar si no lo recuerdas.")
            if(pin == 8423):
                #print(pin)
                cell3 = sheet.find("Henry Mosquera")
                id = update.message.from_user.id
                bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                bot.sendMessage(chat_id= id, text="??Espera... este pin s?? lo reconozco!????")
                time.sleep(1)
                bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                bot.sendMessage(chat_id= id, text="Esta es la informaci??n de tu cuenta: \n\n")
                bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)     
                context.bot.sendMessage(chat_id= id, parse_mode= "HTML", text=
                f"<b>ESTADO:</b> {sheet.cell(cell3.row, cell3.col-3).value}\n" 
                f"<b>PLAN:</b> {sheet.cell(cell3.row, cell3.col-2).value}\n"    
                f"<b>PRECIO:</b> ${sheet.cell(cell3.row, cell3.col-1).value} COP/mes\n"
                f"<b>NOMBRE:</b> {sheet.cell(cell3.row, cell3.col).value}\n"
                f"<b>CORREO ELECTR??NICO:</b> {sheet.cell(cell3.row, cell3.col+1).value}\n"
                f"<b>FECHA DE PAGO OPORTUNO:</b> {sheet.cell(cell3.row, cell3.col+3).value}\n"
                f"<b>FECHA DE CORTE:</b> {sheet.cell(cell3.row, cell3.col+4).value}"   )
            
            time.sleep(1)
            break
            #time.sleep(1)
        except ValueError:
                update.message.reply_text("Oopss! ese no era un n??mero v??lido, por favor ingresa s??lo 4 n??meros o env??a /saltar si no lo recuerdas.")
                time.sleep(1)
                break
    #id = update.message.from_user.id
    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
    bot.sendMessage(chat_id= id, parse_mode= "HTML", text="Espero la informaci??n brindada sea de ayuda, si tienes alguna inquietud no dudes en contactarnos, el comando /asesor te puede ayudar. ??Tus amigos de <b>Netflix Colombia</b>!????????\n\n/start para regresar al men?? principal.")
    return ConversationHandler.END

def saltar_pin(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    id = update.message.from_user.id
    logger.info("Usuario %s %s no envi?? pin.", user.first_name, user.last_name)
    context.bot.sendMessage(chat_id= id, parse_mode= "HTML", text=
        'Puedes intentarlo m??s tarde. El comando /ayuda te puede ser ??til.\n'
         '??Tus amigos de <b>Netflix Colombia</b>????????!'
    )

    return ConversationHandler.END



def promociones(update: Update, context: CallbackContext) -> int:

    user = update.message.from_user
 
    logger.info(f'El usuario {user.first_name} {user.last_name}, ha seleccionado el comando /promociones.')
    id = update.message.chat_id

    update.message.reply_text(
        text='En esta secci??n encontrar??s las promociones vigentes.\n\n'
    )
    with open('img/TarifasNetflixColombia2021.jpeg','rb') as photo_file:
     bot.sendChatAction(chat_id=id, action=ChatAction.UPLOAD_PHOTO, timeout=None)
     time.sleep(1)
     bot.sendPhoto(chat_id=id, photo=photo_file, caption='Tarifas Netflix Colombia 2021.')
     bot.sendChatAction(chat_id=id, action=ChatAction.TYPING, timeout=None)
     time.sleep(1)
     context.bot.sendMessage(chat_id=id, parse_mode='MarkdownV2',
     text="*Plan b??sico 1 pantalla SD:*\n??? *3 meses:* $45\.000 COP\n??? *6 meses:* $80\.000 COP\n??? *12 meses:* $150\.000 COP\n\n"
     "*Plan est??ndar 2 pantallas HD:*\n??? *3 meses:* $80\.000 COP\n??? *6 meses:* $150\.000 COP\n??? *12 meses:* $280\.000 COP\n\n"
     "*Plan premium 4 pantallas UHD:*\n??? *3 meses:* $95\.000 COP\n??? *6 meses:* $180\.000 COP\n??? *12 meses:* $350\.000 COP\n"
    )
    with open('videos/netflix_gif.mp4','rb') as video_file:
     bot.sendChatAction(chat_id=id, action=ChatAction.TYPING, timeout=None)
     time.sleep(1)
     bot.sendMessage(chat_id=id, parse_mode= "HTML", text="Recuerda que el comando /pago te brindar?? la informaci??n necesaria para que realices tu compra.\n"
     "Atentamente, el equipo de <b>Netflix Colombia</b>????????.")
     bot.sendChatAction(chat_id=id, action=ChatAction.TYPING, timeout=None)
     bot.send_video(chat_id=id, video=video_file, caption='@netflixcolombiabot', timeout=None)

    return ConversationHandler.END

def preguntas(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    id = update.message.from_user.id
    logger.info(f'El usuario {user.first_name}{user.last_name}({id}) ingres?? el comando /preguntas')
    context.bot.sendMessage(chat_id= id, parse_mode="HTML", text= "En esta secci??n encontrar??s las preguntas frecuentes que suelen hacerse los usuarios, espero te sirva. ??????\n\n"
    "<b><i>(Env??a s??lo el n??mero correspondiente a la pregunta)</i></b>\n\n"

    "<b>1.</b> ??Por qu?? mi cuenta se cancel?? si ya realic?? el pago?\n"
    "<b>2.</b> ??C??mo y cu??ndo debo pagar mi cuenta?\n"
    "<b>3.</b> ??Por qu?? me sale un aviso diciendo que quedan pocos d??as de membres??a?\n"
    "<b>4.</b> ??C??mo puedo saber si alguien m??s utiliza mi cuenta?\n"
    "<b>5.</b> ??C??mo puedo cambiar la contrase??a de mi cuenta de Netflix?\n"
    "<b>6.</b> ??Puedo comprar una cuenta de Netflix y agregarle mi correo electr??nico?\n"
    "<b>7.</b> ??S??lo manejan cuentas de Netflix o tambi??n otras plataformas?\n"
    "<b>8.</b> ??Manejan planes por varios meses?\n"
    "<b>9.</b> ??C??mo puedo adquirir una cuenta?\n"
    "<b>10.</b> ??Cu??nto tiempo se tarda en activar mi cuenta una vez realizado el pago?\n"
    "<b>11.</b> ??D??nde puedo enviar el comprobante de pago?\n"
    "<b>12.</b> ??Cu??l es la contrase??a de mi cuenta de Netflix?\n"
    )
    # if(update.message.text.find("1") == 0):
    #     logger.info(f'El usuario {user.first_name} {user.last_name}, seleccion?? la pregunta 1.')
    #     update.message.reply_text("<b>??Por qu?? mi cuenta se cancel?? si ya realic?? el pago?</b>\n"
    #     "R/ Hay que tener en cuenta que el m??todo de pago de las cuentas var??a y dependiendo de la fecha de "
    #     "vencimiento del mismo, la cuenta de Netflix puede inhabilitarse. Cabe aclarar que en la mayor??a de los casos "
    #     "esta fecha de vencimiento en la informaci??n de pago es diferente a la fecha de pago oportuno del usuario.\n"
    #     "Pero no te preocupes, si realizaste el pago la membres??a de tu cuenta de Netflix se restablecer?? el mismo d??a autom??ticamente.\n\n"
    #     "??Tus amigos de Netflix????????!"
    #     )
    # if(update.message.text.find("2") == 0):
    #     logger.info(f'El usuario {user.first_name} {user.last_name}, seleccion?? la pregunta 2.')
    #     update.message.reply_text("<b>??C??mo y cu??ndo debo pagar mi cuenta?</b>\n"
    #     "R/ Recuerda que el pago puede ser por transferencia o consignaci??n bancaria a una cuenta de "
    #     "ahorros Bancolombia, Nequi o Daviplata, el comando /pago te brindar?? la informaci??n necesaria para que realices tu pago. "
    #     "Para saber el estado de tu cuenta y los detalles de tu cuenta visita el comando /micuenta y sigue los pasos.\n"
    #     "Dicho comando te brindar?? la informaci??n necesaria de tu cuenta incluyendo la fecha de pago.\n\n"
    #     "??Tus amigos de Netflix????????!"
    #     )

    #return ConversationHandler.END

def asesor(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    id = update.message.from_user.id
    logger.info(f'El usuario {user.first_name} {user.last_name}({id}) ingres?? el comando /asesor')
    
    buttonrestContra = InlineKeyboardButton(
        text='Necesito restablecer mi contrase??a',
        url='https://www.netflix.com/co/LoginHelp'
    )

    buttonPayment = InlineKeyboardButton(
        text='Necesito actualizar mi forma de pago',
        url='https://www.netflix.com/co/YourAccountPayment'
    )

    bot.sendChatAction(chat_id=id, action=ChatAction.TYPING, timeout=None)
    time.sleep(1)
    context.bot.sendMessage(chat_id= id, parse_mode="HTML", text= f"??Hola <b>{user.first_name}</b>! Espero te encuentres muy bien, Antes de chatear...\n\n"
     "Puedes resolver r??pidamente algunos problemas habituales sin necesidad de recibir ayuda en directo:")
    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
    time.sleep(1)
    update.message.reply_text(
        'Escoge una opci??n\n\n',
        reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton(text='No encuentro una serie o pel??cula en Netflix', callback_data='opcion1')],
        [buttonrestContra],
        [buttonPayment],  
        [InlineKeyboardButton(text='??Quiero hablar con un asesor!', callback_data='opcion4')]
        ]),
    )


def about(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    id = update.message.from_user.id
    logger.info(f'El usuario {user.first_name}{user.last_name}({id}) ingres?? el comando /about')
    context.bot.sendMessage(chat_id= id, parse_mode="HTML", text= "Esta secci??n se encuentra en mantenimiento, estamos trabajando arduamente para mejorar su servicio.")
    time.sleep(1)
    with open('img/mantenimiento2.png','rb') as photo_file:
     bot.sendChatAction(chat_id=id, action=ChatAction.UPLOAD_PHOTO, timeout=None)
     time.sleep(1)
     bot.sendPhoto(chat_id=id, photo=photo_file, caption='Secci??n en mantenimiento.')
     bot.sendChatAction(chat_id=id, action=ChatAction.TYPING, timeout=None)
     time.sleep(1.5)
    update.message.reply_text("Por favor disculpe las molestias.\n\n"
    "/start para volver al men?? principal.")

def ayuda(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    id = update.message.from_user.id
    logger.info(f'El usuario {user.first_name} {user.last_name}({id}) ingres?? el comando /ayuda')
    
    buttonLogging = InlineKeyboardButton(
        text='Iniciar sesi??n',
        url='https://www.netflix.com/co/Login?nextpage=https%3A%2F%2Fhelp.netflix.com%2Fes-es%2F'
    )

    bot.sendChatAction(chat_id=id, action=ChatAction.TYPING, timeout=None)
    time.sleep(0.5)

    update.message.reply_text(parse_mode="HTML", text=f'??Hola <b>{user.first_name}</b>! Espero te encuentres muy bien.\n'
        'Bienvenido(a) al <b>Centro de ayuda</b> de <b>Netflix Colombia</b>.\n\n'
        'Inicia sesi??n para obtener ayuda personalizada o mira los temas populares\n\n',
        reply_markup=InlineKeyboardMarkup([
        [buttonLogging],
        [InlineKeyboardButton(text='????C??mo suscribirse a Netflix', callback_data='how_to_suscribe')],
        [InlineKeyboardButton(text='????Planes y precios', callback_data='plans_and_prices')],
        [InlineKeyboardButton(text='????No puedo iniciar sesi??n en Netflix', callback_data='i_cant_start')],
        [InlineKeyboardButton(text='C??mo comenzar', callback_data='how_to_start'), InlineKeyboardButton(text='No se puede ver', callback_data='it_cant_be_see')],
        [InlineKeyboardButton(text='Gestionar mi cuenta', callback_data='manage_account'), InlineKeyboardButton(text='Ver Netflix', callback_data='watch_netflix')],
        [InlineKeyboardButton(text='Enlaces r??pidos', callback_data='quick_links'), InlineKeyboardButton(text='Art??culos sugeridos', callback_data='suggested_articles')],
        [InlineKeyboardButton(text='Ir al men?? principal', callback_data='inicio')]
        ])
    )


def help(update: Update, context: CallbackContext) -> int:
    
    query = update.callback_query
    query.answer()

    user =query.message.from_user
    id = query.message.chat_id
    logger.info(f'El usuario {user.first_name} {user.last_name} {id} ha ingresado al comando /ayuda.')

    buttonLogging = InlineKeyboardButton(
        text='Iniciar sesi??n',
        url='https://www.netflix.com/co/Login?nextpage=https%3A%2F%2Fhelp.netflix.com%2Fes-es%2F'
    )

    query.edit_message_text(parse_mode="HTML", text=f'??Hola <b>{user.first_name}</b>! Espero te encuentres muy bien.\n'
    'Bienvenido(a) al <b>Centro de ayuda</b> de <b>Netflix Colombia</b>.\n\n'
        'Inicia sesi??n para obtener ayuda personalizada o mira los temas populares\n\n',
        reply_markup=InlineKeyboardMarkup([
        [buttonLogging],
        [InlineKeyboardButton(text='????C??mo suscribirse a Netflix', callback_data='how_to_suscribe')],
        [InlineKeyboardButton(text='????Planes y precios', callback_data='plans_and_prices')],
        [InlineKeyboardButton(text='????No puedo iniciar sesi??n en Netflix', callback_data='i_cant_start')],
        [InlineKeyboardButton(text='C??mo comenzar', callback_data='how_to_start'), InlineKeyboardButton(text='No se puede ver', callback_data='it_cant_be_see')],
        [InlineKeyboardButton(text='Gestionar mi cuenta', callback_data='manage_account'), InlineKeyboardButton(text='Ver Netflix', callback_data='watch_netflix' )],
        [InlineKeyboardButton(text='Enlaces r??pidos', callback_data='quick_links'), InlineKeyboardButton(text='Art??culos sugeridos', callback_data='suggested_articles')],
        [InlineKeyboardButton(text='Ir al men?? principal', callback_data='inicio')]
        ])
    )

    return ConversationHandler.END

def how_to_suscribe(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    user = query.message.from_user
    id = query.message.from_user.id
    logger.info(f'El usuario {user.first_name}{user.last_name}({id}) seleccion?? el bot??n C??mo suscribirse a Netflix')

    buttonMoreInfo = InlineKeyboardButton(
        text='M??s informaci??n sobre Netflix',
        url='https://help.netflix.com/es-es/node/412'
    )

    query.edit_message_text(
        parse_mode= "HTML", text='<b>C??mo suscribirse a Netflix</b>\n\n'
        '??nete a los millones de suscriptores de todo el mundo que disfrutan de acceso ilimitado a series, pel??culas, documentales y otros contenidos premiados sin un solo anuncio.\n\n'
        'Como suscriptor de Netflix, se te cobrar?? una vez al mes en el d??a en que te suscribiste. Sin contratos, sin cargos por cancelaci??n y sin compromisos. Tienes la flexibilidad de <a href="https://help.netflix.com/es-es/node/22" target="_self">cambiar de plan</a> o de <a href="https://help.netflix.com/es-es/node/407" target="_self">cancelar</a> la suscripci??n en l??nea en cualquier momento si decides que Netflix no es para ti.\n\n'
        '??Suscribirse a una cuenta de Netflix es muy f??cil! Realiza los pasos siguientes para tu plataforma.\n\n',
        reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton(text='Android', callback_data='android')],
        [InlineKeyboardButton(text='Ordenador', callback_data='ordenador')],
        [InlineKeyboardButton(text='iPhone, iPad o iPad touch', callback_data='iphone')],
        [InlineKeyboardButton(text='Smart TV y reproductores multimedia de contenido en streaming', callback_data='smartTV')],
        [InlineKeyboardButton(text='Decodificador', callback_data='decodificador')],
        [buttonMoreInfo],
        [InlineKeyboardButton(text='Atr??s', callback_data='help')],
        [InlineKeyboardButton(text='Men?? principal', callback_data='inicio')],
        ]),
    )

    return ConversationHandler.END

def android(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    user = query.message.from_user
    id = query.message.from_user.id
    logger.info(f'El usuario {user.first_name}{user.last_name} (ID:{id}) seleccion?? el bot??n Android')

    buttonWhatIsNetflix = InlineKeyboardButton(
        text='M??s informaci??n sobre Netflix',
        url='https://help.netflix.com/es-es/node/412'
    )

    query.edit_message_text(
        parse_mode= "HTML", text='<b>Android</b>\n\n'
        'Elige una de las siguientes opciones para suscribirte desde tu dispositivo Android:\n\n'
        '???Descarga la aplicaci??n de Netflix de Google Play Store en un dispositivo con Android 5.0 o posterior.\n'
        '???Visita <a href="https://www.netflix.com/signup" target="_self">netflix.com/signup</a> desde un navegador m??vil.\n\n'
        'Desde la aplicaci??n de Netflix o en netflix.com puedes:\n\n'
        ' 1?????? Selecciona el plan ideal para ti. Puedes cambiar a un plan inferior o superior cuando quieras.\n'
        ' 2?????? Crea una cuenta introduciendo tu direcci??n de correo y creando una contrase??a.\n'
        ' 3?????? Introduce un m??todo de pago.\n'
        ' 4?????? Eso es todo. ??Y reproduce en streaming!\n\n'
        '??Te ha resultado ??til este art??culo?\n\n',
        reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton(text='S??', callback_data='answer_yes'),InlineKeyboardButton(text='No', callback_data='answer_not')],
        [buttonWhatIsNetflix],
        [InlineKeyboardButton(text='Atr??s', callback_data='how_to_suscribe')],
        [InlineKeyboardButton(text='Men?? principal', callback_data='inicio')],
        ]),
    )

    return ConversationHandler.END

def ordenador(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    user = query.message.from_user
    id = query.message.from_user.id
    logger.info(f'El usuario {user.first_name}{user.last_name} (ID:{id}) seleccion?? el bot??n Ordenador')

    buttonWhatIsNetflix = InlineKeyboardButton(
        text='M??s informaci??n sobre Netflix',
        url='https://help.netflix.com/es-es/node/412'
    )

    query.edit_message_text(
        parse_mode= "HTML", text='<b>Ordenador</b>\n\n'
        '1?????? Visita <a href="https://www.netflix.com/signup" target="_self">netflix.com/signup</a>.\n'
        '2?????? Selecciona el plan ideal para ti. Puedes cambiar a un plan inferior o superior cuando quieras.\n'
        '3?????? Crea una cuenta introduciendo tu direcci??n de correo y creando una contrase??a.\n'
        '4?????? Introduce un m??todo de pago.\n'
        '5?????? Eso es todo. ??Y reproduce en streaming!\n\n'
        '??Te ha resultado ??til este art??culo?\n\n',
        reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton(text='S??', callback_data='answer_yes'),InlineKeyboardButton(text='No', callback_data='answer_not')],
        [buttonWhatIsNetflix],
        [InlineKeyboardButton(text='Atr??s', callback_data='how_to_suscribe')],
        [InlineKeyboardButton(text='Men?? principal', callback_data='inicio')],
        ]),
    )

    return ConversationHandler.END

def iphone(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    user = query.message.from_user
    id = query.message.from_user.id
    logger.info(f'El usuario {user.first_name}{user.last_name} (ID:{id}) seleccion?? el bot??n iPhone, iPad...')

    buttonWhatIsNetflix = InlineKeyboardButton(
        text='M??s informaci??n sobre Netflix',
        url='https://help.netflix.com/es-es/node/412'
    )

    query.edit_message_text(
        parse_mode= "HTML", text='<b>iPhone, iPad o iPod touch</b>\n\n'
        '1?????? Visita <a href="https://www.netflix.com/signup" target="_self">netflix.com/signup</a> desde un navegador m??vil.\n\n'
        '    ??????<b>Nota:</b> No se admite la suscripci??n a trav??s de la aplicaci??n de Netflix para iOS.\n\n'
        '2?????? Selecciona el plan ideal para ti. Puedes cambiar a un plan inferior o superior cuando quieras.\n'
        '3?????? Crea una cuenta introduciendo tu direcci??n de correo y creando una contrase??a.\n'
        '4?????? Introduce un m??todo de pago.\n'
        '5?????? Descarga e inicia sesi??n en la aplicaci??n de Netflix en un dispositivo con iOS 13.0 o posterior.\n'
        '6?????? Eso es todo. ??Y reproduce en streaming!\n\n'
        '??Te ha resultado ??til este art??culo?\n\n',
        reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton(text='S??', callback_data='answer_yes'),InlineKeyboardButton(text='No', callback_data='answer_not')],
        [buttonWhatIsNetflix],
        [InlineKeyboardButton(text='Atr??s', callback_data='how_to_suscribe')],
        [InlineKeyboardButton(text='Men?? principal', callback_data='inicio')],
        ]),
    )

    return ConversationHandler.END

def smartTV(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    user = query.message.from_user
    id = query.message.from_user.id
    logger.info(f'El usuario {user.first_name}{user.last_name} (ID:{id}) seleccion?? el bot??n smart TV y reproductores multimedia.')

    buttonWhatIsNetflix = InlineKeyboardButton(
        text='M??s informaci??n sobre Netflix',
        url='https://help.netflix.com/es-es/node/412'
    )

    query.edit_message_text(
        parse_mode= "HTML", text='<b>Smart TV y reproductores multimedia de contenido en streaming</b>\n\n'
        '1?????? Abre la aplicaci??n de Netflix.\n\n'
        '    ?????? <b>Nota:</b> Si necesitas ayuda para encontrar la aplicaci??n, busca en nuestro <a href="https://help.netflix.com/es-es/" target="_self">Centro de ayuda</a> el art??culo '
        '??C??mo usar Netflix en??, seguido de la marca de tu dispositivo (p. ej., Samsung, Roku, Xbox). Algunos dispositivos tambi??n incluyen un bot??n Netflix en el mando a distancia.\n\n'
        '2?????? En la mayor??a de Smart TVs y reproductores multimedia de contenido en streaming tendr??s que empezar por facilitar tu direcci??n de correo electr??nico o tu n??mero de tel??fono.\n\n'
        '    ???? Una vez facilitado, recibir??s un correo o un SMS con un enlace de activaci??n que te permitir?? seguir con el proceso de suscripci??n.\n\n'
        '3?????? Selecciona el plan ideal para ti. Puedes cambiar a un plan inferior o superior cuando quieras.\n'
        '4?????? Crea una cuenta introduciendo tu direcci??n de correo y creando una contrase??a.\n'
        '5?????? Introduce un m??todo de pago.\n'
        '6?????? Eso es todo. ??Y reproduce en streaming!\n\n'
        '??Te ha resultado ??til este art??culo?\n\n',
        reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton(text='S??', callback_data='answer_yes'),InlineKeyboardButton(text='No', callback_data='answer_not')],
        [buttonWhatIsNetflix],
        [InlineKeyboardButton(text='Atr??s', callback_data='how_to_suscribe')],
        [InlineKeyboardButton(text='Men?? principal', callback_data='inicio')],
        ]),
    )

    return ConversationHandler.END

def decodificador(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    user = query.message.from_user
    id = query.message.from_user.id
    logger.info(f'El usuario {user.first_name}{user.last_name} (ID:{id}) seleccion?? el bot??n Decodificador')

    buttonWhatIsNetflix = InlineKeyboardButton(
        text='M??s informaci??n sobre Netflix',
        url='https://help.netflix.com/es-es/node/412'
    )

    query.edit_message_text(
        parse_mode= "HTML", text='<b>Decodificador</b>\n\n'
        '1?????? Abre la aplicaci??n de Netflix.\n\n'
        '    ?????? <b>Nota:</b> Si necesitas ayuda para encontrar la aplicaci??n, busca en nuestro <a href="https://help.netflix.com/es-es/" target="_self">Centro de ayuda</a> el art??culo '
        '??C??mo usar Netflix en??, seguido de la marca de tu dispositivo (p. ej., Samsung, Roku, Xbox). Algunos dispositivos tambi??n incluyen un bot??n Netflix en el mando a distancia.\n\n'
        '2?????? Selecciona el plan ideal para ti. Puedes cambiar a un plan inferior o superior cuando quieras.\n'
        '3?????? Crea una cuenta introduciendo tu direcci??n de correo y creando una contrase??a.\n'
        '4?????? Introduce un m??todo de pago.\n'
        '5?????? Eso es todo. ??Y reproduce en streaming!\n\n'
        '??Te ha resultado ??til este art??culo?\n\n',
        reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton(text='S??', callback_data='answer_yes'),InlineKeyboardButton(text='No', callback_data='answer_not')],
        [buttonWhatIsNetflix],
        [InlineKeyboardButton(text='Atr??s', callback_data='how_to_suscribe')],
        [InlineKeyboardButton(text='Men?? principal', callback_data='inicio')],
        ]),
    )

    return ConversationHandler.END

def answer_yes(update: Update, context: CallbackContext) -> int:

    query = update.callback_query
    query.answer()
    user = query.message.from_user
    id = query.message.chat_id
    logger.info(f'El usuario {user.first_name} {user.last_name} {id} ingres?? a la secci??n de art??culo ??til.')

    query.edit_message_text(parse_mode='HTML', text='<b>??Gracias por tus comentarios!</b>\n\n' 
    '<b>??Tienes alguna sugerencia que nos ayude a seguir mejorando? (Opcional)</b>\n'
    '<i><b>Nota:</b> No respondemos a comentarios individuales. No dejes datos personales.</i>\n\n'
    'Por favor escr??benos tus comentarios o env??a /saltar si prefieres omitir este paso.')

    return ANSWERYES

def suggestion(update: Update, context: CallbackContext) -> int:

    user_name = update.effective_user['first_name']
    user_last = update.effective_user['last_name']
    user_id = update.effective_user['id']

    suggesting = update.message.text

    logger.info("La sugerencia que indica el usuario %s %s es: %s", user_name, user_last, suggesting)
    update.message.reply_text(
        text=f"Muchas gracias, hemos registrado tu comentario satisfactoriamente.\n\n",
        reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton(text='Volver al men?? principal', callback_data='inicio')]
        ])
        )

    context.bot.sendMessage(chat_id='1587610512', parse_mode="HTML", text=f"<b>El usuario {user_name} {user_last} ID: {user_id} ha indicado que le ha sido ??til el art??culo, el comentario descrito por el usuario es:</b> {suggesting}")

    return ConversationHandler.END

def answer_not(update: Update, context: CallbackContext) -> int:

    query = update.callback_query
    query.answer()
    user = query.message.from_user
    id = query.message.chat_id
    logger.info(f'El usuario {user.first_name} {user.last_name} {id} indic??que no le fue ??til el art??culo.')

    query.edit_message_text(parse_mode='HTML', text='<b>??Qu?? ha fallado? (Opcional)</b>\n\n'
    '<i><b>Nota:</b> Dinos c??mo podemos mejorar. No respondemos a comentarios individuales. No dejes datos personales.</i>\n\n'
    'Por favor escr??benos tus comentarios o env??a /saltar si prefieres omitir este paso.')

    return ANSWERNOT

def suggestion2(update: Update, context: CallbackContext) -> int:

    user_name = update.effective_user['first_name']
    user_last = update.effective_user['last_name']
    user_id = update.effective_user['id']

    suggesting2 = update.message.text

    logger.info("La sugerencia que indica el usuario %s %s es: %s", user_name, user_last, suggesting2)
    update.message.reply_text(parse_mode="HTML",
        text=f"Gracias por tus comentarios.\n\n"
        '<b>Nota:</b> En este momento no podemos responder a comentarios individuales.',
        reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton(text='men?? principal', callback_data='inicio')]
        ])
        )

    context.bot.sendMessage(chat_id='1587610512', parse_mode="HTML", text=f"<b>El usuario {user_name} {user_last} ID: {user_id} ha indicado que no le ha sido ??til el art??culo, la sugerencia descrita por el usuario es:</b> {suggesting2}")

    return ConversationHandler.END

def saltar_suggesting(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    id = update.message.from_user.id
    logger.info("Usuario %s %s no envi?? sugerencia.", user.first_name, user.last_name)
    update.message.reply_text(parse_mode="HTML",
        text=f"Espero te haya sido ??til el art??culo, recuerda que para nosotros siempre es un placer atenderte.\n\n"
        '??El equipo de <b>Netflix Colombia</b>????????!',
        reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton(text='men?? principal', callback_data='inicio')]
        ])
        )

    return ConversationHandler.END

def plans_and_prices(update: Update, context:CallbackContext) -> int:

    query = update.callback_query
    query.answer()

    user =query.message.from_user
    id = query.message.chat_id
    logger.info(f'El usuario {user.first_name} {user.last_name} {id} ha ingresado al comando /ayuda y seleccionado el bot??n Planes y precios.')

    buttonWhatIsNetflix = InlineKeyboardButton(
        text='M??s informaci??n sobre Netflix',
        url='https://help.netflix.com/es-es/node/412'
    )

    query.edit_message_text(parse_mode='HTML', text='Viendo informaci??n en este momento exclus??vamente para <b>COLOMBIA</b>.\n\n'
    '<b>Planes y precios</b>\n\n'
    'Netflix ofrece varios planes para que elijas el m??s adecuado. El plan que elijas determinar?? la cantidad de dispositivos en los que puedes ver Netflix <b>al mismo tiempo</b>.\n\n'
    'Con todos nuestros planes, puedes descargar la aplicaci??n de Netflix en tus dispositivos favoritos y ver pel??culas y series ilimitadas.\n\n'
    )
    with open('img/preciosNetflixCol2021.jpg', 'rb') as PlansPrices:
     bot.sendChatAction(chat_id=id, action=ChatAction.UPLOAD_PHOTO, timeout=None)
     time.sleep(1)
     bot.sendPhoto(chat_id= id, photo= PlansPrices, caption='Planes y precios')
     bot.sendChatAction(chat_id= id, action=ChatAction.TYPING, timeout=None)
     time.sleep(1)
     bot.sendMessage(chat_id= id, parse_mode="HTML",text='Suscr??bete a Netflix Colombia hoy y selecciona entre varias opciones de pago. Como miembro de Netflix, se te cobrar?? una vez por mes en la fecha de suscripci??n. Tienes total libertad para cambiar de plan o cancelar el servicio online en cualquier momento.\n\n'
     '    ??????<b>Nota:</b> *Seg??n el lugar en el que vivas, <a href="https://help.netflix.com/es/node/50068" target="_self">es posible que se te cobren impuestos</a>, adem??s del precio de la suscripci??n.'
     )
     bot.sendChatAction(chat_id= id, action=ChatAction.TYPING, timeout=None)
     time.sleep(0.5)
    query.message.reply_text(
        parse_mode= "HTML", text=
        '??Te ha resultado ??til este art??culo?\n\n',
        reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton(text='S??', callback_data='answer_yes'),InlineKeyboardButton(text='No', callback_data='answer_not')],
        [buttonWhatIsNetflix],
        [InlineKeyboardButton(text='Atr??s', callback_data='help')],
        [InlineKeyboardButton(text='Men?? principal', callback_data='inicio')],
        ]),
    )

    return ConversationHandler.END

def i_cant_start(update: Update, context:CallbackContext) -> int:

    query = update.callback_query
    query.answer()

    user =query.message.from_user
    id = query.message.chat_id
    logger.info(f'El usuario {user.first_name}{user.last_name}({id}) ingres?? al comando /ayuda y seleccion?? el bot??n "No puedo iniciar sesi??n en Netflix".')


    query.edit_message_text(parse_mode='HTML', text='<b>No se puede iniciar sesi??n en Netflix</b>\n\n'
    'Si olvidaste tu email o contrase??a de inicio de sesi??n de Netflix, o no tienes acceso a estos datos, puedes <a href="https://www.netflix.com/loginhelp" target="_blank">restablecer la contrase??a.</a>\n\n'
    'Si conoces el email y la contrase??a de la cuenta de Netflix, pero no puedes iniciar sesi??n, sigue las instrucciones de la secci??n que corresponda a continuaci??n.\n\n'
    '<b>No es posible iniciar sesi??n en ning??n dispositivo</b>\n'
    'Aparece este error cuando intentas iniciar sesi??n con una cuenta existente:\n'
    )
    with open("img/can't_find_email.png", 'rb') as cant_find_email:
     bot.sendChatAction(chat_id=id, action=ChatAction.UPLOAD_PHOTO, timeout=None)
     time.sleep(1)
     bot.sendPhoto(chat_id= id, photo= cant_find_email, caption="")
     bot.sendChatAction(chat_id= id, action=ChatAction.TYPING, timeout=None)
     time.sleep(0.5)
    query.message.reply_text(
        parse_mode= "HTML", text=
        'Sigue estos pasos:\n\n'
        '<b>1.</b> Visita <a href="http://netflix.com/loginhelp" target="_blank">netflix.com/loginhelp</a>\n'
        '<b>2.</b> Selecciona <b>No me acuerdo de mi email ni de mi tel??fono</b> y completa el formulario.\n'
        '  ??????Sino ves esta opci??n, esto significa que la recuperaci??n de la cuenta mediante la informaci??n de facturaci??n no est?? disponible en tu pa??s.\n'
        '<b>3.</b> Selecciona <b>Encontrar cuenta</b>.\n\n'
        'Si te facturamos a trav??s de otra compa????a o tienes Netflix como parte de un paquete, busca el nombre del proveedor de servicios en el <a href="https://help.netflix.com/" target="_blank">Centro de ayuda</a> de Netflix. Selecciona el art??culo de facturaci??n relacionado y ve a la secci??n "Tengo problemas para iniciar sesi??n en Netflix".\n'
        '<b>4.</b> Si seguiste los pasos indicados m??s arriba y sigues sin poder iniciar sesi??n, comun??cate con el <b>Servicio al Cliente de Netflix</b> y habla con uno de nuestros asesores con el comando /asesor.\n\n\n'
        '<b>No se puede iniciar sesi??n en un dispositivo espec??fico</b>',
        reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton(text='Reproductor de Blue-ray', callback_data='blue_ray')],
        [InlineKeyboardButton(text='Computadoras', callback_data='laptops')],
        [InlineKeyboardButton(text='Tablet o tel??fono m??vil', callback_data='cellphone')],
        [InlineKeyboardButton(text='Reproductor multimedia o decodificador', callback_data='decoder')],
        [InlineKeyboardButton(text='Smart TV', callback_data='smarTV')],
        [InlineKeyboardButton(text='Consola de videojuegos', callback_data='videogame_console')],
        [InlineKeyboardButton(text='Todos los dem??s dispositivos', callback_data='another_devices')],
        [InlineKeyboardButton(text='Atr??s', callback_data='help')],
        [InlineKeyboardButton(text='Men?? principal', callback_data='inicio')],
        ]),
    )

    return ConversationHandler.END

def blue_ray(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    user = query.message.from_user
    id = query.message.from_user.id
    logger.info(f'El usuario {user.first_name}{user.last_name}({id}) seleccion?? el bot??n Blue-ray')

    buttonMoreInfo = InlineKeyboardButton(
        text='M??s informaci??n sobre Netflix',
        url='https://help.netflix.com/es-es/node/412'
    )

    query.edit_message_text(
        parse_mode= "HTML", text='Pasos para inicio de sesi??n en Reproductor de Blue-ray',
        reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton(text='Verificar el email y la contrase??a', callback_data='check_email')],
        [InlineKeyboardButton(text='Restablecer tu contrase??a', callback_data='restore_password')],
        [InlineKeyboardButton(text='iniciar sesi??n con netflix.com/tv8', callback_data='tv8')],
        [InlineKeyboardButton(text='Restablecer Netflix', callback_data='restore_netflix')],
        [InlineKeyboardButton(text='Reinicia tu dispositivo', callback_data='restart_device')],
        [InlineKeyboardButton(text='Reinicia la red dom??stica', callback_data='restart_network')],
        [InlineKeyboardButton(text='Mejora la calidad de tu se??al de wifi', callback_data='wifi_signal')],
        [InlineKeyboardButton(text='Conecta el reproductor de Blue-ray al m??dem', callback_data='blue_ray_to_modem')],
        [InlineKeyboardButton(text='Restablecer configuraci??n de conexi??n predeterminada', callback_data='restart_config_network')],
        [InlineKeyboardButton(text='Qu?? hacer a continuaci??n', callback_data='what_i_have_to_do')],
        [buttonMoreInfo],
        [InlineKeyboardButton(text='Atr??s', callback_data='i_cant_start')],
        [InlineKeyboardButton(text='Men?? principal', callback_data='inicio')],
        ]),
    )

    return ConversationHandler.END

def check_email(update:Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    user = query.message.from_user
    id = query.message.from_user.id
    logger.info(f'El usuario ha ingresado al comando /ayuda, seleccionado el not??n "No puedo iniciar sesi??n en Netflix", ingres?? al bot??n "Reproductor de Blue-ray" y luego al bot??n "Verificar email y la contrase??a"')

    query.edit_message_text(parse_mode='HTML', text='<b>Verificar el email y la contrase??a</b>\n\n'
    'Confirma que hayas ingresado el email y la contrase??a correctos antes de intentar iniciar sesi??n nuevamente. Si est??s usando el control remoto para iniciar sesi??n, puedes volver a la pantalla de ingreso de la direcci??n de email para verificar a actualizar esta informaci??n. Si a??n no puedes iniciar sesi??n, sigue el procedimiento de resoluci??n de problemas, comun??cate con el Servicio al <b>Cliente de Netflix Colombia.</b>',
    reply_markup=InlineKeyboardMarkup([ 
        [InlineKeyboardButton(text='Servicio al Cliente de Netflix Colombia', callback_data='customer_service')],
        [InlineKeyboardButton(text='Atr??s', callback_data='blue_ray')],
        [InlineKeyboardButton(text='Men?? principal', callback_data='inicio')]
    ])   
    )

def restore_password(update:Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    user = query.message.from_user
    id = query.message.from_user.id
    logger.info(f'El usuario ha ingresado al comando /ayuda, seleccionado el not??n "No puedo iniciar sesi??n en Netflix", ingres?? al bot??n "Reproductor de Blue-ray" y luego al bot??n "Restablecer contrase??a"')

    query.edit_message_text(parse_mode='HTML', text='<b>Restablecer la contrase??a</b>\n\n'
    'Para restablecer la contrase??a, <a href="https://www.netflix.com/LoginHelp" target="_blank">env??ate un email de restablecimiento de la contrase??a</a>. Si anteriormente agregaste un n??mero de tel??fono verificado a tu cuenta, tambi??n puedes restablecer la contrase??a por mensaje de texto (SMS) haciendo clic en <a href="https://www.netflix.com/LoginHelp" target="_blank">??Olvidaste tu contrase??a?</a> y seleccionando la opci??n de mensaje de texto (SMS). \n\n Si a??n no puedes iniciar sesi??n, sigue el procedimiento de resoluci??n de problemas, comun??cate con el Servicio al <b>Cliente de Netflix Colombia.</b>',
    reply_markup=InlineKeyboardMarkup([ 
        [InlineKeyboardButton(text='Servicio al Cliente de Netflix Colombia', callback_data='customer_service')],
        [InlineKeyboardButton(text='Atr??s', callback_data='blue_ray')],
        [InlineKeyboardButton(text='Men?? principal', callback_data='inicio')]
    ])   
    )

def tv8(update:Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    user = query.message.from_user
    id = query.message.from_user.id
    logger.info(f'El usuario ha ingresado al comando /ayuda, seleccionado el not??n "No puedo iniciar sesi??n en Netflix", ingres?? al bot??n "Reproductor de Blue-ray" y luego al bot??n "Iniciar sesi??n con netflix.com/tv8"')

    query.edit_message_text(parse_mode='HTML', text='<b>Iniciar sesi??n con netflix.com/tv8</b>\n\n'
    'Si seleccionaste la opci??n de <b>inicio de sesi??n desde la Web</b>, usar??s otro dispositivo para iniciar sesi??n y ver en tu TV en lugar del control remoto.\n\n'
    '  <b>1.</b> En tu computadora o dispositivo m??vil, ve a netflix.com/tv8.\n'
    '  <b>2.</b> Ingresa el c??digo que aparece en tu TV.\n'
    '    ??? Verifica que el c??digo que ingresaste coincida con el de tu TV en <b>Paso 2: Ingresar c??digo de inicio de sesi??n</b>.\n'
    '  <b>3.</b> Si se te solicita, ingresa tu email y contrase??a de Netflix.\n'
    '  <b>4.</b> Ver Netflix en tu TV.\n\n'
    '<b>C??mo usar el c??digo QR</b>.\n\n'
    '  <b>1.</b> Apunta la c??mara de tu tel??fono o tablet al c??digo QR de la pantalla de la TV.\n'
    '  <b>2.</b> Toca el banner que aparece para abrir netflix.com/tv8 en el navegador de tu m??vil.\n'
    '  <b>3.</b> En el navegador de tu m??vil, ingresa el c??digo que aparece en tu TV.\n'
    '    ??? Verifica que el c??digo que ingresaste coincida con el de tu TV en <b>Paso 2: Ingresar c??digo de inicio de sesi??n</b>.\n'
    '  <b>4.</b> Si se te solicita, ingresa tu email y contrase??a de Netflix.\n'
    '  <b>5.</b> Ver Netflix en tu TV.',
    reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton(text='Atr??s', callback_data='blue_ray')],
        [InlineKeyboardButton(text='Men?? principal', callback_data='inicio')]
    ])   
    )

def restore_netflix(update:Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    user = query.message.from_user
    id = query.message.from_user.id
    logger.info(f'El usuario ha ingresado al comando /ayuda, seleccionado el not??n "No puedo iniciar sesi??n en Netflix", ingres?? al bot??n "Reproductor de Blue-ray" y luego al bot??n "Restablecer Netflix"')

    query.edit_message_text(parse_mode='HTML', text='<b>Restablecer Netflix</b>\n\n'
    '  <b>1.</b> Ve a la pantalla de cierre de sesi??n:\n'
    '    ??? Si a??n est??s en la pantalla de error, selecciona <b>M??s informaci??n</b> o <b>M??s detalles</b>.\n'
    '    ??? En la pantalla de inicio de Netflix, selecciona <b>Configuraci??n</b> o el ??cono <b>Configuraci??n??????</b>.\n'
    '    ??? Si est??s en otra pantalla, ejecuta los siguientes comandos de '
    '    flecha en tu control remoto: <b>Arriba</b>, <b>Arriba</b>, <b>Abajo</b>, <b>Abajo</b>, <b>Izquierda</b>, <b>Derecha</b>, <b>Izquierda</b>, <b>Derecha</b>, <b>Arriba</b>, <b>Arriba</b>, <b>Arriba</b>, <b>Arriba</b>.\n'
    '  <b>2.</b> En la pantalla de cierre de sesi??n, selecciona <b>Restablecer</b>.\n'
    '    ??? Si no ves <b>Restablecer</b>, selecciona <b>Cerrar sesi??n</b> o <b>Desactivar</b>.\n'
    '  <b>3.</b> Una vez que cierres sesi??n, vuelve a iniciar sesi??n y prueba Netflix nuevamente.\n',
    reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton(text='Atr??s', callback_data='blue_ray')],
        [InlineKeyboardButton(text='Men?? principal', callback_data='inicio')]
    ])   
    )

def restart_device(update:Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    user = query.message.from_user
    id = query.message.from_user.id
    logger.info(f'El usuario ha ingresado al comando /ayuda, seleccionado el not??n "No puedo iniciar sesi??n en Netflix", ingres?? al bot??n "Reproductor de Blue-ray" y luego al bot??n "Reinicia tu dispositivo"')

    query.edit_message_text(parse_mode='HTML', text='<b>Reinicia tu dispositivo</b>\n\n'
    '  <b>1.</b> Desconecta el dispositivo de la alimentaci??n durante al menos 1 minuto.\n'
    '  <b>2.</b> Con el dispositivo desconectado, presiona el bot??n de encendido del dispositivo para descargarlo.\n'
    '    ??? Si no puedes acceder al bot??n de encendido o tu dispositivo no tiene uno, deja el dispositivo desconectado durante al menos 3 minutos.\n'
    '  <b>3.</b> Vuelve a conectar tu dispositivo.\n'
    '  <b>4.</b> Enciende el dispositivo.\n\n'
    '  <b>5.</b> Vuelve a probar Netflix.',
    reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton(text='Atr??s', callback_data='blue_ray')],
        [InlineKeyboardButton(text='Men?? principal', callback_data='inicio')]
    ])
    )

def restart_network(update: Update, context:CallbackContext) -> int:

    query = update.callback_query
    query.answer()

    user =query.message.from_user
    id = query.message.chat_id
    logger.info(f'El usuario {user.first_name}{user.last_name}({id}) ha ingresado al comando /ayuda, seleccionado el not??n "No puedo iniciar sesi??n en Netflix", ingres?? al bot??n "Reproductor de Blue-ray" y luego al bot??n "Reinicia la red dom??stica".')


    query.edit_message_text(parse_mode='HTML', text='<b>Reinicia la red dom??stica</b>\n\n'
    )
    with open("img/blue-ray1.png", 'rb') as blue_ray_1:
     bot.sendChatAction(chat_id=id, action=ChatAction.UPLOAD_PHOTO, timeout=None)
     time.sleep(1)
     bot.sendPhoto(chat_id= id, photo= blue_ray_1, caption="1. Apaga o desconecta el reproductor de Blu-ray.")
    with open("img/unpplugin-modem.png", 'rb') as modem:
     bot.sendChatAction(chat_id=id, action=ChatAction.UPLOAD_PHOTO, timeout=None)
     time.sleep(1)
     bot.sendPhoto(chat_id= id, photo= modem, caption="2. Desconecta el m??dem (y el enrutador inal??mbrico, si se trata de un dispositivo independiente) de la alimentaci??n el??ctrica durante al menos 30 segundos.")
    with open("img/connect-modem.png", 'rb') as connect:
     bot.sendChatAction(chat_id=id, action=ChatAction.UPLOAD_PHOTO, timeout=None)
     time.sleep(1)
     bot.sendPhoto(chat_id= id, photo= connect, caption="3. Conecta el m??dem y espera hasta que todas las luces indicadoras est??n encendidas y hayan dejado de parpadear. Si el enrutador es independiente del m??dem, con??ctalo y espera hasta que todas las luces indicadoras hayan dejado de parpadear.")
    with open("img/turn-on.png", 'rb') as turn:
     bot.sendChatAction(chat_id=id, action=ChatAction.UPLOAD_PHOTO, timeout=None)
     time.sleep(1)
     bot.sendPhoto(chat_id= id, photo= turn, caption="4. Vuelve a encender el reproductor de Blu-ray.")
     bot.sendChatAction(chat_id= id, action=ChatAction.TYPING, timeout=None)
     time.sleep(0.5)
    query.message.reply_text(
        parse_mode= "HTML", text=
        '  <b>5.</b> Prueba Netflix nuevamente.\n',
        reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton(text='Atr??s', callback_data='blue_ray')],
        [InlineKeyboardButton(text='Men?? principal', callback_data='inicio')],
        ]),
    )

    return ConversationHandler.END

def signal_wifi(update:Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    user = query.message.from_user
    id = query.message.from_user.id
    logger.info(f'El usuario {user.first_name} {user.last_name}, ha ingresado al comando /ayuda, seleccionado el not??n "No puedo iniciar sesi??n en Netflix", ingres?? al bot??n "Reproductor de Blue-ray" y luego al bot??n "Mejora la calidad de tu se??al de wifi"')

    query.edit_message_text(parse_mode='HTML', text='<b>Mejora la calidad de tu se??al de wifi</b>\n\n'
    'Si est??s conect??ndote a trav??s de una red wifi, y los pasos anteriores no resuelven el problema, sigue estas sugerencias:\n\n'
    '    ?????? Si no puedes acceder al bot??n de encendido o tu dispositivo no tiene uno, deja el dispositivo desconectado durante al menos 3 minutos.\n'
    '  <b>3.</b> Vuelve a conectar tu dispositivo.\n'
    '  <b>4.</b> Enciende el dispositivo.\n\n'
    '  <b>5.</b> Vuelve a probar Netflix.',
    reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton(text='Atr??s', callback_data='blue_ray')],
        [InlineKeyboardButton(text='Men?? principal', callback_data='inicio')]
    ])
    )

def how_to_start(update:Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    user = query.message.from_user
    id = query.message.from_user.id
    logger.info(f'El usuario ha ingresado al comando /ayuda y seleccionado el bot??n "C??mo comenzar".')

    query.edit_message_text(parse_mode='HTML', text='<b>C??mo comenzar</b>\n\n'
    '?????? <a href="https://help.netflix.com/es-es/node/412?ui_action=kb-article-popular-categories" target="_self">??Qu?? es Netflix?</a>\n\n'
    '?????? <a href="https://help.netflix.com/es-es/node/116380?ui_action=kb-article-popular-categories" target="_self">??C??mo pagar Netflix?</a>\n\n'
    '?????? <a href="https://help.netflix.com/es-es/node/101653?ui_action=kb-article-popular-categories" target="_self">??C??mo descargar la aplicaci??n de Netflix?</a>\n\n',
    reply_markup=InlineKeyboardMarkup([ 
        [InlineKeyboardButton(text='Atr??s', callback_data='help')],
        [InlineKeyboardButton(text='Men?? principal', callback_data='inicio')]
    ])   
    )

def it_cant_be_see(update:Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    user = query.message.from_user
    id = query.message.from_user.id
    logger.info(f'El usuario ha ingresado al comando /ayuda y seleccionado el bot??n "No se puede ver".')

    query.edit_message_text(parse_mode='HTML', text='<b>No se puede ver</b>\n\n'
    '?????? <a href="https://help.netflix.com/es-es/node/365?ui_action=kb-article-popular-categories" target="_self">??C??mo cambiar tu contrase??a de Netflix?</a>\n\n'
    '?????? <a href="https://help.netflix.com/es-es/node/12983?ui_action=kb-article-popular-categories" target="_self">No encuentro la aplicaci??n de Netflix de las tiendas de aplicaciones</a>\n\n'
    '?????? <a href="https://help.netflix.com/es-es/node/57688?ui_action=kb-article-popular-categories" target="_self">Netflix muestra el mensaje: ??Esta aplicaci??n no es compatible con tu dispositivo??.</a>\n\n',
    reply_markup=InlineKeyboardMarkup([ 
        [InlineKeyboardButton(text='Atr??s', callback_data='help')],
        [InlineKeyboardButton(text='Men?? principal', callback_data='inicio')]
    ])   
    )

def manage_account(update:Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    user = query.message.from_user
    id = query.message.from_user.id
    logger.info(f'El usuario ha ingresado al comando /ayuda y seleccionado el bot??n "Gestionar cuenta".')

    query.edit_message_text(parse_mode='HTML', text='<b>Gestionar mi cuenta</b>\n\n'
    '?????? Consulta toda la informaci??n acerca de los <b><u>planes y precios</u></b> con el comando /planes\n\n'
    '?????? <a href="https://help.netflix.com/es-es/node/41049?ui_action=kb-article-popular-categories" target="_self">Facturaci??n y pagos</a>\n\n'
    '?????? <a href="https://help.netflix.com/es-es/node/111934?ui_action=kb-article-popular-categories" target="_self">Se ha cambiado mi direcci??n de correo electr??nico sin mi permiso</a>\n\n',
    reply_markup=InlineKeyboardMarkup([ 
        [InlineKeyboardButton(text='Atr??s', callback_data='help')],
        [InlineKeyboardButton(text='Men?? principal', callback_data='inicio')]
    ])   
    )

def watch_netflix(update:Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    user = query.message.from_user
    id = query.message.from_user.id
    logger.info(f'El usuario ha ingresado al comando /ayuda y seleccionado el bot??n "Ver Netflix".')

    query.edit_message_text(parse_mode='HTML', text='<b>Ver Netflix</b>\n\n'
    '?????? <a href="https://help.netflix.com/es-es/node/54816?ui_action=kb-article-popular-categories" target="_self">??C??mo descargar series y pel??culas para verlas sin conexi??n?</a>\n\n'
    '?????? <a href="https://help.netflix.com/es-es/node/33222?ui_action=kb-article-popular-categories" target="_self">??C??mo ver Netflix en tu televisor?</a>\n\n'
    '?????? <a href="https://help.netflix.com/es-es/node/49?ui_action=kb-article-popular-categories" target="_self">??C??mo usar dispositivos m??viles para ver Netflix en televisores?</a>\n\n',
    reply_markup=InlineKeyboardMarkup([ 
        [InlineKeyboardButton(text='Atr??s', callback_data='help')],
        [InlineKeyboardButton(text='Men?? principal', callback_data='inicio')]
    ])   
    )

def quick_links(update:Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    user = query.message.from_user
    id = query.message.from_user.id
    logger.info(f'El usuario ha ingresado al comando /ayuda y seleccionado el bot??n "Enlaces r??pidos".')

    query.edit_message_text(parse_mode='HTML', text='<b>Enlaces r??pidos</b>\n\n'
    '?????? <a href="https://www.netflix.com/password" target="_self">Restablecer contrase??a??</a>\n\n'
    '?????? <a href="https://www.netflix.com/email" target="_self">Actualizar correo??</a>\n\n'
    '?????? <a href="https://www.netflix.com/co/loginhelp" target="_self">Obtener ayuda para iniciar sesi??n??</a>\n\n'
    '?????? <a href="https://www.netflix.com/YourAccountPayment" target="_self">Actualizar m??todo de pago??</a>\n\n'
    '?????? <a href="https://help.netflix.com/es-es/titlerequest?ui_action=title-suggestion-quicklinks" target="_self">Solicitar series o pel??culas??</a>\n\n',
    reply_markup=InlineKeyboardMarkup([ 
        [InlineKeyboardButton(text='Atr??s', callback_data='help')],
        [InlineKeyboardButton(text='Men?? principal', callback_data='inicio')]
    ])   
    )

def suggested_articles(update:Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    user = query.message.from_user
    id = query.message.from_user.id
    logger.info(f'El usuario ha ingresado al comando /ayuda y seleccionado el bot??n "Art??culos sugeridos".')

    query.edit_message_text(parse_mode='HTML', text='<b>Art??culos sugeridos</b>\n\n'
    '?????? <a href="https://help.netflix.com/es-es/node/102377" target="_self">Primeros pasos con Netflix</a>\n\n'
    '?????? <a href="https://help.netflix.com/es-es/node/10421" target="_self">C??mo crear y editar perfiles</a>\n\n'
    '?????? <a href="https://help.netflix.com/es-es/node/54816" target="_self">C??mo descargar series y pel??culas para verlas sin conexi??n</a>\n\n'
    '?????? <a href="https://help.netflix.com/es-es/node/32950" target="_self">Tarjetas de regalo de Netflix</a>\n\n'
    '?????? <a href="https://help.netflix.com/es-es/node/13243" target="_self">C??mo proteger tu cuenta</a>\n\n'
    '?????? <a href="https://help.netflix.com/es-es/node/25970" target="_self">C??mo configurar tu n??mero de tel??fono para recuperar tu contrase??a</a>\n\n'
    '?????? <a href="https://help.netflix.com/es-es/node/13245" target="_self">C??mo cambiar el idioma en Netflix</a>\n\n'
    '?????? <a href="https://help.netflix.com/es-es/node/22205" target="_self">C??mo ocultar t??tulos del historial de visionado</a>\n\n'
    '?????? Busca m??s art??culos en nuestro <a href="https://help.netflix.com/es-es" target="_self">Centro de ayuda</a>\n\n',
    reply_markup=InlineKeyboardMarkup([ 
        [InlineKeyboardButton(text='Atr??s', callback_data='help')],
        [InlineKeyboardButton(text='Men?? principal', callback_data='inicio')]
    ])
    )

def sol_series(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()

    user = query.message.from_user
    logger.info(f'El usuario {user.first_name} {user.last_name}, ha escogido solicita series o pel??culas.')
    id = query.message.chat_id

    query.edit_message_text(
        parse_mode="HTML", text='<b>Solicita series o pel??culas</b>\n\n'
        '??Hay alguna serie o pel??cula que te gustar??a ver en Netflix? <a href="https://help.netflix.com/es/titlerequest" target="_self">D??noslo a continuaci??n</a>.\n\n'
        '??Te preguntas por qu?? un t??tulo ya no est?? disponible? Visita <a href="https://help.netflix.com/es/node/60541?ui_action=expired-content-link" target="_self">??Por qu?? algunas series y pel??culas desaparecen de Netflix?</a>.\n\n'
        'Si buscas ayuda para encontrar un t??tulo, visita <a href="https://help.netflix.com/es/node/47765" target="_self">??C??mo encuentro pel??culas y series en Netflix?</a>.'
    )
    
    bot.sendChatAction(chat_id=id, action=ChatAction.TYPING, timeout=None)
    time.sleep(1)
    query.message.reply_text(parse_mode="HTML", text="<b>??Qu?? sucede si ya solicit?? una serie o pel??cula?</b>\n\n"
    "Si ya enviaste una solicitud, puedes relajarte: hemos recibido tu comentario.")
    bot.sendChatAction(chat_id=id, action=ChatAction.TYPING, timeout=None)
    time.sleep(1)
    query.message.reply_text(parse_mode="HTML", text='No podemos responder solicitudes individuales, pero puedes mantenerte al d??a acerca de los nuevos t??tulos que llegan a Netflix '
    '<a href="https://help.netflix.com/es/node/14422/CO" target="_self">sigui??ndonos</a> en las redes sociales y <a href="https://help.netflix.com/es/node/25" target="_self">suscribi??ndote</a> a nuestros emails "Ahora en Netflix".')
    bot.sendChatAction(chat_id=id, action=ChatAction.TYPING, timeout=None)
    time.sleep(1)
    query.message.reply_text("/start para regresar al men?? principal.")
    with open('stickers/besopatito.tgs','rb') as sticker_file:
     bot.sendChatAction(chat_id=id, action=ChatAction.TYPING, timeout=None)
     time.sleep(0.5)
     bot.sendSticker(chat_id=id, sticker=sticker_file) 

    return ConversationHandler.END

def customer_service(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()

    user = query.message.from_user
    logger.info(f'El usuario {user.first_name} {user.last_name}, ha escogido el comando /asesor')
    id = query.message.chat_id
    
    buttonrestContra = InlineKeyboardButton(
        text='Necesito restablecer mi contrase??a',
        url='https://www.netflix.com/co/LoginHelp'
    )

    buttonPayment = InlineKeyboardButton(
        text='Necesito actualizar mi forma de pago',
        url='https://www.netflix.com/co/YourAccountPayment'
    )

    bot.sendChatAction(chat_id=id, action=ChatAction.TYPING, timeout=None)
    time.sleep(1)
    query.edit_message_text(parse_mode="HTML", text= f"??Hola <b>{user.first_name}</b>! Espero te encuentres muy bien, Antes de chatear...\n\n"
     "Puedes resolver r??pidamente algunos problemas habituales sin necesidad de recibir ayuda en directo:")
    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
    time.sleep(1)
    query.message.reply_text(
        'Escoge una opci??n\n\n',
        reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton(text='No encuentro una serie o pel??cula en Netflix', callback_data='opcion1')],
        [buttonrestContra],
        [buttonPayment],  
        [InlineKeyboardButton(text='??Quiero hablar con un asesor!', callback_data='opcion4')]
        ]),
    )

def chat_directo(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()

    user = query.message.from_user
    logger.info(f'El usuario {user.first_name} {user.last_name}, ha escogido la funci??n chat directo.')
    id = query.message.chat_id

    query.edit_message_text(
        parse_mode="HTML", text='<b>Describe tu problema</b>\n\n'
        '??C??mo podemos ayudarte el d??a de hoy?\n\n'
        'Por favor describe el inconveniente que est??s presentando y uno de nuestros asesores se comunicar?? contigo lo m??s pronto posible.\n\n'
    )

    return CONVERSATION

def conversation(update, context):

    user_name = update.effective_user['first_name']
    user_last = update.effective_user['last_name']
    user_id = update.effective_user['id']

    inconveniente = update.message.text

    logger.info("El inconveniente que presenta el usuario %s %s es: %s", user_name, user_last, inconveniente)
    update.message.reply_text(
        text=f"Muchas gracias, hemos registrado tu respuesta satisfactoriamente, en breve uno de nuestros asesores se pondr?? en contacto contigo.\n\n")
    update.message.reply_text(parse_mode="HTML", text="<b>??Qu?? pasa si ya he solicitado hablar con un asesor?</b>\n\n"
    "Si ya enviaste una solicitud, puedes relajarte, hemos recibido tu mensaje, tiempo de espera: 5 a 15 minutos.")
    update.message.reply_text(parse_mode="HTML", text='??Quieres recibir una respuesta inmediata? '
    '<a href="https://t.me/netflixcolombiaoficial" target="_self">chatea con nosotros</a>')
    update.message.reply_text("/start para regresar al men?? principal.")

    context.bot.sendMessage(chat_id='YOUR_TELEGRAM_CHAT_ID', parse_mode="HTML", text=f"<b>El usuario {user_name} {user_last} ID: {user_id} ha solicitado hablar con un asesor, el problema descrito por el usuario es:</b> {inconveniente}")

    return ConversationHandler.END


def cancel(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    id = update.message.from_user.id
    logger.info("El usuario %s %s cancel?? la conversaci??n.", user.first_name, user.last_name)
    context.bot.sendMessage(chat_id=id, parse_mode="HTML", text=
        'Espero sinceramente haber sido de ayuda el d??a de hoy y que la informaci??n brindada contestara tu consulta/problema. ' 
        'Por mi parte me despido que tengas un excelente d??a. ??Tus amigos de <b>Netflix Colombia</b>????????!', reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END


# def get_weather(api_key, city):
    
#     url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

#     response = requests.get(url).json()
    
#     temp = response['main']['temp']
#     tempC = temp - 273.15

#     humidity = response['main']['humidity']

#     country = response['sys']['country']
#     lugar = response['name']

#     return TEMP

# def temperatura(update: Update, context: CallbackContext) -> int:
    
#     update.message.reply_text(f"{lugar}, {country}\n\n" 
#     "Temperatura: {0:.2f}".format(tempC), "??C\n"
#     f"Humedad: {humidity}%")

def main() -> None:
    # Create the Updater and pass it your bot's token.
    updater = Updater(token=TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Add conversation handler with the states GENDER, PHOTO, LOCATION and BIO
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start),
            CommandHandler('recomendaciones', recomendaciones),
            CommandHandler('planes', planes),
            CommandHandler('micuenta', micuenta),
            CommandHandler('promociones', promociones),
            CommandHandler('preguntas', preguntas),
            CommandHandler('asesor', asesor),
            CommandHandler('about', about),
            CommandHandler('ayuda', ayuda),
            MessageHandler(Filters.text & ~Filters.command, prueba.despedida),
            CallbackQueryHandler(pattern='pel??culas', callback=peliculas_call_handler),
            CallbackQueryHandler(pattern='series', callback=series_call_handler),
            CallbackQueryHandler(pattern='b??sico', callback=plan_basico),
            CallbackQueryHandler(pattern='est??ndar', callback=plan_estandar),
            CallbackQueryHandler(pattern='premium', callback=plan_premium),
            CallbackQueryHandler(pattern='dani_ace', callback=dani_acevedo),
            CallbackQueryHandler(pattern='mariai_giraldo', callback=mariai_giraldo),
            CallbackQueryHandler(pattern='juan_gu', callback=juan_gu),
            CallbackQueryHandler(pattern='sophi_jara', callback=sophi_jara),
            CallbackQueryHandler(pattern='cindy_berrio', callback=cindy_berrio),
            CallbackQueryHandler(pattern='geral_durango', callback=geral_durango),
            CallbackQueryHandler(pattern='estefa_sierra', callback=estefa_sierra),         
            CallbackQueryHandler(pattern='kate_hernandez', callback=kate_hernandez),
            CallbackQueryHandler(pattern='keli_suarez', callback=keli_suarez),
            CallbackQueryHandler(pattern='stiven_duque', callback=stiven_duque),
            CallbackQueryHandler(pattern='fabian_duque', callback=fabian_duque),
            CallbackQueryHandler(pattern='horacio_alzate', callback=horacio_alzate),
            CallbackQueryHandler(pattern='elkin_carmona', callback=elkin_carmona),
            CallbackQueryHandler(pattern='kate_betancur', callback=kate_betancur),
            CallbackQueryHandler(pattern='viviana_toro', callback=viviana_toro),
            CallbackQueryHandler(pattern='cami_sanchez', callback=cami_sanchez),
            CallbackQueryHandler(pattern='diana_sanchez', callback=diana_sanchez),
            CallbackQueryHandler(pattern='joan_angarita', callback=joan_angarita),
            CallbackQueryHandler(pattern='brarlynn_mu??oz', callback=brarlynn_mu??oz),
            CallbackQueryHandler(pattern='karen_fonseca', callback=karen_fonseca),
            CallbackQueryHandler(pattern='david_chavarriaga', callback=david_chavarriaga),
            CallbackQueryHandler(pattern='clau_jimenez', callback=clau_jimenez),
            CallbackQueryHandler(pattern='yimar', callback=yimar),
            CallbackQueryHandler(pattern='claudia_lopez', callback=claudia_lopez),
            CallbackQueryHandler(pattern='diana_jimenez', callback=diana_jimenez),
            CallbackQueryHandler(pattern='manuela_montoya', callback=manuela_montoya),
            CallbackQueryHandler(pattern='mauro_pati??o', callback=mauro_patino),
            CallbackQueryHandler(pattern='henry_mosquera', callback=henry_mosquera),
            CallbackQueryHandler(pattern='how_to_suscribe', callback=how_to_suscribe),
            CallbackQueryHandler(pattern='plans_and_prices', callback=plans_and_prices),
            CallbackQueryHandler(pattern='i_cant_start', callback=i_cant_start),
            CallbackQueryHandler(pattern='how_to_start', callback=how_to_start),
            CallbackQueryHandler(pattern='it_cant_be_see', callback=it_cant_be_see),
            CallbackQueryHandler(pattern='manage_account', callback=manage_account),
            CallbackQueryHandler(pattern='watch_netflix', callback=watch_netflix),
            CallbackQueryHandler(pattern='quick_links', callback=quick_links),
            CallbackQueryHandler(pattern='suggested_articles', callback=suggested_articles),
            CallbackQueryHandler(pattern='android', callback=android),
            CallbackQueryHandler(pattern='ordenador', callback=ordenador),
            CallbackQueryHandler(pattern='iphone', callback=iphone),
            CallbackQueryHandler(pattern='smartTV', callback=smartTV),
            CallbackQueryHandler(pattern='decodificador', callback=decodificador),
            CallbackQueryHandler(pattern='blue_ray', callback=blue_ray),
            CallbackQueryHandler(pattern='check_email', callback=check_email),
            CallbackQueryHandler(pattern='restore_password', callback=restore_password),
            CallbackQueryHandler(pattern='tv8', callback=tv8),
            CallbackQueryHandler(pattern='restore_netflix', callback=restore_netflix),
            CallbackQueryHandler(pattern='restart_device', callback=restart_device),
            CallbackQueryHandler(pattern='restart_network', callback=restart_network),
            CallbackQueryHandler(pattern='customer_service', callback=customer_service),
            CallbackQueryHandler(pattern='answer_yes', callback=answer_yes),
            CallbackQueryHandler(pattern='answer_not', callback=answer_not),
            CallbackQueryHandler(pattern='opcion1', callback=sol_series),
            CallbackQueryHandler(pattern='opcion4', callback=chat_directo),
            #CallbackQueryHandler(pattern='comenzar', callback=comenzar),
            CallbackQueryHandler(pattern='help', callback=help),
            CallbackQueryHandler(pattern='inicio', callback=inicio)
            #CallbackQueryHandler(dispatcher='correo', callback=correo)
        ],
        states ={
            MICUENTA: [MessageHandler(Filters.text & ~Filters.command, micuenta)],
            CORREO: [MessageHandler(Filters.text & ~Filters.command, correo), CommandHandler('saltar', saltar_correo)],
            PIN_JUANGUT: [MessageHandler(Filters.text & ~Filters.command, pin_juang), CommandHandler('saltar', saltar_pin)],
            PIN_DANIACEVEDO: [MessageHandler(Filters.text & ~Filters.command, pin_daniace), CommandHandler('saltar', saltar_pin)],
            PIN_MARIAIG: [MessageHandler(Filters.text & ~Filters.command, pin_mariaig), CommandHandler('saltar', saltar_pin)],
            PIN_SOPHI: [MessageHandler(Filters.text & ~Filters.command, pin_sophi), CommandHandler('saltar', saltar_pin)],
            PIN_CINDYB: [MessageHandler(Filters.text & ~Filters.command, pin_cindyb), CommandHandler('saltar', saltar_pin)],
            PIN_GERALD: [MessageHandler(Filters.text & ~Filters.command, pin_gerald), CommandHandler('saltar', saltar_pin)],
            PIN_ESTEFASIERRA: [MessageHandler(Filters.text & ~Filters.command, pin_estefasierra), CommandHandler('saltar', saltar_pin)],
            PIN_KATEHDZ: [MessageHandler(Filters.text & ~Filters.command, pin_katehdz), CommandHandler('saltar', saltar_pin)],
            PIN_KELISUAREZ: [MessageHandler(Filters.text & ~Filters.command, pin_kelisuarez), CommandHandler('saltar', saltar_pin)],
            PIN_STIVEND: [MessageHandler(Filters.text & ~Filters.command, pin_stivend), CommandHandler('saltar', saltar_pin)],
            PIN_FABIAND: [MessageHandler(Filters.text & ~Filters.command, pin_fabiand), CommandHandler('saltar', saltar_pin)],
            PIN_HORACIOA: [MessageHandler(Filters.text & ~Filters.command, pin_horacioa), CommandHandler('saltar', saltar_pin)],
            PIN_ELKINCAR: [MessageHandler(Filters.text & ~Filters.command, pin_elkinc), CommandHandler('saltar', saltar_pin)],
            PIN_KTBETANCUR: [MessageHandler(Filters.text & ~Filters.command, pin_ktbetancur), CommandHandler('saltar', saltar_pin)],
            PIN_VIVITORO: [MessageHandler(Filters.text & ~Filters.command, pin_vivitoro), CommandHandler('saltar', saltar_pin)],
            PIN_CAMISANCHEZ: [MessageHandler(Filters.text & ~Filters.command, pin_camisanchez), CommandHandler('saltar', saltar_pin)],
            PIN_DIANASAN: [MessageHandler(Filters.text & ~Filters.command, pin_dianasanchez), CommandHandler('saltar', saltar_pin)],
            PIN_JOANANGA: [MessageHandler(Filters.text & ~Filters.command, pin_joanangarita), CommandHandler('saltar', saltar_pin)],
            PIN_BRARLYNNM: [MessageHandler(Filters.text & ~Filters.command, pin_brarlynnm), CommandHandler('saltar', saltar_pin)],
            PIN_KARENF: [MessageHandler(Filters.text & ~Filters.command, pin_karenf), CommandHandler('saltar', saltar_pin)],
            PIN_DAVIDCHA: [MessageHandler(Filters.text & ~Filters.command, pin_davidcha), CommandHandler('saltar', saltar_pin)],
            PIN_CLAUJIMENEZ: [MessageHandler(Filters.text & ~Filters.command, pin_claujimenez), CommandHandler('saltar', saltar_pin)],
            PIN_YIMAR: [MessageHandler(Filters.text & ~Filters.command, pin_yimar), CommandHandler('saltar', saltar_pin)],
            PIN_CLAULOPEZ: [MessageHandler(Filters.text & ~Filters.command, pin_claulopez), CommandHandler('saltar', saltar_pin)],
            PIN_DIANAJIMENEZ: [MessageHandler(Filters.text & ~Filters.command, pin_dianajimenez), CommandHandler('saltar', saltar_pin)],
            PIN_MANUELAMON: [MessageHandler(Filters.text & ~Filters.command, pin_manuelamon), CommandHandler('saltar', saltar_pin)],
            PIN_MAUROPATINO: [MessageHandler(Filters.text & ~Filters.command, pin_mauropatino), CommandHandler('saltar', saltar_pin)],
            PIN_HENRYMOSQUERA: [MessageHandler(Filters.text & ~Filters.command, pin_henrymosquera), CommandHandler('saltar', saltar_pin)],
            CONVERSATION: [MessageHandler(Filters.text & ~Filters.command, conversation)],
            ANSWERYES: [MessageHandler(Filters.text & ~Filters.command, suggestion), CommandHandler('saltar', saltar_suggesting)],
            ANSWERNOT: [MessageHandler(Filters.text & ~Filters.command, suggestion2), CommandHandler('saltar', saltar_suggesting)]
            #LOCATION: [
            #     MessageHandler(Filters.location, planes),
            #     CommandHandler('skip', skip_location),
            # ],
            # BIO: [MessageHandler(Filters.text & ~Filters.command, bio)],
            #DESPEDIDA: [dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, prueba.despedida))],
            #START: [CommandHandler('start', start), CommandHandler('skip', start )],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    updater.dispatcher.add_handler(CommandHandler("pago", pago))
    updater.dispatcher.add_handler(CommandHandler('cancel', cancel))
    #dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, chatear))
    #dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, prueba.despedida))
    #dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, prueba.despedida))
    #dispatcher.add_handler(MessageHandler(Filters.text, correo))
    

    dispatcher.add_handler(conv_handler)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()


