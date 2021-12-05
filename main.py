import uses
import messages


@uses.bot.message_handler(commands=['start'])
def start_message(message):
    uses.bot.send_message(message.chat.id, messages.first_message)


@uses.bot.message_handler(commands=['button'])
def button_message(message):
    markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = uses.types.KeyboardButton("Кнопка")
    markup.add(item1)
    uses.bot.send_message(message.chat.id, messages.button_message, reply_markup=markup)


@uses.bot.message_handler(content_types='text')
def message_reply(message):
    if message.text == "Кнопка":
        uses.bot.send_message(message.chat.id, messages.reply_button_message)


uses.bot.polling()
