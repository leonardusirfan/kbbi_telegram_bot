from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import ast
from kbbi import KBBI

def message_func(update, context):
    print('Update : ', update)
    send_result(update, str(KBBI(update.message.text)))
    
def kamus_func(update, context):
    print('Update : ', update)
    text = update.message.text
    text = text.partition(' ')[2]
    result = str(KBBI(text))
    send_result(update, result)
        
def send_result(update, text):
    if text:
        update.message.reply_text(text)
    else:
        update.message.reply_text("Maaf, kata yang anda cari tidak ditemukan")

def error(update, context):
    print('Update : ', update)
    print('Error : ', context.error)
    
def start(update, context):
    update.message.reply_text("Selamat datang di KBBI duta bahasa Jateng. Silahkan masukkan kata dengan manggunakan /\n\nContoh: /makan")

def read_dictionary ():
    file = open("kamus.txt", "r")
    contents = file.read()
    values = ast.literal_eval(contents)
    file.close()
    
    return values

def main():
    updater = Updater('1525836337:AAGcJyYjgM0ltSljw9Mh2uCvJAGuiEYNiyQ', use_context = True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("kamus", kamus_func))
    dp.add_handler(MessageHandler(Filters.text, message_func))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()