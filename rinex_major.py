from telegram.ext import Updater,MessageHandler,Filters
from Adafruit_IO import Client
#adafruit
global aio
aio = Client('dineshreddy', 'aio_Nljd68HtjUkowEswwGgqMtWlYgOf')

#telegram bot
def f1(bot,update):
    chatid=bot.message.chat_id
    l_on='https://all-free-download.com/free-vector/download/glowing-light-bulb_55903.html'
    l_off='https://www.freeiconspng.com/thumbs/bulb-off-icon/bulb-off-icon-28.png'
    f_on='https://i.pinimg.com/originals/0b/66/0e/0b660ec34ec02851be8f0be00b5c30f6.png'
    f_off='https://images-na.ssl-images-amazon.com/images/I/61fnSm36NpL._SL1500_.jpg'
    a=bot.message.text
    if a.lower()in ['turn on light','light on']:
        d=aio.receive('major.light')
        if d.value.lower()=='on':
            bot.message.reply_text('Light is already in on')
        else:
            aio.send('major.light', 'on')
            bot.message.reply_text('Light turned on')
        update.bot.sendPhoto(chat_id=chatid,photo=l_on)

    elif a.lower()in ['turn off light','light off']:
        d=aio.receive('major.light')
        if d.value.lower()=='off':
            bot.message.reply_text('Light is already in off')
        else:
            aio.send('major.light', 'off')
            bot.message.reply_text('Light turned off')
        update.bot.sendPhoto(chat_id=chatid,photo=l_off)
    elif a.lower()in ['turn on fan','fan on']:
        d=aio.receive('major.fan')
        if d.value.lower()=='on':
            bot.message.reply_text('fan is already turned on')
        else:
            aio.send('major.fan', 'on')
            bot.message.reply_text('fan turned on')
        update.bot.sendPhoto(chat_id=chatid,photo=f_on)
    elif a.lower()in ['turn off fan','fan off']:
        d=aio.receive('major.fan')
        if d.value.lower()=='off':
            bot.message.reply_text('fan is already off')
        else:
            aio.send('major.fan', 'off')
            bot.message.reply_text('fan turned off')
        update.bot.sendPhoto(chat_id=chatid,photo=f_off)
    elif a.lower() in ['how are you','how r u']:
        bot.message.reply_text('I am fine \nhow can i help you')
    else:
        bot.message.reply_text('Can you please give the command with respect to light and fan')
    
bt='1851997399:AAEMvnWkzNQkxz5s-t_gABJ8cyMl-k1fPME'
u=Updater(bt,use_context=True)
dp=u.dispatcher
dp.add_handler(MessageHandler(Filters.text,f1))
u.start_polling()
u.idle()
