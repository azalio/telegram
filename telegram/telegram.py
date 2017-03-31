#!/usr/bin/env python
# -*- coding: utf-8 -*-
import telepot
import sys
import magic


class Telegram:
    def __init__(self, token):
        self.bot = telepot.Bot(token)

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
        self.bot.sendPhoto(chat_id, photo)

    def _send_video_(self, path):
        video = self._open_file_(path)
        self.bot.sendVideo(chat_id, video)

    @staticmethod
    def _open_file_(path):
        try:
            return open(path)
        except IOError as ex:
            print("Can't open file: {} with error: ".format(path, ex.message))


def main(path):
    bot = Telegram(token)
    bot.send_file(path)


if __name__ == "__main__":
    token = ''  # Telegram token
    chat_id = 12452435  # Telegram id
    path = sys.argv[1]  # Path to photoÅ
    main(path)
