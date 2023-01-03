# message = "〇〇〇〇年〇〇月〇〇日〇〇時〇〇分〇〇秒　〇〇地域　M〇〇　深さ〇〇km　最大震度〇〇"

import requests
import re
import datetime
import urllib.request, urllib.error
import csv
import requests
import os
from email.mime.text import MIMEText
import smtplib
import sys
import urllib.request, urllib.error
from bs4 import BeautifulSoup
import csv

class quake_mail_class():
    def quake_mail(self, quake_news, to_address):

        # SMTP認証情報
        account = "subaodezhen641@gmail.com"
        # password = "19960701jishin"
        password = "ubqrmyfjgxsojiwg"

        # 送受信先
        to_email = to_address
        from_email = "subaodezhen641@gmail.com"

        # MIMEの作成
        subject = "地震速報"
        # message = "地震速報"
        message = quake_news
        msg = MIMEText(message, "html")
        msg["Subject"] = subject
        msg["To"] = to_email
        msg["From"] = from_email

        # メール送信処理
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(account, password)
        server.send_message(msg)
        server.quit()

class y_news_class():
    def y_news(self, url):
        self.url = url
        data_bank = []
        # print(url)
        feed = feedparser.parse(url)
        # print(feed)
        for entry in feed.entries:
            data_bank.append(entry.title)
            data_bank.append(entry.link)
            print('タイトル:', entry.title)
            print('URL:', entry.link)
        return data_bank

# print("<p>" + "@@@ @@@ @@@ @@@" + "</p>")

url = "https://headline.5ch.net/bbynamazu/news.rss"
url = "https://ja.wikipedia.org/wiki/%E5%85%AC%E5%AE%89%E8%AD%A6%E5%AF%9F"



path = './data/quake_data.txt'

# url = "https://kabuoji3.com/stock/6501/2019/"
# URLを指定する
html = urllib.request.urlopen(url)
# URLを開く
soup = BeautifulSoup(html, "html.parser")
# BeautifulSoup で開く
# HTMLからニュース一覧に使用しているaタグを絞りこんでいく
data_now = str(soup)

f = open(path, 'r', encoding='UTF-8')
data_before = f.read()
# print(data_before)

if (data_before == data_now):
    print("no change")
else:
    print("There are some changes")

    f = open(path, 'w')
    f.write(data_now)  # 何も書き込まなくてファイルは作成されました
    # data_now = list(data_now)
    # print(data_now)

    TOKEN = 'ubh9DRuV9zdbxHuY7bRdyigA1nSVTaMj1O8E2oE9QJt'
    api_url = 'https://notify-api.line.me/api/notify'
    #時刻を送る内容の変数に設定
    # send_contents = time
    # send_contents = "プログラムが起動されました。"
    send_contents = "ページに変化がありました"
    TOKEN_dic = {'Authorization': 'Bearer' + ' ' + TOKEN}
    send_dic = {'message': send_contents}

    requests.post(api_url, headers=TOKEN_dic, data=send_dic)

f.close()

 # while true; do python3 quake.py; sleep 20s; done
