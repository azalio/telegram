#!/usr/bin/env python
"""Send files to telegram user"""
# -*- coding: utf-8 -*-
import telepot
import sys
import magic


class Telegram:
    def __init__(self, token, chat_id):
        self.bot = telepot.Bot(token)
        self.chat_id = chat_id

    def send_text(self):
        pass

    def send_file(self, path):
        filetype = magic.from_file(path, mime=True).split('/')[0]
        if filetype == 'image':
            self._send_photo_(path)
        elif filetype == 'video':
            self._send_video_(path)

    def _send_photo_(self, path):
        photo = self._open_file_(path)
        self.bot.sendPhoto(self.chat_id, photo)

    def _send_video_(self, path):
        video = self._open_file_(path)
        self.bot.sendVideo(self.chat_id, video)

    @staticmethod
    def _open_file_(path):
        try:
            return open(path)
        except IOError as ex:
            print("Can't open file: {} with error: ".format(path, ex.message))


def run(args=None):
    if args is None:
        args = sys.argv[1:]

    token = args[0]
    path = args[1]
    chat_id = args[2]

    bot = Telegram(token, chat_id)
    bot.send_file(path)

