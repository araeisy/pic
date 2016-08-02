#!/usr/bin/python
# -*- coding: utf-8 -*-
import telebot
from telebot import types
import re
from urllib import urlretrieve as dw
import sys
import os
#import color
reload(sys)
sys.setdefaultencoding("utf-8")

bot = telebot.TeleBot('213469836:AAFqp1scCFDfmS6sqFRshAID8Fup_cicdcU')
admin = 195801672
botusername = 'CloudDownloaderBot'

@bot.message_handler(commands=['start', 'help'])
def welcome(m):
    cid = m.chat.id
    markup = types.InlineKeyboardMarkup()
    a = types.InlineKeyboardButton("Taylor Team \xE2\x9C\x8C", url="https://telegram.me/taylor_team")
    c = types.InlineKeyboardButton("Add group \xE2\x9C\x8C", url="https://telegram.me/ID_bot_robot?startgroup=test")
    markup.add(a, c)
    b = types.InlineKeyboardButton("Developer ID bot \xE2\x9C\x8C", url="https://telegram.me/negative_officiall")
    markup.add(b)
    nn = types.InlineKeyboardButton("Inline Mode", switch_inline_query='')
    markup.add(nn)
    ret_msg = bot.send_message(cid, "Hello I'm ID bot \n\n Send : \n  /id or /me or /info   \n\n\n get your id : \n /idme (just pv) \nsend Your feedback : /feedback [msg]\n\n\n list inline mod : \ntype @ID_bot_robot\n\nBot version 3", disable_notification=True, reply_markup=markup)
    assert ret_msg.message_id
    if m.chat.type == 'private':
        if re.match('(ftp|http)://.*\.(png)$',text):
            bot.send_message(m.chat.id, '\xD8\xAF\xD8\xB1\x20\xD8\xAD\xD8\xA7\xD9\x84\x20\xD8\xAF\xD8\xB1\xDB\x8C\xD8\xA7\xD9\x81\xD8\xAA\x20\xD8\xA7\xD8\xB7\xD9\x84\xD8\xA7\xD8\xB9\xD8\xA7\xD8\xAA\x20\x2E\x2E\x2E\x20\x28\x50\x4E\x47\x29')
            dw(text,'s.png')
            bot.send_photo(m.chat.id, open('s.png'))
            os.remove('s.png') 
        if re.match('(ftp|http|https)://.*\.(jpg)$',text):
            bot.send_message(m.chat.id, '\xD8\xAF\xD8\xB1\x20\xD8\xAD\xD8\xA7\xD9\x84\x20\xD8\xAF\xD8\xB1\xDB\x8C\xD8\xA7\xD9\x81\xD8\xAA\x20\xD8\xA7\xD8\xB7\xD9\x84\xD8\xA7\xD8\xB9\xD8\xA7\xD8\xAA\x20\x2E\x2E\x2E\x20\x28\x4A\x50\x47\x29')
            dw(text,'s.jpg')
            bot.send_photo(m.chat.id, open('s.jpg'))
            os.remove('s.jpg') 
        if re.match('(ftp|http|https)://.*\.(zip)$',text):
            bot.send_message(m.chat.id, '\xD8\xAF\xD8\xB1\x20\xD8\xAD\xD8\xA7\xD9\x84\x20\xD8\xAF\xD8\xB1\xDB\x8C\xD8\xA7\xD9\x81\xD8\xAA\x20\xD8\xA7\xD8\xB7\xD9\x84\xD8\xA7\xD8\xB9\xD8\xA7\xD8\xAA\x20\x2E\x2E\x2E\x20\x28\x5A\x49\x50\x29')
            dw(text,'file.zip')
            bot.send_photo(m.chat.id, open('file.zip'))
            os.remove('file.zip')
    if m.chat.type == 'group' or  m.chat.type == 'supergroup':
        if m.reply_to_message:
            if m.reply_to_message.from_user.username == botusername:
                if re.match('(ftp|http|https)://.*\.(png)$',text):
                    bot.send_message(m.chat.id, '\xD8\xAF\xD8\xB1\x20\xD8\xAD\xD8\xA7\xD9\x84\x20\xD8\xAF\xD8\xB1\xDB\x8C\xD8\xA7\xD9\x81\xD8\xAA\x20\xD8\xA7\xD8\xB7\xD9\x84\xD8\xA7\xD8\xB9\xD8\xA7\xD8\xAA\x20\x2E\x2E\x2E\x20\x28\x50\x4E\x47\x29')
                    dw(text,'s.png')
                    bot.send_photo(m.chat.id, open('s.png'))
                    os.remove('s.png') 
                if re.match('(ftp|http|https)://.*\.(jpg)$',text):      #
                    bot.send_message(m.chat.id, '\xD8\xAF\xD8\xB1\x20\xD8\xAD\xD8\xA7\xD9\x84\x20\xD8\xAF\xD8\xB1\xDB\x8C\xD8\xA7\xD9\x81\xD8\xAA\x20\xD8\xA7\xD8\xB7\xD9\x84\xD8\xA7\xD8\xB9\xD8\xA7\xD8\xAA\x20\x2E\x2E\x2E\x20\x28\x4A\x50\x47\x29')              # pic download File (Group by reply)
                    dw(text,'s.jpg')                                    #
                    bot.send_photo(m.chat.id, open('s.jpg'))          
                    os.remove('s.jpg')
                    print 'Remove jpg file'
                if re.match('(ftp|http|https)://.*\.(zip)$',text):
                    bot.send_message(m.chat.id, '\xD8\xAF\xD8\xB1\x20\xD8\xAD\xD8\xA7\xD9\x84\x20\xD8\xAF\xD8\xB1\xDB\x8C\xD8\xA7\xD9\x81\xD8\xAA\x20\xD8\xA7\xD8\xB7\xD9\x84\xD8\xA7\xD8\xB9\xD8\xA7\xD8\xAA\x20\x2E\x2E\x2E\x20\x28\x5A\x49\x50\x29')              #
                    dw(text,'file.zip')                                 # zip files
                    bot.send_photo(m.chat.id, open('file.zip'))         #
                    os.remove('file.zip')
                    print 'Remove zip file'


bot.polling(True)
