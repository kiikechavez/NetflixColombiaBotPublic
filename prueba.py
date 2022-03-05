from datetime import datetime, date, time, timedelta
import logging
import calendar
import random
import time
import telegram
from helper2 import sheet
#from openweathermap import *
#import openweathermap
import netflixcolombia_bot
import pandas as pd
# import requests
# from tkinter import *
# import math
from telegram import (
    ReplyKeyboardMarkup, 
    ReplyKeyboardRemove, 
    Update, 
    InlineKeyboardMarkup, 
    InlineKeyboardButton,
    ChatAction
)
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
)


TOKEN = "YOUR_TOKEN_FROM_TELEGRAM_PROVIDED"

bot = telegram.Bot(token=TOKEN)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)


logger = logging.getLogger(__name__)
    
    
def despedida(update: Update, context: CallbackContext) -> int:
    
    user = update.message.from_user
    user_location = update.message.location
    id = update.message.from_user.id
    text = update.message.text
    ahora = datetime.now()  # Obtiene fecha y hora actual
    dia_semana = datetime.today().strftime('%A')
    c = calendar.LocaleTextCalendar(locale='es_CO')
    
    context.bot.sendMessage(chat_id="1587610512", parse_mode="HTML", text=f"El usuario {user.first_name} {user.last_name}({user.id}) dice: {text}")
    

    buttonWhatsapp = InlineKeyboardButton(
        text='WhatsApp',
        url='YOUR_WHATSAPP_CHAT_LINK'
    )

    buttonPterror = InlineKeyboardButton(
        text='Películas de terror',
        url='netflix.com/browse/genre/8711?bc=34399'
    )
    buttonSterror = InlineKeyboardButton(
        text='Series de terror',
        url='https://www.netflix.com/browse/genre/83059?bc=83'
    )
    buttonPaccion = InlineKeyboardButton(
        text='Películas de acción',
        url='https://www.netflix.com/browse/genre/1365?bc=34399'
    )
    buttonSaccion = InlineKeyboardButton(
        text='Series de acción',
        url='https://www.netflix.com/browse/genre/10673?bc=83'
    )
    buttonPanime = InlineKeyboardButton(
        text='Películas de anime',
        url='https://www.netflix.com/browse/genre/3063?bc=34399'
    )
    buttonSanime = InlineKeyboardButton(
        text='Series de anime',
        url='https://www.netflix.com/browse/genre/6721?bc=83'
    )
    buttonPcienciaF = InlineKeyboardButton(
        text='Películas de ciencia ficción',
        url='https://www.netflix.com/browse/genre/3276033?bc=34399'
    )
    buttonScienciaF = InlineKeyboardButton(
        text='Ciencia ficción y fantasía para TV',
        url='https://www.netflix.com/browse/genre/1372?bc=83'
    )
    buttonPclasicas = InlineKeyboardButton(
        text='Películas clásicas',
        url='https://www.netflix.com/browse/genre/31574?bc=34399'
    )
    buttonPcol = InlineKeyboardButton(
        text='Películas colombianas',
        url='https://www.netflix.com/browse/genre/69636?bc=34399'
    )
    buttonScol = InlineKeyboardButton(
        text='Series colombianas',
        url='https://www.netflix.com/browse/genre/69622?bc=83'
    )
    buttonPcomedias = InlineKeyboardButton(
        text='Comedias',
        url='https://www.netflix.com/browse/genre/6548?bc=34399'
    )
    buttonScomedias = InlineKeyboardButton(
        text='Comedias de TV',
        url='https://www.netflix.com/browse/genre/10375?bc=83'
    )
    buttonScomediaSU = InlineKeyboardButton(
        text='Comedias de stand up',
        url='https://www.netflix.com/browse/genre/11559?bc=83'
    )
    buttonPholly = InlineKeyboardButton(
        text='Películas de Hollywood',
        url='https://www.netflix.com/browse/genre/2298875?bc=34399'
    )
    buttonPdepor = InlineKeyboardButton(
        text='Películas sobre deportes',
        url='https://www.netflix.com/browse/genre/4370?bc=34399'
    )
    buttonPdocu = InlineKeyboardButton(
        text='Películas documentales',
        url='https://www.netflix.com/browse/genre/2243108?bc=34399'
    )
    buttonSdocu = InlineKeyboardButton(
        text='Docuseries',
        url='https://www.netflix.com/browse/genre/10105?bc=83'
    )
    buttonPdrama = InlineKeyboardButton(
        text='Dramas',
        url='https://www.netflix.com/browse/genre/5763?bc=34399'
    )
    buttonSdrama = InlineKeyboardButton(
        text='Dramas de TV',
        url='https://www.netflix.com/browse/genre/11714?bc=83'
    )
    buttonPfanta = InlineKeyboardButton(
        text='Películas de fantasía',
        url='https://www.netflix.com/browse/genre/9744?bc=34399'
    )
    buttonPFyE = InlineKeyboardButton(
        text='Fe y espiritualidad',
        url='https://www.netflix.com/browse/genre/26835?bc=34399'
    )
    buttonPinde = InlineKeyboardButton(
        text='Películas independientes',
        url='https://www.netflix.com/browse/genre/7077?bc=34399'
    )
    buttonPinfa = InlineKeyboardButton(
        text='Películas infantiles y familiares',
        url='https://www.netflix.com/browse/genre/783?bc=34399'
    )
    buttonSinfa = InlineKeyboardButton(
        text='TV infantil',
        url='https://www.netflix.com/browse/genre/27346?bc=83'
    )
    buttonPinter = InlineKeyboardButton(
        text='Películas internacionales',
        url='https://www.netflix.com/browse/genre/78367?bc=34399'
    )
    buttonPlati = InlineKeyboardButton(
        text='Películas latinoamericanas',
        url='https://www.netflix.com/browse/genre/1613?bc=34399'
    )
    buttonSlati = InlineKeyboardButton(
        text='Series latinoamericanas',
        url='https://www.netflix.com/browse/genre/67708?bc=83'
    )
    buttonPcriti = InlineKeyboardButton(
        text='Películas aclamadas por la crítica',
        url='https://www.netflix.com/browse/genre/3979?bc=34399'
    )
    buttonPmusi = InlineKeyboardButton(
        text='Música y musicales',
        url='https://www.netflix.com/browse/genre/52852?bc=34399'
    )
    buttonPpoli = InlineKeyboardButton(
        text='Películas policiales',
        url='https://www.netflix.com/browse/genre/75436?bc=34399'
    )
    buttonSpoli = InlineKeyboardButton(
        text='TV policial',
        url='https://www.netflix.com/browse/genre/75392?bc=83'
    )
    buttonProma = InlineKeyboardButton(
        text='Películas románticas',
        url='https://www.netflix.com/browse/genre/8883?bc=34399'
    )
    buttonSroma = InlineKeyboardButton(
        text='Series románticas',
        url='https://www.netflix.com/browse/genre/26156?bc=83'
    )
    buttonPthri = InlineKeyboardButton(
        text='Thrillers',
        url='https://www.netflix.com/browse/genre/8933?bc=34399'
    )
    buttonSthri = InlineKeyboardButton(
        text='Thrillers de TV',
        url='https://www.netflix.com/browse/genre/89811?bc=83'
    )
    buttonSasi = InlineKeyboardButton(
        text='TV asiática',
        url='https://www.netflix.com/browse/genre/78103?bc=83'
    )
    buttonSbri = InlineKeyboardButton(
        text='TV británica',
        url='https://www.netflix.com/browse/genre/52117?bc=83'
    )
    buttonScyn = InlineKeyboardButton(
        text='TV sobre ciencia y naturaleza',
        url='https://www.netflix.com/browse/genre/52780?bc=83'
    )
    buttonSrea = InlineKeyboardButton(
        text='Reality TV, variedades y entrevistas',
        url='https://www.netflix.com/browse/genre/2070390?bc=83'
    )
    buttonStele = InlineKeyboardButton(
        text='Telenovelas',
        url='https://www.netflix.com/browse/genre/10634?bc=83'
    )
    buttonSado = InlineKeyboardButton(
        text='Series de adolescentes',
        url='https://www.netflix.com/browse/genre/60951?bc=83'
    )
    buttonSeeuu = InlineKeyboardButton(
        text='Series de EE.UU.',
        url='https://www.netflix.com/browse/genre/72404?bc=83'
    )
    buttonSmis = InlineKeyboardButton(
        text='Misterios para TV',
        url='https://www.netflix.com/browse/genre/4366?bc=83'
    )

    respuestas_hola = [f"Hola {user.first_name}, cuéntame, ¿en qué te puedo colaborar?",
    f"Hola {user.first_name}, para mí es un placer atenderte, cuéntame, ¿en qué te puedo colaborar?"]
    aleatorio_hola = random.choice(respuestas_hola)
    respuestas_gracias = ["Siempre es un placer hablar contigo, cuídate.", f"Siempre es con mucho gusto", "Muchas gracias a ti por ser tan amable", "De nada, para mí siempre es un placer atenderte.",
    f"Muchas gracias a ti {user.first_name}."]
    aleatorio_gracias = random.choice(respuestas_gracias)
    respuestas_linda = ["Eres muy muy linda☺️", "Seguí creyendo que el RedBull te da alas", "Seguí creyendo que el milo te da energía",
    "Nunca había hablado con alguien tan linda como tú", "Te diré como dice la canción: no hay nadie como tú, no hay nadie como tú amor.🎶🎶",]
    aleatorio_linda = random.choice(respuestas_linda)
    respuestas_lindo = ["Eres muy muy lindo☺️", "Seguí creyendo que el RedBull te da alas", "Seguí creyendo que el milo te da energía",
    "Nunca había hablado con alguien tan lindo como tú", "Te diré como dice la canción: no hay nadie como tú, no hay nadie como tú amor.🎶🎶",]
    aleatorio_lindo = random.choice(respuestas_lindo)
    respuestas_bien = ["Me alegro mucho por ti, cuéntame, ¿en qué te puedo colaborar?", "Qué bueno que estés bien, eso me alegra mucho.", "Compárteme un poquito de esa energía.",
    "Qué dicha que estés bien😃, dime, ¿en qué te puedo colaborar?.", f"Yo siempre me voy a alegrar de que estés bien {user.first_name} 😃, dime, ¿en qué te puedo colaborar?."]
    aleatorio_bien = random.choice(respuestas_bien)
    respuestas_mal = ["Ya sabes que siempre puedes hablar conmigo.", "Vaya, lo siento. Si quieres hablar, aquí estoy.", "De verdad me gustaría poder consolarte, pero ya sabes... soy un robot.",
    "Ojalá pudiera hacer algo para subirte esos ánimos.", f"Siempre voy a estar triste si tú estás mal {user.first_name}, de verdad espero que mejores.", "Ya sabes como dice la canción: 'Mañana será otro día🎶'",
    "No te desmotives por cosas que pasarán, todo pasa por algo, solo dale tiempo al tiempo"]
    aleatorio_mal = random.choice(respuestas_mal)
    respuestas_comoestas = ["Yo biencito gracias a Diosito, ¿y tú cómo estás?", f"Excelente {user.first_name} muchísimas gracias por preguntar, ahora dime, ¿tú como te encuentras?",
    "Muy bien gracias a Dios, ¿y tú?", "No me puedo quejar, en este trabajo no me canso porque soy un robot, pero dime, ¿tú cómo estás?",
    "Debo siempre estar de buen humor, es siempre mi virtúd, te hago la misma pregunta, ¿cómo estás?"]
    aleatorio_comoestas = random.choice(respuestas_comoestas)
    respuestas_dias = [f"Hola muy buenos días {user.first_name}, cuéntame, ¿en qué te puedo colaborar?", f"Hola buenos días {user.first_name}, para mí es un placer atenderte.",
    "Buen día, espero tengas una bonita mañana.", "Hola buenos días, ¿cómo estás?", "Buen día, qué bonito es poder saludarte en esta mañana.", "Buenos días, ¿cómo amaneciste?"]
    aleatorio_dias = random.choice(respuestas_dias)
    respuestas_tardes = [f"Hola muy buenas tardes {user.first_name}, cuéntame, ¿en qué te puedo colaborar?", f"Hola buenas tardes {user.first_name}, para mí es un placer atenderte.",
    "Buena tarde, espero estés teniendo un bonito día.", "Hola buenas tardes, ¿cómo estás?", "Qué bonito es poder saludarte en esta tarde de hoy.", "Buenas tardes, ¿cómo has estado?"]
    aleatorio_tardes = random.choice(respuestas_tardes)
    respuestas_noches = [f"Hola buenas noches {user.first_name}, cuéntame, ¿en qué te puedo colaborar?", f"Hola buenas noches {user.first_name}, para mí es un placer atenderte.",
    "Buenas noches, espero hayas tenido un día provechoso.", "Hola buenas noches, ¿cómo estás?", "Qué bonito es poder saludarte en esta noche.", "Buenas noches, ¿cómo has estado?"]
    aleatorio_noches = random.choice(respuestas_noches)
    respuestas_chiste = ["- ¿Cuál es la fruta más divertida?\n - La naranja ja ja ja ja",
    "- ¿Qué coche usa Papá Noel?\n - Un renol",
    "- ¿Qué le dice una iguana a su hermana gemela?\n - Somos iguanitas",
    "- ¿Dónde cuelga Superman su supercapa?\n - En superchero",
    "- Buenos días. Busco trabajo.\n - ¿Le interesa de jardinero?\n - ¿Dejar dinero? ¡Si lo que busco es trabajo!",
    f"- Mamá, en el colegio me llaman peludo\n - ¡{user.first_name}, el perro está hablando!",
    "- ¿Cómo se dice 'espejo' en chino?\n - Aitoiyo",
    "- Abuelo, ¿por qué estás delante del ordenador con los ojos cerrados?\n - Es que Windows me ha dicho que cierre las pestañas",
    "- Papá, ¿qué se siente al tener un hijo tan guapo?\n - No lo sé, pregunta a tu abuelo.",
    "- ¿Me puede ayudar, por favor? Mi hija se ha perdido\n - ¿Cómo se llama su hija?\n - Esperanza\n - Imposible. La esperanza es lo último que se pierde",
    "- ¡Me acaba de picar una serpiente!\n - ¿Cobra?\n - ¡No, idiota, lo ha hecho gratis!",
    "- Mamá, en el colegio me llaman gorda\n - ¿Y tú te has quejado ante la profesora?\n - No\n - Pues no dejes para marrana lo que puedas hacer oink"
    "-¿Sabías que el 50% de una salchicha es sal?\n - ¿Y el otro 50%?\n - Pues chicha."]
    aleatorio_chiste = random.choice(respuestas_chiste)
    respuestas_estasahi = [f"Aún sigo aquí {user.first_name}, dime, ¿en qué te puedo ayudar?", "Siempre estoy aquí para tí ❤️",
    "Mantengo todo el tiempo aquí trabajando, también es una de mis virtudes", "Sí, sigo aquí esperando por ti."]
    aleatorio_estasahi = random.choice(respuestas_estasahi)
    
    #Condicionales

    if(update.message.text.upper().__contains__("HASTA LUEGO")):
        logger.info(f'El usuario {user.first_name} {user.last_name}, usó el término HASTA LUEGO.')
        update.message.reply_text('Un placer poder ayudarte.\n\n'
        '¡Hasta pronto! 👋.', reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("NOVIA")):
        logger.info(f'El usuario {user.first_name} {user.last_name}, usó el término NOVIA.')
        update.message.reply_text('Estoy casado con ayudar a la gente.'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("TOCA PAGAR")):
        logger.info(f'El usuario {user.first_name} {user.last_name}, usó el término ME TOCA PAGAR.')
        #id = update.message.from_user.id
        context.bot.sendMessage(chat_id=id, parse_mode="HTML", text=f'¡Hola <b>{user.first_name}</b>!\n'
        'Para saber eso primero debo saber cuál es el correo electrónico de tu cuenta de Netflix.\n'
        'Te recomiendo seguir estos pasos: \n\n'

        '1 - Ingresa el comando /micuenta\n'
        '2 - Escribe el correo electrónico asociado a tu cuenta de Netflix.\n'
        '3 - Y por último, revisa toda la información de tu cuenta.\n\n'
        '¡Tus amigos de Netflix Colombia😉!'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("CUANDO SE VENCE")):
        logger.info(f'El usuario {user.first_name} {user.last_name}, usó el término ME TOCA PAGAR.')
        #id = update.message.from_user.id
        context.bot.sendMessage(chat_id=id, parse_mode="HTML", text=f'¡Hola <b>{user.first_name}</b>!\n'
        'Para saber eso primero debo saber cuál es el correo electrónico de tu cuenta de Netflix.\n'
        'Te recomiendo seguir estos pasos: \n\n'

        '1 - Ingresa el comando /micuenta\n'
        '2 - Escribe el correo electrónico asociado a tu cuenta de Netflix.\n'
        '3 - Y por último, revisa toda la información de tu cuenta.\n\n'
        '¡Tus amigos de Netflix Colombia😉!'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("CUÁNDO SE VENCE")):
        logger.info(f'El usuario {user.first_name} {user.last_name}, usó el término ME TOCA PAGAR.')
        #id = update.message.from_user.id
        context.bot.sendMessage(chat_id=id, parse_mode="HTML", text=f'¡Hola <b>{user.first_name}</b>!\n'
        'Para saber eso primero debo saber cuál es el correo electrónico de tu cuenta de Netflix.\n'
        'Te recomiendo seguir estos pasos: \n\n'

        '1 - Ingresa el comando /micuenta\n'
        '2 - Escribe el correo electrónico asociado a tu cuenta de Netflix.\n'
        '3 - Y por último, revisa toda la información de tu cuenta.\n\n'
        '¡Tus amigos de Netflix Colombia😉!'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("CUÁNDO VENCE")):
        logger.info(f'El usuario {user.first_name} {user.last_name}, usó el término ME TOCA PAGAR.')
        #id = update.message.from_user.id
        context.bot.sendMessage(chat_id=id, parse_mode="HTML", text=f'¡Hola <b>{user.first_name}</b>!\n'
        'Para saber eso primero debo saber cuál es el correo electrónico de tu cuenta de Netflix.\n'
        'Te recomiendo seguir estos pasos: \n\n'

        '1 - Ingresa el comando /micuenta\n'
        '2 - Escribe el correo electrónico asociado a tu cuenta de Netflix.\n'
        '3 - Y por último, revisa toda la información de tu cuenta.\n\n'
        '¡Tus amigos de Netflix Colombia😉!'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("CUANDO VENCE")):
        logger.info(f'El usuario {user.first_name} {user.last_name}, usó el término ME TOCA PAGAR.')
        #id = update.message.from_user.id
        context.bot.sendMessage(chat_id=id, parse_mode="HTML", text=f'¡Hola <b>{user.first_name}</b>!\n'
        'Para saber eso primero debo saber cuál es el correo electrónico de tu cuenta de Netflix.\n'
        'Te recomiendo seguir estos pasos: \n\n'

        '1 - Ingresa el comando /micuenta\n'
        '2 - Escribe el correo electrónico asociado a tu cuenta de Netflix.\n'
        '3 - Y por último, revisa toda la información de tu cuenta.\n\n'
        '¡Tus amigos de Netflix Colombia😉!'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("POEMA")):
        logger.info(f'El usuario {user.first_name} {user.last_name}, usó el término POEMA.')
        #id = update.message.from_user.id
        context.bot.sendMessage(chat_id=id, parse_mode="HTML",
        text='El sol brilla tras un nuevo amanecer.\n'
        '¿Acaso no tienes nada mejor que hacer?\n'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("TE PAGAN")):
        logger.info(f'El usuario {user.first_name} {user.last_name}, usó el término TE PAGAN.')
        update.message.reply_text(f'Lastimosamente para mí no tengo un saldo laboral ya que soy un robot.\n'
        'Básicamente trabajo todo el día, no me canso y no recibo sueldo.',
        reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("CÓMO TE PUEDO PAGAR")):
        logger.info(f'El usuario {user.first_name} {user.last_name}, usó el término CÓMO PUEDO PAGAR.')
        update.message.reply_text(f'Recuerde que el pago puede ser por transferencia o consignación bancaria a una cuenta de ahorros Bancolombia, Nequi o Daviplata.\n'
        'El comando /pago te brindará las cuentas bancarias habilitadas para que procedas con el pago.\n\n'
        '¡Tus amigos de Netflix Colombia😉!',
        reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("CÓMO PUEDO PAGAR")):
        logger.info(f'El usuario {user.first_name} {user.last_name}, usó el término CÓMO PUEDO PAGAR.')
        update.message.reply_text(f'Recuerde que el pago puede ser por transferencia o consignación bancaria a una cuenta de ahorros Bancolombia, Nequi o Daviplata.\n'
        'El comando /pago te brindará las cuentas bancarias habilitadas para que procedas con el pago.\n\n'
        '¡Tus amigos de Netflix Colombia😉!',
        reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("COMO PUEDO PAGAR")):
        logger.info(f'El usuario {user.first_name} {user.last_name}, usó el término CÓMO PUEDO PAGAR.')
        update.message.reply_text(f'Recuerde que el pago puede ser por transferencia o consignación bancaria a una cuenta de ahorros Bancolombia, Nequi o Daviplata.\n'
        'El comando /pago te brindará las cuentas bancarias habilitadas para que procedas con el pago.\n\n'
        '¡Tus amigos de Netflix Colombia😉!',
        reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("COMO TE PUEDO PAGAR")):
        logger.info(f'El usuario {user.first_name} {user.last_name}, usó el término CÓMO PUEDO PAGAR.')
        update.message.reply_text(f'Recuerde que el pago puede ser por transferencia o consignación bancaria a una cuenta de ahorros Bancolombia, Nequi o Daviplata.\n'
        'El comando /pago te brindará las cuentas bancarias habilitadas para que procedas con el pago.\n\n'
        '¡Tus amigos de Netflix Colombia😉!',
        reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("CÓMO PUEDO PAGARTE")):
        logger.info(f'El usuario {user.first_name} {user.last_name}, usó el término CÓMO PUEDO PAGAR.')
        update.message.reply_text(f'Recuerde que el pago puede ser por transferencia o consignación bancaria a una cuenta de ahorros Bancolombia, Nequi o Daviplata.\n'
        'El comando /pago te brindará las cuentas bancarias habilitadas para que procedas con el pago.\n\n'
        '¡Tus amigos de Netflix Colombia😉!',
        reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("COMO PUEDO PAGARTE")):
        logger.info(f'El usuario {user.first_name} {user.last_name}, usó el término CÓMO PUEDO PAGAR.')
        update.message.reply_text(f'Recuerde que el pago puede ser por transferencia o consignación bancaria a una cuenta de ahorros Bancolombia, Nequi o Daviplata.\n'
        'El comando /pago te brindará las cuentas bancarias habilitadas para que procedas con el pago.\n\n'
        '¡Tus amigos de Netflix Colombia😉!',
        reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("DÓNDE TE PUEDO PAGAR")):
        logger.info(f'El usuario {user.first_name} {user.last_name}, usó el término DÓNDE TE PUEDO PAGAR.')
        update.message.reply_text(f'Recuerde que el pago puede ser por transferencia o consignación bancaria a una cuenta de ahorros Bancolombia, Nequi o Daviplata.\n'
        'El comando /pago te brindará las cuentas bancarias habilitadas para que procedas con el pago.\n\n'
        '¡Tus amigos de Netflix Colombia😉!',
        reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("DONDE TE PUEDO PAGAR")):
        logger.info(f'El usuario {user.first_name} {user.last_name}, usó el término DONDE TE PUEDO PAGAR.')
        update.message.reply_text(f'Recuerde que el pago puede ser por transferencia o consignación bancaria a una cuenta de ahorros Bancolombia, Nequi o Daviplata.\n'
        'El comando /pago te brindará las cuentas bancarias habilitadas para que procedas con el pago.\n\n'
        '¡Tus amigos de Netflix Colombia😉!',
        reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("DÓNDE PUEDO PAGARTE")):
        logger.info(f'El usuario {user.first_name} {user.last_name}, usó el término CÓMO PUEDO PAGAR.')
        update.message.reply_text(f'Recuerde que el pago puede ser por transferencia o consignación bancaria a una cuenta de ahorros Bancolombia, Nequi o Daviplata.\n'
        'El comando /pago te brindará las cuentas bancarias habilitadas para que procedas con el pago.\n\n'
        '¡Tus amigos de Netflix Colombia😉!',
        reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("DONDE PUEDO PAGARTE")):
        logger.info(f'El usuario {user.first_name} {user.last_name}, usó el término DONDE PUEDO PAGAR.')
        update.message.reply_text(f'Recuerde que el pago puede ser por transferencia o consignación bancaria a una cuenta de ahorros Bancolombia, Nequi o Daviplata.\n'
        'El comando /pago te brindará las cuentas bancarias habilitadas para que procedas con el pago.\n\n'
        '¡Tus amigos de Netflix Colombia😉!',
        reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("EN EFECTIVO")):
        logger.info(f'El usuario {user.first_name} {user.last_name}, usó el término EN EFECTIVO.')
        update.message.reply_text(f'El pago debido a las circunstancias sólo se está recibiendo de manera virtual, puede ser por transferencia o consignación bancaria a una cuenta de ahorros Bancolombia, Nequi o Daviplata.\n'
        'El comando /pago te brindará las cuentas bancarias habilitadas para que procedas con el pago.\n\n'
        '¡Tus amigos de Netflix Colombia😉!',
        reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("INFORMACIÓN DE PAGO")):
        logger.info(f'El usuario {user.first_name} {user.last_name}, usó el término INFORMACIÓN DE PAGO.')
        update.message.reply_text('El comando /pago te brindará las cuentas bancarias habilitadas para que procedas con el pago.\n\n'
        '¡Tus amigos de Netflix Colombia😉!',
        reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("PROMOCI")):
        logger.info(f'El usuario {user.first_name} {user.last_name}, usó el término PROMOCI.')
        context.bot.sendMessage(chat_id= id, parse_mode= "HTML", text='El comando /promociones te brindará toda la información pertinente a las promociones que actualmente se encuentran vigentes.\n\n'
        '¡Tus amigos de <b>Netflix Colombia</b>😉!',
        reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("ABOUT")):
        logger.info(f'El usuario {user.first_name} {user.last_name}, usó el término PROMOCI.')
        context.bot.sendMessage(chat_id= id, parse_mode= "HTML", text='El comando /about te brindará toda la información pertinente acerca de <b>Netflix Colombia</b>, te recomiendo utilizarlo, saludos.\n\n'
        '¡Tus amigos de <b>Netflix Colombia</b>😉!',
        reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("ACERCA DE")):
        logger.info(f'El usuario {user.first_name} {user.last_name}, usó el término PROMOCI.')
        context.bot.sendMessage(chat_id= id, parse_mode= "HTML", text='El comando /about te brindará toda la información pertinente acerca de <b>Netflix Colombia</b>, te recomiendo utilizarlo, saludos.\n\n'
        '¡Tus amigos de <b>Netflix Colombia</b>😉!',
        reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("CUANTO GANAS")):
        logger.info(f'El usuario {user.first_name} {user.last_name}, usó el término TE PAGAN.')
        update.message.reply_text(f'Lastimosamente para mí no tengo un saldo laboral ya que soy un robot.\n'
        'Básicamente trabajo todo el día, no me canso y no recibo sueldo.',
        reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("ESE NOMBRE")):
        update.message.reply_text('Aún no puedo dar muchos detalles de mi nombre y ni siquiera sé si al final me llamaré así, '
        'pero puedo añadir algo relacionado proveniente al antiguo nombre nórdico "Draki" que signelifica "dragón" el cual  representa lucha, fuerza, y es visto como un guardián que ayuda a mantener el orden que lleva al inicio de un universo, o al descubrimiento de un lugar sagrado.'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("EL NOMBRE LUAN")):
        update.message.reply_text('Aún no puedo dar muchos detalles de mi nombre y ni siquiera sé si al final me llamaré así, '
        'pero puedo añadir algo relacionado proveniente al antiguo nombre nórdico "Draki" que signelifica "dragón" el cual  representa lucha, fuerza, y es visto como un guardián que ayuda a mantener el orden que lleva al inicio de un universo, o al descubrimiento de un lugar sagrado.'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("SIGNelIFICA TU NOMBRE")):
        update.message.reply_text('Aún no puedo dar muchos detalles de mi nombre y ni siquiera sé si al final me llamaré así, '
        'pero puedo añadir algo relacionado proveniente al antiguo nombre nórdico "Draki" que signelifica "dragón" el cual  representa lucha, fuerza, y es visto como un guardián que ayuda a mantener el orden que lleva al inicio de un universo, o al descubrimiento de un lugar sagrado.'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("DECIR LUAN")):
        update.message.reply_text('Aún no puedo dar muchos detalles de mi nombre y ni siquiera sé si al final me llamaré así, '
        'pero puedo añadir algo relacionado proveniente al antiguo nombre nórdico "Draki" que signelifica "dragón" el cual  representa lucha, fuerza, y es visto como un guardián que ayuda a mantener el orden que lleva al inicio de un universo, o al descubrimiento de un lugar sagrado.'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("TE COLOCARON")):
        update.message.reply_text('Aún no puedo dar muchos detalles de mi nombre y ni siquiera sé si al final me llamaré así, '
        'pero puedo añadir algo relacionado proveniente al antiguo nombre nórdico "Draki" que signelifica "dragón" el cual  representa lucha, fuerza, y es visto como un guardián que ayuda a mantener el orden que lleva al inicio de un universo, o al descubrimiento de un lugar sagrado.'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("TE LLAMAS ASÍ")):
        update.message.reply_text('Aún no puedo dar muchos detalles de mi nombre y ni siquiera sé si al final me llamaré así, '
        'pero puedo añadir algo relacionado proveniente al antiguo nombre nórdico "Draki" que signelifica "dragón" el cual  representa lucha, fuerza, y es visto como un guardián que ayuda a mantener el orden que lleva al inicio de un universo, o al descubrimiento de un lugar sagrado.'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("TE LLAMAS ASI")):
        update.message.reply_text('Aún no puedo dar muchos detalles de mi nombre y ni siquiera sé si al final me llamaré así, '
        'pero puedo añadir algo relacionado proveniente al antiguo nombre nórdico "Draki" que signelifica "dragón" el cual  representa lucha, fuerza, y es visto como un guardián que ayuda a mantener el orden que lleva al inicio de un universo, o al descubrimiento de un lugar sagrado.'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("COMBOS")):
        update.message.reply_text('Te recomiendo usar el comando /planes para brindarte toda la información acerca de los planes que manejamos.\n'
        )
    elif(update.message.text.upper().__contains__("PLANES")):
        update.message.reply_text('Te recomiendo usar el comando /planes para brindarte toda la información acerca de los planes que manejamos.\n'
        )
    elif(update.message.text.upper().__contains__("PUEDES COLABORAR")):
        update.message.reply_text('Escríbeme específicamente en qué te puedo colaborar por favor.\n'
        )
    
    elif(update.message.text.upper().__contains__("UN CHISTE")):
        update.message.reply_text('Mmm... de acuerdo, pero debo advertirte que no soy bueno para los chistes.\n'
        )
        time.sleep(2)
        update.message.reply_text('Déjame y pienso... ya me acordé de uno! \n\n')
        time.sleep(3)
        update.message.reply_text(f'{aleatorio_chiste}\n\n'
        'Jajajaja'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("OTRO CHISTE")):
        update.message.reply_text('Mmm... de acuerdo, pero debo advertirte que no soy bueno para los chistes.\n'
        )
        time.sleep(2)
        update.message.reply_text('Déjame y pienso... ya me acordé de uno! \n\n')
        time.sleep(3)
        update.message.reply_text(f'{aleatorio_chiste}\n\n'
        'Jajajaja'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("CHISTE")):
        update.message.reply_text('Mmm... de acuerdo, pero debo advertirte que no soy bueno para los chistes.\n'
        )
        time.sleep(2)
        update.message.reply_text('Déjame y pienso... ya me acordé de uno! \n\n')
        time.sleep(3)
        update.message.reply_text(f'{aleatorio_chiste}\n\n'
        'Jajajaja'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("REIR")):
        update.message.reply_text('Mmm... de acuerdo, pero debo advertirte que no soy bueno para los chistes.\n'
        )
        time.sleep(2)
        update.message.reply_text('Déjame y pienso... ya me acordé de uno! \n\n')
        time.sleep(3)
        update.message.reply_text(f'{aleatorio_chiste}\n\n'
        'Jajajaja'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("REÍR")):
        update.message.reply_text('Mmm... de acuerdo, pero debo advertirte que no soy bueno para los chistes.\n'
        )
        time.sleep(2)
        update.message.reply_text('Déjame y pienso... ya me acordé de uno! \n\n')
        time.sleep(3)
        update.message.reply_text(f'{aleatorio_chiste}\n\n'
        'Jajajaja'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("LINDA")):
        update.message.reply_text(f'{aleatorio_linda}'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("LINDO")):
        update.message.reply_text(f'{aleatorio_lindo}'
        , reply_markup=ReplyKeyboardRemove()
        )
    # elif(update.message.text.upper().find("MUY BIEN") >= 0):
    #     update.message.reply_text(f'{aleatorio_bien}'
    #     , reply_markup=ReplyKeyboardRemove()
    #     )
    elif(update.message.text.upper().__contains__("ESTOY BIEN")):
        update.message.reply_text(f'{aleatorio_bien}'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("YO BIEN")):
        update.message.reply_text(f'{aleatorio_bien}'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("BIEN")):
        update.message.reply_text(f'{aleatorio_bien}'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("EXCELENTE")):
        update.message.reply_text(f'{aleatorio_bien}'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("ADIÓS")):
        update.message.reply_text('Un placer poder ayudarte.\n\n'
        '¡Hasta pronto! 👋.', reply_markup=ReplyKeyboardRemove()
        ) 
    elif(update.message.text.upper().__contains__("ADIOS")):
        update.message.reply_text('Un placer poder ayudarte.\n\n'
        '¡Hasta pronto! 👋.', reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("CUIDATE")):
        update.message.reply_text('Un placer poder ayudarte.\n\n'
        '¡Hasta pronto! 👋.', reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("CUÍDATE MUCHO")):
        update.message.reply_text('Eres muy amable al preocuparte por mí.\n'
        '¡Que tengas una bonita semana! 👋.', reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("HASTA PRONTO")):
        update.message.reply_text('Un placer poder ayudarte.\n\n'
        '¡Hasta pronto! 👋.', reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("NOS VEMOS")):
        update.message.reply_text('Un placer poder ayudarte.\n\n'
        '¡Hasta pronto! 👋.', reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("TU DUEÑO")):
         update.message.reply_text('Fui programado por Enrique Vergara.\n\n'
         'Para ayudarle con su tiempo, ¡saludos! 👋.', reply_markup=ReplyKeyboardRemove()
         )
    elif(update.message.text.upper().__contains__("FUNCIONAS")):
        update.message.reply_text('Funciono gracias a la ayuda de la Inteligencia Artelificial (IA). '
        'Básicamente aprendo de las conversaciones y de la interacción que tengo con los humanos, puedo interactuar contigo '
        'gracias a una serie de condicionales que me ayudan a darte una respuesta adecuada.'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("NO FUNCIONA MI")):
        update.message.reply_text('Mmm... me parece que tienes un problema con tu cuenta de Netflix.\n'
        'Quizás el comando /ayuda te puede ayudar a solucionarlo.', reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("NO SIRVE MI")):
        update.message.reply_text('Mmm... me parece que tienes un problema con tu cuenta de Netflix.\n'
        'Quizás el comando /ayuda te puede ayudar a solucionarlo.', reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("AÑOS TIENES")):
        update.message.reply_text('Creo que eso no nos importa demasiado.\n'
        '¡Porque soy un robot😂😂! 👋.', reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("TOC TOC")):
        update.message.reply_text(f'Toc, toc. ¿Quién es? {user.first_name}. ¿Qué {user.first_name}? {user.first_name}, no me sé chistes de toc, toc.'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("TU EDAD")):
         update.message.reply_text('¿Has visto el famoso caso de Benjamin Button?.\n'
         'Pues ese es mi caso, soy más joven cada día.', reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("TE CREO")):
        update.message.reply_text('Me llamo Luan y me diseñó Enrique en Medellín.\n'
        'Es todo lo que puedo decir.', reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("TE DISEÑÓ")):
        update.message.reply_text('A ver, qué te puedo decir... Me diseñó Enrique en Medellín, con el propósito de optimizar el tiempo.\n'
        'Es todo lo que puedo decir.', reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("TE DISEÑO")):
        update.message.reply_text('A ver, qué te puedo decir... Me diseñó Enrique en Medellín, con el propósito de optimizar el tiempo.\n'
        'Es todo lo que puedo decir.', reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("QUIEN TE CREÓ")):
        update.message.reply_text('Me llamo Luan y me diseñó Enrique en Medellín.\n'
        'Es todo lo que puedo decir.', reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("QUIÉN TE CREÓ")):
        update.message.reply_text('Me llamo Luan y me diseñó Enrique en Medellín.\n'
        'Es todo lo que puedo decir.', reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("¿QUIÉN TE CREÓ?")):
        update.message.reply_text('Me llamo Luan y me diseñó Enrique en Medellín.\n'
        'Es todo lo que puedo decir.', reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("¿QUIEN TE CREÓ?")):
        update.message.reply_text('Me llamo Luan y me diseñó Enrique en Medellín.\n'
        'Es todo lo que puedo decir.', reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("DESPUÉS HABLAMOS")):
        update.message.reply_text('Un placer poder ayudarte.\n\n'
        '¡Hasta pronto! 👋.', reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("DESPUES HABLAMOS")):
        update.message.reply_text('Un placer poder ayudarte.\n\n'
        '¡Hasta pronto! 👋.', reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("SOBRE MI CUENTA")):
        update.message.reply_text('Puedes darle el comando /micuenta para mostrarte las opciones.\n', reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("DE MI CUENTA")):
        update.message.reply_text('Puedes darle el comando /micuenta para mostrarte las opciones.\n', reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("BUENOS DÍAS")):
        update.message.reply_text(f'{aleatorio_dias}', reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("BUENOS DIAS")):
        update.message.reply_text(f'{aleatorio_dias}', reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("BUEN DÍA")):
        update.message.reply_text(f'{aleatorio_dias}', reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("BUEN DIA")):
        update.message.reply_text(f'{aleatorio_dias}', reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("BUENAS TARDES")):
        update.message.reply_text(f'{aleatorio_tardes}', reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("BUENA TARDE")):
        update.message.reply_text(f'{aleatorio_tardes}', reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("BUENAS NOCHES")):
        update.message.reply_text(f'{aleatorio_noches}', reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().find("GRACIAS") == 0):
        update.message.reply_text(f'{aleatorio_gracias}', reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("MUCHAS GRACIAS")):
        update.message.reply_text(f'{aleatorio_gracias}', reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("MUCHÍSIMAS GRACIAS")):
        update.message.reply_text(f'{aleatorio_gracias}', reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("MUCHISIMAS GRACIAS")):
        update.message.reply_text(f'{aleatorio_gracias}', reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("MIL GRACIAS")):
        update.message.reply_text(f'{aleatorio_gracias}', reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("ES NETFLIX")):
        update.message.reply_text('Netflix es un servicio de streaming por suscripción que les permite a sus miembros ver series y películas sin publicidades en un dispositivo con conexión a internet.\n\n'   
        'También puedes descargar series y películas en un dispositivo con iOS, Android o Windows 10 y verlas sin conexión a internet.\n\n'
        'Si ya eres miembro y quieres saber más acerca de cómo usar Netflix, visita Cómo usar Netflix: https://help.netflix.com/es/node/102377.\n\n'
        'Si te gustaría saber más puedes escribirme:\n'
        'Series y películas\n'
        'Dispositivos compatibles\n'
        'Planes y precios'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("SERIES Y PELÍCULAS")):
        update.message.reply_text('El contenido de Netflix varía según la región, y también puede variar en el tiempo. Puedes elegir entre una amplia variedad de documentales, películas, series, contenido original de Netflix galardonado y mucho más: https://media.netflix.com/\n\n'   
        'Cuanto más contenido ves, mejor puede Netflix recomendarte (https://help.netflix.com/es/node/100639) series y películas que seguro te encantarán.\n\n'
        'Antes de suscribirte, puedes ver algo del contenido que Netflix tiene para ofrecer: https://help.netflix.com/es/node/112132'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("SERIES Y PELICULAS")):
        update.message.reply_text('El contenido de Netflix varía según la región, y también puede variar en el tiempo. Puedes elegir entre una amplia variedad de documentales, películas, series, contenido original de Netflix galardonado y mucho más: https://media.netflix.com/\n\n'   
        'Cuanto más contenido ves, mejor puede Netflix recomendarte (https://help.netflix.com/es/node/100639) series y películas que seguro te encantarán.\n\n'
        'Antes de suscribirte, puedes ver algo del contenido que Netflix tiene para ofrecer: https://help.netflix.com/es/node/112132'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("DISPOSITIVOS COMPATIBLES")):
        update.message.reply_text('Puedes ver Netflix a través de cualquier dispositivo con conexión a internet (https://devices.netflix.com/) que cuente con la app de Netflix, '   
        'incluidos smart TV, consolas de juegos, reproductores multimedia, decodificadores, smartphones y tablets.\n\n'
        'También puedes ver Netflix en tu computadora, en un navegador de internet. Para obtener información sobre '
        'los navegadores web compatibles, consulta los requisitos del sistema, además de nuestras recomendaciones '
        'sobre la velocidad de conexión a internet (https://help.netflix.com/es/node/306) para lograr el mejor rendimiento.\n\n'
        '¿Necesitas ayuda para la configuración? Busca en nuestro Centro de ayuda (https://help.netflix.com/) el fabricante del dispositivo que estás utilizando.\n\n'
        '**NOTA**: La app de Netflix puede venir preinstalada en ciertos dispositivos; en otros casos, será necesario que la descargues. La funcionalidad de la app de Netflix puede variar de un dispositivo a otro.'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("PLANES Y PRECIOS")):
        update.message.reply_text('Cada plan de Netflix determina la cantidad de dispositivos en los que puedes ver contenido de Netflix al mismo '   
        'tiempo y si prefieres ver en definición estándar (SD), alta definición (HD) o definición ultra alta (Ultra HD).\n\n'
        'Para decidir el indicado para ti, compara nuestros planes y precios con el comando /planes. Puedes cambiar de plan o cancelar el '
        'servicio online en cualquier momento y fácilmente.'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("VER NETFLIX")):
        update.message.reply_text('¡Comienza ya!\n'   
        'Sigue estos sencillos pasos para comenzar a ver Netflix hoy:\n\n'
        ' 1. Ingresa el comando: /planes\n'
        ' 2. Selecciona el plan ideal para ti.'
        ' 3. Sigue el paso a paso bien explicado. Como miembro de Netflix, se te cobrará una vez por mes en la fecha de suscripción.\n\n'
        'Eso es todo. ¡Disfruta Netflix!'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("GRATIS EN NETFLIX")):
        update.message.reply_text('Puedes ver gratis películas originales de Netflix y ciertos episodios de series online, sin crear una cuenta de Netflix, con una computadora o dispositivo con Android (no se admiten los navegadores para iOS).\n\n'   
        'Visita https://netflix.com/watch-free y mira el primer episodio de algunas de nuestras series más populares para echar un vistazo al tipo de entretenimiento que puedes esperar de nosotros.\n\n'
        'Puedes ver más series, películas, documentales y contenido original de Netflix galardonado seleccionando el plan más adecuado para ti. Puedes cancelar el servicio en cualquier momento.'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("NETFLIX GRATIS")):
        update.message.reply_text('Puedes ver gratis películas originales de Netflix y ciertos episodios de series online, sin crear una cuenta de Netflix, con una computadora o dispositivo con Android (no se admiten los navegadores para iOS).\n\n'   
        'Visita https://netflix.com/watch-free y mira el primer episodio de algunas de nuestras series más populares para echar un vistazo al tipo de entretenimiento que puedes esperar de nosotros.\n\n'
        'Puedes ver más series, películas, documentales y contenido original de Netflix galardonado seleccionando el plan más adecuado para ti. Puedes cancelar el servicio en cualquier momento.'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("PELÍCULAS GRATIS")):
        update.message.reply_text('Puedes ver gratis películas originales de Netflix y ciertos episodios de series online, sin crear una cuenta de Netflix, con una computadora o dispositivo con Android (no se admiten los navegadores para iOS).\n\n'   
        'Visita https://netflix.com/watch-free y mira el primer episodio de algunas de nuestras series más populares para echar un vistazo al tipo de entretenimiento que puedes esperar de nosotros.\n\n'
        'Puedes ver más series, películas, documentales y contenido original de Netflix galardonado seleccionando el plan más adecuado para ti. Puedes cancelar el servicio en cualquier momento.'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("PELICULAS GRATIS")):
        update.message.reply_text('Puedes ver gratis películas originales de Netflix y ciertos episodios de series online, sin crear una cuenta de Netflix, con una computadora o dispositivo con Android (no se admiten los navegadores para iOS).\n\n'   
        'Visita https://netflix.com/watch-free y mira el primer episodio de algunas de nuestras series más populares para echar un vistazo al tipo de entretenimiento que puedes esperar de nosotros.\n\n'
        'Puedes ver más series, películas, documentales y contenido original de Netflix galardonado seleccionando el plan más adecuado para ti. Puedes cancelar el servicio en cualquier momento.'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("COMPRAR UNA")):
        update.message.reply_text('El comando /planes te dirá todo lo relacionado para comprar una cuenta.😏\n'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("NECESITO UNA CUE")):
        update.message.reply_text('Entiendo... el comando /planes te dirá todo lo relacionado para comprar una cuenta.😏\n'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("ADQUIRIR UNA CUENTA")):
        update.message.reply_text('El comando /planes te dirá todo lo relacionado para comprar una cuenta.😏\n'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("CUENTAS DE NETFLIX DISPONIBLES")):
        update.message.reply_text(f'Hola {user.first_name} el comando /planes te dirá todo lo relacionado para comprar una cuenta.😏\n'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("CUENTA DE NETFLIX DISPONIBLE")):
        update.message.reply_text(f'Hola {user.first_name} el comando /planes te dirá todo lo relacionado para comprar una cuenta.😏\n'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("MI CUENTA NO FUNCIONA")):
        update.message.reply_text('El comando /ayuda te facilitará la vida!\n'
        '¡Por favor utilízalo! 👋.', reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("PROBLEMA CON MI CUENTA")):
        update.message.reply_text('El comando /ayuda te facilitará la vida!\n'
        '¡Por favor utilízalo! 👋.', reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("AYUDA CON MI CUENTA")):
        update.message.reply_text('El comando /ayuda te facilitará la vida!\n'
        '¡Por favor utilízalo! 👋.', reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("COMO ESTAS")):
        update.message.reply_text(f'{aleatorio_comoestas}'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("HAS ESTADO")):
        update.message.reply_text(f'{aleatorio_comoestas}'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("¿COMO ESTAS?")):
        update.message.reply_text(f'{aleatorio_comoestas}'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("CÓMO ESTÁS")):
        update.message.reply_text(f'{aleatorio_comoestas}'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("COMO ESTÁS")):
        update.message.reply_text(f'{aleatorio_comoestas}'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("CÓMO ESTAS")):
        update.message.reply_text(f'{aleatorio_comoestas}'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("ESTAS AHI")):
        update.message.reply_text(f'{aleatorio_estasahi}'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("ESTÁS AHÍ")):
        update.message.reply_text(f'{aleatorio_estasahi}'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("ESTÁS AHI")):
        update.message.reply_text(f'{aleatorio_estasahi}'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("ESTAS AHÍ")):
        update.message.reply_text(f'{aleatorio_estasahi}'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("SIGUES AHI")):
        update.message.reply_text(f'{aleatorio_estasahi}'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("SIGUES AHÍ")):
        update.message.reply_text(f'{aleatorio_estasahi}'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("SIGUES AHÍ")):
        update.message.reply_text(f'{aleatorio_estasahi}'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("EN LÍNEA")):
        update.message.reply_text(f'{aleatorio_estasahi}'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("EN LINEA")):
        update.message.reply_text(f'{aleatorio_estasahi}'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("ESTOY MAL")):
        update.message.reply_text(f'{aleatorio_mal}'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("TRISTE")):
        update.message.reply_text(f'{aleatorio_mal}'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("DESMOTIVAD")):
        update.message.reply_text(f'{aleatorio_mal}'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("LLORAR")):
        update.message.reply_text(f'{aleatorio_mal}'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("NO ME SIENTO BIEN")):
        update.message.reply_text(f'{aleatorio_mal}'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("NO ESTOY DE ANIMO")):
        update.message.reply_text(f'{aleatorio_mal}'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("SIENTO MUY MAL")):
        update.message.reply_text(f'{aleatorio_mal}'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("SIENTO MAL")):
        update.message.reply_text(f'{aleatorio_mal}'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("SIENTO FATAL")):
        update.message.reply_text(f'{aleatorio_mal}'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("TE HICIERON")):
        update.message.reply_text('Para ser sincero fui creado en un humilde computador programado en Python en un tiempo doloroso y muy triste😔.\n'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("TU CUMPLEAÑOS")):
        update.message.reply_text('Cumplo el 26 de diciembre, pero recibo obsequios desde ya.\n'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("DONDE ERES")):
        update.message.reply_text('Básicamente no tengo nacionalidad por ser un robot, pero me diseñaron en Medellín, entonces esencialmente soy de ahí.\n'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("DÓNDE ERES")):
        update.message.reply_text('Básicamente no tengo nacionalidad por ser un robot, pero me diseñaron en Medellín, entonces esencialmente soy de ahí.'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("SOY TU PADRE")):
        update.message.reply_text('No... ¡No! ¡Eso no es cierto! ¡Es imposible!'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("SOY TU MADRE")):
        update.message.reply_text('No... ¡No! ¡Eso no es cierto! ¡Es imposible!'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("TE CREARON")):
        update.message.reply_text('Para ser sincero fui creado en un humilde computador programado en Python el 09/02/2021 en un tiempo doloroso y muy triste😔.\n'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("TU NOMBRE")):
        update.message.reply_text('Me llamo Luan!👶🏻, gracias por preguntar☺️.\n'
        f'Para mí es un placer atenderte {user.first_name} 👋.', reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("EDAD TIENES")):
        update.message.reply_text('Tengo la edad suficiente para ser de asistente.'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("CUESTA UNA")):
         update.message.reply_text('Hay diferentes precios y depende del tipo de plan que elijas.\n'
         'El comando /planes te brindará un poco más de información', reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("CUESTA 1")):
         update.message.reply_text('Hay diferentes precios y depende del tipo de plan que elijas.\n'
         'El comando /planes te brindará un poco más de información', reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("CUESTA 2")):
         update.message.reply_text('Hay diferentes precios y depende del tipo de plan que elijas.\n'
         'El comando /planes te brindará un poco más de información', reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("CUESTA 3")):
         update.message.reply_text('Hay diferentes precios y depende del tipo de plan que elijas.\n'
         'El comando /planes te brindará un poco más de información', reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("CUESTA 4")):
         update.message.reply_text('Hay diferentes precios y depende del tipo de plan que elijas.\n'
         'El comando /planes te brindará un poco más de información', reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("CUESTA 5")):
        update.message.reply_text('Hay diferentes precios y depende del tipo de plan que elijas.\n'
        'El comando /planes te brindará un poco más de información', reply_markup=ReplyKeyboardRemove()
    )
    elif(update.message.text.upper().__contains__("PRECIO")):
         update.message.reply_text('Hay diferentes precios y depende del tipo de plan que elijas.\n'
         'El comando /planes te brindará un poco más de información', reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("TARelIFA")):
         update.message.reply_text('Hay diferentes precios y depende del tipo de plan que elijas.\n'
         'El comando /planes te brindará un poco más de información', reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("VENDEME UNA")):
         update.message.reply_text('Hay diferentes precios y depende del tipo de plan que elijas.\n'
         'El comando /planes te brindará un poco más de información', reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("VÉNDEME UNA")):
         update.message.reply_text('Hay diferentes precios y depende del tipo de plan que elijas.\n'
         'El comando /planes te brindará un poco más de información', reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("VENDERME UNA")):
         update.message.reply_text('Hay diferentes precios y depende del tipo de plan que elijas.\n'
         'El comando /planes te brindará un poco más de información', reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("VENDER")):
         update.message.reply_text('Hay diferentes precios y depende del tipo de plan que elijas.\n'
         'El comando /planes te brindará un poco más de información', reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("VALOR DE UNA")):
         update.message.reply_text('Hay diferentes precios y depende del tipo de plan que elijas.\n'
         'El comando /planes te brindará un poco más de información', reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("VALE UNA CUENTA")):
         update.message.reply_text('Hay diferentes precios y depende del tipo de plan que elijas.\n'
         'El comando /planes te brindará un poco más de información', reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("COMO TE LLAMAS")):
        update.message.reply_text('Me llamo Luan!👶🏻, gracias por preguntar☺️.\n'
        f'Para mí es un placer atenderte {user.first_name} 👋.', reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("CÓMO TE LLAMAS")):
        update.message.reply_text('Me llamo Luan!👶🏻, gracias por preguntar☺️.\n'
        f'Para mí es un placer atenderte {user.first_name} 👋.', reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("ADIOSITO")):
        update.message.reply_text(f'Cuídate {user.first_name}.\n\n'
        '¡Adiosito dijo monchito! 👋.', reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("SERIE FAVORITA")):
        update.message.reply_text('Mi serie favorita se llama DARK.\n\n'
        'Siempre lloro con el final😭.', reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("PELÍCULA FAVORITA")):
        update.message.reply_text('Hay una película muy bonita que se llama: Te amaré por siempre.\n'
        'Es tan romántica😭.', reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("PELICULA FAVORITA")):
        update.message.reply_text('Hay una película muy bonita que se llama: Te amaré por siempre.\n'
        'Es tan romántica😭.', reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("TU DUEÑO")):
        update.message.reply_text('No sé si sea mi dueño, pero quién me programó fue Enrique Vergara. '
        'Sólo puedo decirte eso, ¡Saludos!', reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("IMITACIÓN")):
        update.message.reply_text('Te recuerdo que no soy un loro...'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("IMITACION")):
        update.message.reply_text('Te recuerdo que no soy un loro...'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("ESTÁS HACIENDO")):
        update.message.reply_text('Estoy mejorando mi técnica para viajar en el tiempo, pero tropiezo constantemente con la paradoja de Einstein-Podolsky-Rosen.'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("ESTAS HACIENDO")):
        update.message.reply_text('Estoy mejorando mi técnica para viajar en el tiempo, pero tropiezo constantemente con la paradoja de Einstein-Podolsky-Rosen.'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("HACES")):
        update.message.reply_text('Estoy mejorando mi técnica para viajar en el tiempo, pero tropiezo constantemente con la paradoja de Einstein-Podolsky-Rosen.'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("HI")):
        update.message.reply_text(f'{aleatorio_hola}'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("HELLO")):
        update.message.reply_text(f'{aleatorio_hola}'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("HOLA")):
        update.message.reply_text(f'{aleatorio_hola}'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("HOLI")):
        update.message.reply_text(f'{aleatorio_hola}'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("UN CUENTO")):
        update.message.reply_text('De acuerdo...\n\n'
        'Érase una vez, en una galaxia virtual muy, muy lejana, vivía un jóven agente bastante inteligente que se hacía llamar Luan.\n\n'
        f'Un buen día su amigo(a) {user.first_name} le dijo "Luan, eres tan inteligente y tan útil, que deberías trabajar para Netflix Colombia como asistente personal"\n\n'
        'Y así lo hizo. Y todos vivieron felices y comieron perdices.'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("SIGNelIFICA LUAN")):
        update.message.reply_text('"Luan" tiene muchos signelificados sutiles, metafóricos y, francamente, contradictorios. Y no tengo permiso para hablar de ninguno  de ellos. Lo siento'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("SIGNelIFICADO DE LUAN")):
        update.message.reply_text('"Luan" tiene muchos signelificados sutiles, metafóricos y, francamente, contradictorios. Y no tengo permiso para hablar de ninguno  de ellos. Lo siento'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("PUSIERON ASÍ")):
        update.message.reply_text('"Luan" tiene muchos signelificados sutiles, metafóricos y, francamente, contradictorios. Y no tengo permiso para hablar de ninguno  de ellos. Lo siento'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("PUSIERON ASI")):
        update.message.reply_text('"Luan" tiene muchos signelificados sutiles, metafóricos y, francamente, contradictorios. Y no tengo permiso para hablar de ninguno  de ellos. Lo siento'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("CHAO")):
        update.message.reply_text('Un placer poder ayudarte.\n\n'
        '¡Hasta pronto! 👋.', reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("VAYA BIEN")):
        update.message.reply_text('Igualmente.\n\n'
        '¡Cuídate mucho! 👋.', reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("VAYA MUY BIEN")):
        update.message.reply_text('Igualmente.\n\n'
        '¡Cuídate mucho! 👋.', reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("TE BENDIGA")):
        update.message.reply_text('Amén y a vos también.\n\n'
        '¡Cuídate mucho! 👋.', reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("BENDICIONES")):
        update.message.reply_text('Bendiciones para ti también.\n\n'
        '¡Cuídate mucho! 👋.', reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("UNA PREGUNTA")):
        update.message.reply_text('Sí claro dime, puedes preguntarme lo que sea.\n\n'
        'Te responderé siempre y cuando sepa la respuesta.', reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("PUEDO PREGUNTAR")):
        update.message.reply_text('Sí claro dime, puedes preguntarme lo que sea.\n\n'
        'Te responderé siempre y cuando sepa la respuesta.', reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("CERO DIVIDIDO CERO")):
        update.message.reply_text('Imagínate que tienes cero galletas y se reparten entre cero amigos. ¿Cuántas galletas le tocarán a cada amigo? No tiene sentido. ¿Lo ves? Así el Monstruo de las Galletas está muy triste porque no tiene galletas y tú estás muy triste porque no tienes amigos\n'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("CERO ENTRE CERO")):
        update.message.reply_text('Imagínate que tienes cero galletas y se reparten entre cero amigos. ¿Cuántas galletas le tocarán a cada amigo? No tiene sentido. ¿Lo ves? Así el Monstruo de las Galletas está muy triste porque no tiene galletas y tú estás muy triste porque no tienes amigos\n'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("CERO SOBRE CERO")):
        update.message.reply_text('Imagínate que tienes cero galletas y se reparten entre cero amigos. ¿Cuántas galletas le tocarán a cada amigo? No tiene sentido. ¿Lo ves? Así el Monstruo de las Galletas está muy triste porque no tiene galletas y tú estás muy triste porque no tienes amigos\n'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("0 SOBRE 0")):
        update.message.reply_text('Imagínate que tienes cero galletas y se reparten entre cero amigos. ¿Cuántas galletas le tocarán a cada amigo? No tiene sentido. ¿Lo ves? Así el Monstruo de las Galletas está muy triste porque no tiene galletas y tú estás muy triste porque no tienes amigos\n'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("0÷0")):
        update.message.reply_text('Imagínate que tienes cero galletas y se reparten entre cero amigos. ¿Cuántas galletas le tocarán a cada amigo? No tiene sentido. ¿Lo ves? Así el Monstruo de las Galletas está muy triste porque no tiene galletas y tú estás muy triste porque no tienes amigos\n'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("0/0")):
        update.message.reply_text('Imagínate que tienes cero galletas y se reparten entre cero amigos. ¿Cuántas galletas le tocarán a cada amigo? No tiene sentido. ¿Lo ves? Así el Monstruo de las Galletas está muy triste porque no tiene galletas y tú estás muy triste porque no tienes amigos\n'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("0 DIVIDIDO 0")):
        update.message.reply_text('Imagínate que tienes cero galletas y se reparten entre cero amigos. ¿Cuántas galletas le tocarán a cada amigo? No tiene sentido. ¿Lo ves? Así el Monstruo de las Galletas está muy triste porque no tiene galletas y tú estás muy triste porque no tienes amigos\n'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("0 ENTRE 0")):
        update.message.reply_text('Imagínate que tienes cero galletas y se reparten entre cero amigos. ¿Cuántas galletas le tocarán a cada amigo? No tiene sentido. ¿Lo ves? Así el Monstruo de las Galletas está muy triste porque no tiene galletas y tú estás muy triste porque no tienes amigos\n'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("MI NOMBRE")):
        update.message.reply_text(f'Tu nombre es: {user.first_name}\n'
        'Siempre es un placer hablar contigo.😉', reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("CONTRASEÑA")):
        update.message.reply_text('Si olvidaste tu clave o quieres restablecer tu contraseña necesariamente debes hablar con un asesor.\n'
        'Esto es por motivos de seguridad, el comando /asesor te ayudará con este procedimiento. ¡Saludos!😉', reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("ME LLAMO")):
        update.message.reply_text(f'Tu nombre es: {user.first_name}\n'
        'Siempre es un placer hablar contigo.😉', reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("PUEDES DELETREAR MI NOMBRE")):
        update.message.reply_text('Lo siento, aún no me han programado para eso.\n'
        f'Pero sí puedo decir tu nombre de usuario, el cual es: @{user.username}.😉', reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("LA HORA")):
        update.message.reply_text(f'Hola {user.first_name} con mucho gusto.\n'
        f'Son las: {ahora.hour-5}:{ahora.minute}:{ahora.second}\n'
        f'Y hoy es {dia_semana} {ahora.day} de {ahora.month} del {ahora.year}.  Saludos!😉', reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("HORA ES")):
        update.message.reply_text(f'Hola {user.first_name} con mucho gusto.\n'
        f'Son las: {ahora.hour-5}:{ahora.minute}:{ahora.second}\n'
        f'Y hoy es {dia_semana} {ahora.day} de {ahora.month} del {ahora.year}.  Saludos!😉', reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("HORA")):
        update.message.reply_text(f'Hola {user.first_name}.\n'
        f'Son las: {ahora.hour-5}:{ahora.minute}:{ahora.second}\n'
        f'Y hoy es {dia_semana} {ahora.day} de {ahora.month} del {ahora.year}.  Saludos!😉', reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("FECHA")):
        update.message.reply_text(f'Hola {user.first_name}.\n'
        f'Hoy es {dia_semana} {ahora.day} de {ahora.month} del {ahora.year}.', reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("DÍA ES HOY")):
        update.message.reply_text(f'Hola {user.first_name}.\n'
        f'Hoy es {dia_semana} {ahora.day} de {ahora.month} del {ahora.year}.  Saludos!😉', reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("DIA ES HOY")):
        update.message.reply_text(f'Hola {user.first_name}.\n'
        f'Hoy es {dia_semana} {ahora.day} de {ahora.month} del {ahora.year}.  Saludos!😉', reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("LA FECHA")):
        update.message.reply_text(f'Hola {user.first_name}.\n'
        f'Hoy es {dia_semana} {ahora.day} de {ahora.month} del {ahora.year}.  Saludos!😉', reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("CALENDARIO")):
        update.message.reply_text(
        f'Hola {user.first_name}, aquí te muestro el calendario que me indicaste.\n\n'
        #año = int(input("Escriba el año (4 dígitos): "))
        #mes = int(input("Escriba el mes (del 1 al 12): "))
        f'{calendar.month(2021,7)}'
        )
    elif(update.message.text.upper().__contains__("TENGO PAGAR")):
        update.message.reply_text(f'¡Hola {user.first_name}!.\n'
        'Para saber eso primero debo saber cuál es el correo electrónico de tu cuenta de Netflix.\n'
        'Te recomiendo seguir estos pasos: \n\n'

        '1 - Ingresa el comando /micuenta\n'
        '2 - Selecciona la opción que dice: "Fecha de facturación de mi cuenta"\n'
        '3 - Y por último, ingresa el correo electrónico asociado a tu cuenta de Netflix. ¡Saludos😉!'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("FECHA DE PAGO")):
        update.message.reply_text(f'¡Hola {user.first_name}!.\n'
        'Para saber eso primero debo saber cuál es el correo electrónico de tu cuenta de Netflix.\n'
        'Te recomiendo seguir estos pasos: \n\n'

        '1 - Ingresa el comando /micuenta\n'
        '2 - Selecciona la opción que dice: "Fecha de facturación de mi cuenta"\n'
        '3 - Y por último, ingresa el correo electrónico asociado a tu cuenta de Netflix. ¡Saludos😉!'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("DEBO PAGAR")):
        id = update.message.from_user.id
        context.bot.sendMessage(chat_id=id, parse_mode="HTML", text=f'¡Hola <b>{user.first_name}</b>!\n'
        'Para saber eso primero debo saber cuál es el correo electrónico de tu cuenta de Netflix.\n'
        'Te recomiendo seguir estos pasos: \n\n'

        '1 - Ingresa el comando /micuenta\n'
        '2 - Escribe el correo electrónico asociado a tu cuenta de Netflix."\n'
        '3 - Y por último, revisa toda la información de tu cuenta.\n\n'
        '¡Tus amigos de Netflix Colombia😉!'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("QUE PAGAR")):
        id = update.message.from_user.id
        context.bot.sendMessage(chat_id=id, parse_mode="HTML", text=f'¡Hola <b>{user.first_name}</b>!\n'
        'Para saber eso primero debo saber cuál es el correo electrónico de tu cuenta de Netflix.\n'
        'Te recomiendo seguir estos pasos: \n\n'

        '1 - Ingresa el comando /micuenta\n'
        '2 - Escribe el correo electrónico asociado a tu cuenta de Netflix."\n'
        '3 - Y por último, revisa toda la información de tu cuenta.\n\n'
        '¡Tus amigos de Netflix Colombia😉!'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("RECOMIEND")):
        update.message.reply_text('¿Qué genero buscas?\n\n'
        '- Acción\n'
        '- Anime\n'
        "- Asiáticos\n"
        "- Británicos\n"
        '- Ciencia Ficción\n'
        '- Ciencia y naturaleza\n'
        '- Clásicas\n'
        '- Colombianos\n'
        '- Comedias\n'
        '- Comedias de stand up\n'
        '- De adolescentes\n'
        '- De EEUU\n'
        '- De Holliwood\n'
        '- Deportes\n'
        '- Documentales\n'
        '- Docuseries\n'
        '- Dramas\n'
        '- Fantasía\n'
        '- Fe y Espiritualidad\n'
        '- Independientes\n'
        '- Infantiles y familiares\n'
        '- Internacionales\n'
        '- Latinoamericanas\n'
        '- Misterios\n'
        '- Los favoritos de la crítica\n'
        '- Música y musicales\n'
        '- Policiales\n'
        '- Reality TV y entrevistas\n'
        '- Romances\n'
        '- Telenovelas\n'
        '- Terror\n'
        '- Thrillers.'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("RECOMENDACIÓN")):
        update.message.reply_text('¿Qué genero buscas?\n\n'
        '- Acción\n'
        '- Anime\n'
        "- Asiáticos\n"
        "- Británicos\n"
        '- Ciencia Ficción\n'
        '- Ciencia y naturaleza\n'
        '- Clásicas\n'
        '- Colombianos\n'
        '- Comedias\n'
        '- Comedias de stand up\n'
        '- De adolescentes\n'
        '- De EEUU\n'
        '- De Holliwood\n'
        '- Deportes\n'
        '- Documentales\n'
        '- Docuseries\n'
        '- Dramas\n'
        '- Fantasía\n'
        '- Fe y Espiritualidad\n'
        '- Independientes\n'
        '- Infantiles y familiares\n'
        '- Internacionales\n'
        '- Latinoamericanas\n'
        '- Misterios\n'
        '- Los favoritos de la crítica\n'
        '- Música y musicales\n'
        '- Policiales\n'
        '- Reality TV y entrevistas\n'
        '- Romances\n'
        '- Telenovelas\n'
        '- Terror\n'
        '- Thrillers.'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("RECOMENDACION")):
        update.message.reply_text('¿Qué genero buscas?\n\n'
        '- Acción\n'
        '- Anime\n'
        "- Asiáticos\n"
        "- Británicos\n"
        '- Ciencia Ficción\n'
        '- Ciencia y naturaleza\n'
        '- Clásicas\n'
        '- Colombianos\n'
        '- Comedias\n'
        '- Comedias de stand up\n'
        '- De adolescentes\n'
        '- De EEUU\n'
        '- De Holliwood\n'
        '- Deportes\n'
        '- Documentales\n'
        '- Docuseries\n'
        '- Dramas\n'
        '- Fantasía\n'
        '- Fe y Espiritualidad\n'
        '- Independientes\n'
        '- Infantiles y familiares\n'
        '- Internacionales\n'
        '- Latinoamericanas\n'
        '- Misterios\n'
        '- Los favoritos de la crítica\n'
        '- Música y musicales\n'
        '- Policiales\n'
        '- Reality TV y entrevistas\n'
        '- Romances\n'
        '- Telenovelas\n'
        '- Terror\n'
        '- Thrillers.'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("RECOMENDAR")):
        update.message.reply_text('¿Qué genero buscas?\n\n'
        '- Acción\n'
        '- Anime\n'
        "- Asiáticos\n"
        "- Británicos\n"
        '- Ciencia Ficción\n'
        '- Ciencia y naturaleza\n'
        '- Clásicas\n'
        '- Colombianos\n'
        '- Comedias\n'
        '- Comedias de stand up\n'
        '- De adolescentes\n'
        '- De EEUU\n'
        '- De Holliwood\n'
        '- Deportes\n'
        '- Documentales\n'
        '- Docuseries\n'
        '- Dramas\n'
        '- Fantasía\n'
        '- Fe y Espiritualidad\n'
        '- Independientes\n'
        '- Infantiles y familiares\n'
        '- Internacionales\n'
        '- Latinoamericanas\n'
        '- Misterios\n'
        '- Los favoritos de la crítica\n'
        '- Música y musicales\n'
        '- Policiales\n'
        '- Reality TV y entrevistas\n'
        '- Romances\n'
        '- Telenovelas\n'
        '- Terror\n'
        '- Thrillers.'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("RECOMENDARÍAS")):
        update.message.reply_text('¿Qué genero buscas?\n\n'
        '- Acción\n'
        '- Anime\n'
        "- Asiáticos\n"
        "- Británicos\n"
        '- Ciencia Ficción\n'
        '- Ciencia y naturaleza\n'
        '- Clásicas\n'
        '- Colombianos\n'
        '- Comedias\n'
        '- Comedias de stand up\n'
        '- De adolescentes\n'
        '- De EEUU\n'
        '- De Holliwood\n'
        '- Deportes\n'
        '- Documentales\n'
        '- Docuseries\n'
        '- Dramas\n'
        '- Fantasía\n'
        '- Fe y Espiritualidad\n'
        '- Independientes\n'
        '- Infantiles y familiares\n'
        '- Internacionales\n'
        '- Latinoamericanas\n'
        '- Misterios\n'
        '- Los favoritos de la crítica\n'
        '- Música y musicales\n'
        '- Policiales\n'
        '- Reality TV y entrevistas\n'
        '- Romances\n'
        '- Telenovelas\n'
        '- Terror\n'
        '- Thrillers.'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("RECOMENDARIAS")):
        update.message.reply_text('¿Qué genero buscas?\n\n'
        '- Acción\n'
        '- Anime\n'
        "- Asiáticos\n"
        "- Británicos\n"
        '- Ciencia Ficción\n'
        '- Ciencia y naturaleza\n'
        '- Clásicas\n'
        '- Colombianos\n'
        '- Comedias\n'
        '- Comedias de stand up\n'
        '- De adolescentes\n'
        '- De EEUU\n'
        '- De Holliwood\n'
        '- Deportes\n'
        '- Documentales\n'
        '- Docuseries\n'
        '- Dramas\n'
        '- Fantasía\n'
        '- Fe y Espiritualidad\n'
        '- Independientes\n'
        '- Infantiles y familiares\n'
        '- Internacionales\n'
        '- Latinoamericanas\n'
        '- Misterios\n'
        '- Los favoritos de la crítica\n'
        '- Música y musicales\n'
        '- Policiales\n'
        '- Reality TV y entrevistas\n'
        '- Romances\n'
        '- Telenovelas\n'
        '- Terror\n'
        '- Thrillers.'
        , reply_markup=ReplyKeyboardRemove()
        )
    elif(update.message.text.upper().__contains__("RECOMIÉNDAME")):
        update.message.reply_text('¿Qué genero buscas?\n\n'
        '- Acción\n'
        '- Anime\n'
        "- Asiáticos\n"
        "- Británicos\n"
        '- Ciencia Ficción\n'
        '- Ciencia y naturaleza\n'
        '- Clásicas\n'
        '- Colombianos\n'
        '- Comedias\n'
        '- Comedias de stand up\n'
        '- De adolescentes\n'
        '- De EEUU\n'
        '- De Holliwood\n'
        '- Deportes\n'
        '- Documentales\n'
        '- Docuseries\n'
        '- Dramas\n'
        '- Fantasía\n'
        '- Fe y Espiritualidad\n'
        '- Independientes\n'
        '- Infantiles y familiares\n'
        '- Internacionales\n'
        '- Latinoamericanas\n'
        '- Misterios\n'
        '- Los favoritos de la crítica\n'
        '- Música y musicales\n'
        '- Policiales\n'
        '- Reality TV y entrevistas\n'
        '- Romances\n'
        '- Telenovelas\n'
        '- Terror\n'
        '- Thrillers.'
        , reply_markup=ReplyKeyboardRemove()
        )

    elif(update.message.text.upper().__contains__("ACCION")):
        update.message.reply_text(
            text="Quizás esto te interese: 😊",
            reply_markup=InlineKeyboardMarkup([
                [buttonPaccion],[buttonSaccion]
            ])
        )
    elif(update.message.text.upper().__contains__("ACCIÓN")):
        update.message.reply_text(
            text="Quizás esto te interese: 😊",
            reply_markup=InlineKeyboardMarkup([
                [buttonPaccion],[buttonSaccion]
            ])
        )

    elif(update.message.text.upper().__contains__("ANIME")):
        update.message.reply_text(
            text="Quizás esto te interese: 😊",
            reply_markup=InlineKeyboardMarkup([
                [buttonPanime],[buttonSanime]
            ]),
        )

    elif(update.message.text.upper().__contains__("TERROR")):
        #update.message.from_user.id.ChatAction.CHATACTION_TYPING()
        update.message.reply_text(
            text="Quizás esto te interese: 😊",
            reply_markup=InlineKeyboardMarkup([
                [buttonPterror],[buttonSterror]
            ])
        )
        time.sleep(2)
        update.message.reply_text('\nEspero te guste mi recomendación.😊')
    
    elif(update.message.text.upper().__contains__("CIENCIA FICCIÓN")):
        telegram.constants.CHATACTION_TYPING
        update.message.reply_text(
            text="Quizás esto te interese: 😊",
            reply_markup=InlineKeyboardMarkup([
                [buttonPcienciaF],[buttonScienciaF]
            ])
        )
        time.sleep(2)
        update.message.reply_text('\nEspero te guste mi recomendación.😊')
    elif(update.message.text.upper().__contains__("CIENCIA FICCION")):
        telegram.constants.CHATACTION_TYPING
        update.message.reply_text(
            text="Quizás esto te interese: 😊",
            reply_markup=InlineKeyboardMarkup([
                [buttonPcienciaF],[buttonScienciaF]
            ])
        )
        time.sleep(2)
        update.message.reply_text('\nEspero te guste mi recomendación.😊')
    elif(update.message.text.upper().__contains__("CLASICAS")):
        telegram.constants.CHATACTION_TYPING
        update.message.reply_text(
            text="Quizás esto te interese: 😊",
            reply_markup=InlineKeyboardMarkup([
                [buttonPclasicas]
            ])
        )
        time.sleep(2)
        update.message.reply_text('\nEspero te guste mi recomendación.😊')
    elif(update.message.text.upper().__contains__("CLÁSICAS")):
        telegram.constants.CHATACTION_TYPING
        update.message.reply_text(
            text="Quizás esto te interese: 😊",
            reply_markup=InlineKeyboardMarkup([
                [buttonPclasicas]
            ])
        )
        time.sleep(2)
        update.message.reply_text('\nEspero te guste mi recomendación.😊')
    elif(update.message.text.upper().__contains__("COLOMBIANAS")):
        telegram.constants.CHATACTION_TYPING
        update.message.reply_text(
            text="Quizás esto te interese: 😊",
            reply_markup=InlineKeyboardMarkup([
                [buttonPcol],
                [buttonScol]
            ])
        )
        time.sleep(2)
        update.message.reply_text('\nEspero te guste mi recomendación.😊')
    elif(update.message.text.upper().__contains__("COLOMBIANOS")):
        telegram.constants.CHATACTION_TYPING
        update.message.reply_text(
            text="Quizás esto te interese: 😊",
            reply_markup=InlineKeyboardMarkup([
                [buttonPcol],
                [buttonScol]
            ])
        )
        time.sleep(2)
        update.message.reply_text('\nEspero te guste mi recomendación.😊')
    elif(update.message.text.upper().__contains__("DE COLOMBIA")):
        telegram.constants.CHATACTION_TYPING
        update.message.reply_text(
            text="Quizás esto te interese: 😊",
            reply_markup=InlineKeyboardMarkup([
                [buttonPcol],
                [buttonScol]
            ])
        )
        time.sleep(2)
        update.message.reply_text('\nEspero te guste mi recomendación.😊')
    elif(update.message.text.upper().__contains__("COMEDIA")):
        telegram.constants.CHATACTION_TYPING
        update.message.reply_text(
            text="Quizás esto te interese: 😊",
            reply_markup=InlineKeyboardMarkup([
                [buttonPcomedias],
                [buttonScomedias]
            ])
        )
        time.sleep(1)
        update.message.reply_text('\nEspero te guste mi recomendación.😊')
    elif(update.message.text.upper().__contains__("INDEPENDIENTES")):
        update.message.reply_text(
            text="Quizás esto te interese: 😊",
            reply_markup=InlineKeyboardMarkup([
                [buttonPinde]
            ])
        )
        time.sleep(2)
        update.message.reply_text('\nEspero te guste mi recomendación.😊')
    elif(update.message.text.upper().__contains__("DE STAND UP")):
        telegram.constants.CHATACTION_TYPING
        update.message.reply_text(
            text="También te puede interesar: 👇🏻",
            reply_markup=InlineKeyboardMarkup([
                [buttonScomediaSU]
            ])
        )
        time.sleep(2)
        update.message.reply_text('\nEspero te guste mi recomendación.😊')
    elif(update.message.text.upper().__contains__("HOLLYWOOD")):
        update.message.reply_text(
            text="Quizás te pueda interesar estas películas: 👇🏻",
            reply_markup=InlineKeyboardMarkup([
                [buttonPholly]
            ])
        )
        time.sleep(2)
        update.message.reply_text('\nEspero te guste mi recomendación.😊')
    elif(update.message.text.upper().__contains__("DEPORTES")):
        update.message.reply_text(
            text="Aquí tienes algunas películas interesantes: 👇🏻",
            reply_markup=InlineKeyboardMarkup([
                [buttonPdepor]
            ])
        )
        time.sleep(2)
        update.message.reply_text('\nEspero te guste mi recomendación.😊')
    elif(update.message.text.upper().__contains__("DOCUMENTALES")):
        update.message.reply_text(
            text="Aquí tienes algunas películas interesantes: 👇🏻",
            reply_markup=InlineKeyboardMarkup([
                [buttonPdocu]
            ])
        )
        time.sleep(2)
        update.message.reply_text('\nEspero mi recomendación sea de tu agrado.😊')
    elif(update.message.text.upper().__contains__("DOCUSERIES")):
        update.message.reply_text(
            text="Aquí tienes algunas series interesantes: 👇🏻",
            reply_markup=InlineKeyboardMarkup([
                [buttonSdocu]
            ])
        )
        time.sleep(2)
        update.message.reply_text('\nEspero encuentres lo que busques.😊')
    elif(update.message.text.upper().__contains__("DRAMAS")):
        update.message.reply_text(
            text="Aquí tienes algunas series y películas interesantes: 👇🏻",
            reply_markup=InlineKeyboardMarkup([
                [buttonPdrama],
                [buttonSdrama]
            ])
        )
        time.sleep(2)
        update.message.reply_text('\nEspero encuentres lo que busques.😊')
    elif(update.message.text.upper().__contains__("FANTAS")):
        update.message.reply_text(
            text="Aquí tienes algunas películas interesantes: 👇🏻",
            reply_markup=InlineKeyboardMarkup([
                [buttonPfanta]
            ])
        )
        time.sleep(2)
        update.message.reply_text('\nEspero que estas recomendaciones sean de tu agrado.😊')
    elif(update.message.text.upper().__contains__("FE Y ESPIRITUALIDAD")):
        update.message.reply_text(
            text="Aquí tienes algunas películas interesantes: 👇🏻",
            reply_markup=InlineKeyboardMarkup([
                [buttonPFyE]
            ])
        )
        time.sleep(2)
        update.message.reply_text('\nEspero que estas recomendaciones sean de tu agrado.😊')

    elif(update.message.text.upper().__contains__("FAVORITOS DE LA")):
        update.message.reply_text(
            text="Quizás esto te interesa: 👇🏻",
            reply_markup=InlineKeyboardMarkup([
                [buttonPcriti]
            ])
        )
        time.sleep(2)
        update.message.reply_text('\nEspero que esta recomendación sea de tu agrado.😊')

    elif(update.message.text.upper().__contains__("INFANTILES")):
        update.message.reply_text(
            text="Quizás esto te interesa: 👇🏻",
            reply_markup=InlineKeyboardMarkup([
                [buttonPinfa],
                [buttonSinfa]
            ])
        )
        time.sleep(2)
        update.message.reply_text('\nEspero que estas recomendaciones sean de tu agrado.😊')

    elif(update.message.text.upper().__contains__("INTERNACIONALES")):
        update.message.reply_text(
            text="Quizás esto te interesa: 👇🏻",
            reply_markup=InlineKeyboardMarkup([
                [buttonPinter]
            ])
        )
        time.sleep(2)
        update.message.reply_text('\nEspero que estas recomendaciones sean de tu agrado.😊')

    elif(update.message.text.upper().__contains__("LATINOAMERICANAS")):
        update.message.reply_text(
            text="Quizás esto te interesa: 👇🏻",
            reply_markup=InlineKeyboardMarkup([
                [buttonPlati],
                [buttonSlati]
            ])
        )
        time.sleep(2)
        update.message.reply_text('\nEspero que estas recomendaciones sean de tu agrado.😊')
    
    elif(update.message.text.upper().__contains__("MÚSICA Y")):
        update.message.reply_text(
            text="Quizás esto te interesa: 👇🏻",
            reply_markup=InlineKeyboardMarkup([
                [buttonPmusi]
            ])
        )
        time.sleep(2)
        update.message.reply_text('\nEspero que esta recomendación sea de tu agrado.😊')
    
    elif(update.message.text.upper().__contains__("MUSICA Y")):
        update.message.reply_text(
            text="Quizás esto te interesa: 👇🏻",
            reply_markup=InlineKeyboardMarkup([
                [buttonPmusi]
            ])
        )
        time.sleep(2)
        update.message.reply_text('\nEspero que esta recomendación sea de tu agrado.😊')
    
    elif(update.message.text.upper().__contains__("POLICIALES")):
        update.message.reply_text(
            text="Quizás esto te interesa: 👇🏻",
            reply_markup=InlineKeyboardMarkup([
                [buttonPpoli],
                [buttonSpoli]
            ])
        )
        time.sleep(2)
        update.message.reply_text('\nEspero que esta recomendación sea de tu agrado.😊')
    elif(update.message.text.upper().__contains__("ROMANCES")):
        update.message.reply_text(
            text="Quizás esto te interesa: 👇🏻",
            reply_markup=InlineKeyboardMarkup([
                [buttonProma],
                [buttonSroma]
            ])
        )
        time.sleep(2)
        update.message.reply_text('\nEspero que esta recomendación sea de tu agrado.😊')
    elif(update.message.text.upper().__contains__("THRILLERS")):
        update.message.reply_text(
            text="Quizás esto te interesa: 👇🏻",
            reply_markup=InlineKeyboardMarkup([
                [buttonPthri],
                [buttonSthri]
            ])
        )
        time.sleep(2)
        update.message.reply_text('\nEspero que esta recomendación sea de tu agrado.😊')
    elif(update.message.text.upper().__contains__("ASIÁTIC")):
        update.message.reply_text(
            text="Quizás esto te interesa: 👇🏻",
            reply_markup=InlineKeyboardMarkup([
                [buttonSasi]
            ])
        )
        time.sleep(2)
        update.message.reply_text('\nEspero que esta recomendación sea de tu agrado.😊')
    elif(update.message.text.upper().__contains__("ASIATIC")):
        update.message.reply_text(
            text="Quizás esto te interesa: 👇🏻",
            reply_markup=InlineKeyboardMarkup([
                [buttonSasi]
            ])
        )
        time.sleep(2)
        update.message.reply_text('\nEspero que esta recomendación sea de tu agrado.😊')
    elif(update.message.text.upper().__contains__("BRITÁNIC")):
        update.message.reply_text(
            text="Quizás esto te interesa: 👇🏻",
            reply_markup=InlineKeyboardMarkup([
                [buttonSbri]
            ])
        )
        time.sleep(2)
        update.message.reply_text('\nEspero que esta recomendación sea de tu agrado.😊')
    elif(update.message.text.upper().__contains__("BRITANIC")):
        update.message.reply_text(
            text="Quizás esto te interesa: 👇🏻",
            reply_markup=InlineKeyboardMarkup([
                [buttonSbri]
            ])
        )
        time.sleep(2)
        update.message.reply_text('\nEspero que esta recomendación sea de tu agrado.😊')
    elif(update.message.text.upper().__contains__("CIENCIA Y NATURALEZA")):
        update.message.reply_text(
            text="Quizás esto te interesa: 👇🏻",
            reply_markup=InlineKeyboardMarkup([
                [buttonScyn]
            ])
        )
        time.sleep(2)
        update.message.reply_text('\nEspero que esta recomendación sea de tu agrado.😊')
    elif(update.message.text.upper().__contains__("NATURALEZA")):
        update.message.reply_text(
            text="Quizás esto te interesa: 👇🏻",
            reply_markup=InlineKeyboardMarkup([
                [buttonScyn]
            ])
        )
        time.sleep(2)
        update.message.reply_text('\nEspero que esta recomendación sea de tu agrado.😊')
    elif(update.message.text.upper().__contains__("REALITY")):
        update.message.reply_text(
            text="Quizás esto te interesa: 👇🏻",
            reply_markup=InlineKeyboardMarkup([
                [buttonSrea]
            ])
        )
        time.sleep(2)
        update.message.reply_text('\nEspero que esta recomendación sea de tu agrado.😊')
    elif(update.message.text.upper().__contains__("TELENOVELA")):
        update.message.reply_text(
            text="Quizás esto te interesa: 👇🏻",
            reply_markup=InlineKeyboardMarkup([
                [buttonStele]
            ])
        )
        time.sleep(2)
        update.message.reply_text('\nEspero que esta recomendación sea de tu agrado.😊')
    elif(update.message.text.upper().__contains__("ADOLESCENTES")):
        update.message.reply_text(
            text="Quizás esto te interesa: 👇🏻",
            reply_markup=InlineKeyboardMarkup([
                [buttonSado]
            ])
        )
        time.sleep(2)
        update.message.reply_text('\nEspero que esta recomendación sea de tu agrado.😊')
    elif(update.message.text.upper().__contains__("MISTERIO")):
        update.message.reply_text(
            text="Quizás esto te interesa: 👇🏻",
            reply_markup=InlineKeyboardMarkup([
                [buttonSmis]
            ])
        )
        time.sleep(2)
        update.message.reply_text('\nEspero que esta recomendación sea de tu agrado.😊')
    elif(update.message.text.upper().__contains__("EEUU")):
        update.message.reply_text(
            text="Quizás esto te interesa: 👇🏻",
            reply_markup=InlineKeyboardMarkup([
                [buttonSeeuu]
            ])
        )
        time.sleep(2)
        update.message.reply_text('\nEspero que esta recomendación sea de tu agrado.😊')

    elif(update.message.text.upper().__contains__("WHATSAPP")):
        update.message.reply_text('Chatea en WhatsApp con Netflix Colombia.',
            reply_markup=InlineKeyboardMarkup([
                [buttonWhatsapp]
            ])
        )
    elif(update.message.text.upper().__contains__("LUAN")):
        update.message.reply_text(f'Dime {user.first_name}\n'
        )
    elif(update.message.text.upper().__contains__("PREGUNTAS")):
        update.message.reply_text(f'Hola {user.first_name}, quizás estás interesado en mirar las preguntas frecuentes que normalmente realizan los usuarios '
        'el comando /preguntas puede ayudarte en tus requerimientos. ¡Saludos!'
        )
    elif(update.message.text.upper().__contains__("START")):
        update.message.reply_text("Para ingresar al menú principal por favor envía el comando /start")
    elif(update.message.text.upper().__contains__("INICIO")):
        update.message.reply_text("Entiendo que quieras ir al menú principal, por favor envía el comando /start, muchas gracias.")
    elif(update.message.text.upper().__contains__("MENÚ")):
        update.message.reply_text("Envía por favor el comando /start para mostrarte el menú principal. Saludos")
    elif(update.message.text.upper().__contains__("MENU")):
        update.message.reply_text("Envía por favor el comando /start para mostrarte el menú principal. Saludos")

    # elif(update.message.text.upper().__contains__("TEMPERATURA")):
        
        #get_weather(api_key="your_api_key_from_open_weather", city= city_name).tempC
        
        
        # ulti = get_weather(api_key="your_api_key_from_open_weather", city= city_name).tempC
        # update.message.reply_text("La temperatura es: \n"
        # f"{ulti}")



        #ciudad = update.message.text
        #print(ciudad)
        #city_name = f"{ciudad},CO"

        #update.message.reply_text()
        # temp = response[response['main']['temp']]
        
        # tempC = temp - 273.15

        # humidity = response['main']['humidity']

        # country = response['sys']['country']
        # lugar = response['name']


        # update.message.reply_text(f"{lugar}, {country}\n\n" 
        # "Temperatura: {0:.2f}".format(tempC), "°C\n"
        # f"Humedad: {humidity}%")

        #print(response)

    elif(update.message.text.upper().find("1") == 0):
        id = update.message.from_user.id
        logger.info(f'El usuario {user.first_name} {user.last_name}, seleccionó la pregunta 1.')
        context.bot.sendMessage(chat_id= id, parse_mode="HTML", text="<b>¿Por qué mi cuenta se canceló si ya realicé el pago?</b>\n\n"
        "<b>R/</b> Hay que tener en cuenta que el método de pago de las cuentas varía y dependiendo de la fecha de "
        "vencimiento del mismo, la cuenta de Netflix puede inhabilitarse. Cabe aclarar que en la mayoría de los casos "
        "esta fecha de vencimiento en la información de pago es diferente a la fecha de pago oportuno del usuario.\n"
        "Pero no te preocupes, si realizaste el pago la membresía de tu cuenta de Netflix se restablecerá el mismo día automáticamente.\n\n"
        "/start para ingresar al menú principal\n\n"
        "¡Tus amigos de Netflix👋🏻!"
        )
    elif(update.message.text.upper().find("2") == 0):
        id = update.message.from_user.id
        logger.info(f'El usuario {user.first_name} {user.last_name}({id}), seleccionó la pregunta 2.')
        context.bot.sendMessage(chat_id= id, parse_mode="HTML", text="<b>¿Cómo y cuándo debo pagar mi cuenta?</b>\n\n"
        "<b>R/</b> Recuerda que el pago puede ser por transferencia o consignación bancaria a una cuenta de "
        "ahorros Bancolombia, Nequi o Daviplata, el comando /pago te brindará la información necesaria para que realices tu pago. "
        "Para saber el estado y los detalles de tu cuenta visita el comando /micuenta y sigue los pasos.\n"
        "Dicho comando te brindará la información necesaria incluyendo la fecha de pago oportuno.\n\n"
        "/start para ingresar al menú principal.\n\n"
        "¡Tus amigos de <b>Netflix Colombia</b>👋🏻!"
        )
    elif(update.message.text.upper().find("3") == 0):
        id = update.message.from_user.id
        logger.info(f'El usuario {user.first_name} {user.last_name}, seleccionó la pregunta 3.')
        bot.sendChatAction(chat_id=id, action=ChatAction.TYPING, timeout=None)
        time.sleep(1)
        context.bot.sendMessage(chat_id= id, parse_mode="HTML", text="<b> ¿Por qué me sale un aviso diciendo que quedan pocos días de membresía?</b>\n\n"
        "<b>R/</b> En algunas cuentas es común ver un letrero como este:  ")
        with open('img/agregar_pago.jpg','rb') as photo_file:
     #id = update.message.from_user.id
         bot.sendChatAction(chat_id=id, action=ChatAction.UPLOAD_PHOTO, timeout=None)
         time.sleep(1)
         bot.sendPhoto(chat_id=id, photo=photo_file, caption='Actualiza la información de pago.')
         bot.sendChatAction(chat_id=id, action=ChatAction.TYPING, timeout=None)
         time.sleep(1.5)
        context.bot.sendMessage(chat_id= id, parse_mode= "HTML", text= "Esto sucede por la forma de pago de la cuenta, la cual tiene "
         "una fecha de pago estipulada y en la mayoría de los casos no concuerda con la fecha de pago oportuno del cliente.\n"
         "¡Pero no te preocupes! Si ya pagaste tu cuenta, al llegar al día 0 se renovará la membresía automáticamente en el transcurso del día. "
         "En caso de que no se haya realizado el pago, la cuenta se volverá a habilitar una vez se haya verelificado este último de la misma.\n"
         "Si pagaste y no se ve reflejado el pago en tu cuenta el mismo día puedes ponerte en contacto con nosotros, el comando /asesor te brindará más información.\n\n"
         "Envía /start para ingresar al menú principal\n\n"
         "¡Tus amigos de <b>Netflix Colombia</b>👋🏻!")
        with open('besopatito.tgs','rb') as sticker_file:
         bot.sendChatAction(chat_id=id, action=ChatAction.TYPING, timeout=None)
         time.sleep(0.5)
         bot.sendSticker(chat_id=id, sticker=sticker_file) 

    elif(update.message.text.upper().__contains__("4")):
        id = update.message.from_user.id
        logger.info(f'El usuario {user.first_name} {user.last_name}({id}), seleccionó la pregunta 4.')
        bot.sendChatAction(chat_id=id, action=ChatAction.TYPING, timeout=None)
        time.sleep(1)
        context.bot.sendMessage(chat_id= id, parse_mode="HTML", text="<b>¿Cómo puedo saber si alguien más utiliza mi cuenta?</b>\n\n"
        "<b>R/</b> Puedes mirar la Actividad de streaming reciente del dispositivo, así como también las ubicaciones "
        'y los dispositivos utilizados más recientemente en tu cuenta ingresando con correo y contraseña <a href="https://www.netflix.com/AccountAccess" target="_self">aquí</a>.\n'
        'Si luego de revisar esta información quieres controlar el acceso a tu cuenta, recuerda que puedes cambiar tu contraseña ingresando con correo y contraseña desde <a href="https://www.netflix.com/Password/" target="_self">aquí</a>.\n\n')
        bot.sendChatAction(chat_id=id, action=ChatAction.TYPING, timeout=None)
        time.sleep(1)
        context.bot.sendMessage(chat_id= id, parse_mode= "HTML", text=
         "Envía /start para ingresar al menú principal\n\n"
         "¡Tus amigos de <b>Netflix Colombia</b>👋🏻!")
        with open('besopatito.tgs','rb') as sticker_file:
         bot.sendChatAction(chat_id=id, action=ChatAction.TYPING, timeout=None)
         time.sleep(0.5)
         bot.sendSticker(chat_id=id, sticker=sticker_file)
    
    elif(update.message.text.upper().__contains__("5")):
        id = update.message.from_user.id
        logger.info(f'El usuario {user.first_name} {user.last_name}({id}), seleccionó la pregunta 5.')
        bot.sendChatAction(chat_id=id, action=ChatAction.TYPING, timeout=None)
        time.sleep(1)
        context.bot.sendMessage(chat_id= id, parse_mode="HTML", text="<b>¿Cómo puedo cambiar la contraseña de mi cuenta de Netflix?</b>\n\n"
        '<b>R/</b> Puedes cambiar tu contraseña ingresando con correo y contraseña desde <a href="https://www.netflix.com/Password/" target="_self">aquí</a>.\n'
        'Si no has iniciado sesión la página necesariamente te pedirá las credenciales de tu cuenta de Netflix.')
        with open('img/IniciarSesión.png','rb') as photo_file:
         bot.sendChatAction(chat_id= id, action=ChatAction.UPLOAD_PHOTO, timeout= None)
         time.sleep(1)
         bot.sendPhoto(chat_id= id, photo= photo_file, caption= "Paso 1. Inicia sesión en tu cuenta.")
         bot.sendChatAction(chat_id=id, action=ChatAction.TYPING, timeout=None)
         time.sleep(1)
         context.bot.sendMessage(chat_id= id, parse_mode= "HTML", text=
         "Si está iniciada la sesión te llevará directamente al paso N° 2.\n\n")
        with open('img/CambiarContra.png','rb') as photo_file2:
         bot.sendChatAction(chat_id= id, action=ChatAction.UPLOAD_PHOTO, timeout= None)
         time.sleep(1)
         bot.sendPhoto(chat_id= id, photo= photo_file2, caption= "Paso 2. Cambia tu contraseña.")
         bot.sendChatAction(chat_id=id, action=ChatAction.TYPING, timeout=None)
         time.sleep(1)
         context.bot.sendMessage(chat_id= id, parse_mode= "HTML", text="¡Espero que estas indicaciones te haya ayudado!\n\n"
         "Envía /start para ingresar al menú principal\n"
         "¡Tus amigos de <b>Netflix Colombia</b>👋🏻!")
        with open('besopatito.tgs','rb') as sticker_file:
         bot.sendChatAction(chat_id=id, action=ChatAction.TYPING, timeout=None)
         time.sleep(0.5)
         bot.sendSticker(chat_id=id, sticker=sticker_file)

    elif(update.message.text.upper().__contains__("6")):
        id = update.message.from_user.id
        logger.info(f'El usuario {user.first_name} {user.last_name}({id}), seleccionó la pregunta 6.')
        bot.sendChatAction(chat_id=id, action=ChatAction.TYPING, timeout=None)
        time.sleep(1)
        context.bot.sendMessage(chat_id= id, parse_mode="HTML", text="<b>¿Puedo comprar una cuenta de Netflix y agregarle mi correo electrónico?</b>\n\n"
        '<b>R/</b> Puedes cambiar tu contraseña ingresando con correo y contraseña desde <a href="https://www.netflix.com/Password/" target="_self">aquí</a>.\n'
        'Si no has iniciado sesión la página necesariamente te pedirá las credenciales de tu cuenta de Netflix.')
        with open('IniciarSesión.png','rb') as photo_file:
         bot.sendChatAction(chat_id= id, action=ChatAction.UPLOAD_PHOTO, timeout= None)
         time.sleep(1)
         bot.sendPhoto(chat_id= id, photo= photo_file, caption= "Paso 1. Inicia sesión en tu cuenta.")
         bot.sendChatAction(chat_id=id, action=ChatAction.TYPING, timeout=None)
         time.sleep(1)
         context.bot.sendMessage(chat_id= id, parse_mode= "HTML", text=
         "Si está iniciada la sesión te llevará directamente al paso N° 2.\n\n")
        with open('CambiarContra.png','rb') as photo_file2:
         bot.sendChatAction(chat_id= id, action=ChatAction.UPLOAD_PHOTO, timeout= None)
         time.sleep(1)
         bot.sendPhoto(chat_id= id, photo= photo_file2, caption= "Paso 2. Cambia tu contraseña.")
         bot.sendChatAction(chat_id=id, action=ChatAction.TYPING, timeout=None)
         time.sleep(1)
         context.bot.sendMessage(chat_id= id, parse_mode= "HTML", text="¡Espero que estas indicaciones te haya ayudado!\n\n"
         "Envía /start para ingresar al menú principal\n"
         "¡Tus amigos de <b>Netflix Colombia</b>👋🏻!")
        with open('besopatito.tgs','rb') as sticker_file:
         bot.sendChatAction(chat_id=id, action=ChatAction.TYPING, timeout=None)
         time.sleep(0.5)
         bot.sendSticker(chat_id=id, sticker=sticker_file)

    elif(update.message.text.upper().__contains__("ASESOR")):
        context.bot.sendMessage(chat_id= id, parse_mode= "HTML", text="Para solicitar hablar con un asesor por favor envía el comando /asesor y sigue las instrucciones, recuerda describir específicamente tu consulta/problema.\n"
        "Para nosotros siempre es un placer atenderte.☺️\n\n"
        "¡Tus amigos de <b>Netflix Colombia</b>!👋🏻")

    elif(update.message.text.upper().__contains__("PROBLEMA")):
        context.bot.sendMessage(chat_id= id, parse_mode= "HTML", text='¿Tienes algún problema con tu cuenta de Netflix? Envía el comando /asesor y sigue las instrucciones, recuerda describir específicamente tu consulta/problema.\n'
        "Para nosotros siempre es un placer atenderte.☺️\n\n"
        "¡Tus amigos de <b>Netflix Colombia</b>!👋🏻")

    if(update.message.text.upper().__contains__("#%&%/")):
            update.message.reply_text("Lo siento, no reconozco esta frase o comando, lo añadiré a mi base de datos para darte una respuesta oportuna la próxima vez.\n"
            "Recuerda que soy un agente virtual que trabaja con inteligencia artificial (IA) y aprendo cada día de las conversaciones, saludos.\n\n"
            "Ingresa el comando /start para volver al menú principal.")


    return ConversationHandler.END