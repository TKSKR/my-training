import telepot
from telepot.loop import MessageLoop


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    if content_type == 'text':
        bot.sendMessage(chat_id, 'Вы написали: {}'.format(msg['text']))


token = '8141553974:AAFEHIpupQp7EK-hN2f5L86aFKO31dx-ZnI'
bot = telepot.Bot(token)
MessageLoop(bot, handle).run_as_thread()

print('Бот запущен')

while True:
    pass
