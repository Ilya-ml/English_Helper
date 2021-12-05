import uses
import messages


@uses.bot.message_handler(commands=['start'])
def start_message(message):
    uses.bot.send_message(message.chat.id, messages.first_message)


@uses.bot.message_handler(commands=['lvl'])
def button_message(message):
    markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = uses.types.KeyboardButton("Begginer")
    item2 = uses.types.KeyboardButton("Elementary")
    item3 = uses.types.KeyboardButton("Pre Intermediate")
    item4 = uses.types.KeyboardButton("Intermediate")
    item5 = uses.types.KeyboardButton("Upper Intermediate")

    markup.add(item1, item2, item3, item4, item5)
    uses.bot.send_message(message.chat.id, messages.choose_level_message, reply_markup=markup)


@uses.bot.message_handler(content_types='text')
def message_reply(message):
    if message.text == "Begginer":
        uses.bot.send_message(message.chat.id, messages.reply_level_message)

    elif message.text == "Elementary":
        uses.bot.send_message(message.chat.id, messages.reply_level_message)

    elif message.text == "Pre Intermediate":
        uses.bot.send_message(message.chat.id, messages.reply_level_message)

    elif message.text == "Intermediate":
        uses.bot.send_message(message.chat.id, messages.reply_level_message)

    elif message.text == "Upper Intermediate":
        uses.bot.send_message(message.chat.id, messages.reply_level_message)


uses.bot.infinity_polling()
