#!/usr/bin/python
# -*- coding: utf-8 -*-
import telebot
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

@bot.message_handler(commands=['start'])
def welcome(m):
    cid = m.chat.id
    markup = types.InlineKeyboardMarkup()
    b = types.InlineKeyboardButton("Our Channel",callback_data='channel')
    markup.add(b)
    redis = r.StrictRedis(host='localhost', port=6379, db=0)
    redis.sadd('start','{}'.format(m.from_user.id))
    ret_msg = bot.send_message(cid, "\xD8\xB3\xD9\x84\xD8\xA7\xD9\x85\x20\xD8\xA8\xD9\x87\x20\xD8\xB1\xD8\xA8\xD8\xA7\xD8\xAA\x20\xD8\xAF\xD8\xA7\xD9\x86\xD9\x84\xD9\x88\xD8\xAF\xD8\xB1\x20\xD8\xAE\xD9\x88\xD8\xB4\x20\xD8\xA2\xD9\x85\xD8\xAF\xDB\x8C\xD8\xAF\x0A\x0A\xDA\xA9\xD8\xA7\xD9\x81\xDB\x8C\xD9\x87\x20\xD9\x84\xDB\x8C\xD9\x86\xDA\xA9\x20\xD8\xB1\xD9\x88\x20\xD8\xA8\xD9\x87\x20\xD9\x85\xD9\x86\x20\xD8\xA8\xD8\xAF\xDB\x8C\x20\xD8\xAA\xD8\xA7\x20\xD8\xAF\xD8\xA7\xD9\x86\xD9\x84\xD9\x88\xD8\xAF\x20\xDA\xA9\xD9\x86\xD9\x85\x20\xD9\x88\x20\xD8\xA8\xD9\x87\xD8\xAA\x20\xD8\xA8\xD9\x81\xD8\xB1\xD8\xB3\xD8\xAA\xD9\x85\x0A\x28\x55\x52\x4C\x20\x70\x6E\x67\x2D\x6A\x70\x67\x2D\x7A\x69\x70\x29\x0A\x0A\xD8\xAC\xD9\x87\xD8\xAA\x20\xD8\xAF\xD8\xB1\xDB\x8C\xD8\xA7\xD9\x81\xD8\xAA\x20\xD8\xA7\xDB\x8C\xD8\xAF\xDB\x8C\x20\xD8\xAE\xD9\x88\xD8\xAF\x20\x3A\x20\x2F\x69\x64\x0A\xD8\xB7\xD8\xB1\xD8\xA7\xD8\xAD\xDB\x8C\x20\xD8\xB4\xD8\xAF\xD9\x87\x20\xD8\xAA\xD9\x88\xD8\xB3\xD8\xB7\x3A\x0A\x40\x58\x48\x41\x43\x4B\x45\x52\x58", disable_notification=True, reply_markup=markup)
    assert ret_msg.message_id

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == "Channel":
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="Our Channel : @TeleAgent_TEAM")
    if m.chat.type == 'private':
        if re.match('(ftp|http)://.*\.(png)$',text):
            bot.send_message(m.chat.id, '\xD8\xAF\xD8\xB1\x20\xD8\xAD\xD8\xA7\xD9\x84\x20\xD8\xAF\xD8\xB1\xDB\x8C\xD8\xA7\xD9\x81\xD8\xAA\x20\xD8\xA7\xD8\xB7\xD9\x84\xD8\xA7\xD8\xB9\xD8\xA7\xD8\xAA\x2E\x2E\x2E')
            dw(text,'s.png')
            bot.send_photo(m.chat.id, open('s.png'))
            os.remove('s.png') 
        if re.match('(ftp|http|https)://.*\.(jpg)$',text):
            bot.send_message(m.chat.id, '\xD8\xAF\xD8\xB1\x20\xD8\xAD\xD8\xA7\xD9\x84\x20\xD8\xAF\xD8\xB1\xDB\x8C\xD8\xA7\xD9\x81\xD8\xAA\x20\xD8\xA7\xD8\xB7\xD9\x84\xD8\xA7\xD8\xB9\xD8\xA7\xD8\xAA\x2E\x2E\x2E')
            dw(text,'s.jpg')
            bot.send_photo(m.chat.id, open('s.jpg'))
            os.remove('s.jpg') 
        if re.match('(ftp|http|https)://.*\.(zip)$',text):
            bot.send_message(m.chat.id, '\xD8\xAF\xD8\xB1\x20\xD8\xAD\xD8\xA7\xD9\x84\x20\xD8\xAF\xD8\xB1\xDB\x8C\xD8\xA7\xD9\x81\xD8\xAA\x20\xD8\xA7\xD8\xB7\xD9\x84\xD8\xA7\xD8\xB9\xD8\xA7\xD8\xAA\x2E\x2E\x2E')
            dw(text,'file.zip')
            bot.send_photo(m.chat.id, open('file.zip'))
            os.remove('file.zip')
    if m.chat.type == 'group' or  m.chat.type == 'supergroup':
        if m.reply_to_message:
            if m.reply_to_message.from_user.username == botusername:
                if re.match('(ftp|http|https)://.*\.(png)$',text):
                    bot.send_message(m.chat.id, '\xD8\xAF\xD8\xB1\x20\xD8\xAD\xD8\xA7\xD9\x84\x20\xD8\xAF\xD8\xB1\xDB\x8C\xD8\xA7\xD9\x81\xD8\xAA\x20\xD8\xA7\xD8\xB7\xD9\x84\xD8\xA7\xD8\xB9\xD8\xA7\xD8\xAA\x2E\x2E\x2E')
                    dw(text,'s.png')
                    bot.send_photo(m.chat.id, open('s.png'))
                    os.remove('s.png') 
                if re.match('(ftp|http|https)://.*\.(jpg)$',text):      #
                    bot.send_message(m.chat.id, '\xD8\xAF\xD8\xB1\x20\xD8\xAD\xD8\xA7\xD9\x84\x20\xD8\xAF\xD8\xB1\xDB\x8C\xD8\xA7\xD9\x81\xD8\xAA\x20\xD8\xA7\xD8\xB7\xD9\x84\xD8\xA7\xD8\xB9\xD8\xA7\xD8\xAA\x2E\x2E\x2E')              # pic download File (Group by reply)
                    dw(text,'s.jpg')                                    #
                    bot.send_photo(m.chat.id, open('s.jpg'))          
                    os.remove('s.jpg')
                    print 'Remove jpg file'
                if re.match('(ftp|http|https)://.*\.(zip)$',text):
                    bot.send_message(m.chat.id, '\xD8\xAF\xD8\xB1\x20\xD8\xAD\xD8\xA7\xD9\x84\x20\xD8\xAF\xD8\xB1\xDB\x8C\xD8\xA7\xD9\x81\xD8\xAA\x20\xD8\xA7\xD8\xB7\xD9\x84\xD8\xA7\xD8\xB9\xD8\xA7\xD8\xAA\x2E\x2E\x2E')              #
                    dw(text,'file.zip')                                 # zip files
                    bot.send_photo(m.chat.id, open('file.zip'))         #
                    os.remove('file.zip')
                    print 'Remove zip file'


bot.polling(True)
