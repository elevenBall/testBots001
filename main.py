#alterei aqui
from telegram.ext import Updater
import argparse
import random
import time
from pythonosc import udp_client
import os,sys
from pydub import AudioSegment


updater = Updater(token='2038695939:AAExF0zToPveyb9H9Hh0K-16DCmecVcPdWM', use_context=True)

dispatcher = updater.dispatcher

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)


parser = argparse.ArgumentParser()
parser.add_argument("--ip", default="192.168.1.20", help="The ip of the OSC server")
parser.add_argument("--port", type=int, default=9001, help="The port the OSC server is listening on")
args = parser.parse_args()
client = udp_client.SimpleUDPClient(args.ip, args.port)



# intro -------------------------------------------------------------------------------------------
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="sou um macaquinho de imitação")

from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
#-------------------------------------------------------------------------------------------------


# enviar o mesmo ---------------------------------------------------------------------------------
def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

from telegram.ext import MessageHandler, Filters
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)
#-------------------------------------------------------------------------------------------------


# COMANDO OLA------------------------------------------------------------------------------------
def ola(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="HEY TUDO?")

from telegram.ext import CommandHandler
ola_handler = CommandHandler('ola', ola)
dispatcher.add_handler(ola_handler)
#-------------------------------------------------------------------------------------------------


# receber audio ----------------------------------------------------------------------------------
def voz(update, context):
    file = context.bot.getFile(update.message.voice.file_id)
    file.download('./voice.ogg')
    convert_ogg_to_wav()


from telegram.ext import MessageHandler, Filters
voz_handler = MessageHandler(Filters.voice & (~Filters.command), voz)
dispatcher.add_handler(voz_handler)
#-------------------------------------------------------------------------------------------------


# COMANDO PLAY -----------------------------------------------------------------------------------
def play(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="vou tocar o audio")

from telegram.ext import CommandHandler
play_handler = CommandHandler('play', play)
dispatcher.add_handler(play_handler)
#-------------------------------------------------------------------------------------------------



# COMANDO pitch -----------------------------------------------------------------------------------
def pitchDef(update, context, ):
    texto1 = update.message.text
    texto2 = texto1.split(':', 1)

    client.send_message("/val1", int(texto2[1]))
    context.bot.send_message(chat_id=update.effective_chat.id, text=texto2[1])

from telegram.ext import CommandHandler
pitchDef_handler = CommandHandler('pitch', pitchDef)
dispatcher.add_handler(pitchDef_handler)
#--------------------------------------------------------------------------------

def convert_ogg_to_wav():
    time.sleep(2)
    song = AudioSegment.from_ogg("voice.ogg")
    song.export("voz.wav", format="wav")

updater.start_polling()

