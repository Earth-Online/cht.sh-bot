#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
command file
"""
import requests
import uuid
from tool import command_wrap
from constant import SEARCH_URL, ANSI_ESCAPE
from telegram import (InputTextMessageContent, InlineQueryResultArticle, 
                      ParseMode)
from telegram.ext import InlineQueryHandler


@command_wrap()
def start(bot, update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text="I'm a bot, please talk to me!")


def search(bot, update):
    query = update.inline_query.query
    if not query:
        return
    query = query.split()
    results = list()
    url = SEARCH_URL+"/".join(query)
    ret = requests.get(url)
    if not ret.ok:
        return
    results.append(
        InlineQueryResultArticle(
            id=uuid.uuid4(),
            title=update.inline_query.query,
            input_message_content=InputTextMessageContent(
                "`"+ANSI_ESCAPE.sub(
                    "",
                    ret.text)+"`",
                parse_mode=ParseMode.MARKDOWN,
            ),
            url=url,
        ))
    update.inline_query.answer(results)


search = InlineQueryHandler(search)
