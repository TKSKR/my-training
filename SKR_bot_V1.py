import telebot
botTimeWeb = telebot.TeleBot('8192142498:AAFt7HWa7ywUslIlK2UMuVhUseBxtzUhswI')
from telebot import types
@botTimeWeb.message_handler(commands=['start'])
def startBot(message):
  first_mess = f"<b>{message.from_user.first_name} {message.from_user.last_name}</b>, привет!\n Хотите ли Вы увеличение окладной части зарплаты в 2025 году?"
  markup = types.InlineKeyboardMarkup()
  button_yes = types.InlineKeyboardButton(text = 'Да, я жадный!', callback_data='yes')
  markup.add(button_yes)
  button_non = types.InlineKeyboardButton(text='Нет, мне хватает', callback_data='non')
  markup.add(button_non)
  button_little = types.InlineKeyboardButton(text="Я не наглый, немножко можно", callback_data='little')
  markup.add(button_little)
  botTimeWeb.send_message(message.chat.id, first_mess, parse_mode='html', reply_markup=markup)
@botTimeWeb.callback_query_handler(func=lambda call:True)
def response(function_call):
  if function_call.message:
     if function_call.data == "yes":
        second_mess = "Не знаю могу ли я это согласовать"
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Думаю Вам поможет это", url="https://www.wildberries.ru/catalog/149479694/detail.aspx/"))
        botTimeWeb.send_message(function_call.message.chat.id, second_mess, reply_markup=markup)
        botTimeWeb.answer_callback_query(function_call.id)
botTimeWeb.infinity_polling()