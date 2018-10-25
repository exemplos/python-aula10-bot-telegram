import telegram


bot = telegram.Bot('785011406:AAEKKSP7YKazMA66p80B-xBs055BtSt0AW4')
try:
    update_id = bot.get_updates()[0].update_id
except:
    update_id = None
    
while True:
    for update in bot.get_updates(offset=update_id, timeout=10):
        update_id = update.update_id + 1
        if update.message:
                update.message.reply_text('Redes mod 3 ' + update.message.text)
                print(update.message.text)