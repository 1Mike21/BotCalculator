import telepot
from telepot.loop import MessageLoop
from config import TOKEN

bot = telepot.Bot(TOKEN)

def handle(message):
    """ Process request like '3+2' """
    content_type, chat_type, chat_id = telepot.glance(message)
    text = message["text"]
    try:
        answer = eval(text)

    except:
        answer = "Неверно введен пример!"
    bot.sendMessage(chat_id, "Ответ: {}".format(answer))


MessageLoop(bot, handle).run_as_thread()

# Keep the program running.
while True:
    n = input('To stop enter "stop":')
    if n.strip() == 'stop':
        break
