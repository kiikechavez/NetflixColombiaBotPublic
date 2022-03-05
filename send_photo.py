import telegram
from telegram import ChatAction
import time
bot_token ="YOUR_TOKEN_BOT_FROM_TELEGRAM_PROVIDED"

bot = telegram.Bot(token=bot_token)


chat_id='chat_id'   #chat id that people that you want to send a message from bot




bot.sendMessage(chat_id=chat_id, parse_mode= "HTML", text=f'Espero sinceramente haber sido de ayuda la noche de hoy y que la información brindada respondiera a su solicitud. Por mi parte me despido que tenga una muy buena noche. ¡Saludos del equipo <b>Netflix Colombia</b>👋🏻!\n'
)

