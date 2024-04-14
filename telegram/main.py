import asyncio
import io
import requests
from typing import Final
from telegram import Update
from telegram.ext import Application, Updater, CommandHandler, CallbackContext, ContextTypes, MessageHandler, filters

TOKEN: Final = '6528685174:AAGe-xDgxVRJLpYYBJOdosLg9PcoiZO4KHE'
BOT_USERNAME: Final = 'facturify'

async def start_command(update: Update, context: CallbackContext):
    await update.message.reply_text('Hola gracias por utilizar Facturify, la mejor solución para facturar en todo momento. Para comenzar a facturar por favor crea tu perfil en la siguiente dirección: https://facturify.com/registro o registrate ejecutando el comando /registro')

async def help_command(update: Update, context: CallbackContext):
    await update.message.reply_text('Puedo ayudarte con las siguientes acciones: \n\n /registro - Registrate en la plataforma de Facturify \n /subir_ticket - Sube un nuevo ticket a la plataforma y empieza el proceso de facturación de este mismo. \n /muestrame_mis_facturas - Te doy una lista de las facturas que tienes actualmente según la lista de parametros que me pidas.')

async def handle_image(update: Update, context: CallbackContext):
    URL = 'http://127.0.0.1:8080/tickets'
        
    try:
        photo_file = await update.message.photo[-1].get_file()
        # Descargar la imagen localmente
        photo_file_path = 'temp_image.jpg'
        await photo_file.download_to_drive(photo_file_path)

        # Enviar la imagen como multipart/form-data
        with open(photo_file_path, 'rb') as file:
            files = {'image': file}
            response = requests.post(URL, files=files)

        # Verificar si la petición fue exitosa
        if response.status_code == 200:
            await update.message.reply_text('Ticket subido correctamente.')
        else:
            await update.message.reply_text('Hubo un error al subir el ticket.')
    except Exception as e:
        print(e)    

# Responses
async def handle_response(text:str)-> str:
    processed: str = text.lower()

    if 'Hola' in text:
        return 'Hola, ¿en qué puedo ayudarte?'
    if 'Adios' in text:
        return 'Adios, espero verte pronto.'
    
    return 'No entiendo lo que me dices, por favor intenta de nuevo.'

async def handle_message(update: Update, context: CallbackContext):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}')
    
    if message_type == 'private':
        if BOT_USERNAME in text:
            await update.message.reply_text('Hola, ¿en qué puedo ayudarte?')
        else:
            return 
    else:
        response: str = await handle_response(text)
    
    await update.message.reply_text(response)

async def error(update: Update, context: CallbackContext):
    print(f'Update {update} caused error {context.error}')

if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()
    
    #Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    
    # Images 
    app.add_handler(MessageHandler(filters.PHOTO, handle_image))
    

    # Error
    app.add_error_handler(error)

    # Polling
    print('Polling...')
    app.run_polling(poll_interval=3)

