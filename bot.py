import telegram
import logging, threading
from telegram.ext import MessageHandler, Filters, ConversationHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, InlineQueryResultDocument
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
import os
#from grab import Grab
#bot = telegram.Bot(token='1186845869:AAGQ3gwXoCHhGfaDiI5ZPUFHrkKOCagH4qs')
TOKEN = '1357777795:AAGtFnV6H2l0ckibTyoaRY-z4DBezTNcJ5c'
PORT = int(os.environ.get('PORT', 5000))

FIRST, SECOND = range(2)
# Callback data
ONE, TWO, THREE, FOUR = range(4)

#error check
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

#start command
def start(update, context):
    user = update.message.from_user
    logger.info("User %s started the conversation.", user.first_name)
    keyboard = [[InlineKeyboardButton("Автокаско", callback_data=str(ONE)),
                 InlineKeyboardButton("Квартира", callback_data=str(TWO))],

                [InlineKeyboardButton("Дом", callback_data=str(THREE))]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Выберите вид страхования:', reply_markup=reply_markup)

    return FIRST

def one(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="Страхование Автокаско: ".format(query.data))
    #try: context.bot.send_document(chat_id=update.effective_chat.id, document = open(f'Каско.PDF', 'rb'))
    #except BadRequest as err:
    #    if err == 'Connection aborted.': context.bot.send_message(chat_id=update.effective_chat.id, text = 'Файл не прошел')
    context.bot.send_document(chat_id=update.effective_chat.id, document = open(f'Каско.PDF', 'rb'))
    context.bot.send_message(chat_id=update.effective_chat.id, text = 'Если у вас возникли вопросы по какому-либо виду страхования, а также если вас интересуют другие виды страхования - пишите мне в личку @AndrewSugako')

    return FIRST

def two(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="Страхование Квартир: ".format(query.data))
    context.bot.send_document(chat_id=update.effective_chat.id, document = open(f'Квартира.PDF', 'rb'))
    context.bot.send_photo(chat_id=update.effective_chat.id, photo = open(f'Квартира.JPG', 'rb'))
    context.bot.send_message(chat_id=update.effective_chat.id, text = 'Если у вас возникли вопросы по какому-либо виду страхования, а также если вас интересуют другие виды страхования - пишите мне в личку @AndrewSugako')
    return ConversationHandler.END

def three(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="Страхование Домов: ".format(query.data))
    context.bot.send_document(chat_id=update.effective_chat.id, document = open(f'Дом.PDF', 'rb'))
    context.bot.send_message(chat_id=update.effective_chat.id, text = 'Если у вас возникли вопросы по какому-либо виду страхования, а также если вас интересуют другие виды страхования - пишите мне в личку @AndrewSugako')
    return ConversationHandler.END

def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Извините, я не понял вашу команду. Отправьте /start для выбора интересующего вас вида страхования.")


#button part
def main():
    updater = Updater("1357777795:AAGtFnV6H2l0ckibTyoaRY-z4DBezTNcJ5c", use_context=True)
    dispatcher = updater.dispatcher
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            FIRST: [CallbackQueryHandler(one, pattern='^' + str(ONE) + '$'),
                    CallbackQueryHandler(two, pattern='^' + str(TWO) + '$'),
                    CallbackQueryHandler(three, pattern='^' + str(THREE) + '$')],
        },
        fallbacks=[CommandHandler('start', start)]
    )

    # Add ConversationHandler to dispatcher that will be used for handling
    # updates
    dispatcher.add_handler(conv_handler)

    #commands
    dispatcher.bot.set_my_commands([['start', 'Нажмите для запуска бота']])

    unknown_handler = MessageHandler(Filters.command, unknown)
    dispatcher.add_handler(unknown_handler)

    # Start the Bot
    updater..start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook('https://boiling-everglades-69165.herokuapp.com/' + TOKEN)


    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()
#unknown commands filter




if __name__ == '__main__':
    main()

#bot start
#updater.start_polling()
