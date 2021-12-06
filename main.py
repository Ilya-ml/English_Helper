import uses
import messages
import begginer
import pre_intermediate
import intermediate
import upper_intermediate
import advanced


# Бот - @EnglishHelperTestBot


@uses.bot.message_handler(commands=['start'])
def start_message(message):
    uses.bot.send_message(message.chat.id, messages.first_message)


@uses.bot.message_handler(commands=['eng_level'])
def button_message(message):
    markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = uses.types.KeyboardButton("Begginer")
    item2 = uses.types.KeyboardButton("Pre-Intermediate")
    item3 = uses.types.KeyboardButton("Intermediate")

    markup.add(item1, item2, item3)
    uses.bot.send_message(message.chat.id, messages.choose_level_message, reply_markup=markup)


@uses.bot.message_handler("Begginer")
def beggg(message):
    markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = uses.types.KeyboardButton("Новые слова")
    item2 = uses.types.KeyboardButton("Тест")
    item3 = uses.types.KeyboardButton("Книги")
    item4 = uses.types.KeyboardButton("Поменять уровень")
    markup.add(item1, item2, item3, item4)
    uses.bot.send_message(message.chat.id, 'Что будем изучать?', reply_markup=markup)


@uses.bot.message_handler("Новые слова")
def new_word_for_beg(message):
    markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = uses.types.KeyboardButton("Окружающий мир")
    item2 = uses.types.KeyboardButton("Семья")
    item3 = uses.types.KeyboardButton("Для туриста")
    item4 = uses.types.KeyboardButton("Социальная коммуникация")
    markup.add(item1, item2, item3, item4)
    uses.bot.send_message(message.chat.id, 'Слова какой темы Вы хотите выучить?', reply_markup=markup)


@uses.bot.message_handler("Назад")
def for_beg(message):
    markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = uses.types.KeyboardButton("Новые слова")
    item2 = uses.types.KeyboardButton("Тест")
    item3 = uses.types.KeyboardButton("Книги")
    item4 = uses.types.KeyboardButton("Поменять уровень")
    markup.add(item1, item2, item3, item4)
    uses.bot.send_message(message.chat.id, 'Что будем изучать?', reply_markup=markup)


@uses.bot.message_handler(content_types='text')
def message_reply(message):

    if message.text == "Begginer":
        beggg(message)

    if message.text == "Pre-Intermediate":
        uses.bot.send_message(message.chat.id, "В скором времени")
        markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = uses.types.KeyboardButton("Поменять уровень")
        markup.add(item1)
        uses.bot.send_message(message.chat.id, 'Поменять уровень?', reply_markup=markup)

    if message.text == "Intermediate":
        uses.bot.send_message(message.chat.id, "В скором времени")
        markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = uses.types.KeyboardButton("Поменять уровень")
        markup.add(item1)
        uses.bot.send_message(message.chat.id, 'Поменять уровень?', reply_markup=markup)


    if message.text == "Новые слова":
        new_word_for_beg(message)

    if message.text == "Окружающий мир":
        uses.bot.send_message(message.chat.id, begginer.nature)
        markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = uses.types.KeyboardButton("Назад")
        markup.add(item1)
        uses.bot.send_message(message.chat.id, "Вернуться назад?",reply_markup=markup)


    if message.text == "Семья":
        uses.bot.send_message(message.chat.id, begginer.family)
        markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = uses.types.KeyboardButton("Назад")
        markup.add(item1)
        uses.bot.send_message(message.chat.id, "Вернуться назад?", reply_markup=markup)


    if message.text == "Для туриста":
        uses.bot.send_message(message.chat.id, begginer.tourism)
        markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = uses.types.KeyboardButton("Назад")
        markup.add(item1)
        uses.bot.send_message(message.chat.id, "Вернуться назад?", reply_markup=markup)

    if message.text == "Социальная коммуникация":
        uses.bot.send_message(message.chat.id, begginer.social)
        markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = uses.types.KeyboardButton("Назад")
        markup.add(item1)
        uses.bot.send_message(message.chat.id, "Вернуться назад?", reply_markup=markup)

    if message.text == "Книги":
            uses.bot.send_message(message.chat.id, begginer.books)
            markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = uses.types.KeyboardButton("Назад")
            markup.add(item1)
            uses.bot.send_message(message.chat.id, "Вернуться назад?", reply_markup=markup)

    if message.text == "Назад":
        for_beg(message)

    if message.text == "Поменять уровень":
        uses.bot.send_message(message.chat.id, 'Чтобы выбрать другой уровень знаний языка, нажмите на /eng_level')

    if message.text == "Тест":
        uses.bot.send_message(message.chat.id, "В скором времени")
        markup = uses.types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = uses.types.KeyboardButton("Назад")
        markup.add(item1)
        uses.bot.send_message(message.chat.id, "Вернуться назад?", reply_markup=markup)


uses.bot.infinity_polling()
