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
    logger.info(f'El usuario {user.first_name} {user.last_name}, ha iniciado una conversación.')
    id = update.message.chat_id
    context.bot.sendMessage(chat_id= id, parse_mode= "HTML",
        text= f' ¡Hola {user.first_name}👋 Soy <b>Luan</b>!👶🏻, agente virtual de <b>Netflix Colombia</b>. Para mí es un placer atenderte.\n'
        'Estoy aquí para ayudarte con las <u>consultas básicas</u> de tus servicios.\n'
        'Puedes hacerme preguntas con frases cortas utilizando <u>estos comandos</u>:\n\n'
        '/start - Inicia la conversación\n'
        '/micuenta - Información de mi cuenta\n'
        '/planes - ¡Quiero adquirir una cuenta!\n'
        '/ayuda - Centro de ayuda\n'
        '/pago - Detalles de pago\n'
        '/recomendaciones - Te recomiendo series y películas\n'
        '/promociones - Promociones vigentes\n'
        '/preguntas - Preguntas frecuentes\n'
        '/asesor - ¡Quiero hablar con un asesor!\n'
        '/about - Acerca de <b>Netflix Colombia</b>\n'
        '/cancel - Finaliza la conversación\n',
    )

    return ConversationHandler.END

def inicio(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    user = query.message.from_user
    logger.info(f'El usuario {user.first_name} {user.last_name}, ha iniciado una conversación.')
    id = query.message.chat_id
    query.edit_message_text(parse_mode= "HTML",
        text= f' ¡Hola {user.first_name}👋 Soy <b>Luan</b>!👶🏻, agente virtual de <b>Netflix Colombia</b>. Para mí es un placer atenderte.\n'
        'Estoy aquí para ayudarte con las <u>consultas básicas</u> de tus servicios.\n'
        'Puedes hacerme preguntas con frases cortas utilizando <u>estos comandos</u>:\n\n'
        '/start - Inicia la conversación\n'
        '/micuenta - Información de mi cuenta\n'
        '/planes - ¡Quiero adquirir una cuenta!\n'
        '/ayuda - Centro de ayuda\n'
        '/pago - Detalles de pago\n'
        '/recomendaciones - Te recomiendo series y películas\n'
        '/promociones - Promociones vigentes\n'
        '/preguntas - Preguntas frecuentes\n'
        '/asesor - ¡Quiero hablar con un asesor!\n'
        '/about - Acerca de <b>Netflix Colombia</b>\n'
        '/cancel - Finaliza la conversación\n',
    )

    return ConversationHandler.END


def pago(update: Update, context: CallbackContext) -> int:

    user = update.message.from_user
    logger.info(f'El usuario {user.first_name} {user.last_name}, ha solicitado la información de pago.')
    id = update.message.chat_id
    bot.sendChatAction(chat_id=id, action=ChatAction.TYPING, timeout=None)
    time.sleep(1)
    context.bot.sendMessage(chat_id=id, parse_mode="HTML",
        text=f'Hola {user.first_name}, te comparto la información de pago habilitada:\n\n'
        '<b>Netflix Colombia Soluciones</b>\n'
        'Cuenta de ahorros Bancolombia: <a href="https://sucursalpersonas.transaccionesbancolombia.com/" target="_blank">YOUR_PAYMENT_INFORMATION</a>\n'
        'Cuenta de ahorros Nequi o Daviplata: <a href="https://transacciones.nequi.com/" target="_self">YOUR_TELEPHONE_NUMBER</a>\n\n'
    )
    bot.sendChatAction(chat_id=id, action=ChatAction.TYPING, timeout=None)
    time.sleep(1)
    context.bot.sendMessage(chat_id= id, parse_mode= "HTML", text='Recuerde que el pago puede realizarlo de manera física desde un corresponsal bancario correspondiente, '
    'desde la Sucursal Virtual o App personas.\n\n'
    'Puedes enviar tu comprobante de pago una vez realizado el mismo <a href="https://t.me/netflixcolombiaoficial" target="_self">aquí</a>. ¡Saludos!'
    )
    bot.sendChatAction(chat_id=id, action=ChatAction.TYPING, timeout=None)
    time.sleep(1)
    update.message.reply_text('/start para regresar al menú principal.',
        reply_markup=ReplyKeyboardRemove(),
    
    )
    #return START

def planes(update: Update, context: CallbackContext) -> int:

    user = update.message.from_user
    id = update.message.chat_id
    logger.info(f'El usuario {user.first_name} {user.last_name}({id}), ha ingresado el comando /planes.')
    bot.sendChatAction(chat_id=id, action=ChatAction.TYPING, timeout=None)
    update.message.reply_text(
        '¿En cuál plan estás interesado(a)?\n\n',
        reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton(text='Plan Básico', callback_data='básico')],
        [InlineKeyboardButton(text='Plan Estándar', callback_data='estándar')],
        [InlineKeyboardButton(text='Plan Premium', callback_data='premium')]
        ])
    )

def recomendaciones(update: Update, context: CallbackContext):
    user = update.message.from_user
    logger.info(f'El usuario {user.first_name} {user.last_name}, ha ingresado al comando /recomendaciones.')
    id = update.message.chat_id
    bot.sendChatAction(chat_id=id, action=ChatAction.TYPING, timeout=None)
    update.message.reply_text("¿Qué quieres que te recomiende?\n\n",
        reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton(text='Películas', callback_data='películas')],
        [InlineKeyboardButton(text='Series', callback_data='series')]
    ])
    )

def peliculas_call_handler(update, context):
    
    query = update.callback_query
    query.answer()

    user = query.message.from_user
    logger.info(f'El usuario {user.first_name} {user.last_name}, ha escogido la opción películas.')
    id = query.message.chat_id
    bot.sendChatAction(chat_id=id, action=ChatAction.TYPING, timeout=None)
    time.sleep(2)
    query.edit_message_text(
        text='¿Qué genero buscas?\n Sección: películas\n\n'
        '- Acción\n'
        '- Anime\n'
        '- Ciencia Ficción\n'
        '- Clásicas\n'
        '- Colombianos\n'
        '- Comedias\n'
        '- De Hollywood\n'
        '- Deportes\n'
        '- Documentales\n'
        '- Dramas\n'
        '- Fantasía\n'
        '- Fe y Espiritualidad\n'
        '- Independientes\n'
        '- Infantiles y familiares\n'
        '- Internacionales\n'
        '- Latinoamericanas\n'
        '- Los favoritos de la crítica\n'
        '- Música y musicales\n'
        '- Policiales\n'
        '- Romances\n'
        '- Terror\n'
        '- Thrillers'
        )
    bot.sendChatAction(chat_id=id, action=ChatAction.TYPING, timeout=None)
    time.sleep(1)
    query.message.reply_text('\nEscríbeme lo que buscas y con mucho gusto te ayudaré. 😉')
    return ConversationHandler.END

def series_call_handler(update, context):

    query = update.callback_query
    query.answer()

    user = query.message.from_user
    logger.info(f'El usuario {user.first_name} {user.last_name}, ha escogido la opción series.')
    id = query.message.chat_id
    bot.sendChatAction(chat_id=id, action=ChatAction.TYPING, timeout=None)
    time.sleep(2)
    query.edit_message_text(
        text='¿Qué genero buscas?\n Sección: Series\n\n'
        '- Acción\n'
        '- Animes\n'
        '- Asiáticos\n'
        '- Británicos\n'
        '- Ciencia Ficción\n'
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
    query.message.reply_text('\nEscríbeme lo que buscas y con mucho gusto te ayudaré. 😉')
    return ConversationHandler.END

def plan_basico(update: Update, context: CallbackContext) -> int:


    query = update.callback_query
    query.answer()

    user = query.message.from_user
    logger.info(f'El usuario {user.first_name} {user.last_name}, ha escogido el plan básico.')
    id = query.message.chat_id
    #query.message.reply_text('Te envío la información pertinente al Plan Básico.\n\n')
    
    # print(id)
    query.edit_message_text(
        text='Aquí te envío toda la información correspondiente al plan básico.'
    )
    with open('img/basicPrices.PNG','rb') as photo_file:
     bot.sendChatAction(chat_id=id, action=ChatAction.UPLOAD_PHOTO, timeout=None)
     time.sleep(1)
     bot.sendPhoto(chat_id=id, photo=photo_file, caption='Precios y descripción plan básico.')
     bot.sendChatAction(chat_id=id, action=ChatAction.TYPING, timeout=None)
    time.sleep(1)
    query.message.reply_text("La disponibilidad del contenido en Full HD (1080p), Ultra HD (4K) y HDR depende de tu servicio de internet y del dispositivo en uso. No todo el contenido está disponible en HD, Full HD, Ultra HD o HDR. Consulta los Términos de uso para obtener más información. "
    "Solo las personas que vivan contigo pueden usar tu cuenta. Puedes ver Netflix en 4 dispositivos distintos al mismo tiempo con el plan Premium, en 2 con el plan Estándar y en 1 con el plan Básico.")
    bot.sendChatAction(chat_id=id, action=ChatAction.TYPING, timeout=None)
    time.sleep(1)
    query.message.reply_text("Recuerda que el comando /pago te brindará información de las cuentas bancarias habilitadas para que realices tu compra.")
    bot.sendChatAction(chat_id=id, action=ChatAction.TYPING, timeout=None)
    time.sleep(1)
    query.message.reply_text("/start para regresar al menú principal.")
    with open('stickers/besopatito.tgs','rb') as sticker_file:
     bot.sendChatAction(chat_id=id, action=ChatAction.TYPING, timeout=None)
     time.sleep(0.5)
     bot.sendSticker(chat_id=id, sticker=sticker_file) 

    return ConversationHandler.END

def plan_estandar(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()

    user = query.message.from_user
    logger.info(f'El usuario {user.first_name} {user.last_name}, ha escogido el plan estándar.')
    id = query.message.chat_id

    query.edit_message_text(
        text='Aquí te envío toda la información respecto al plan estándar.'
    )
    with open('img/StandarPrices.PNG','rb') as photo_file:
     bot.sendChatAction(chat_id=id, action=ChatAction.UPLOAD_PHOTO, timeout=None)
     time.sleep(1)
     bot.sendPhoto(chat_id=id, photo=photo_file, caption='Precios y descripción plan estándar.')
     bot.sendChatAction(chat_id=id, action=ChatAction.TYPING, timeout=None)
     time.sleep(1)
    query.message.reply_text("La disponibilidad del contenido en Full HD (1080p), Ultra HD (4K) y HDR depende de tu servicio de internet y del dispositivo en uso. No todo el contenido está disponible en HD, Full HD, Ultra HD o HDR. Consulta los Términos de uso para obtener más información. "
    "Solo las personas que vivan contigo pueden usar tu cuenta. Puedes ver Netflix en 4 dispositivos distintos al mismo tiempo con el plan Premium, en 2 con el plan Estándar y en 1 con el plan Básico.")
    bot.sendChatAction(chat_id=id, action=ChatAction.TYPING, timeout=None)
    time.sleep(1)
    query.message.reply_text("Recuerda que el comando /pago te brindará información de las cuentas habilitadas para que realices tu compra.")
    bot.sendChatAction(chat_id=id, action=ChatAction.TYPING, timeout=None)
    time.sleep(1)
    query.message.reply_text("/start para regresar al menú principal.")
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
        text='Aquí te envío toda la información respecto al plan premium.'
    )
    with open('img/PremiumPrices.PNG','rb') as photo_file:
     bot.sendChatAction(chat_id=id, action=ChatAction.UPLOAD_PHOTO, timeout=None)
     time.sleep(1)
     bot.sendPhoto(chat_id=id, photo=photo_file, caption='Precios y descripción plan premium.')
     bot.sendChatAction(chat_id=id, action=ChatAction.TYPING, timeout=None)
     time.sleep(1)
    query.message.reply_text("La disponibilidad del contenido en Full HD (1080p), Ultra HD (4K) y HDR depende de tu servicio de internet y del dispositivo en uso. No todo el contenido está disponible en HD, Full HD, Ultra HD o HDR. Consulta los Términos de uso para obtener más información. "
    "Solo las personas que vivan contigo pueden usar tu cuenta. Puedes ver Netflix en 4 dispositivos distintos al mismo tiempo con el plan Premium, en 2 con el plan Estándar y en 1 con el plan Básico.")
    bot.sendChatAction(chat_id=id, action=ChatAction.TYPING, timeout=None)
    time.sleep(1)
    query.message.reply_text("Recuerda que el comando /pago te brindará información de las cuentas habilitadas para que realices tu compra.")
    bot.sendChatAction(chat_id=id, action=ChatAction.TYPING, timeout=None)
    time.sleep(1)
    query.message.reply_text("/start para regresar al menú principal.")
    with open('stickers/besopatito.tgs','rb') as sticker_file:
     bot.sendChatAction(chat_id=id, action=ChatAction.TYPING, timeout=None)
     time.sleep(0.5)
     bot.sendSticker(chat_id=id, sticker=sticker_file) 

    return ConversationHandler.END

def micuenta(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    logger.info(f'El usuario {user.first_name} {user.last_name}, ha ingresado al comando /micuenta.')
    update.message.reply_text(
        'Por favor envíame el correo electrónico (todo en minúscula) que tienes asociado,  para validar la información.\n\n'
        'O envía /saltar si no lo recuerdas',
        reply_markup=ReplyKeyboardRemove(),
    )

    return CORREO


def correo(update, context):

    user_name = update.effective_user['first_name']
    user_last = update.effective_user['last_name']
    user_id = update.effective_user['id']

    email = update.message.text

    logger.info("Correo que ingresó %s %s fue %s", user_name, user_last, email)
    update.message.reply_text(
        text=f"Esta es la dirección de correo electrónico que nos has proporcionado: \n{email}\n\n")
    
    for i in range(1):
        try:
            cell = sheet.find(email)

            if(email == "email_from_google_sheets_database"):
                update.message.reply_text("Por favor selecciona el nombre de tu perfil.\n\n",
                reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(text='Camila Sánchez', callback_data='cami_sanchez')],
                [InlineKeyboardButton(text='Diana Sánchez', callback_data='diana_sanchez')],
                [InlineKeyboardButton(text='Joan', callback_data='joan_angarita')],
                [InlineKeyboardButton(text='Joan Angarita 2', callback_data='joan_angarita')]
                ])
                )
            
            elif(email == "email_from_google_sheets_database"):
                update.message.reply_text("Por favor selecciona el nombre de tu perfil.\n\n",
                reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(text='Keli Suárez', callback_data='keli_suarez')],
                [InlineKeyboardButton(text='Stiven', callback_data='stiven_duque')],
                [InlineKeyboardButton(text='Fabián', callback_data='fabian_duque')],
                [InlineKeyboardButton(text='Horacio Alzáte', callback_data='horacio_alzate')]
                ])
                )
            
            elif(email == "email_from_google_sheets_database"):
                update.message.reply_text("Por favor selecciona el nombre de tu perfil.\n\n",
                reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(text='Daniela Acevedo', callback_data='dani_ace')],
                [InlineKeyboardButton(text='Juan Gutiérrez', callback_data='juan_gu')],
                [InlineKeyboardButton(text='Sophia Jaramillo', callback_data='sophi_jara')],
                [InlineKeyboardButton(text='Maria Isabel Giraldo', callback_data='mariai_giraldo')]
                ])
                )
            
            elif(email == "email_from_google_sheets_database"):
                update.message.reply_text("Por favor selecciona el nombre de tu perfil.\n\n",
                reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(text='Jhon', callback_data='brarlynn_muñoz')],
                [InlineKeyboardButton(text='Brarlynn', callback_data='brarlynn_muñoz')],
                [InlineKeyboardButton(text='Karen Fonseca', callback_data='karen_fonseca')],
                [InlineKeyboardButton(text='David', callback_data='david_chavarriaga')]
                ])
                )
            
            elif(email == "email_from_google_sheets_database"):
                update.message.reply_text("Por favor selecciona el nombre de tu perfil.\n\n",
                reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(text='Clau Jiménez', callback_data='clau_jimenez')],
                [InlineKeyboardButton(text='Yimar', callback_data='yimar')],
                [InlineKeyboardButton(text='Claudia López', callback_data='claudia_lopez')],
                [InlineKeyboardButton(text='Diana Jiménez', callback_data='diana_jimenez')]
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
                [InlineKeyboardButton(text='Berenice', callback_data='mauro_patiño')],
                [InlineKeyboardButton(text='Henry', callback_data='henry_mosquera')]
                ])
                )

            else:
                context.bot.sendMessage(chat_id=user_id, parse_mode= "HTML", text="Esta es la información de tu cuenta: \n\n"

                        f"<b>ESTADO:</b> {sheet.cell(cell.row, cell.col-4).value}\n" 
                        f"<b>PLAN:</b> {sheet.cell(cell.row, cell.col-3).value}\n"    
                        f"<b>PRECIO:</b> ${sheet.cell(cell.row, cell.col-2).value} COP/mes\n"
                        f"<b>NOMBRE:</b> {sheet.cell(cell.row, cell.col-1).value}\n"
                        f"<b>CORREO ELECTRÓNICO:</b> {sheet.cell(cell.row, cell.col).value}\n"
                        f"<b>FECHA DE PAGO OPORTUNO:</b> {sheet.cell(cell.row, cell.col+2).value}\n"
                        f"<b>FECHA DE CORTE:</b> {sheet.cell(cell.row, cell.col+3).value}"   )
                bot.sendChatAction(chat_id= user_id, action= ChatAction.TYPING, timeout= None)
                context.bot.sendMessage(chat_id= user_id, parse_mode= "HTML", text="Espero la información brindada sea de ayuda, si tienes alguna inquietud no dudes en contactarnos, el comando /asesor te puede ayudar. ¡Tus amigos de <b>Netflix Colombia</b>!👋🏻\n\n/start para regresar al menú principal.")
        
        except gspread.CellNotFound:
            context.bot.sendMessage(chat_id=user_id, parse_mode= "HTML", text="El correo electrónico proporcionado no fue hallado en nuestra base de datos. Recuerda ingresar tu correo en minúscula.\n\n"
            "/micuenta para intentarlo nuevamente o envía /start para volver al menú principal.")

    return ConversationHandler.END

def saltar_correo(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    id = update.message.from_user.id
    logger.info("Usuario %s %s no envió correo.", user.first_name, user.last_name)
    context.bot.sendMessage(chat_id= id, parse_mode="HTML", text=
        'Puedes intentarlo más tarde. El comando /asesor te puede ser útil.\n'
        '/start para volver al menú principal.\n\n'
        '¡Tus amigos de <b>Netflix Colombia</b>👋🏻!'
    )

    return ConversationHandler.END

def dani_acevedo(update: Update, context: CallbackContext) -> int:

    query = update.callback_query
    query.answer()
    user = query.message.from_user
    logger.info(f'El usuario {user.first_name} {user.last_name}, ha escogido el perfil Daniela Acevedo.')
    query.message.reply_text('Has ingresado el perfil "Daniela Acevedo" por motivos de seguridad para mirar la información de tu cuenta envíame el pin de 4 dígitos asociado a tu perfil.\n\n'
        "O envía /saltar si no lo recuerdas.",
        reply_markup=ReplyKeyboardRemove(),
        )
    
    return PIN_DANIACEVEDO

def pin_daniace(update: Update, context: CallbackContext) -> int:
              
    while True:
        try:
            pin = int(update.message.text)
            update.message.reply_text("El pin ingresado no corresponde al del perfil seleccionado.\n"
            "Inténtalo de nuevo o envía /saltar si no lo recuerdas.")
            if(pin == 2201):
                #print(pin)
                cell3 = sheet.find("Daniela Acevedo")
                id = update.message.from_user.id
                bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                bot.sendMessage(chat_id= id, text="¡Espera... este pin sí lo reconozco!😁")
                time.sleep(1)
                bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                bot.sendMessage(chat_id= id, text="Esta es la información de tu cuenta: \n\n")
                bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)     
                context.bot.sendMessage(chat_id= id, parse_mode= "HTML", text=
                f"<b>ESTADO:</b> {sheet.cell(cell3.row, cell3.col-3).value}\n" 
                f"<b>PLAN:</b> {sheet.cell(cell3.row, cell3.col-2).value}\n"    
                f"<b>PRECIO:</b> ${sheet.cell(cell3.row, cell3.col-1).value} COP/mes\n"
                f"<b>NOMBRE:</b> {sheet.cell(cell3.row, cell3.col).value}\n"
                f"<b>CORREO ELECTRÓNICO:</b> {sheet.cell(cell3.row, cell3.col+1).value}\n"
                f"<b>FECHA DE PAGO OPORTUNO:</b> {sheet.cell(cell3.row, cell3.col+3).value}\n"
                f"<b>FECHA DE CORTE:</b> {sheet.cell(cell3.row, cell3.col+4).value}"   )
            
            time.sleep(1)
            break
            #time.sleep(1)
        except ValueError:
                update.message.reply_text("Oopss! ese no era un número válido, por favor ingresa sólo 4 números o envía /saltar si no lo recuerdas.")
                time.sleep(1)
                break
    #id = update.message.from_user.id
    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
    bot.sendMessage(chat_id= id, parse_mode= "HTML", text="Espero la información brindada sea de ayuda, si tienes alguna inquietud no dudes en contactarnos, el comando /asesor te puede ayudar. ¡Tus amigos de <b>Netflix Colombia</b>!👋🏻\n\n/start para regresar al menú principal.")
    return ConversationHandler.END

def mariai_giraldo(update: Update, context: CallbackContext) -> int:

    query = update.callback_query
    query.answer()
    user = query.message.from_user
    logger.info(f'El usuario {user.first_name} {user.last_name}, ha escogido el perfil Maria Isabel Giraldo')
    query.message.reply_text('Has escogido el perfil "Maria Isabel Giraldo" por motivos de seguridad para mirar la información de tu cuenta envíame el pin de 4 dígitos asociado a tu perfil.\n\n'
        'O envía /saltar si no lo recuerdas.',
        reply_markup=ReplyKeyboardRemove(),
        )
    
    return PIN_MARIAIG

def pin_mariaig(update: Update, context: CallbackContext) -> int:
              
    while True:
        try:
            pin = int(update.message.text)
            update.message.reply_text("El pin ingresado no corresponde al del perfil seleccionado.\n"
            "Inténtalo de nuevo o envía /saltar si no lo recuerdas.")
            if(pin == 514):
                #print(pin)
                cell3 = sheet.find("Maria Isabel Giraldo")
                id = update.message.from_user.id
                bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                bot.sendMessage(chat_id= id, text="¡Espera... este pin sí lo reconozco!😁")
                time.sleep(1)
                bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                bot.sendMessage(chat_id= id, text="Esta es la información de tu cuenta: \n\n")
                bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)     
                context.bot.sendMessage(chat_id= id, parse_mode= "HTML", text=
                f"<b>ESTADO:</b> {sheet.cell(cell3.row, cell3.col-3).value}\n" 
                f"<b>PLAN:</b> {sheet.cell(cell3.row, cell3.col-2).value}\n"    
                f"<b>PRECIO:</b> ${sheet.cell(cell3.row, cell3.col-1).value} COP/mes\n"
                f"<b>NOMBRE:</b> {sheet.cell(cell3.row, cell3.col).value}\n"
                f"<b>CORREO ELECTRÓNICO:</b> {sheet.cell(cell3.row, cell3.col+1).value}\n"
                f"<b>FECHA DE PAGO OPORTUNO:</b> {sheet.cell(cell3.row, cell3.col+3).value}\n"
                f"<b>FECHA DE CORTE:</b> {sheet.cell(cell3.row, cell3.col+4).value}"   )
            
            time.sleep(1)
            break
            #time.sleep(1)
        except ValueError:
                update.message.reply_text("Oopss! ese no era un número válido, por favor ingresa sólo 4 números o envía /saltar si no lo recuerdas.")
                time.sleep(1)
                break
    #id = update.message.from_user.id
    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
    bot.sendMessage(chat_id= id, parse_mode= "HTML", text="Espero la información brindada sea de ayuda, si tienes alguna inquietud no dudes en contactarnos, el comando /asesor te puede ayudar. ¡Tus amigos de <b>Netflix Colombia</b>!👋🏻\n\n/start para regresar al menú principal.")
    return ConversationHandler.END

def juan_gu(update: Update, context: CallbackContext) -> int:

    query = update.callback_query
    query.answer()
    user = query.message.from_user
    logger.info(f'El usuario {user.first_name} {user.last_name}, ha escogido el perfil Juan Gutiérrez.')
    query.message.reply_text("Por motivos de seguridad para mirar la información de tu cuenta envíame el pin de 4 dígitos asociado a tu perfil.\n\n"
        "O envía /saltar si no lo recuerdas.",
        reply_markup=ReplyKeyboardRemove(),
        )
    return PIN_JUANGUT

def pin_juang(update: Update, context: CallbackContext) -> int:
        #if(update.message.text.find("2612") == 0):
              
    while True:
        try:
            pin = int(update.message.text)
            update.message.reply_text("El pin ingresado no corresponde al del perfil seleccionado.\n"
            "Inténtalo de nuevo o envía /saltar si no lo recuerdas.")
            if(pin == 4488):
                #print(pin)
                cell3 = sheet.find("Juan Gutiérrez")
                id = update.message.from_user.id
                bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                bot.sendMessage(chat_id= id, text="¡Espera... este pin sí lo reconozco!😁")
                time.sleep(1)
                bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                bot.sendMessage(chat_id= id, text="Esta es la información de tu cuenta: \n\n")
                bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)     
                context.bot.sendMessage(chat_id= id, parse_mode= "HTML", text=
                f"<b>ESTADO:</b> {sheet.cell(cell3.row, cell3.col-3).value}\n" 
                f"<b>PLAN:</b> {sheet.cell(cell3.row, cell3.col-2).value}\n"    
                f"<b>PRECIO:</b> ${sheet.cell(cell3.row, cell3.col-1).value} COP/mes\n"
                f"<b>NOMBRE:</b> {sheet.cell(cell3.row, cell3.col).value}\n"
                f"<b>CORREO ELECTRÓNICO:</b> {sheet.cell(cell3.row, cell3.col+1).value}\n"
                f"<b>FECHA DE PAGO OPORTUNO:</b> {sheet.cell(cell3.row, cell3.col+3).value}\n"
                f"<b>FECHA DE CORTE:</b> {sheet.cell(cell3.row, cell3.col+4).value}"   )
            
            time.sleep(1)
            break
            #time.sleep(1)
        except ValueError:
                update.message.reply_text("Oopss! ese no era un número válido, por favor ingresa sólo 4 números o envía /saltar si no lo recuerdas.")
                time.sleep(1)
                break
    #id = update.message.from_user.id
    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
    bot.sendMessage(chat_id= id, parse_mode= "HTML", text="Espero la información brindada sea de ayuda, si tienes alguna inquietud no dudes en contactarnos, el comando /asesor te puede ayudar. ¡Tus amigos de <b>Netflix Colombia</b>!👋🏻\n\n/start para regresar al menú principal.")
    return ConversationHandler.END

def sophi_jara(update: Update, context: CallbackContext) -> int:

    query = update.callback_query
    query.answer()
    user = query.message.from_user
    logger.info(f'El usuario {user.first_name} {user.last_name}, ha escogido el perfil Sophia Jaramillo.')
    query.message.reply_text("Por motivos de seguridad para mirar la información de tu cuenta envíame el pin de 4 dígitos asociado a tu perfil.\n\n"
        "O envía /saltar si no lo recuerdas.",
        reply_markup=ReplyKeyboardRemove(),
        )
    return PIN_SOPHI

def pin_sophi(update: Update, context: CallbackContext) -> int:
              
    while True:
        try:
            pin = int(update.message.text)
            update.message.reply_text("El pin ingresado no corresponde al del perfil seleccionado.\n"
            "Inténtalo de nuevo o envía /saltar si no lo recuerdas.")
            if(pin == 926):
                #print(pin)
                cell3 = sheet.find("Sophia Jaramillo")
                id = update.message.from_user.id
                bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                bot.sendMessage(chat_id= id, text="¡Espera... este pin sí lo reconozco!😁")
                time.sleep(1)
                bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                bot.sendMessage(chat_id= id, text="Esta es la información de tu cuenta: \n\n")
                bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)     
                context.bot.sendMessage(chat_id= id, parse_mode= "HTML", text=
                f"<b>ESTADO:</b> {sheet.cell(cell3.row, cell3.col-3).value}\n" 
                f"<b>PLAN:</b> {sheet.cell(cell3.row, cell3.col-2).value}\n"    
                f"<b>PRECIO:</b> ${sheet.cell(cell3.row, cell3.col-1).value} COP/mes\n"
                f"<b>NOMBRE:</b> {sheet.cell(cell3.row, cell3.col).value}\n"
                f"<b>CORREO ELECTRÓNICO:</b> {sheet.cell(cell3.row, cell3.col+1).value}\n"
                f"<b>FECHA DE PAGO OPORTUNO:</b> {sheet.cell(cell3.row, cell3.col+3).value}\n"
                f"<b>FECHA DE CORTE:</b> {sheet.cell(cell3.row, cell3.col+4).value}"   )
            
            time.sleep(1)
            break
            #time.sleep(1)
        except ValueError:
                update.message.reply_text("Oopss! ese no era un número válido, por favor ingresa sólo 4 números o envía /saltar si no lo recuerdas.")
                time.sleep(1)
                break
    #id = update.message.from_user.id
    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
    bot.sendMessage(chat_id= id, parse_mode= "HTML", text="Espero la información brindada sea de ayuda, si tienes alguna inquietud no dudes en contactarnos, el comando /asesor te puede ayudar. ¡Tus amigos de <b>Netflix Colombia</b>!👋🏻\n\n/start para regresar al menú principal.")
    return ConversationHandler.END

def cindy_berrio(update: Update, context: CallbackContext) -> int:

    query = update.callback_query
    query.answer()
    user = query.message.from_user
    logger.info(f'El usuario {user.first_name} {user.last_name}, ha escogido el perfil Cindy Berrio.')
    query.message.reply_text("Por motivos de seguridad para mirar la información de tu cuenta envíame el pin de 4 dígitos asociado a tu perfil.\n\n"
        "O envía /saltar si no lo recuerdas.",
        reply_markup=ReplyKeyboardRemove(),
        )
    return PIN_CINDYB

def pin_cindyb(update: Update, context: CallbackContext) -> int:

    for i in range(1):          
        while True:
            try:
                pin = int(update.message.text)
                update.message.reply_text("El pin ingresado no corresponde al del perfil seleccionado.\n"
                "Inténtalo de nuevo o envía /saltar si no lo recuerdas.")
                if(pin == 1122): #el primer dígito es 0 pero no aparece (cero a la izquierda)
                    #print(pin)
                    cell3 = sheet.find("Cindy Berrio")
                    id = update.message.from_user.id
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                    bot.sendMessage(chat_id= id, text="¡Espera... este pin sí lo reconozco!😁")
                    time.sleep(1)
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                    bot.sendMessage(chat_id= id, text="Esta es la información de tu cuenta: \n\n")
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)     
                    context.bot.sendMessage(chat_id= id, parse_mode= "HTML", text=
                    f"<b>ESTADO:</b> {sheet.cell(cell3.row, cell3.col-3).value}\n" 
                    f"<b>PLAN:</b> {sheet.cell(cell3.row, cell3.col-2).value}\n"    
                    f"<b>PRECIO:</b> ${sheet.cell(cell3.row, cell3.col-1).value} COP/mes\n"
                    f"<b>NOMBRE:</b> {sheet.cell(cell3.row, cell3.col).value}\n"
                    f"<b>CORREO ELECTRÓNICO:</b> {sheet.cell(cell3.row, cell3.col+1).value}\n"
                    f"<b>FECHA DE PAGO OPORTUNO:</b> {sheet.cell(cell3.row, cell3.col+3).value}\n"
                    f"<b>FECHA DE CORTE:</b> {sheet.cell(cell3.row, cell3.col+4).value}"   )
                
                time.sleep(1)
                break
                #time.sleep(1)
            except ValueError:
                    update.message.reply_text("Oopss! ese no era un número válido, por favor ingresa sólo 4 números o envía /saltar si no lo recuerdas.")
                    time.sleep(1)
                    break
        #id = update.message.from_user.id
        bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
        bot.sendMessage(chat_id= id, parse_mode= "HTML", text="Espero la información brindada sea de ayuda, si tienes alguna inquietud no dudes en contactarnos, el comando /asesor te puede ayudar. ¡Tus amigos de <b>Netflix Colombia</b>!👋🏻\n\n/start para regresar al menú principal.")
    return ConversationHandler.END

def geral_durango(update: Update, context: CallbackContext) -> int:

    query = update.callback_query
    query.answer()
    user = query.message.from_user
    logger.info(f'El usuario {user.first_name} {user.last_name}, ha escogido el perfil Geral Durango.')
    query.message.reply_text("Por motivos de seguridad para mirar la información de tu cuenta envíame el pin de 4 dígitos asociado a tu perfil.\n\n"
        "O envía /saltar si no lo recuerdas.",
        reply_markup=ReplyKeyboardRemove(),
        )
    return PIN_GERALD

def pin_gerald(update: Update, context: CallbackContext) -> int:

    for i in range(1):          
        while True:
            try:
                pin = int(update.message.text)
                update.message.reply_text("El pin ingresado no corresponde al del perfil seleccionado.\n"
                "Inténtalo de nuevo o envía /saltar si no lo recuerdas.")
                if(pin == 62): #los dos primeros dígitos son 0 pero no aparece (cero a la izquierda)
                    cell3 = sheet.find("Geraldine Durango")
                    id = update.message.from_user.id
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                    bot.sendMessage(chat_id= id, text="¡Espera... este pin sí lo reconozco!😁")
                    time.sleep(1)
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                    bot.sendMessage(chat_id= id, text="Esta es la información de tu cuenta: \n\n")
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)     
                    context.bot.sendMessage(chat_id= id, parse_mode= "HTML", text=
                    f"<b>ESTADO:</b> {sheet.cell(cell3.row, cell3.col-3).value}\n" 
                    f"<b>PLAN:</b> {sheet.cell(cell3.row, cell3.col-2).value}\n"    
                    f"<b>PRECIO:</b> ${sheet.cell(cell3.row, cell3.col-1).value} COP/mes\n"
                    f"<b>NOMBRE:</b> {sheet.cell(cell3.row, cell3.col).value}\n"
                    f"<b>CORREO ELECTRÓNICO:</b> {sheet.cell(cell3.row, cell3.col+1).value}\n"
                    f"<b>FECHA DE PAGO OPORTUNO:</b> {sheet.cell(cell3.row, cell3.col+3).value}\n"
                    f"<b>FECHA DE CORTE:</b> {sheet.cell(cell3.row, cell3.col+4).value}"   )
                
                time.sleep(1)
                break
                #time.sleep(1)
            except ValueError:
                    update.message.reply_text("Oopss! ese no era un número válido, por favor ingresa sólo 4 números o envía /saltar si no lo recuerdas.")
                    time.sleep(1)
                    break
        #id = update.message.from_user.id
        bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
        bot.sendMessage(chat_id= id, parse_mode= "HTML", text="Espero la información brindada sea de ayuda, si tienes alguna inquietud no dudes en contactarnos, el comando /asesor te puede ayudar. ¡Tus amigos de <b>Netflix Colombia</b>!👋🏻\n\n/start para regresar al menú principal.")
    return ConversationHandler.END

def estefa_sierra(update: Update, context: CallbackContext) -> int:

    query = update.callback_query
    query.answer()
    user = query.message.from_user
    logger.info(f'El usuario {user.first_name} {user.last_name}, ha escogido el perfil a nombre de Estefania Sierra.')
    query.message.reply_text('Has seleccionado el perfil "Estefania" por motivos de seguridad para mirar la información de tu cuenta envíame el pin de 4 dígitos asociado a tu perfil.\n\n'
        "O envía /saltar si no lo recuerdas.",
        reply_markup=ReplyKeyboardRemove(),
        )
    return PIN_ESTEFASIERRA

def pin_estefasierra(update: Update, context: CallbackContext) -> int:

    for i in range(1):          
        while True:
            try:
                pin = int(update.message.text)
                update.message.reply_text("El pin ingresado no corresponde al del perfil seleccionado.\n"
                "Inténtalo de nuevo o envía /saltar si no lo recuerdas.")
                if(pin == 1808): #los dos primeros dígitos son 0 pero no aparece (cero a la izquierda)
                    cell3 = sheet.find("Estefania Sierra")
                    id = update.message.from_user.id
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                    bot.sendMessage(chat_id= id, text="¡Espera... este pin sí lo reconozco!😁")
                    time.sleep(1)
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                    bot.sendMessage(chat_id= id, text="Esta es la información de tu cuenta: \n\n")
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)     
                    context.bot.sendMessage(chat_id= id, parse_mode= "HTML", text=
                    f"<b>ESTADO:</b> {sheet.cell(cell3.row, cell3.col-3).value}\n" 
                    f"<b>PLAN:</b> {sheet.cell(cell3.row, cell3.col-2).value}\n"    
                    f"<b>PRECIO:</b> ${sheet.cell(cell3.row, cell3.col-1).value} COP/mes\n"
                    f"<b>NOMBRE:</b> {sheet.cell(cell3.row, cell3.col).value}\n"
                    f"<b>CORREO ELECTRÓNICO:</b> {sheet.cell(cell3.row, cell3.col+1).value}\n"
                    f"<b>FECHA DE PAGO OPORTUNO:</b> {sheet.cell(cell3.row, cell3.col+3).value}\n"
                    f"<b>FECHA DE CORTE:</b> {sheet.cell(cell3.row, cell3.col+4).value}"   )
                
                time.sleep(1)
                break
                #time.sleep(1)
            except ValueError:
                    update.message.reply_text("Oopss! ese no era un número válido, por favor ingresa sólo 4 números o envía /saltar si no lo recuerdas.")
                    time.sleep(1)
                    break
        #id = update.message.from_user.id
        bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
        bot.sendMessage(chat_id= id, parse_mode= "HTML", text="Espero la información brindada sea de ayuda, si tienes alguna inquietud no dudes en contactarnos, el comando /asesor te puede ayudar. ¡Tus amigos de <b>Netflix Colombia</b>!👋🏻\n\n/start para regresar al menú principal.")
    return ConversationHandler.END

def kate_hernandez(update: Update, context: CallbackContext) -> int:

    query = update.callback_query
    query.answer()
    user = query.message.from_user
    logger.info(f'El usuario {user.first_name} {user.last_name}, ha escogido el perfil Katerine Hernández.')
    query.message.reply_text("Por motivos de seguridad para mirar la información de tu cuenta envíame el pin de 4 dígitos asociado a tu perfil.\n\n"
        "O envía /saltar si no lo recuerdas.",
        reply_markup=ReplyKeyboardRemove(),
        )
    return PIN_KATEHDZ

def pin_katehdz(update: Update, context: CallbackContext) -> int:

    for i in range(1):          
        while True:
            try:
                pin = int(update.message.text)
                update.message.reply_text("El pin ingresado no corresponde al del perfil seleccionado.\n"
                "Inténtalo de nuevo o envía /saltar si no lo recuerdas.")
                if(pin == 1216):
                    cell3 = sheet.find("Katerine Hernández")
                    id = update.message.from_user.id
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                    bot.sendMessage(chat_id= id, text="¡Espera... este pin sí lo reconozco!😁")
                    time.sleep(1)
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                    bot.sendMessage(chat_id= id, text="Esta es la información de tu cuenta: \n\n")
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)     
                    context.bot.sendMessage(chat_id= id, parse_mode= "HTML", text=
                    f"<b>ESTADO:</b> {sheet.cell(cell3.row, cell3.col-3).value}\n" 
                    f"<b>PLAN:</b> {sheet.cell(cell3.row, cell3.col-2).value}\n"    
                    f"<b>PRECIO:</b> ${sheet.cell(cell3.row, cell3.col-1).value} COP/mes\n"
                    f"<b>NOMBRE:</b> {sheet.cell(cell3.row, cell3.col).value}\n"
                    f"<b>CORREO ELECTRÓNICO:</b> {sheet.cell(cell3.row, cell3.col+1).value}\n"
                    f"<b>FECHA DE PAGO OPORTUNO:</b> {sheet.cell(cell3.row, cell3.col+3).value}\n"
                    f"<b>FECHA DE CORTE:</b> {sheet.cell(cell3.row, cell3.col+4).value}"   )
                
                time.sleep(1)
                break
            except ValueError:
                    update.message.reply_text("Oopss! ese no era un número válido, por favor ingresa sólo 4 números o envía /saltar si no lo recuerdas.")
                    time.sleep(1)
                    break
        #id = update.message.from_user.id
        bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
        bot.sendMessage(chat_id= id, parse_mode= "HTML", text="Espero la información brindada sea de ayuda, si tienes alguna inquietud no dudes en contactarnos, el comando /asesor te puede ayudar. ¡Tus amigos de <b>Netflix Colombia</b>!👋🏻\n\n/start para regresar al menú principal.")
    return ConversationHandler.END

def keli_suarez(update: Update, context: CallbackContext) -> int:

    query = update.callback_query
    query.answer()
    user = query.message.from_user
    logger.info(f'El usuario {user.first_name} {user.last_name}, ha escogido el perfil Keli Suárez.')
    query.message.reply_text('Has escogido el perfil "Keli Suárez", por motivos de seguridad para mirar la información de tu cuenta envíame el pin de 4 dígitos asociado a tu perfil.\n\n'
        "O envía /saltar si no lo recuerdas.",
        reply_markup=ReplyKeyboardRemove(),
        )
    return PIN_KELISUAREZ

def pin_kelisuarez(update: Update, context: CallbackContext) -> int:

    for i in range(1):          
        while True:
            try:
                pin = int(update.message.text)
                update.message.reply_text("El pin ingresado no corresponde al del perfil seleccionado.\n"
                "Inténtalo de nuevo o envía /saltar si no lo recuerdas.")
                if(pin == 727): #pin: 0727
                    cell3 = sheet.find("Keli Suárez")
                    id = update.message.from_user.id
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                    bot.sendMessage(chat_id= id, text="¡Espera... este pin sí lo reconozco!😁")
                    time.sleep(1)
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                    bot.sendMessage(chat_id= id, text="Esta es la información de tu cuenta: \n\n")
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)     
                    context.bot.sendMessage(chat_id= id, parse_mode= "HTML", text=
                    f"<b>ESTADO:</b> {sheet.cell(cell3.row, cell3.col-3).value}\n" 
                    f"<b>PLAN:</b> {sheet.cell(cell3.row, cell3.col-2).value}\n"    
                    f"<b>PRECIO:</b> ${sheet.cell(cell3.row, cell3.col-1).value} COP/mes\n"
                    f"<b>NOMBRE:</b> {sheet.cell(cell3.row, cell3.col).value}\n"
                    f"<b>CORREO ELECTRÓNICO:</b> {sheet.cell(cell3.row, cell3.col+1).value}\n"
                    f"<b>FECHA DE PAGO OPORTUNO:</b> {sheet.cell(cell3.row, cell3.col+3).value}\n"
                    f"<b>FECHA DE CORTE:</b> {sheet.cell(cell3.row, cell3.col+4).value}"   )
                
                time.sleep(1)
                break
            except ValueError:
                    update.message.reply_text("Oopss! ese no era un número válido, por favor ingresa sólo 4 números o envía /saltar si no lo recuerdas.")
                    time.sleep(1)
                    break
        #id = update.message.from_user.id
        bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
        bot.sendMessage(chat_id= id, parse_mode= "HTML", text="Espero la información brindada sea de ayuda, si tienes alguna inquietud no dudes en contactarnos, el comando /asesor te puede ayudar. ¡Tus amigos de <b>Netflix Colombia</b>!👋🏻\n\n/start para regresar al menú principal.")
    return ConversationHandler.END

def stiven_duque(update: Update, context: CallbackContext) -> int:

    query = update.callback_query
    query.answer()
    user = query.message.from_user
    logger.info(f'El usuario {user.first_name} {user.last_name}, ha escogido el perfil Keli Suárez.')
    query.message.reply_text('Has escogido el perfil "Stiven", por motivos de seguridad para mirar la información de tu cuenta envíame el pin de 4 dígitos asociado a tu perfil.\n\n'
        "O envía /saltar si no lo recuerdas.",
        reply_markup=ReplyKeyboardRemove(),
        )
    return PIN_STIVEND

def pin_stivend(update: Update, context: CallbackContext) -> int:

    for i in range(1):          
        while True:
            try:
                pin = int(update.message.text)
                update.message.reply_text("El pin ingresado no corresponde al del perfil seleccionado.\n"
                "Inténtalo de nuevo o envía /saltar si no lo recuerdas.")
                if(pin == 9866):
                    cell3 = sheet.find("Stiven Duque")
                    id = update.message.from_user.id
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                    bot.sendMessage(chat_id= id, text="¡Espera... este pin sí lo reconozco!😁")
                    time.sleep(1)
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                    bot.sendMessage(chat_id= id, text="Esta es la información de tu cuenta: \n\n")
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)     
                    context.bot.sendMessage(chat_id= id, parse_mode= "HTML", text=
                    f"<b>ESTADO:</b> {sheet.cell(cell3.row, cell3.col-3).value}\n" 
                    f"<b>PLAN:</b> {sheet.cell(cell3.row, cell3.col-2).value}\n"    
                    f"<b>PRECIO:</b> ${sheet.cell(cell3.row, cell3.col-1).value} COP/mes\n"
                    f"<b>NOMBRE:</b> {sheet.cell(cell3.row, cell3.col).value}\n"
                    f"<b>CORREO ELECTRÓNICO:</b> {sheet.cell(cell3.row, cell3.col+1).value}\n"
                    f"<b>FECHA DE PAGO OPORTUNO:</b> {sheet.cell(cell3.row, cell3.col+3).value}\n"
                    f"<b>FECHA DE CORTE:</b> {sheet.cell(cell3.row, cell3.col+4).value}"   )
                
                time.sleep(1)
                break
            except ValueError:
                    update.message.reply_text("Oopss! ese no era un número válido, por favor ingresa sólo 4 números o envía /saltar si no lo recuerdas.")
                    time.sleep(1)
                    break
        #id = update.message.from_user.id
        bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
        bot.sendMessage(chat_id= id, parse_mode= "HTML", text="Espero la información brindada sea de ayuda, si tienes alguna inquietud no dudes en contactarnos, el comando /asesor te puede ayudar. ¡Tus amigos de <b>Netflix Colombia</b>!👋🏻\n\n/start para regresar al menú principal.")
    return ConversationHandler.END

def fabian_duque(update: Update, context: CallbackContext) -> int:

    query = update.callback_query
    query.answer()
    user = query.message.from_user
    logger.info(f'El usuario {user.first_name} {user.last_name}, ha escogido el perfil Stiven Duque.')
    query.message.reply_text("Por motivos de seguridad para mirar la información de tu cuenta envíame el pin de 4 dígitos asociado a tu perfil.\n\n"
        "O envía /saltar si no lo recuerdas.",
        reply_markup=ReplyKeyboardRemove(),
        )
    return PIN_FABIAND

def pin_fabiand(update: Update, context: CallbackContext) -> int:

    for i in range(1):          
        while True:
            try:
                pin = int(update.message.text)
                update.message.reply_text("El pin ingresado no corresponde al del perfil seleccionado.\n"
                "Inténtalo de nuevo o envía /saltar si no lo recuerdas.")
                if(pin == 9866):
                    cell3 = sheet.find("Stiven Duque")
                    id = update.message.from_user.id
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                    bot.sendMessage(chat_id= id, text="¡Espera... este pin sí lo reconozco!😁")
                    time.sleep(1)
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                    bot.sendMessage(chat_id= id, text="Esta es la información de tu cuenta: \n\n")
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)     
                    context.bot.sendMessage(chat_id= id, parse_mode= "HTML", text=
                    f"<b>ESTADO:</b> {sheet.cell(cell3.row, cell3.col-3).value}\n" 
                    f"<b>PLAN:</b> {sheet.cell(cell3.row, cell3.col-2).value}\n"    
                    f"<b>PRECIO:</b> ${sheet.cell(cell3.row, cell3.col-1).value} COP/mes\n"
                    f"<b>NOMBRE:</b> {sheet.cell(cell3.row, cell3.col).value}\n"
                    f"<b>CORREO ELECTRÓNICO:</b> {sheet.cell(cell3.row, cell3.col+1).value}\n"
                    f"<b>FECHA DE PAGO OPORTUNO:</b> {sheet.cell(cell3.row, cell3.col+3).value}\n"
                    f"<b>FECHA DE CORTE:</b> {sheet.cell(cell3.row, cell3.col+4).value}"   )
                
                time.sleep(1)
                break
            except ValueError:
                    update.message.reply_text("Oopss! ese no era un número válido, por favor ingresa sólo 4 números o envía /saltar si no lo recuerdas.")
                    time.sleep(1)
                    break
        #id = update.message.from_user.id
        bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
        bot.sendMessage(chat_id= id, parse_mode= "HTML", text="Espero la información brindada sea de ayuda, si tienes alguna inquietud no dudes en contactarnos, el comando /asesor te puede ayudar. ¡Tus amigos de <b>Netflix Colombia</b>!👋🏻\n\n/start para regresar al menú principal.")
    return ConversationHandler.END

def horacio_alzate(update: Update, context: CallbackContext) -> int:

    query = update.callback_query
    query.answer()
    user = query.message.from_user
    logger.info(f'El usuario {user.first_name} {user.last_name}, ha escogido el perfil Horacio Alzate.')
    query.message.reply_text("Por motivos de seguridad para mirar la información de tu cuenta envíame el pin de 4 dígitos asociado a tu perfil.\n\n"
        "O envía /saltar si no lo recuerdas.",
        reply_markup=ReplyKeyboardRemove(),
        )
    return PIN_HORACIOA

def pin_horacioa(update: Update, context: CallbackContext) -> int:

    for i in range(1):          
        while True:
            try:
                pin = int(update.message.text)
                update.message.reply_text("El pin ingresado no corresponde al del perfil seleccionado.\n"
                "Inténtalo de nuevo o envía /saltar si no lo recuerdas.")
                if(pin == 4444):
                    cell3 = sheet.find("Horacio Alzáte")
                    id = update.message.from_user.id
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                    bot.sendMessage(chat_id= id, text="¡Espera... este pin sí lo reconozco!😁")
                    time.sleep(1)
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                    bot.sendMessage(chat_id= id, text="Esta es la información de tu cuenta: \n\n")
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)     
                    context.bot.sendMessage(chat_id= id, parse_mode= "HTML", text=
                    f"<b>ESTADO:</b> {sheet.cell(cell3.row, cell3.col-3).value}\n" 
                    f"<b>PLAN:</b> {sheet.cell(cell3.row, cell3.col-2).value}\n"    
                    f"<b>PRECIO:</b> ${sheet.cell(cell3.row, cell3.col-1).value} COP/mes\n"
                    f"<b>NOMBRE:</b> {sheet.cell(cell3.row, cell3.col).value}\n"
                    f"<b>CORREO ELECTRÓNICO:</b> {sheet.cell(cell3.row, cell3.col+1).value}\n"
                    f"<b>FECHA DE PAGO OPORTUNO:</b> {sheet.cell(cell3.row, cell3.col+3).value}\n"
                    f"<b>FECHA DE CORTE:</b> {sheet.cell(cell3.row, cell3.col+4).value}"   )
                
                time.sleep(1)
                break
            except ValueError:
                    update.message.reply_text("Oopss! ese no era un número válido, por favor ingresa sólo 4 números o envía /saltar si no lo recuerdas.")
                    time.sleep(1)
                    break
        #id = update.message.from_user.id
        bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
        bot.sendMessage(chat_id= id, parse_mode= "HTML", text="Espero la información brindada sea de ayuda, si tienes alguna inquietud no dudes en contactarnos, el comando /asesor te puede ayudar. ¡Tus amigos de <b>Netflix Colombia</b>!👋🏻\n\n/start para regresar al menú principal.")
    return ConversationHandler.END

def elkin_carmona(update: Update, context: CallbackContext) -> int:

    query = update.callback_query
    query.answer()
    user = query.message.from_user
    logger.info(f'El usuario {user.first_name} {user.last_name}, ha escogido el perfil Elkin Carmona.')
    query.message.reply_text('Has escogido el perfil "Elkin" por motivos de seguridad para mirar la información de tu cuenta envíame el pin de 4 dígitos asociado a tu perfil.\n\n'
        "O envía /saltar si no lo recuerdas.",
        reply_markup=ReplyKeyboardRemove(),
        )
    return PIN_ELKINCAR

def pin_elkinc(update: Update, context: CallbackContext) -> int:

    for i in range(1):          
        while True:
            try:
                pin = int(update.message.text)
                update.message.reply_text("El pin ingresado no corresponde al del perfil seleccionado.\n"
                "Inténtalo de nuevo o envía /saltar si no lo recuerdas.")
                if(pin == 1927):
                    cell3 = sheet.find("Elkin Carmona")
                    id = update.message.from_user.id
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                    bot.sendMessage(chat_id= id, text="¡Espera... este pin sí lo reconozco!😁")
                    time.sleep(1)
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                    bot.sendMessage(chat_id= id, text="Esta es la información de tu cuenta: \n\n")
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)     
                    context.bot.sendMessage(chat_id= id, parse_mode= "HTML", text=
                    f"<b>ESTADO:</b> {sheet.cell(cell3.row, cell3.col-3).value}\n" 
                    f"<b>PLAN:</b> {sheet.cell(cell3.row, cell3.col-2).value}\n"    
                    f"<b>PRECIO:</b> ${sheet.cell(cell3.row, cell3.col-1).value} COP/mes\n"
                    f"<b>NOMBRE:</b> {sheet.cell(cell3.row, cell3.col).value}\n"
                    f"<b>CORREO ELECTRÓNICO:</b> {sheet.cell(cell3.row, cell3.col+1).value}\n"
                    f"<b>FECHA DE PAGO OPORTUNO:</b> {sheet.cell(cell3.row, cell3.col+3).value}\n"
                    f"<b>FECHA DE CORTE:</b> {sheet.cell(cell3.row, cell3.col+4).value}"   )
                
                time.sleep(1)
                break
            except ValueError:
                    update.message.reply_text("Oopss! ese no era un número válido, por favor ingresa sólo 4 números o envía /saltar si no lo recuerdas.")
                    time.sleep(1)
                    break
        #id = update.message.from_user.id
        bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
        bot.sendMessage(chat_id= id, parse_mode= "HTML", text="Espero la información brindada sea de ayuda, si tienes alguna inquietud no dudes en contactarnos, el comando /asesor te puede ayudar. ¡Tus amigos de <b>Netflix Colombia</b>!👋🏻\n\n/start para regresar al menú principal.")
    return ConversationHandler.END

def kate_betancur(update: Update, context: CallbackContext) -> int:

    query = update.callback_query
    query.answer()
    user = query.message.from_user
    logger.info(f'El usuario {user.first_name} {user.last_name}, ha escogido el perfil a nombre de Katerine Betancur.')
    query.message.reply_text("Por motivos de seguridad para mirar la información de tu cuenta envíame el pin de 4 dígitos asociado a tu perfil.\n\n"
        "O envía /saltar si no lo recuerdas.",
        reply_markup=ReplyKeyboardRemove(),
        )
    return PIN_KTBETANCUR

def pin_ktbetancur(update: Update, context: CallbackContext) -> int:

    for i in range(1):          
        while True:
            try:
                pin = int(update.message.text)
                update.message.reply_text("El pin ingresado no corresponde al del perfil seleccionado.\n"
                "Inténtalo de nuevo o envía /saltar si no lo recuerdas.")
                if(pin == 7378):
                    cell3 = sheet.find("Katerine Betancur Cardona")
                    id = update.message.from_user.id
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                    bot.sendMessage(chat_id= id, text="¡Espera... este pin sí lo reconozco!😁")
                    time.sleep(1)
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                    bot.sendMessage(chat_id= id, text="Esta es la información de tu cuenta: \n\n")
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)     
                    context.bot.sendMessage(chat_id= id, parse_mode= "HTML", text=
                    f"<b>ESTADO:</b> {sheet.cell(cell3.row, cell3.col-3).value}\n" 
                    f"<b>PLAN:</b> {sheet.cell(cell3.row, cell3.col-2).value}\n"    
                    f"<b>PRECIO:</b> ${sheet.cell(cell3.row, cell3.col-1).value} COP/mes\n"
                    f"<b>NOMBRE:</b> {sheet.cell(cell3.row, cell3.col).value}\n"
                    f"<b>CORREO ELECTRÓNICO:</b> {sheet.cell(cell3.row, cell3.col+1).value}\n"
                    f"<b>FECHA DE PAGO OPORTUNO:</b> {sheet.cell(cell3.row, cell3.col+3).value}\n"
                    f"<b>FECHA DE CORTE:</b> {sheet.cell(cell3.row, cell3.col+4).value}"   )
                
                time.sleep(1)
                break
            except ValueError:
                    update.message.reply_text("Oopss! ese no era un número válido, por favor ingresa sólo 4 números o envía /saltar si no lo recuerdas.")
                    time.sleep(1)
                    break
        #id = update.message.from_user.id
        bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
        bot.sendMessage(chat_id= id, parse_mode= "HTML", text="Espero la información brindada sea de ayuda, si tienes alguna inquietud no dudes en contactarnos, el comando /asesor te puede ayudar. ¡Tus amigos de <b>Netflix Colombia</b>!👋🏻\n\n/start para regresar al menú principal.")
    return ConversationHandler.END

def viviana_toro(update: Update, context: CallbackContext) -> int:

    query = update.callback_query
    query.answer()
    user = query.message.from_user
    logger.info(f'El usuario {user.first_name} {user.last_name}, ha escogido el perfil a nombre de Katerine Betancur.')
    query.message.reply_text('Has seleccionado el perfil "Vivi Toro" por motivos de seguridad para mirar la información de tu cuenta envíame el pin de 4 dígitos asociado a tu perfil.\n\n'
        "O envía /saltar si no lo recuerdas.",
        reply_markup=ReplyKeyboardRemove(),
        )
    return PIN_VIVITORO

def pin_vivitoro(update: Update, context: CallbackContext) -> int:

    for i in range(1):          
        while True:
            try:
                pin = int(update.message.text)
                update.message.reply_text("El pin ingresado no corresponde al del perfil seleccionado.\n"
                "Inténtalo de nuevo o envía /saltar si no lo recuerdas.")
                if(pin == 423):
                    cell3 = sheet.find("Viviana Toro")
                    id = update.message.from_user.id
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                    bot.sendMessage(chat_id= id, text="¡Espera... este pin sí lo reconozco!😁")
                    time.sleep(1)
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                    bot.sendMessage(chat_id= id, text="Esta es la información de tu cuenta: \n\n")
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)     
                    context.bot.sendMessage(chat_id= id, parse_mode= "HTML", text=
                    f"<b>ESTADO:</b> {sheet.cell(cell3.row, cell3.col-3).value}\n" 
                    f"<b>PLAN:</b> {sheet.cell(cell3.row, cell3.col-2).value}\n"    
                    f"<b>PRECIO:</b> ${sheet.cell(cell3.row, cell3.col-1).value} COP/mes\n"
                    f"<b>NOMBRE:</b> {sheet.cell(cell3.row, cell3.col).value}\n"
                    f"<b>CORREO ELECTRÓNICO:</b> {sheet.cell(cell3.row, cell3.col+1).value}\n"
                    f"<b>FECHA DE PAGO OPORTUNO:</b> {sheet.cell(cell3.row, cell3.col+3).value}\n"
                    f"<b>FECHA DE CORTE:</b> {sheet.cell(cell3.row, cell3.col+4).value}"   )
                
                time.sleep(1)
                break
            except ValueError:
                    update.message.reply_text("Oopss! ese no era un número válido, por favor ingresa sólo 4 números o envía /saltar si no lo recuerdas.")
                    time.sleep(1)
                    break
        #id = update.message.from_user.id
        bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
        bot.sendMessage(chat_id= id, parse_mode= "HTML", text="Espero la información brindada sea de ayuda, si tienes alguna inquietud no dudes en contactarnos, el comando /asesor te puede ayudar. ¡Tus amigos de <b>Netflix Colombia</b>!👋🏻\n\n/start para regresar al menú principal.")
    return ConversationHandler.END

def cami_sanchez(update: Update, context: CallbackContext) -> int:

    query = update.callback_query
    query.answer()
    user = query.message.from_user
    logger.info(f'El usuario {user.first_name} {user.last_name}, ha escogido el perfil a nombre de Camila Sánchez.')
    query.message.reply_text('Has escogido el perfil "Camila Sánchez" por motivos de seguridad para mirar la información de tu cuenta envíame el pin de 4 dígitos asociado a tu perfil.\n\n'
        "O envía /saltar si no lo recuerdas.",
        reply_markup=ReplyKeyboardRemove(),
        )
    return PIN_CAMISANCHEZ

def pin_camisanchez(update: Update, context: CallbackContext) -> int:

    for i in range(1):          
        while True:
            try:
                pin = int(update.message.text)
                update.message.reply_text("El pin ingresado no corresponde al del perfil seleccionado.\n"
                "Inténtalo de nuevo o envía /saltar si no lo recuerdas.")
                if(pin == 1958):
                    cell3 = sheet.find("Camila Sánchez")
                    id = update.message.from_user.id
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                    bot.sendMessage(chat_id= id, text="¡Espera... este pin sí lo reconozco!😁")
                    time.sleep(1)
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                    bot.sendMessage(chat_id= id, text="Esta es la información de tu cuenta: \n\n")
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)     
                    context.bot.sendMessage(chat_id= id, parse_mode= "HTML", text=
                    f"<b>ESTADO:</b> {sheet.cell(cell3.row, cell3.col-3).value}\n" 
                    f"<b>PLAN:</b> {sheet.cell(cell3.row, cell3.col-2).value}\n"    
                    f"<b>PRECIO:</b> ${sheet.cell(cell3.row, cell3.col-1).value} COP/mes\n"
                    f"<b>NOMBRE:</b> {sheet.cell(cell3.row, cell3.col).value}\n"
                    f"<b>CORREO ELECTRÓNICO:</b> {sheet.cell(cell3.row, cell3.col+1).value}\n"
                    f"<b>FECHA DE PAGO OPORTUNO:</b> {sheet.cell(cell3.row, cell3.col+3).value}\n"
                    f"<b>FECHA DE CORTE:</b> {sheet.cell(cell3.row, cell3.col+4).value}"   )
                
                time.sleep(1)
                break
            except ValueError:
                    update.message.reply_text("Oopss! ese no era un número válido, por favor ingresa sólo 4 números o envía /saltar si no lo recuerdas.")
                    time.sleep(1)
                    break
        #id = update.message.from_user.id
        bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
        bot.sendMessage(chat_id= id, parse_mode= "HTML", text="Espero la información brindada sea de ayuda, si tienes alguna inquietud no dudes en contactarnos, el comando /asesor te puede ayudar. ¡Tus amigos de <b>Netflix Colombia</b>!👋🏻\n\n/start para regresar al menú principal.")
    return ConversationHandler.END

def diana_sanchez(update: Update, context: CallbackContext) -> int:

    query = update.callback_query
    query.answer()
    user = query.message.from_user
    logger.info(f'El usuario {user.first_name} {user.last_name}, ha escogido el perfil a nombre de Diana Sánchez.')
    query.message.reply_text('Has escogido el perfil "Diana Sánchez" por motivos de seguridad para mirar la información de tu cuenta envíame el pin de 4 dígitos asociado a tu perfil.\n\n'
        "O envía /saltar si no lo recuerdas.",
        reply_markup=ReplyKeyboardRemove(),
        )
    return PIN_DIANASAN

def pin_dianasanchez(update: Update, context: CallbackContext) -> int:

    for i in range(1):          
        while True:
            try:
                pin = int(update.message.text)
                update.message.reply_text("El pin ingresado no corresponde al del perfil seleccionado.\n"
                "Inténtalo de nuevo o envía /saltar si no lo recuerdas.")
                if(pin == 126):
                    cell3 = sheet.find("Diana Sánchez")
                    id = update.message.from_user.id
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                    bot.sendMessage(chat_id= id, text="¡Espera... este pin sí lo reconozco!😁")
                    time.sleep(1)
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                    bot.sendMessage(chat_id= id, text="Esta es la información de tu cuenta: \n\n")
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)     
                    context.bot.sendMessage(chat_id= id, parse_mode= "HTML", text=
                    f"<b>ESTADO:</b> {sheet.cell(cell3.row, cell3.col-3).value}\n" 
                    f"<b>PLAN:</b> {sheet.cell(cell3.row, cell3.col-2).value}\n"    
                    f"<b>PRECIO:</b> ${sheet.cell(cell3.row, cell3.col-1).value} COP/mes\n"
                    f"<b>NOMBRE:</b> {sheet.cell(cell3.row, cell3.col).value}\n"
                    f"<b>CORREO ELECTRÓNICO:</b> {sheet.cell(cell3.row, cell3.col+1).value}\n"
                    f"<b>FECHA DE PAGO OPORTUNO:</b> {sheet.cell(cell3.row, cell3.col+3).value}\n"
                    f"<b>FECHA DE CORTE:</b> {sheet.cell(cell3.row, cell3.col+4).value}"   )
                
                time.sleep(1)
                break
            except ValueError:
                    update.message.reply_text("Oopss! ese no era un número válido, por favor ingresa sólo 4 números o envía /saltar si no lo recuerdas.")
                    time.sleep(1)
                    break
        #id = update.message.from_user.id
        bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
        bot.sendMessage(chat_id= id, parse_mode= "HTML", text="Espero la información brindada sea de ayuda, si tienes alguna inquietud no dudes en contactarnos, el comando /asesor te puede ayudar. ¡Tus amigos de <b>Netflix Colombia</b>!👋🏻\n\n/start para regresar al menú principal.")
    return ConversationHandler.END

def joan_angarita(update: Update, context: CallbackContext) -> int:

    query = update.callback_query
    query.answer()
    user = query.message.from_user
    logger.info(f'El usuario {user.first_name} {user.last_name}, ha escogido el perfil a nombre de Joan Angarita.')
    query.message.reply_text('Por motivos de seguridad para mirar la información de tu cuenta envíame el pin de 4 dígitos asociado a tu perfil.\n\n'
        "O envía /saltar si no lo recuerdas.",
        reply_markup=ReplyKeyboardRemove(),
        )
    return PIN_JOANANGA

def pin_joanangarita(update: Update, context: CallbackContext) -> int:

    for i in range(1):          
        while True:
            try:
                pin = int(update.message.text)
                update.message.reply_text("El pin ingresado no corresponde al del perfil seleccionado.\n"
                "Inténtalo de nuevo o envía /saltar si no lo recuerdas.")
                if(pin == 2503):
                    cell3 = sheet.find("Joan Angarita")
                    id = update.message.from_user.id
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                    bot.sendMessage(chat_id= id, text="¡Espera... este pin sí lo reconozco!😁")
                    time.sleep(1)
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                    bot.sendMessage(chat_id= id, text="Esta es la información de tu cuenta: \n\n")
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)     
                    context.bot.sendMessage(chat_id= id, parse_mode= "HTML", text=
                    f"<b>ESTADO:</b> {sheet.cell(cell3.row, cell3.col-3).value}\n" 
                    f"<b>PLAN:</b> {sheet.cell(cell3.row, cell3.col-2).value}\n"    
                    f"<b>PRECIO:</b> ${sheet.cell(cell3.row, cell3.col-1).value} COP/mes\n"
                    f"<b>NOMBRE:</b> {sheet.cell(cell3.row, cell3.col).value}\n"
                    f"<b>CORREO ELECTRÓNICO:</b> {sheet.cell(cell3.row, cell3.col+1).value}\n"
                    f"<b>FECHA DE PAGO OPORTUNO:</b> {sheet.cell(cell3.row, cell3.col+3).value}\n"
                    f"<b>FECHA DE CORTE:</b> {sheet.cell(cell3.row, cell3.col+4).value}"   )
                
                time.sleep(1)
                break
            except ValueError:
                    update.message.reply_text("Oopss! ese no era un número válido, por favor ingresa sólo 4 números o envía /saltar si no lo recuerdas.")
                    time.sleep(1)
                    break
        #id = update.message.from_user.id
        bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
        bot.sendMessage(chat_id= id, parse_mode= "HTML", text="Espero la información brindada sea de ayuda, si tienes alguna inquietud no dudes en contactarnos, el comando /asesor te puede ayudar. ¡Tus amigos de <b>Netflix Colombia</b>!👋🏻\n\n/start para regresar al menú principal.")
    return ConversationHandler.END

def brarlynn_muñoz(update: Update, context: CallbackContext) -> int:

    query = update.callback_query
    query.answer()
    user = query.message.from_user
    logger.info(f'El usuario {user.first_name} {user.last_name}, ha escogido el perfil a nombre de Brarlynn Muñoz.')
    query.message.reply_text('Por motivos de seguridad para mirar la información de tu cuenta envíame el pin de 4 dígitos asociado a tu perfil.\n\n'
        "O envía /saltar si no lo recuerdas.",
        reply_markup=ReplyKeyboardRemove(),
        )
    return PIN_BRARLYNNM

def pin_brarlynnm(update: Update, context: CallbackContext) -> int:

    for i in range(1):          
        while True:
            try:
                pin = int(update.message.text)
                update.message.reply_text("El pin ingresado no corresponde al del perfil seleccionado.\n"
                "Inténtalo de nuevo o envía /saltar si no lo recuerdas.")
                if(pin == 4321):
                    cell3 = sheet.find("Brarlynn Muñoz")
                    id = update.message.from_user.id
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                    bot.sendMessage(chat_id= id, text="¡Espera... este pin sí lo reconozco!😁")
                    time.sleep(1)
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                    bot.sendMessage(chat_id= id, text="Esta es la información de tu cuenta: \n\n")
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)     
                    context.bot.sendMessage(chat_id= id, parse_mode= "HTML", text=
                    f"<b>ESTADO:</b> {sheet.cell(cell3.row, cell3.col-3).value}\n" 
                    f"<b>PLAN:</b> {sheet.cell(cell3.row, cell3.col-2).value}\n"    
                    f"<b>PRECIO:</b> ${sheet.cell(cell3.row, cell3.col-1).value} COP/mes\n"
                    f"<b>NOMBRE:</b> {sheet.cell(cell3.row, cell3.col).value}\n"
                    f"<b>CORREO ELECTRÓNICO:</b> {sheet.cell(cell3.row, cell3.col+1).value}\n"
                    f"<b>FECHA DE PAGO OPORTUNO:</b> {sheet.cell(cell3.row, cell3.col+3).value}\n"
                    f"<b>FECHA DE CORTE:</b> {sheet.cell(cell3.row, cell3.col+4).value}"   )
                
                time.sleep(1)
                break
            except ValueError:
                    update.message.reply_text("Oopss! ese no era un número válido, por favor ingresa sólo 4 números o envía /saltar si no lo recuerdas.")
                    time.sleep(1)
                    break
        #id = update.message.from_user.id
        bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
        bot.sendMessage(chat_id= id, parse_mode= "HTML", text="Espero la información brindada sea de ayuda, si tienes alguna inquietud no dudes en contactarnos, el comando /asesor te puede ayudar. ¡Tus amigos de <b>Netflix Colombia</b>!👋🏻\n\n/start para regresar al menú principal.")
    return ConversationHandler.END

def karen_fonseca(update: Update, context: CallbackContext) -> int:

    query = update.callback_query
    query.answer()
    user = query.message.from_user
    logger.info(f'El usuario {user.first_name} {user.last_name}, ha escogido el perfil a nombre de Karen Fonseca.')
    query.message.reply_text('Has escogido el perfil "Karen Fonseca" por motivos de seguridad para mirar la información de tu cuenta envíame el pin de 4 dígitos asociado a tu perfil.\n\n'
        "O envía /saltar si no lo recuerdas.",
        reply_markup=ReplyKeyboardRemove(),
        )
    return PIN_KARENF

def pin_karenf(update: Update, context: CallbackContext) -> int:

    for i in range(1):          
        while True:
            try:
                pin = int(update.message.text)
                update.message.reply_text("El pin ingresado no corresponde al del perfil seleccionado.\n"
                "Inténtalo de nuevo o envía /saltar si no lo recuerdas.")
                if(pin == 1797):
                    cell3 = sheet.find("Karen Fonseca")
                    id = update.message.from_user.id
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                    bot.sendMessage(chat_id= id, text="¡Espera... este pin sí lo reconozco!😁")
                    time.sleep(1)
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                    bot.sendMessage(chat_id= id, text="Esta es la información de tu cuenta: \n\n")
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)     
                    context.bot.sendMessage(chat_id= id, parse_mode= "HTML", text=
                    f"<b>ESTADO:</b> {sheet.cell(cell3.row, cell3.col-3).value}\n" 
                    f"<b>PLAN:</b> {sheet.cell(cell3.row, cell3.col-2).value}\n"    
                    f"<b>PRECIO:</b> ${sheet.cell(cell3.row, cell3.col-1).value} COP/mes\n"
                    f"<b>NOMBRE:</b> {sheet.cell(cell3.row, cell3.col).value}\n"
                    f"<b>CORREO ELECTRÓNICO:</b> {sheet.cell(cell3.row, cell3.col+1).value}\n"
                    f"<b>FECHA DE PAGO OPORTUNO:</b> {sheet.cell(cell3.row, cell3.col+3).value}\n"
                    f"<b>FECHA DE CORTE:</b> {sheet.cell(cell3.row, cell3.col+4).value}"   )
                
                time.sleep(1)
                break
            except ValueError:
                    update.message.reply_text("Oopss! ese no era un número válido, por favor ingresa sólo 4 números o envía /saltar si no lo recuerdas.")
                    time.sleep(1)
                    break
        #id = update.message.from_user.id
        bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
        bot.sendMessage(chat_id= id, parse_mode= "HTML", text="Espero la información brindada sea de ayuda, si tienes alguna inquietud no dudes en contactarnos, el comando /asesor te puede ayudar. ¡Tus amigos de <b>Netflix Colombia</b>!👋🏻\n\n/start para regresar al menú principal.")
    return ConversationHandler.END

def david_chavarriaga(update: Update, context: CallbackContext) -> int:

    query = update.callback_query
    query.answer()
    user = query.message.from_user
    logger.info(f'El usuario {user.first_name} {user.last_name}, ha escogido el perfil a nombre de David Chavarriaga Sepúlveda.')
    query.message.reply_text('Has escogido el perfil "David" por motivos de seguridad para mirar la información de tu cuenta envíame el pin de 4 dígitos asociado a tu perfil.\n\n'
        "O envía /saltar si no lo recuerdas.",
        reply_markup=ReplyKeyboardRemove(),
        )
    return PIN_DAVIDCHA

def pin_davidcha(update: Update, context: CallbackContext) -> int:

    for i in range(1):          
        while True:
            try:
                pin = int(update.message.text)
                update.message.reply_text("El pin ingresado no corresponde al del perfil seleccionado.\n"
                "Inténtalo de nuevo o envía /saltar si no lo recuerdas.")
                if(pin == 9669):
                    cell3 = sheet.find("David Chavarriaga Sepúlveda")
                    id = update.message.from_user.id
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                    bot.sendMessage(chat_id= id, text="¡Espera... este pin sí lo reconozco!😁")
                    time.sleep(1)
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                    bot.sendMessage(chat_id= id, text="Esta es la información de tu cuenta: \n\n")
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)     
                    context.bot.sendMessage(chat_id= id, parse_mode= "HTML", text=
                    f"<b>ESTADO:</b> {sheet.cell(cell3.row, cell3.col-3).value}\n" 
                    f"<b>PLAN:</b> {sheet.cell(cell3.row, cell3.col-2).value}\n"    
                    f"<b>PRECIO:</b> ${sheet.cell(cell3.row, cell3.col-1).value} COP/mes\n"
                    f"<b>NOMBRE:</b> {sheet.cell(cell3.row, cell3.col).value}\n"
                    f"<b>CORREO ELECTRÓNICO:</b> {sheet.cell(cell3.row, cell3.col+1).value}\n"
                    f"<b>FECHA DE PAGO OPORTUNO:</b> {sheet.cell(cell3.row, cell3.col+3).value}\n"
                    f"<b>FECHA DE CORTE:</b> {sheet.cell(cell3.row, cell3.col+4).value}"   )
                
                time.sleep(1)
                break
            except ValueError:
                    update.message.reply_text("Oopss! ese no era un número válido, por favor ingresa sólo 4 números o envía /saltar si no lo recuerdas.")
                    time.sleep(1)
                    break
        #id = update.message.from_user.id
        bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
        bot.sendMessage(chat_id= id, parse_mode= "HTML", text="Espero la información brindada sea de ayuda, si tienes alguna inquietud no dudes en contactarnos, el comando /asesor te puede ayudar. ¡Tus amigos de <b>Netflix Colombia</b>!👋🏻\n\n/start para regresar al menú principal.")
    return ConversationHandler.END

def clau_jimenez(update: Update, context: CallbackContext) -> int:

    query = update.callback_query
    query.answer()
    user = query.message.from_user
    logger.info(f'El usuario {user.first_name} {user.last_name}, ha escogido el perfil a nombre de Claudia Jiménez')
    query.message.reply_text('Has escogido el perfil "Clau Jiménez" por motivos de seguridad para mirar la información de tu cuenta envíame el pin de 4 dígitos asociado a tu perfil.\n\n'
        "O envía /saltar si no lo recuerdas.",
        reply_markup=ReplyKeyboardRemove(),
        )
    return PIN_CLAUJIMENEZ

def pin_claujimenez(update: Update, context: CallbackContext) -> int:

    for i in range(1):          
        while True:
            try:
                pin = int(update.message.text)
                update.message.reply_text("El pin ingresado no corresponde al del perfil seleccionado.\n"
                "Inténtalo de nuevo o envía /saltar si no lo recuerdas.")
                if(pin == 1454):
                    cell3 = sheet.find("Claudia Jiménez")
                    id = update.message.from_user.id
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                    bot.sendMessage(chat_id= id, text="¡Espera... este pin sí lo reconozco!😁")
                    time.sleep(1)
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                    bot.sendMessage(chat_id= id, text="Esta es la información de tu cuenta: \n\n")
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)     
                    context.bot.sendMessage(chat_id= id, parse_mode= "HTML", text=
                    f"<b>ESTADO:</b> {sheet.cell(cell3.row, cell3.col-3).value}\n" 
                    f"<b>PLAN:</b> {sheet.cell(cell3.row, cell3.col-2).value}\n"    
                    f"<b>PRECIO:</b> ${sheet.cell(cell3.row, cell3.col-1).value} COP/mes\n"
                    f"<b>NOMBRE:</b> {sheet.cell(cell3.row, cell3.col).value}\n"
                    f"<b>CORREO ELECTRÓNICO:</b> {sheet.cell(cell3.row, cell3.col+1).value}\n"
                    f"<b>FECHA DE PAGO OPORTUNO:</b> {sheet.cell(cell3.row, cell3.col+3).value}\n"
                    f"<b>FECHA DE CORTE:</b> {sheet.cell(cell3.row, cell3.col+4).value}"   )
                
                time.sleep(1)
                break
            except ValueError:
                    update.message.reply_text("Oopss! ese no era un número válido, por favor ingresa sólo 4 números o envía /saltar si no lo recuerdas.")
                    time.sleep(1)
                    break
        #id = update.message.from_user.id
        bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
        bot.sendMessage(chat_id= id, parse_mode= "HTML", text="Espero la información brindada sea de ayuda, si tienes alguna inquietud no dudes en contactarnos, el comando /asesor te puede ayudar. ¡Tus amigos de <b>Netflix Colombia</b>!👋🏻\n\n/start para regresar al menú principal.")
    return ConversationHandler.END

def yimar(update: Update, context: CallbackContext) -> int:

    query = update.callback_query
    query.answer()
    user = query.message.from_user
    logger.info(f'El usuario {user.first_name} {user.last_name}, ha escogido el perfil a nombre de Claudia Jiménez')
    query.message.reply_text('Has escogido el perfil "Yimar" por motivos de seguridad para mirar la información de tu cuenta envíame el pin de 4 dígitos asociado a tu perfil.\n\n'
        "O envía /saltar si no lo recuerdas.",
        reply_markup=ReplyKeyboardRemove(),
        )
    return PIN_YIMAR

def pin_yimar(update: Update, context: CallbackContext) -> int:

    for i in range(1):          
        while True:
            try:
                pin = int(update.message.text)
                update.message.reply_text("El pin ingresado no corresponde al del perfil seleccionado.\n"
                "Inténtalo de nuevo o envía /saltar si no lo recuerdas.")
                if(pin == 1308):
                    cell3 = sheet.find("Yimar (papá de brayan)")
                    id = update.message.from_user.id
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                    bot.sendMessage(chat_id= id, text="¡Espera... este pin sí lo reconozco!😁")
                    time.sleep(1)
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                    bot.sendMessage(chat_id= id, text="Esta es la información de tu cuenta: \n\n")
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)     
                    context.bot.sendMessage(chat_id= id, parse_mode= "HTML", text=
                    f"<b>ESTADO:</b> {sheet.cell(cell3.row, cell3.col-3).value}\n" 
                    f"<b>PLAN:</b> {sheet.cell(cell3.row, cell3.col-2).value}\n"    
                    f"<b>PRECIO:</b> ${sheet.cell(cell3.row, cell3.col-1).value} COP/mes\n"
                    f"<b>NOMBRE:</b> {sheet.cell(cell3.row, cell3.col).value}\n"
                    f"<b>CORREO ELECTRÓNICO:</b> {sheet.cell(cell3.row, cell3.col+1).value}\n"
                    f"<b>FECHA DE PAGO OPORTUNO:</b> {sheet.cell(cell3.row, cell3.col+3).value}\n"
                    f"<b>FECHA DE CORTE:</b> {sheet.cell(cell3.row, cell3.col+4).value}"   )
                
                time.sleep(1)
                break
            except ValueError:
                    update.message.reply_text("Oopss! ese no era un número válido, por favor ingresa sólo 4 números o envía /saltar si no lo recuerdas.")
                    time.sleep(1)
                    break
        #id = update.message.from_user.id
        bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
        bot.sendMessage(chat_id= id, parse_mode= "HTML", text="Espero la información brindada sea de ayuda, si tienes alguna inquietud no dudes en contactarnos, el comando /asesor te puede ayudar. ¡Tus amigos de <b>Netflix Colombia</b>!👋🏻\n\n/start para regresar al menú principal.")
    return ConversationHandler.END

def claudia_lopez(update: Update, context: CallbackContext) -> int:

    query = update.callback_query
    query.answer()
    user = query.message.from_user
    logger.info(f'El usuario {user.first_name} {user.last_name}, ha escogido el perfil a nombre de Claudia Jiménez')
    query.message.reply_text('Has escogido el perfil "Claudia López" por motivos de seguridad para mirar la información de tu cuenta envíame el pin de 4 dígitos asociado a tu perfil.\n\n'
        "O envía /saltar si no lo recuerdas.",
        reply_markup=ReplyKeyboardRemove(),
        )
    return PIN_CLAULOPEZ

def pin_claulopez(update: Update, context: CallbackContext) -> int:

    for i in range(1):          
        while True:
            try:
                pin = int(update.message.text)
                update.message.reply_text("El pin ingresado no corresponde al del perfil seleccionado.\n"
                "Inténtalo de nuevo o envía /saltar si no lo recuerdas.")
                if(pin == 518):
                    cell3 = sheet.find("Claudia López")
                    id = update.message.from_user.id
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                    bot.sendMessage(chat_id= id, text="¡Espera... este pin sí lo reconozco!😁")
                    time.sleep(1)
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                    bot.sendMessage(chat_id= id, text="Esta es la información de tu cuenta: \n\n")
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)     
                    context.bot.sendMessage(chat_id= id, parse_mode= "HTML", text=
                    f"<b>ESTADO:</b> {sheet.cell(cell3.row, cell3.col-3).value}\n" 
                    f"<b>PLAN:</b> {sheet.cell(cell3.row, cell3.col-2).value}\n"    
                    f"<b>PRECIO:</b> ${sheet.cell(cell3.row, cell3.col-1).value} COP/mes\n"
                    f"<b>NOMBRE:</b> {sheet.cell(cell3.row, cell3.col).value}\n"
                    f"<b>CORREO ELECTRÓNICO:</b> {sheet.cell(cell3.row, cell3.col+1).value}\n"
                    f"<b>FECHA DE PAGO OPORTUNO:</b> {sheet.cell(cell3.row, cell3.col+3).value}\n"
                    f"<b>FECHA DE CORTE:</b> {sheet.cell(cell3.row, cell3.col+4).value}"   )
                
                time.sleep(1)
                break
            except ValueError:
                    update.message.reply_text("Oopss! ese no era un número válido, por favor ingresa sólo 4 números o envía /saltar si no lo recuerdas.")
                    time.sleep(1)
                    break
        #id = update.message.from_user.id
        bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
        bot.sendMessage(chat_id= id, parse_mode= "HTML", text="Espero la información brindada sea de ayuda, si tienes alguna inquietud no dudes en contactarnos, el comando /asesor te puede ayudar. ¡Tus amigos de <b>Netflix Colombia</b>!👋🏻\n\n/start para regresar al menú principal.")
    return ConversationHandler.END

def diana_jimenez(update: Update, context: CallbackContext) -> int:

    query = update.callback_query
    query.answer()
    user = query.message.from_user
    logger.info(f'El usuario {user.first_name} {user.last_name}, ha escogido el perfil a nombre de Claudia Jiménez')
    query.message.reply_text('Has escogido el perfil "Diana Jiménez" por motivos de seguridad para mirar la información de tu cuenta envíame el pin de 4 dígitos asociado a tu perfil.\n\n'
        "O envía /saltar si no lo recuerdas.",
        reply_markup=ReplyKeyboardRemove(),
        )
    return PIN_DIANAJIMENEZ

def pin_dianajimenez(update: Update, context: CallbackContext) -> int:

    for i in range(1):          
        while True:
            try:
                pin = int(update.message.text)
                update.message.reply_text("El pin ingresado no corresponde al del perfil seleccionado.\n"
                "Inténtalo de nuevo o envía /saltar si no lo recuerdas.")
                if(pin == 3060):
                    cell3 = sheet.find("Diana Jiménez")
                    id = update.message.from_user.id
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                    bot.sendMessage(chat_id= id, text="¡Espera... este pin sí lo reconozco!😁")
                    time.sleep(1)
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                    bot.sendMessage(chat_id= id, text="Esta es la información de tu cuenta: \n\n")
                    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)     
                    context.bot.sendMessage(chat_id= id, parse_mode= "HTML", text=
                    f"<b>ESTADO:</b> {sheet.cell(cell3.row, cell3.col-3).value}\n" 
                    f"<b>PLAN:</b> {sheet.cell(cell3.row, cell3.col-2).value}\n"    
                    f"<b>PRECIO:</b> ${sheet.cell(cell3.row, cell3.col-1).value} COP/mes\n"
                    f"<b>NOMBRE:</b> {sheet.cell(cell3.row, cell3.col).value}\n"
                    f"<b>CORREO ELECTRÓNICO:</b> {sheet.cell(cell3.row, cell3.col+1).value}\n"
                    f"<b>FECHA DE PAGO OPORTUNO:</b> {sheet.cell(cell3.row, cell3.col+3).value}\n"
                    f"<b>FECHA DE CORTE:</b> {sheet.cell(cell3.row, cell3.col+4).value}"   )
                
                time.sleep(1)
                break
            except ValueError:
                    update.message.reply_text("Oopss! ese no era un número válido, por favor ingresa sólo 4 números o envía /saltar si no lo recuerdas.")
                    time.sleep(1)
                    break
        #id = update.message.from_user.id
        bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
        bot.sendMessage(chat_id= id, parse_mode= "HTML", text="Espero la información brindada sea de ayuda, si tienes alguna inquietud no dudes en contactarnos, el comando /asesor te puede ayudar. ¡Tus amigos de <b>Netflix Colombia</b>!👋🏻\n\n/start para regresar al menú principal.")
    return ConversationHandler.END

def manuela_montoya(update: Update, context: CallbackContext) -> int:

    query = update.callback_query
    query.answer()
    user = query.message.from_user
    logger.info(f'El usuario {user.first_name} {user.last_name}, ha escogido el perfil Daniela Acevedo.')
    query.message.reply_text("Has escogido el perfil Manuela, por motivos de seguridad para mirar la información de tu cuenta envíame el pin de 4 dígitos asociado a tu perfil.\n\n"
        "O envía /saltar si no lo recuerdas.",
        reply_markup=ReplyKeyboardRemove(),
        )
    
    return PIN_MANUELAMON

def pin_manuelamon(update: Update, context: CallbackContext) -> int:
              
    while True:
        try:
            pin = int(update.message.text)
            update.message.reply_text("El pin ingresado no corresponde al del perfil seleccionado.\n"
            "Inténtalo de nuevo o envía /saltar si no lo recuerdas.")
            if(pin == 0000):
                #print(pin)
                cell3 = sheet.find("Manuela Montoya Quintero")
                id = update.message.from_user.id
                bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                bot.sendMessage(chat_id= id, text="¡Espera... este pin sí lo reconozco!😁")
                time.sleep(1)
                bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                bot.sendMessage(chat_id= id, text="Esta es la información de tu cuenta: \n\n")
                bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)     
                context.bot.sendMessage(chat_id= id, parse_mode= "HTML", text=
                f"<b>ESTADO:</b> {sheet.cell(cell3.row, cell3.col-3).value}\n" 
                f"<b>PLAN:</b> {sheet.cell(cell3.row, cell3.col-2).value}\n"    
                f"<b>PRECIO:</b> ${sheet.cell(cell3.row, cell3.col-1).value} COP/mes\n"
                f"<b>NOMBRE:</b> {sheet.cell(cell3.row, cell3.col).value}\n"
                f"<b>CORREO ELECTRÓNICO:</b> {sheet.cell(cell3.row, cell3.col+1).value}\n"
                f"<b>FECHA DE PAGO OPORTUNO:</b> {sheet.cell(cell3.row, cell3.col+3).value}\n"
                f"<b>FECHA DE CORTE:</b> {sheet.cell(cell3.row, cell3.col+4).value}"   )
            
            time.sleep(1)
            break
            #time.sleep(1)
        except ValueError:
                update.message.reply_text("Oopss! ese no era un número válido, por favor ingresa sólo 4 números o envía /saltar si no lo recuerdas.")
                time.sleep(1)
                break
    #id = update.message.from_user.id
    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
    bot.sendMessage(chat_id= id, parse_mode= "HTML", text="Espero la información brindada sea de ayuda, si tienes alguna inquietud no dudes en contactarnos, el comando /asesor te puede ayudar. ¡Tus amigos de <b>Netflix Colombia</b>!👋🏻\n\n/start para regresar al menú principal.")
    return ConversationHandler.END

def mauro_patino(update: Update, context: CallbackContext) -> int:

    query = update.callback_query
    query.answer()
    user = query.message.from_user
    logger.info(f'El usuario {user.first_name} {user.last_name}, ha escogido el perfil Daniela Acevedo.')
    query.message.reply_text("Has escogido el perfil Berenice, por motivos de seguridad para mirar la información de tu cuenta envíame el pin de 4 dígitos asociado a tu perfil.\n\n"
        "O envía /saltar si no lo recuerdas.",
        reply_markup=ReplyKeyboardRemove(),
        )
    
    return PIN_MAUROPATINO

def pin_mauropatino(update: Update, context: CallbackContext) -> int:
              
    while True:
        try:
            pin = int(update.message.text)
            update.message.reply_text("El pin ingresado no corresponde al del perfil seleccionado.\n"
            "Inténtalo de nuevo o envía /saltar si no lo recuerdas.")
            if(pin == 1953):
                #print(pin)
                cell3 = sheet.find("Berenice (Mauro Patiño)")
                id = update.message.from_user.id
                bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                bot.sendMessage(chat_id= id, text="¡Espera... este pin sí lo reconozco!😁")
                time.sleep(1)
                bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                bot.sendMessage(chat_id= id, text="Esta es la información de tu cuenta: \n\n")
                bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)     
                context.bot.sendMessage(chat_id= id, parse_mode= "HTML", text=
                f"<b>ESTADO:</b> {sheet.cell(cell3.row, cell3.col-3).value}\n" 
                f"<b>PLAN:</b> {sheet.cell(cell3.row, cell3.col-2).value}\n"    
                f"<b>PRECIO:</b> ${sheet.cell(cell3.row, cell3.col-1).value} COP/mes\n"
                f"<b>NOMBRE:</b> {sheet.cell(cell3.row, cell3.col).value}\n"
                f"<b>CORREO ELECTRÓNICO:</b> {sheet.cell(cell3.row, cell3.col+1).value}\n"
                f"<b>FECHA DE PAGO OPORTUNO:</b> {sheet.cell(cell3.row, cell3.col+3).value}\n"
                f"<b>FECHA DE CORTE:</b> {sheet.cell(cell3.row, cell3.col+4).value}"   )
            
            time.sleep(1)
            break
            #time.sleep(1)
        except ValueError:
                update.message.reply_text("Oopss! ese no era un número válido, por favor ingresa sólo 4 números o envía /saltar si no lo recuerdas.")
                time.sleep(1)
                break
    #id = update.message.from_user.id
    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
    bot.sendMessage(chat_id= id, parse_mode= "HTML", text="Espero la información brindada sea de ayuda, si tienes alguna inquietud no dudes en contactarnos, el comando /asesor te puede ayudar. ¡Tus amigos de <b>Netflix Colombia</b>!👋🏻\n\n/start para regresar al menú principal.")
    return ConversationHandler.END

def henry_mosquera(update: Update, context: CallbackContext) -> int:

    query = update.callback_query
    query.answer()
    user = query.message.from_user
    logger.info(f'El usuario {user.first_name} {user.last_name}, ha escogido el perfil Henry Mosquera.')
    query.message.reply_text("Has escogido el perfil Henry, por motivos de seguridad para mirar la información de tu cuenta envíame el pin de 4 dígitos asociado a tu perfil.\n\n"
        "O envía /saltar si no lo recuerdas.",
        reply_markup=ReplyKeyboardRemove(),
        )
    
    return PIN_HENRYMOSQUERA

def pin_henrymosquera(update: Update, context: CallbackContext) -> int:
              
    while True:
        try:
            pin = int(update.message.text)
            update.message.reply_text("El pin ingresado no corresponde al del perfil seleccionado.\n"
            "Inténtalo de nuevo o envía /saltar si no lo recuerdas.")
            if(pin == 8423):
                #print(pin)
                cell3 = sheet.find("Henry Mosquera")
                id = update.message.from_user.id
                bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                bot.sendMessage(chat_id= id, text="¡Espera... este pin sí lo reconozco!😁")
                time.sleep(1)
                bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
                bot.sendMessage(chat_id= id, text="Esta es la información de tu cuenta: \n\n")
                bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)     
                context.bot.sendMessage(chat_id= id, parse_mode= "HTML", text=
                f"<b>ESTADO:</b> {sheet.cell(cell3.row, cell3.col-3).value}\n" 
                f"<b>PLAN:</b> {sheet.cell(cell3.row, cell3.col-2).value}\n"    
                f"<b>PRECIO:</b> ${sheet.cell(cell3.row, cell3.col-1).value} COP/mes\n"
                f"<b>NOMBRE:</b> {sheet.cell(cell3.row, cell3.col).value}\n"
                f"<b>CORREO ELECTRÓNICO:</b> {sheet.cell(cell3.row, cell3.col+1).value}\n"
                f"<b>FECHA DE PAGO OPORTUNO:</b> {sheet.cell(cell3.row, cell3.col+3).value}\n"
                f"<b>FECHA DE CORTE:</b> {sheet.cell(cell3.row, cell3.col+4).value}"   )
            
            time.sleep(1)
            break
            #time.sleep(1)
        except ValueError:
                update.message.reply_text("Oopss! ese no era un número válido, por favor ingresa sólo 4 números o envía /saltar si no lo recuerdas.")
                time.sleep(1)
                break
    #id = update.message.from_user.id
    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
    bot.sendMessage(chat_id= id, parse_mode= "HTML", text="Espero la información brindada sea de ayuda, si tienes alguna inquietud no dudes en contactarnos, el comando /asesor te puede ayudar. ¡Tus amigos de <b>Netflix Colombia</b>!👋🏻\n\n/start para regresar al menú principal.")
    return ConversationHandler.END

def saltar_pin(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    id = update.message.from_user.id
    logger.info("Usuario %s %s no envió pin.", user.first_name, user.last_name)
    context.bot.sendMessage(chat_id= id, parse_mode= "HTML", text=
        'Puedes intentarlo más tarde. El comando /ayuda te puede ser útil.\n'
         '¡Tus amigos de <b>Netflix Colombia</b>👋🏻!'
    )

    return ConversationHandler.END



def promociones(update: Update, context: CallbackContext) -> int:

    user = update.message.from_user
 
    logger.info(f'El usuario {user.first_name} {user.last_name}, ha seleccionado el comando /promociones.')
    id = update.message.chat_id

    update.message.reply_text(
        text='En esta sección encontrarás las promociones vigentes.\n\n'
    )
    with open('img/TarifasNetflixColombia2021.jpeg','rb') as photo_file:
     bot.sendChatAction(chat_id=id, action=ChatAction.UPLOAD_PHOTO, timeout=None)
     time.sleep(1)
     bot.sendPhoto(chat_id=id, photo=photo_file, caption='Tarifas Netflix Colombia 2021.')
     bot.sendChatAction(chat_id=id, action=ChatAction.TYPING, timeout=None)
     time.sleep(1)
     context.bot.sendMessage(chat_id=id, parse_mode='MarkdownV2',
     text="*Plan básico 1 pantalla SD:*\n✅ *3 meses:* $45\.000 COP\n✅ *6 meses:* $80\.000 COP\n✅ *12 meses:* $150\.000 COP\n\n"
     "*Plan estándar 2 pantallas HD:*\n✅ *3 meses:* $80\.000 COP\n✅ *6 meses:* $150\.000 COP\n✅ *12 meses:* $280\.000 COP\n\n"
     "*Plan premium 4 pantallas UHD:*\n✅ *3 meses:* $95\.000 COP\n✅ *6 meses:* $180\.000 COP\n✅ *12 meses:* $350\.000 COP\n"
    )
    with open('videos/netflix_gif.mp4','rb') as video_file:
     bot.sendChatAction(chat_id=id, action=ChatAction.TYPING, timeout=None)
     time.sleep(1)
     bot.sendMessage(chat_id=id, parse_mode= "HTML", text="Recuerda que el comando /pago te brindará la información necesaria para que realices tu compra.\n"
     "Atentamente, el equipo de <b>Netflix Colombia</b>👋🏻.")
     bot.sendChatAction(chat_id=id, action=ChatAction.TYPING, timeout=None)
     bot.send_video(chat_id=id, video=video_file, caption='@netflixcolombiabot', timeout=None)

    return ConversationHandler.END

def preguntas(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    id = update.message.from_user.id
    logger.info(f'El usuario {user.first_name}{user.last_name}({id}) ingresó el comando /preguntas')
    context.bot.sendMessage(chat_id= id, parse_mode="HTML", text= "En esta sección encontrarás las preguntas frecuentes que suelen hacerse los usuarios, espero te sirva. ☺️\n\n"
    "<b><i>(Envía sólo el número correspondiente a la pregunta)</i></b>\n\n"

    "<b>1.</b> ¿Por qué mi cuenta se canceló si ya realicé el pago?\n"
    "<b>2.</b> ¿Cómo y cuándo debo pagar mi cuenta?\n"
    "<b>3.</b> ¿Por qué me sale un aviso diciendo que quedan pocos días de membresía?\n"
    "<b>4.</b> ¿Cómo puedo saber si alguien más utiliza mi cuenta?\n"
    "<b>5.</b> ¿Cómo puedo cambiar la contraseña de mi cuenta de Netflix?\n"
    "<b>6.</b> ¿Puedo comprar una cuenta de Netflix y agregarle mi correo electrónico?\n"
    "<b>7.</b> ¿Sólo manejan cuentas de Netflix o también otras plataformas?\n"
    "<b>8.</b> ¿Manejan planes por varios meses?\n"
    "<b>9.</b> ¿Cómo puedo adquirir una cuenta?\n"
    "<b>10.</b> ¿Cuánto tiempo se tarda en activar mi cuenta una vez realizado el pago?\n"
    "<b>11.</b> ¿Dónde puedo enviar el comprobante de pago?\n"
    "<b>12.</b> ¿Cuál es la contraseña de mi cuenta de Netflix?\n"
    )
    # if(update.message.text.find("1") == 0):
    #     logger.info(f'El usuario {user.first_name} {user.last_name}, seleccionó la pregunta 1.')
    #     update.message.reply_text("<b>¿Por qué mi cuenta se canceló si ya realicé el pago?</b>\n"
    #     "R/ Hay que tener en cuenta que el método de pago de las cuentas varía y dependiendo de la fecha de "
    #     "vencimiento del mismo, la cuenta de Netflix puede inhabilitarse. Cabe aclarar que en la mayoría de los casos "
    #     "esta fecha de vencimiento en la información de pago es diferente a la fecha de pago oportuno del usuario.\n"
    #     "Pero no te preocupes, si realizaste el pago la membresía de tu cuenta de Netflix se restablecerá el mismo día automáticamente.\n\n"
    #     "¡Tus amigos de Netflix👋🏻!"
    #     )
    # if(update.message.text.find("2") == 0):
    #     logger.info(f'El usuario {user.first_name} {user.last_name}, seleccionó la pregunta 2.')
    #     update.message.reply_text("<b>¿Cómo y cuándo debo pagar mi cuenta?</b>\n"
    #     "R/ Recuerda que el pago puede ser por transferencia o consignación bancaria a una cuenta de "
    #     "ahorros Bancolombia, Nequi o Daviplata, el comando /pago te brindará la información necesaria para que realices tu pago. "
    #     "Para saber el estado de tu cuenta y los detalles de tu cuenta visita el comando /micuenta y sigue los pasos.\n"
    #     "Dicho comando te brindará la información necesaria de tu cuenta incluyendo la fecha de pago.\n\n"
    #     "¡Tus amigos de Netflix👋🏻!"
    #     )

    #return ConversationHandler.END

def asesor(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    id = update.message.from_user.id
    logger.info(f'El usuario {user.first_name} {user.last_name}({id}) ingresó el comando /asesor')
    
    buttonrestContra = InlineKeyboardButton(
        text='Necesito restablecer mi contraseña',
        url='https://www.netflix.com/co/LoginHelp'
    )

    buttonPayment = InlineKeyboardButton(
        text='Necesito actualizar mi forma de pago',
        url='https://www.netflix.com/co/YourAccountPayment'
    )

    bot.sendChatAction(chat_id=id, action=ChatAction.TYPING, timeout=None)
    time.sleep(1)
    context.bot.sendMessage(chat_id= id, parse_mode="HTML", text= f"¡Hola <b>{user.first_name}</b>! Espero te encuentres muy bien, Antes de chatear...\n\n"
     "Puedes resolver rápidamente algunos problemas habituales sin necesidad de recibir ayuda en directo:")
    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
    time.sleep(1)
    update.message.reply_text(
        'Escoge una opción\n\n',
        reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton(text='No encuentro una serie o película en Netflix', callback_data='opcion1')],
        [buttonrestContra],
        [buttonPayment],  
        [InlineKeyboardButton(text='¡Quiero hablar con un asesor!', callback_data='opcion4')]
        ]),
    )


def about(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    id = update.message.from_user.id
    logger.info(f'El usuario {user.first_name}{user.last_name}({id}) ingresó el comando /about')
    context.bot.sendMessage(chat_id= id, parse_mode="HTML", text= "Esta sección se encuentra en mantenimiento, estamos trabajando arduamente para mejorar su servicio.")
    time.sleep(1)
    with open('img/mantenimiento2.png','rb') as photo_file:
     bot.sendChatAction(chat_id=id, action=ChatAction.UPLOAD_PHOTO, timeout=None)
     time.sleep(1)
     bot.sendPhoto(chat_id=id, photo=photo_file, caption='Sección en mantenimiento.')
     bot.sendChatAction(chat_id=id, action=ChatAction.TYPING, timeout=None)
     time.sleep(1.5)
    update.message.reply_text("Por favor disculpe las molestias.\n\n"
    "/start para volver al menú principal.")

def ayuda(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    id = update.message.from_user.id
    logger.info(f'El usuario {user.first_name} {user.last_name}({id}) ingresó el comando /ayuda')
    
    buttonLogging = InlineKeyboardButton(
        text='Iniciar sesión',
        url='https://www.netflix.com/co/Login?nextpage=https%3A%2F%2Fhelp.netflix.com%2Fes-es%2F'
    )

    bot.sendChatAction(chat_id=id, action=ChatAction.TYPING, timeout=None)
    time.sleep(0.5)

    update.message.reply_text(parse_mode="HTML", text=f'¡Hola <b>{user.first_name}</b>! Espero te encuentres muy bien.\n'
        'Bienvenido(a) al <b>Centro de ayuda</b> de <b>Netflix Colombia</b>.\n\n'
        'Inicia sesión para obtener ayuda personalizada o mira los temas populares\n\n',
        reply_markup=InlineKeyboardMarkup([
        [buttonLogging],
        [InlineKeyboardButton(text='📋Cómo suscribirse a Netflix', callback_data='how_to_suscribe')],
        [InlineKeyboardButton(text='📋Planes y precios', callback_data='plans_and_prices')],
        [InlineKeyboardButton(text='📋No puedo iniciar sesión en Netflix', callback_data='i_cant_start')],
        [InlineKeyboardButton(text='Cómo comenzar', callback_data='how_to_start'), InlineKeyboardButton(text='No se puede ver', callback_data='it_cant_be_see')],
        [InlineKeyboardButton(text='Gestionar mi cuenta', callback_data='manage_account'), InlineKeyboardButton(text='Ver Netflix', callback_data='watch_netflix')],
        [InlineKeyboardButton(text='Enlaces rápidos', callback_data='quick_links'), InlineKeyboardButton(text='Artículos sugeridos', callback_data='suggested_articles')],
        [InlineKeyboardButton(text='Ir al menú principal', callback_data='inicio')]
        ])
    )


def help(update: Update, context: CallbackContext) -> int:
    
    query = update.callback_query
    query.answer()

    user =query.message.from_user
    id = query.message.chat_id
    logger.info(f'El usuario {user.first_name} {user.last_name} {id} ha ingresado al comando /ayuda.')

    buttonLogging = InlineKeyboardButton(
        text='Iniciar sesión',
        url='https://www.netflix.com/co/Login?nextpage=https%3A%2F%2Fhelp.netflix.com%2Fes-es%2F'
    )

    query.edit_message_text(parse_mode="HTML", text=f'¡Hola <b>{user.first_name}</b>! Espero te encuentres muy bien.\n'
    'Bienvenido(a) al <b>Centro de ayuda</b> de <b>Netflix Colombia</b>.\n\n'
        'Inicia sesión para obtener ayuda personalizada o mira los temas populares\n\n',
        reply_markup=InlineKeyboardMarkup([
        [buttonLogging],
        [InlineKeyboardButton(text='📋Cómo suscribirse a Netflix', callback_data='how_to_suscribe')],
        [InlineKeyboardButton(text='📋Planes y precios', callback_data='plans_and_prices')],
        [InlineKeyboardButton(text='📋No puedo iniciar sesión en Netflix', callback_data='i_cant_start')],
        [InlineKeyboardButton(text='Cómo comenzar', callback_data='how_to_start'), InlineKeyboardButton(text='No se puede ver', callback_data='it_cant_be_see')],
        [InlineKeyboardButton(text='Gestionar mi cuenta', callback_data='manage_account'), InlineKeyboardButton(text='Ver Netflix', callback_data='watch_netflix' )],
        [InlineKeyboardButton(text='Enlaces rápidos', callback_data='quick_links'), InlineKeyboardButton(text='Artículos sugeridos', callback_data='suggested_articles')],
        [InlineKeyboardButton(text='Ir al menú principal', callback_data='inicio')]
        ])
    )

    return ConversationHandler.END

def how_to_suscribe(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    user = query.message.from_user
    id = query.message.from_user.id
    logger.info(f'El usuario {user.first_name}{user.last_name}({id}) seleccionó el botón Cómo suscribirse a Netflix')

    buttonMoreInfo = InlineKeyboardButton(
        text='Más información sobre Netflix',
        url='https://help.netflix.com/es-es/node/412'
    )

    query.edit_message_text(
        parse_mode= "HTML", text='<b>Cómo suscribirse a Netflix</b>\n\n'
        'Únete a los millones de suscriptores de todo el mundo que disfrutan de acceso ilimitado a series, películas, documentales y otros contenidos premiados sin un solo anuncio.\n\n'
        'Como suscriptor de Netflix, se te cobrará una vez al mes en el día en que te suscribiste. Sin contratos, sin cargos por cancelación y sin compromisos. Tienes la flexibilidad de <a href="https://help.netflix.com/es-es/node/22" target="_self">cambiar de plan</a> o de <a href="https://help.netflix.com/es-es/node/407" target="_self">cancelar</a> la suscripción en línea en cualquier momento si decides que Netflix no es para ti.\n\n'
        '¡Suscribirse a una cuenta de Netflix es muy fácil! Realiza los pasos siguientes para tu plataforma.\n\n',
        reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton(text='Android', callback_data='android')],
        [InlineKeyboardButton(text='Ordenador', callback_data='ordenador')],
        [InlineKeyboardButton(text='iPhone, iPad o iPad touch', callback_data='iphone')],
        [InlineKeyboardButton(text='Smart TV y reproductores multimedia de contenido en streaming', callback_data='smartTV')],
        [InlineKeyboardButton(text='Decodificador', callback_data='decodificador')],
        [buttonMoreInfo],
        [InlineKeyboardButton(text='Atrás', callback_data='help')],
        [InlineKeyboardButton(text='Menú principal', callback_data='inicio')],
        ]),
    )

    return ConversationHandler.END

def android(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    user = query.message.from_user
    id = query.message.from_user.id
    logger.info(f'El usuario {user.first_name}{user.last_name} (ID:{id}) seleccionó el botón Android')

    buttonWhatIsNetflix = InlineKeyboardButton(
        text='Más información sobre Netflix',
        url='https://help.netflix.com/es-es/node/412'
    )

    query.edit_message_text(
        parse_mode= "HTML", text='<b>Android</b>\n\n'
        'Elige una de las siguientes opciones para suscribirte desde tu dispositivo Android:\n\n'
        '⏺Descarga la aplicación de Netflix de Google Play Store en un dispositivo con Android 5.0 o posterior.\n'
        '⏺Visita <a href="https://www.netflix.com/signup" target="_self">netflix.com/signup</a> desde un navegador móvil.\n\n'
        'Desde la aplicación de Netflix o en netflix.com puedes:\n\n'
        ' 1️⃣ Selecciona el plan ideal para ti. Puedes cambiar a un plan inferior o superior cuando quieras.\n'
        ' 2️⃣ Crea una cuenta introduciendo tu dirección de correo y creando una contraseña.\n'
        ' 3️⃣ Introduce un método de pago.\n'
        ' 4️⃣ Eso es todo. ¡Y reproduce en streaming!\n\n'
        '¿Te ha resultado útil este artículo?\n\n',
        reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton(text='Sí', callback_data='answer_yes'),InlineKeyboardButton(text='No', callback_data='answer_not')],
        [buttonWhatIsNetflix],
        [InlineKeyboardButton(text='Atrás', callback_data='how_to_suscribe')],
        [InlineKeyboardButton(text='Menú principal', callback_data='inicio')],
        ]),
    )

    return ConversationHandler.END

def ordenador(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    user = query.message.from_user
    id = query.message.from_user.id
    logger.info(f'El usuario {user.first_name}{user.last_name} (ID:{id}) seleccionó el botón Ordenador')

    buttonWhatIsNetflix = InlineKeyboardButton(
        text='Más información sobre Netflix',
        url='https://help.netflix.com/es-es/node/412'
    )

    query.edit_message_text(
        parse_mode= "HTML", text='<b>Ordenador</b>\n\n'
        '1️⃣ Visita <a href="https://www.netflix.com/signup" target="_self">netflix.com/signup</a>.\n'
        '2️⃣ Selecciona el plan ideal para ti. Puedes cambiar a un plan inferior o superior cuando quieras.\n'
        '3️⃣ Crea una cuenta introduciendo tu dirección de correo y creando una contraseña.\n'
        '4️⃣ Introduce un método de pago.\n'
        '5️⃣ Eso es todo. ¡Y reproduce en streaming!\n\n'
        '¿Te ha resultado útil este artículo?\n\n',
        reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton(text='Sí', callback_data='answer_yes'),InlineKeyboardButton(text='No', callback_data='answer_not')],
        [buttonWhatIsNetflix],
        [InlineKeyboardButton(text='Atrás', callback_data='how_to_suscribe')],
        [InlineKeyboardButton(text='Menú principal', callback_data='inicio')],
        ]),
    )

    return ConversationHandler.END

def iphone(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    user = query.message.from_user
    id = query.message.from_user.id
    logger.info(f'El usuario {user.first_name}{user.last_name} (ID:{id}) seleccionó el botón iPhone, iPad...')

    buttonWhatIsNetflix = InlineKeyboardButton(
        text='Más información sobre Netflix',
        url='https://help.netflix.com/es-es/node/412'
    )

    query.edit_message_text(
        parse_mode= "HTML", text='<b>iPhone, iPad o iPod touch</b>\n\n'
        '1️⃣ Visita <a href="https://www.netflix.com/signup" target="_self">netflix.com/signup</a> desde un navegador móvil.\n\n'
        '    ⚠️<b>Nota:</b> No se admite la suscripción a través de la aplicación de Netflix para iOS.\n\n'
        '2️⃣ Selecciona el plan ideal para ti. Puedes cambiar a un plan inferior o superior cuando quieras.\n'
        '3️⃣ Crea una cuenta introduciendo tu dirección de correo y creando una contraseña.\n'
        '4️⃣ Introduce un método de pago.\n'
        '5️⃣ Descarga e inicia sesión en la aplicación de Netflix en un dispositivo con iOS 13.0 o posterior.\n'
        '6️⃣ Eso es todo. ¡Y reproduce en streaming!\n\n'
        '¿Te ha resultado útil este artículo?\n\n',
        reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton(text='Sí', callback_data='answer_yes'),InlineKeyboardButton(text='No', callback_data='answer_not')],
        [buttonWhatIsNetflix],
        [InlineKeyboardButton(text='Atrás', callback_data='how_to_suscribe')],
        [InlineKeyboardButton(text='Menú principal', callback_data='inicio')],
        ]),
    )

    return ConversationHandler.END

def smartTV(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    user = query.message.from_user
    id = query.message.from_user.id
    logger.info(f'El usuario {user.first_name}{user.last_name} (ID:{id}) seleccionó el botón smart TV y reproductores multimedia.')

    buttonWhatIsNetflix = InlineKeyboardButton(
        text='Más información sobre Netflix',
        url='https://help.netflix.com/es-es/node/412'
    )

    query.edit_message_text(
        parse_mode= "HTML", text='<b>Smart TV y reproductores multimedia de contenido en streaming</b>\n\n'
        '1️⃣ Abre la aplicación de Netflix.\n\n'
        '    ⚠️ <b>Nota:</b> Si necesitas ayuda para encontrar la aplicación, busca en nuestro <a href="https://help.netflix.com/es-es/" target="_self">Centro de ayuda</a> el artículo '
        '«Cómo usar Netflix en», seguido de la marca de tu dispositivo (p. ej., Samsung, Roku, Xbox). Algunos dispositivos también incluyen un botón Netflix en el mando a distancia.\n\n'
        '2️⃣ En la mayoría de Smart TVs y reproductores multimedia de contenido en streaming tendrás que empezar por facilitar tu dirección de correo electrónico o tu número de teléfono.\n\n'
        '    🔘 Una vez facilitado, recibirás un correo o un SMS con un enlace de activación que te permitirá seguir con el proceso de suscripción.\n\n'
        '3️⃣ Selecciona el plan ideal para ti. Puedes cambiar a un plan inferior o superior cuando quieras.\n'
        '4️⃣ Crea una cuenta introduciendo tu dirección de correo y creando una contraseña.\n'
        '5️⃣ Introduce un método de pago.\n'
        '6️⃣ Eso es todo. ¡Y reproduce en streaming!\n\n'
        '¿Te ha resultado útil este artículo?\n\n',
        reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton(text='Sí', callback_data='answer_yes'),InlineKeyboardButton(text='No', callback_data='answer_not')],
        [buttonWhatIsNetflix],
        [InlineKeyboardButton(text='Atrás', callback_data='how_to_suscribe')],
        [InlineKeyboardButton(text='Menú principal', callback_data='inicio')],
        ]),
    )

    return ConversationHandler.END

def decodificador(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    user = query.message.from_user
    id = query.message.from_user.id
    logger.info(f'El usuario {user.first_name}{user.last_name} (ID:{id}) seleccionó el botón Decodificador')

    buttonWhatIsNetflix = InlineKeyboardButton(
        text='Más información sobre Netflix',
        url='https://help.netflix.com/es-es/node/412'
    )

    query.edit_message_text(
        parse_mode= "HTML", text='<b>Decodificador</b>\n\n'
        '1️⃣ Abre la aplicación de Netflix.\n\n'
        '    ⚠️ <b>Nota:</b> Si necesitas ayuda para encontrar la aplicación, busca en nuestro <a href="https://help.netflix.com/es-es/" target="_self">Centro de ayuda</a> el artículo '
        '«Cómo usar Netflix en», seguido de la marca de tu dispositivo (p. ej., Samsung, Roku, Xbox). Algunos dispositivos también incluyen un botón Netflix en el mando a distancia.\n\n'
        '2️⃣ Selecciona el plan ideal para ti. Puedes cambiar a un plan inferior o superior cuando quieras.\n'
        '3️⃣ Crea una cuenta introduciendo tu dirección de correo y creando una contraseña.\n'
        '4️⃣ Introduce un método de pago.\n'
        '5️⃣ Eso es todo. ¡Y reproduce en streaming!\n\n'
        '¿Te ha resultado útil este artículo?\n\n',
        reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton(text='Sí', callback_data='answer_yes'),InlineKeyboardButton(text='No', callback_data='answer_not')],
        [buttonWhatIsNetflix],
        [InlineKeyboardButton(text='Atrás', callback_data='how_to_suscribe')],
        [InlineKeyboardButton(text='Menú principal', callback_data='inicio')],
        ]),
    )

    return ConversationHandler.END

def answer_yes(update: Update, context: CallbackContext) -> int:

    query = update.callback_query
    query.answer()
    user = query.message.from_user
    id = query.message.chat_id
    logger.info(f'El usuario {user.first_name} {user.last_name} {id} ingresó a la sección de artículo útil.')

    query.edit_message_text(parse_mode='HTML', text='<b>¡Gracias por tus comentarios!</b>\n\n' 
    '<b>¿Tienes alguna sugerencia que nos ayude a seguir mejorando? (Opcional)</b>\n'
    '<i><b>Nota:</b> No respondemos a comentarios individuales. No dejes datos personales.</i>\n\n'
    'Por favor escríbenos tus comentarios o envía /saltar si prefieres omitir este paso.')

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
        [InlineKeyboardButton(text='Volver al menú principal', callback_data='inicio')]
        ])
        )

    context.bot.sendMessage(chat_id='1587610512', parse_mode="HTML", text=f"<b>El usuario {user_name} {user_last} ID: {user_id} ha indicado que le ha sido útil el artículo, el comentario descrito por el usuario es:</b> {suggesting}")

    return ConversationHandler.END

def answer_not(update: Update, context: CallbackContext) -> int:

    query = update.callback_query
    query.answer()
    user = query.message.from_user
    id = query.message.chat_id
    logger.info(f'El usuario {user.first_name} {user.last_name} {id} indicóque no le fue útil el artículo.')

    query.edit_message_text(parse_mode='HTML', text='<b>¿Qué ha fallado? (Opcional)</b>\n\n'
    '<i><b>Nota:</b> Dinos cómo podemos mejorar. No respondemos a comentarios individuales. No dejes datos personales.</i>\n\n'
    'Por favor escríbenos tus comentarios o envía /saltar si prefieres omitir este paso.')

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
        [InlineKeyboardButton(text='menú principal', callback_data='inicio')]
        ])
        )

    context.bot.sendMessage(chat_id='1587610512', parse_mode="HTML", text=f"<b>El usuario {user_name} {user_last} ID: {user_id} ha indicado que no le ha sido útil el artículo, la sugerencia descrita por el usuario es:</b> {suggesting2}")

    return ConversationHandler.END

def saltar_suggesting(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    id = update.message.from_user.id
    logger.info("Usuario %s %s no envió sugerencia.", user.first_name, user.last_name)
    update.message.reply_text(parse_mode="HTML",
        text=f"Espero te haya sido útil el artículo, recuerda que para nosotros siempre es un placer atenderte.\n\n"
        '¡El equipo de <b>Netflix Colombia</b>👋🏻!',
        reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton(text='menú principal', callback_data='inicio')]
        ])
        )

    return ConversationHandler.END

def plans_and_prices(update: Update, context:CallbackContext) -> int:

    query = update.callback_query
    query.answer()

    user =query.message.from_user
    id = query.message.chat_id
    logger.info(f'El usuario {user.first_name} {user.last_name} {id} ha ingresado al comando /ayuda y seleccionado el botón Planes y precios.')

    buttonWhatIsNetflix = InlineKeyboardButton(
        text='Más información sobre Netflix',
        url='https://help.netflix.com/es-es/node/412'
    )

    query.edit_message_text(parse_mode='HTML', text='Viendo información en este momento exclusívamente para <b>COLOMBIA</b>.\n\n'
    '<b>Planes y precios</b>\n\n'
    'Netflix ofrece varios planes para que elijas el más adecuado. El plan que elijas determinará la cantidad de dispositivos en los que puedes ver Netflix <b>al mismo tiempo</b>.\n\n'
    'Con todos nuestros planes, puedes descargar la aplicación de Netflix en tus dispositivos favoritos y ver películas y series ilimitadas.\n\n'
    )
    with open('img/preciosNetflixCol2021.jpg', 'rb') as PlansPrices:
     bot.sendChatAction(chat_id=id, action=ChatAction.UPLOAD_PHOTO, timeout=None)
     time.sleep(1)
     bot.sendPhoto(chat_id= id, photo= PlansPrices, caption='Planes y precios')
     bot.sendChatAction(chat_id= id, action=ChatAction.TYPING, timeout=None)
     time.sleep(1)
     bot.sendMessage(chat_id= id, parse_mode="HTML",text='Suscríbete a Netflix Colombia hoy y selecciona entre varias opciones de pago. Como miembro de Netflix, se te cobrará una vez por mes en la fecha de suscripción. Tienes total libertad para cambiar de plan o cancelar el servicio online en cualquier momento.\n\n'
     '    ⚠️<b>Nota:</b> *Según el lugar en el que vivas, <a href="https://help.netflix.com/es/node/50068" target="_self">es posible que se te cobren impuestos</a>, además del precio de la suscripción.'
     )
     bot.sendChatAction(chat_id= id, action=ChatAction.TYPING, timeout=None)
     time.sleep(0.5)
    query.message.reply_text(
        parse_mode= "HTML", text=
        '¿Te ha resultado útil este artículo?\n\n',
        reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton(text='Sí', callback_data='answer_yes'),InlineKeyboardButton(text='No', callback_data='answer_not')],
        [buttonWhatIsNetflix],
        [InlineKeyboardButton(text='Atrás', callback_data='help')],
        [InlineKeyboardButton(text='Menú principal', callback_data='inicio')],
        ]),
    )

    return ConversationHandler.END

def i_cant_start(update: Update, context:CallbackContext) -> int:

    query = update.callback_query
    query.answer()

    user =query.message.from_user
    id = query.message.chat_id
    logger.info(f'El usuario {user.first_name}{user.last_name}({id}) ingresó al comando /ayuda y seleccionó el botón "No puedo iniciar sesión en Netflix".')


    query.edit_message_text(parse_mode='HTML', text='<b>No se puede iniciar sesión en Netflix</b>\n\n'
    'Si olvidaste tu email o contraseña de inicio de sesión de Netflix, o no tienes acceso a estos datos, puedes <a href="https://www.netflix.com/loginhelp" target="_blank">restablecer la contraseña.</a>\n\n'
    'Si conoces el email y la contraseña de la cuenta de Netflix, pero no puedes iniciar sesión, sigue las instrucciones de la sección que corresponda a continuación.\n\n'
    '<b>No es posible iniciar sesión en ningún dispositivo</b>\n'
    'Aparece este error cuando intentas iniciar sesión con una cuenta existente:\n'
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
        '<b>2.</b> Selecciona <b>No me acuerdo de mi email ni de mi teléfono</b> y completa el formulario.\n'
        '  ⚠️Sino ves esta opción, esto significa que la recuperación de la cuenta mediante la información de facturación no está disponible en tu país.\n'
        '<b>3.</b> Selecciona <b>Encontrar cuenta</b>.\n\n'
        'Si te facturamos a través de otra compañía o tienes Netflix como parte de un paquete, busca el nombre del proveedor de servicios en el <a href="https://help.netflix.com/" target="_blank">Centro de ayuda</a> de Netflix. Selecciona el artículo de facturación relacionado y ve a la sección "Tengo problemas para iniciar sesión en Netflix".\n'
        '<b>4.</b> Si seguiste los pasos indicados más arriba y sigues sin poder iniciar sesión, comunícate con el <b>Servicio al Cliente de Netflix</b> y habla con uno de nuestros asesores con el comando /asesor.\n\n\n'
        '<b>No se puede iniciar sesión en un dispositivo específico</b>',
        reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton(text='Reproductor de Blue-ray', callback_data='blue_ray')],
        [InlineKeyboardButton(text='Computadoras', callback_data='laptops')],
        [InlineKeyboardButton(text='Tablet o teléfono móvil', callback_data='cellphone')],
        [InlineKeyboardButton(text='Reproductor multimedia o decodificador', callback_data='decoder')],
        [InlineKeyboardButton(text='Smart TV', callback_data='smarTV')],
        [InlineKeyboardButton(text='Consola de videojuegos', callback_data='videogame_console')],
        [InlineKeyboardButton(text='Todos los demás dispositivos', callback_data='another_devices')],
        [InlineKeyboardButton(text='Atrás', callback_data='help')],
        [InlineKeyboardButton(text='Menú principal', callback_data='inicio')],
        ]),
    )

    return ConversationHandler.END

def blue_ray(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    user = query.message.from_user
    id = query.message.from_user.id
    logger.info(f'El usuario {user.first_name}{user.last_name}({id}) seleccionó el botón Blue-ray')

    buttonMoreInfo = InlineKeyboardButton(
        text='Más información sobre Netflix',
        url='https://help.netflix.com/es-es/node/412'
    )

    query.edit_message_text(
        parse_mode= "HTML", text='Pasos para inicio de sesión en Reproductor de Blue-ray',
        reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton(text='Verificar el email y la contraseña', callback_data='check_email')],
        [InlineKeyboardButton(text='Restablecer tu contraseña', callback_data='restore_password')],
        [InlineKeyboardButton(text='iniciar sesión con netflix.com/tv8', callback_data='tv8')],
        [InlineKeyboardButton(text='Restablecer Netflix', callback_data='restore_netflix')],
        [InlineKeyboardButton(text='Reinicia tu dispositivo', callback_data='restart_device')],
        [InlineKeyboardButton(text='Reinicia la red doméstica', callback_data='restart_network')],
        [InlineKeyboardButton(text='Mejora la calidad de tu señal de wifi', callback_data='wifi_signal')],
        [InlineKeyboardButton(text='Conecta el reproductor de Blue-ray al módem', callback_data='blue_ray_to_modem')],
        [InlineKeyboardButton(text='Restablecer configuración de conexión predeterminada', callback_data='restart_config_network')],
        [InlineKeyboardButton(text='Qué hacer a continuación', callback_data='what_i_have_to_do')],
        [buttonMoreInfo],
        [InlineKeyboardButton(text='Atrás', callback_data='i_cant_start')],
        [InlineKeyboardButton(text='Menú principal', callback_data='inicio')],
        ]),
    )

    return ConversationHandler.END

def check_email(update:Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    user = query.message.from_user
    id = query.message.from_user.id
    logger.info(f'El usuario ha ingresado al comando /ayuda, seleccionado el notón "No puedo iniciar sesión en Netflix", ingresó al botón "Reproductor de Blue-ray" y luego al botón "Verificar email y la contraseña"')

    query.edit_message_text(parse_mode='HTML', text='<b>Verificar el email y la contraseña</b>\n\n'
    'Confirma que hayas ingresado el email y la contraseña correctos antes de intentar iniciar sesión nuevamente. Si estás usando el control remoto para iniciar sesión, puedes volver a la pantalla de ingreso de la dirección de email para verificar a actualizar esta información. Si aún no puedes iniciar sesión, sigue el procedimiento de resolución de problemas, comunícate con el Servicio al <b>Cliente de Netflix Colombia.</b>',
    reply_markup=InlineKeyboardMarkup([ 
        [InlineKeyboardButton(text='Servicio al Cliente de Netflix Colombia', callback_data='customer_service')],
        [InlineKeyboardButton(text='Atrás', callback_data='blue_ray')],
        [InlineKeyboardButton(text='Menú principal', callback_data='inicio')]
    ])   
    )

def restore_password(update:Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    user = query.message.from_user
    id = query.message.from_user.id
    logger.info(f'El usuario ha ingresado al comando /ayuda, seleccionado el notón "No puedo iniciar sesión en Netflix", ingresó al botón "Reproductor de Blue-ray" y luego al botón "Restablecer contraseña"')

    query.edit_message_text(parse_mode='HTML', text='<b>Restablecer la contraseña</b>\n\n'
    'Para restablecer la contraseña, <a href="https://www.netflix.com/LoginHelp" target="_blank">envíate un email de restablecimiento de la contraseña</a>. Si anteriormente agregaste un número de teléfono verificado a tu cuenta, también puedes restablecer la contraseña por mensaje de texto (SMS) haciendo clic en <a href="https://www.netflix.com/LoginHelp" target="_blank">¿Olvidaste tu contraseña?</a> y seleccionando la opción de mensaje de texto (SMS). \n\n Si aún no puedes iniciar sesión, sigue el procedimiento de resolución de problemas, comunícate con el Servicio al <b>Cliente de Netflix Colombia.</b>',
    reply_markup=InlineKeyboardMarkup([ 
        [InlineKeyboardButton(text='Servicio al Cliente de Netflix Colombia', callback_data='customer_service')],
        [InlineKeyboardButton(text='Atrás', callback_data='blue_ray')],
        [InlineKeyboardButton(text='Menú principal', callback_data='inicio')]
    ])   
    )

def tv8(update:Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    user = query.message.from_user
    id = query.message.from_user.id
    logger.info(f'El usuario ha ingresado al comando /ayuda, seleccionado el notón "No puedo iniciar sesión en Netflix", ingresó al botón "Reproductor de Blue-ray" y luego al botón "Iniciar sesión con netflix.com/tv8"')

    query.edit_message_text(parse_mode='HTML', text='<b>Iniciar sesión con netflix.com/tv8</b>\n\n'
    'Si seleccionaste la opción de <b>inicio de sesión desde la Web</b>, usarás otro dispositivo para iniciar sesión y ver en tu TV en lugar del control remoto.\n\n'
    '  <b>1.</b> En tu computadora o dispositivo móvil, ve a netflix.com/tv8.\n'
    '  <b>2.</b> Ingresa el código que aparece en tu TV.\n'
    '    ✅ Verifica que el código que ingresaste coincida con el de tu TV en <b>Paso 2: Ingresar código de inicio de sesión</b>.\n'
    '  <b>3.</b> Si se te solicita, ingresa tu email y contraseña de Netflix.\n'
    '  <b>4.</b> Ver Netflix en tu TV.\n\n'
    '<b>Cómo usar el código QR</b>.\n\n'
    '  <b>1.</b> Apunta la cámara de tu teléfono o tablet al código QR de la pantalla de la TV.\n'
    '  <b>2.</b> Toca el banner que aparece para abrir netflix.com/tv8 en el navegador de tu móvil.\n'
    '  <b>3.</b> En el navegador de tu móvil, ingresa el código que aparece en tu TV.\n'
    '    ✅ Verifica que el código que ingresaste coincida con el de tu TV en <b>Paso 2: Ingresar código de inicio de sesión</b>.\n'
    '  <b>4.</b> Si se te solicita, ingresa tu email y contraseña de Netflix.\n'
    '  <b>5.</b> Ver Netflix en tu TV.',
    reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton(text='Atrás', callback_data='blue_ray')],
        [InlineKeyboardButton(text='Menú principal', callback_data='inicio')]
    ])   
    )

def restore_netflix(update:Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    user = query.message.from_user
    id = query.message.from_user.id
    logger.info(f'El usuario ha ingresado al comando /ayuda, seleccionado el notón "No puedo iniciar sesión en Netflix", ingresó al botón "Reproductor de Blue-ray" y luego al botón "Restablecer Netflix"')

    query.edit_message_text(parse_mode='HTML', text='<b>Restablecer Netflix</b>\n\n'
    '  <b>1.</b> Ve a la pantalla de cierre de sesión:\n'
    '    ✅ Si aún estás en la pantalla de error, selecciona <b>Más información</b> o <b>Más detalles</b>.\n'
    '    ✅ En la pantalla de inicio de Netflix, selecciona <b>Configuración</b> o el ícono <b>Configuración⚙️</b>.\n'
    '    ✅ Si estás en otra pantalla, ejecuta los siguientes comandos de '
    '    flecha en tu control remoto: <b>Arriba</b>, <b>Arriba</b>, <b>Abajo</b>, <b>Abajo</b>, <b>Izquierda</b>, <b>Derecha</b>, <b>Izquierda</b>, <b>Derecha</b>, <b>Arriba</b>, <b>Arriba</b>, <b>Arriba</b>, <b>Arriba</b>.\n'
    '  <b>2.</b> En la pantalla de cierre de sesión, selecciona <b>Restablecer</b>.\n'
    '    ✅ Si no ves <b>Restablecer</b>, selecciona <b>Cerrar sesión</b> o <b>Desactivar</b>.\n'
    '  <b>3.</b> Una vez que cierres sesión, vuelve a iniciar sesión y prueba Netflix nuevamente.\n',
    reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton(text='Atrás', callback_data='blue_ray')],
        [InlineKeyboardButton(text='Menú principal', callback_data='inicio')]
    ])   
    )

def restart_device(update:Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    user = query.message.from_user
    id = query.message.from_user.id
    logger.info(f'El usuario ha ingresado al comando /ayuda, seleccionado el notón "No puedo iniciar sesión en Netflix", ingresó al botón "Reproductor de Blue-ray" y luego al botón "Reinicia tu dispositivo"')

    query.edit_message_text(parse_mode='HTML', text='<b>Reinicia tu dispositivo</b>\n\n'
    '  <b>1.</b> Desconecta el dispositivo de la alimentación durante al menos 1 minuto.\n'
    '  <b>2.</b> Con el dispositivo desconectado, presiona el botón de encendido del dispositivo para descargarlo.\n'
    '    ✅ Si no puedes acceder al botón de encendido o tu dispositivo no tiene uno, deja el dispositivo desconectado durante al menos 3 minutos.\n'
    '  <b>3.</b> Vuelve a conectar tu dispositivo.\n'
    '  <b>4.</b> Enciende el dispositivo.\n\n'
    '  <b>5.</b> Vuelve a probar Netflix.',
    reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton(text='Atrás', callback_data='blue_ray')],
        [InlineKeyboardButton(text='Menú principal', callback_data='inicio')]
    ])
    )

def restart_network(update: Update, context:CallbackContext) -> int:

    query = update.callback_query
    query.answer()

    user =query.message.from_user
    id = query.message.chat_id
    logger.info(f'El usuario {user.first_name}{user.last_name}({id}) ha ingresado al comando /ayuda, seleccionado el notón "No puedo iniciar sesión en Netflix", ingresó al botón "Reproductor de Blue-ray" y luego al botón "Reinicia la red doméstica".')


    query.edit_message_text(parse_mode='HTML', text='<b>Reinicia la red doméstica</b>\n\n'
    )
    with open("img/blue-ray1.png", 'rb') as blue_ray_1:
     bot.sendChatAction(chat_id=id, action=ChatAction.UPLOAD_PHOTO, timeout=None)
     time.sleep(1)
     bot.sendPhoto(chat_id= id, photo= blue_ray_1, caption="1. Apaga o desconecta el reproductor de Blu-ray.")
    with open("img/unpplugin-modem.png", 'rb') as modem:
     bot.sendChatAction(chat_id=id, action=ChatAction.UPLOAD_PHOTO, timeout=None)
     time.sleep(1)
     bot.sendPhoto(chat_id= id, photo= modem, caption="2. Desconecta el módem (y el enrutador inalámbrico, si se trata de un dispositivo independiente) de la alimentación eléctrica durante al menos 30 segundos.")
    with open("img/connect-modem.png", 'rb') as connect:
     bot.sendChatAction(chat_id=id, action=ChatAction.UPLOAD_PHOTO, timeout=None)
     time.sleep(1)
     bot.sendPhoto(chat_id= id, photo= connect, caption="3. Conecta el módem y espera hasta que todas las luces indicadoras estén encendidas y hayan dejado de parpadear. Si el enrutador es independiente del módem, conéctalo y espera hasta que todas las luces indicadoras hayan dejado de parpadear.")
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
        [InlineKeyboardButton(text='Atrás', callback_data='blue_ray')],
        [InlineKeyboardButton(text='Menú principal', callback_data='inicio')],
        ]),
    )

    return ConversationHandler.END

def signal_wifi(update:Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    user = query.message.from_user
    id = query.message.from_user.id
    logger.info(f'El usuario {user.first_name} {user.last_name}, ha ingresado al comando /ayuda, seleccionado el notón "No puedo iniciar sesión en Netflix", ingresó al botón "Reproductor de Blue-ray" y luego al botón "Mejora la calidad de tu señal de wifi"')

    query.edit_message_text(parse_mode='HTML', text='<b>Mejora la calidad de tu señal de wifi</b>\n\n'
    'Si estás conectándote a través de una red wifi, y los pasos anteriores no resuelven el problema, sigue estas sugerencias:\n\n'
    '    ➡️ Si no puedes acceder al botón de encendido o tu dispositivo no tiene uno, deja el dispositivo desconectado durante al menos 3 minutos.\n'
    '  <b>3.</b> Vuelve a conectar tu dispositivo.\n'
    '  <b>4.</b> Enciende el dispositivo.\n\n'
    '  <b>5.</b> Vuelve a probar Netflix.',
    reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton(text='Atrás', callback_data='blue_ray')],
        [InlineKeyboardButton(text='Menú principal', callback_data='inicio')]
    ])
    )

def how_to_start(update:Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    user = query.message.from_user
    id = query.message.from_user.id
    logger.info(f'El usuario ha ingresado al comando /ayuda y seleccionado el botón "Cómo comenzar".')

    query.edit_message_text(parse_mode='HTML', text='<b>Cómo comenzar</b>\n\n'
    '➡️ <a href="https://help.netflix.com/es-es/node/412?ui_action=kb-article-popular-categories" target="_self">¿Qué es Netflix?</a>\n\n'
    '➡️ <a href="https://help.netflix.com/es-es/node/116380?ui_action=kb-article-popular-categories" target="_self">¿Cómo pagar Netflix?</a>\n\n'
    '➡️ <a href="https://help.netflix.com/es-es/node/101653?ui_action=kb-article-popular-categories" target="_self">¿Cómo descargar la aplicación de Netflix?</a>\n\n',
    reply_markup=InlineKeyboardMarkup([ 
        [InlineKeyboardButton(text='Atrás', callback_data='help')],
        [InlineKeyboardButton(text='Menú principal', callback_data='inicio')]
    ])   
    )

def it_cant_be_see(update:Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    user = query.message.from_user
    id = query.message.from_user.id
    logger.info(f'El usuario ha ingresado al comando /ayuda y seleccionado el botón "No se puede ver".')

    query.edit_message_text(parse_mode='HTML', text='<b>No se puede ver</b>\n\n'
    '➡️ <a href="https://help.netflix.com/es-es/node/365?ui_action=kb-article-popular-categories" target="_self">¿Cómo cambiar tu contraseña de Netflix?</a>\n\n'
    '➡️ <a href="https://help.netflix.com/es-es/node/12983?ui_action=kb-article-popular-categories" target="_self">No encuentro la aplicación de Netflix de las tiendas de aplicaciones</a>\n\n'
    '➡️ <a href="https://help.netflix.com/es-es/node/57688?ui_action=kb-article-popular-categories" target="_self">Netflix muestra el mensaje: «Esta aplicación no es compatible con tu dispositivo».</a>\n\n',
    reply_markup=InlineKeyboardMarkup([ 
        [InlineKeyboardButton(text='Atrás', callback_data='help')],
        [InlineKeyboardButton(text='Menú principal', callback_data='inicio')]
    ])   
    )

def manage_account(update:Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    user = query.message.from_user
    id = query.message.from_user.id
    logger.info(f'El usuario ha ingresado al comando /ayuda y seleccionado el botón "Gestionar cuenta".')

    query.edit_message_text(parse_mode='HTML', text='<b>Gestionar mi cuenta</b>\n\n'
    '➡️ Consulta toda la información acerca de los <b><u>planes y precios</u></b> con el comando /planes\n\n'
    '➡️ <a href="https://help.netflix.com/es-es/node/41049?ui_action=kb-article-popular-categories" target="_self">Facturación y pagos</a>\n\n'
    '➡️ <a href="https://help.netflix.com/es-es/node/111934?ui_action=kb-article-popular-categories" target="_self">Se ha cambiado mi dirección de correo electrónico sin mi permiso</a>\n\n',
    reply_markup=InlineKeyboardMarkup([ 
        [InlineKeyboardButton(text='Atrás', callback_data='help')],
        [InlineKeyboardButton(text='Menú principal', callback_data='inicio')]
    ])   
    )

def watch_netflix(update:Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    user = query.message.from_user
    id = query.message.from_user.id
    logger.info(f'El usuario ha ingresado al comando /ayuda y seleccionado el botón "Ver Netflix".')

    query.edit_message_text(parse_mode='HTML', text='<b>Ver Netflix</b>\n\n'
    '➡️ <a href="https://help.netflix.com/es-es/node/54816?ui_action=kb-article-popular-categories" target="_self">¿Cómo descargar series y películas para verlas sin conexión?</a>\n\n'
    '➡️ <a href="https://help.netflix.com/es-es/node/33222?ui_action=kb-article-popular-categories" target="_self">¿Cómo ver Netflix en tu televisor?</a>\n\n'
    '➡️ <a href="https://help.netflix.com/es-es/node/49?ui_action=kb-article-popular-categories" target="_self">¿Cómo usar dispositivos móviles para ver Netflix en televisores?</a>\n\n',
    reply_markup=InlineKeyboardMarkup([ 
        [InlineKeyboardButton(text='Atrás', callback_data='help')],
        [InlineKeyboardButton(text='Menú principal', callback_data='inicio')]
    ])   
    )

def quick_links(update:Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    user = query.message.from_user
    id = query.message.from_user.id
    logger.info(f'El usuario ha ingresado al comando /ayuda y seleccionado el botón "Enlaces rápidos".')

    query.edit_message_text(parse_mode='HTML', text='<b>Enlaces rápidos</b>\n\n'
    '➡️ <a href="https://www.netflix.com/password" target="_self">Restablecer contraseña»</a>\n\n'
    '➡️ <a href="https://www.netflix.com/email" target="_self">Actualizar correo»</a>\n\n'
    '➡️ <a href="https://www.netflix.com/co/loginhelp" target="_self">Obtener ayuda para iniciar sesión»</a>\n\n'
    '➡️ <a href="https://www.netflix.com/YourAccountPayment" target="_self">Actualizar método de pago»</a>\n\n'
    '➡️ <a href="https://help.netflix.com/es-es/titlerequest?ui_action=title-suggestion-quicklinks" target="_self">Solicitar series o películas»</a>\n\n',
    reply_markup=InlineKeyboardMarkup([ 
        [InlineKeyboardButton(text='Atrás', callback_data='help')],
        [InlineKeyboardButton(text='Menú principal', callback_data='inicio')]
    ])   
    )

def suggested_articles(update:Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    user = query.message.from_user
    id = query.message.from_user.id
    logger.info(f'El usuario ha ingresado al comando /ayuda y seleccionado el botón "Artículos sugeridos".')

    query.edit_message_text(parse_mode='HTML', text='<b>Artículos sugeridos</b>\n\n'
    '➡️ <a href="https://help.netflix.com/es-es/node/102377" target="_self">Primeros pasos con Netflix</a>\n\n'
    '➡️ <a href="https://help.netflix.com/es-es/node/10421" target="_self">Cómo crear y editar perfiles</a>\n\n'
    '➡️ <a href="https://help.netflix.com/es-es/node/54816" target="_self">Cómo descargar series y películas para verlas sin conexión</a>\n\n'
    '➡️ <a href="https://help.netflix.com/es-es/node/32950" target="_self">Tarjetas de regalo de Netflix</a>\n\n'
    '➡️ <a href="https://help.netflix.com/es-es/node/13243" target="_self">Cómo proteger tu cuenta</a>\n\n'
    '➡️ <a href="https://help.netflix.com/es-es/node/25970" target="_self">Cómo configurar tu número de teléfono para recuperar tu contraseña</a>\n\n'
    '➡️ <a href="https://help.netflix.com/es-es/node/13245" target="_self">Cómo cambiar el idioma en Netflix</a>\n\n'
    '➡️ <a href="https://help.netflix.com/es-es/node/22205" target="_self">Cómo ocultar títulos del historial de visionado</a>\n\n'
    '➡️ Busca más artículos en nuestro <a href="https://help.netflix.com/es-es" target="_self">Centro de ayuda</a>\n\n',
    reply_markup=InlineKeyboardMarkup([ 
        [InlineKeyboardButton(text='Atrás', callback_data='help')],
        [InlineKeyboardButton(text='Menú principal', callback_data='inicio')]
    ])
    )

def sol_series(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()

    user = query.message.from_user
    logger.info(f'El usuario {user.first_name} {user.last_name}, ha escogido solicita series o películas.')
    id = query.message.chat_id

    query.edit_message_text(
        parse_mode="HTML", text='<b>Solicita series o películas</b>\n\n'
        '¿Hay alguna serie o película que te gustaría ver en Netflix? <a href="https://help.netflix.com/es/titlerequest" target="_self">Dínoslo a continuación</a>.\n\n'
        '¿Te preguntas por qué un título ya no está disponible? Visita <a href="https://help.netflix.com/es/node/60541?ui_action=expired-content-link" target="_self">¿Por qué algunas series y películas desaparecen de Netflix?</a>.\n\n'
        'Si buscas ayuda para encontrar un título, visita <a href="https://help.netflix.com/es/node/47765" target="_self">¿Cómo encuentro películas y series en Netflix?</a>.'
    )
    
    bot.sendChatAction(chat_id=id, action=ChatAction.TYPING, timeout=None)
    time.sleep(1)
    query.message.reply_text(parse_mode="HTML", text="<b>¿Qué sucede si ya solicité una serie o película?</b>\n\n"
    "Si ya enviaste una solicitud, puedes relajarte: hemos recibido tu comentario.")
    bot.sendChatAction(chat_id=id, action=ChatAction.TYPING, timeout=None)
    time.sleep(1)
    query.message.reply_text(parse_mode="HTML", text='No podemos responder solicitudes individuales, pero puedes mantenerte al día acerca de los nuevos títulos que llegan a Netflix '
    '<a href="https://help.netflix.com/es/node/14422/CO" target="_self">siguiéndonos</a> en las redes sociales y <a href="https://help.netflix.com/es/node/25" target="_self">suscribiéndote</a> a nuestros emails "Ahora en Netflix".')
    bot.sendChatAction(chat_id=id, action=ChatAction.TYPING, timeout=None)
    time.sleep(1)
    query.message.reply_text("/start para regresar al menú principal.")
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
        text='Necesito restablecer mi contraseña',
        url='https://www.netflix.com/co/LoginHelp'
    )

    buttonPayment = InlineKeyboardButton(
        text='Necesito actualizar mi forma de pago',
        url='https://www.netflix.com/co/YourAccountPayment'
    )

    bot.sendChatAction(chat_id=id, action=ChatAction.TYPING, timeout=None)
    time.sleep(1)
    query.edit_message_text(parse_mode="HTML", text= f"¡Hola <b>{user.first_name}</b>! Espero te encuentres muy bien, Antes de chatear...\n\n"
     "Puedes resolver rápidamente algunos problemas habituales sin necesidad de recibir ayuda en directo:")
    bot.sendChatAction(chat_id= id, action= ChatAction.TYPING, timeout= None)
    time.sleep(1)
    query.message.reply_text(
        'Escoge una opción\n\n',
        reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton(text='No encuentro una serie o película en Netflix', callback_data='opcion1')],
        [buttonrestContra],
        [buttonPayment],  
        [InlineKeyboardButton(text='¡Quiero hablar con un asesor!', callback_data='opcion4')]
        ]),
    )

def chat_directo(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()

    user = query.message.from_user
    logger.info(f'El usuario {user.first_name} {user.last_name}, ha escogido la función chat directo.')
    id = query.message.chat_id

    query.edit_message_text(
        parse_mode="HTML", text='<b>Describe tu problema</b>\n\n'
        '¿Cómo podemos ayudarte el día de hoy?\n\n'
        'Por favor describe el inconveniente que estás presentando y uno de nuestros asesores se comunicará contigo lo más pronto posible.\n\n'
    )

    return CONVERSATION

def conversation(update, context):

    user_name = update.effective_user['first_name']
    user_last = update.effective_user['last_name']
    user_id = update.effective_user['id']

    inconveniente = update.message.text

    logger.info("El inconveniente que presenta el usuario %s %s es: %s", user_name, user_last, inconveniente)
    update.message.reply_text(
        text=f"Muchas gracias, hemos registrado tu respuesta satisfactoriamente, en breve uno de nuestros asesores se pondrá en contacto contigo.\n\n")
    update.message.reply_text(parse_mode="HTML", text="<b>¿Qué pasa si ya he solicitado hablar con un asesor?</b>\n\n"
    "Si ya enviaste una solicitud, puedes relajarte, hemos recibido tu mensaje, tiempo de espera: 5 a 15 minutos.")
    update.message.reply_text(parse_mode="HTML", text='¿Quieres recibir una respuesta inmediata? '
    '<a href="https://t.me/netflixcolombiaoficial" target="_self">chatea con nosotros</a>')
    update.message.reply_text("/start para regresar al menú principal.")

    context.bot.sendMessage(chat_id='YOUR_TELEGRAM_CHAT_ID', parse_mode="HTML", text=f"<b>El usuario {user_name} {user_last} ID: {user_id} ha solicitado hablar con un asesor, el problema descrito por el usuario es:</b> {inconveniente}")

    return ConversationHandler.END


def cancel(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    id = update.message.from_user.id
    logger.info("El usuario %s %s canceló la conversación.", user.first_name, user.last_name)
    context.bot.sendMessage(chat_id=id, parse_mode="HTML", text=
        'Espero sinceramente haber sido de ayuda el día de hoy y que la información brindada contestara tu consulta/problema. ' 
        'Por mi parte me despido que tengas un excelente día. ¡Tus amigos de <b>Netflix Colombia</b>👋🏻!', reply_markup=ReplyKeyboardRemove()
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
#     "Temperatura: {0:.2f}".format(tempC), "°C\n"
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
            CallbackQueryHandler(pattern='películas', callback=peliculas_call_handler),
            CallbackQueryHandler(pattern='series', callback=series_call_handler),
            CallbackQueryHandler(pattern='básico', callback=plan_basico),
            CallbackQueryHandler(pattern='estándar', callback=plan_estandar),
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
            CallbackQueryHandler(pattern='brarlynn_muñoz', callback=brarlynn_muñoz),
            CallbackQueryHandler(pattern='karen_fonseca', callback=karen_fonseca),
            CallbackQueryHandler(pattern='david_chavarriaga', callback=david_chavarriaga),
            CallbackQueryHandler(pattern='clau_jimenez', callback=clau_jimenez),
            CallbackQueryHandler(pattern='yimar', callback=yimar),
            CallbackQueryHandler(pattern='claudia_lopez', callback=claudia_lopez),
            CallbackQueryHandler(pattern='diana_jimenez', callback=diana_jimenez),
            CallbackQueryHandler(pattern='manuela_montoya', callback=manuela_montoya),
            CallbackQueryHandler(pattern='mauro_patiño', callback=mauro_patino),
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


