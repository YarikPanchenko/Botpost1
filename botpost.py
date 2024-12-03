import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# Замените 'YOUR_BOT_TOKEN' на токен вашего бота
API_TOKEN = '8194965332:AAFw_fVIIdcewvzkOOxp1plo0gSKGUe3Q2w'

bot = telebot.TeleBot(API_TOKEN)
# Функция для создания кнопок

#кнопки рядом


# кнопки друг под другом

def create_keyboard():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Полный каталог", url="https://hermesexpert.ru/"))
    markup.add(InlineKeyboardButton("Связаться с менеджером", url="https://t.me/HermesRoman"))
    return markup

# Обработчик для текстовых сообщений
@bot.message_handler(content_types=['text'])
def handle_text(message):
    markup = create_keyboard()
    bot.send_message(message.chat.id, message.text, reply_markup=markup)

# Обработчик для фото с текстом
@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    markup = create_keyboard()
    file_id = message.photo[-1].file_id
    caption = message.caption if message.caption else ""
    bot.send_photo(message.chat.id, file_id, caption=caption, reply_markup=markup)

# Обработчик для видео
@bot.message_handler(content_types=['video'])
def handle_video(message):
    markup = create_keyboard()
    file_id = message.video.file_id
    caption = message.caption if message.caption else ""
    bot.send_video(message.chat.id, file_id, caption=caption, reply_markup=markup)

# Обработчик для GIF (анимации)
@bot.message_handler(content_types=['animation'])
def handle_animation(message):
    markup = create_keyboard()
    file_id = message.animation.file_id
    caption = message.caption if message.caption else ""
    bot.send_animation(message.chat.id, file_id, caption=caption, reply_markup=markup)

if __name__ == '__main__':
    print("Бот запущен!")
    bot.polling(none_stop=True)