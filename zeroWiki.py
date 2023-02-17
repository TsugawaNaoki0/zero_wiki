import urllib.request, urllib.error
import requests
from bs4 import BeautifulSoup




class zeroWiki_class():
    def zeroWiki(self):
        box = [["https://ja.wikipedia.org/wiki/%E5%85%AC%E5%AE%89%E8%AD%A6%E5%AF%9F", "オバケ"],
               ["https://ja.wikipedia.org/wiki/%E3%82%B5%E3%83%B3%E3%83%80%E3%83%BC%E3%83%BB%E3%83%94%E3%83%81%E3%83%A3%E3%82%A4", "英美"],
               ["https://ja.wikipedia.org/wiki/Apple", "料理人"],
               ["https://ja.wikipedia.org/wiki/%E3%83%9E%E3%83%BC%E3%82%AF%E3%83%BB%E3%82%B6%E3%83%83%E3%82%AB%E3%83%BC%E3%83%90%E3%83%BC%E3%82%B0", "記号"],
               ["https://ja.wikipedia.org/wiki/%E3%82%B8%E3%82%A7%E3%83%95%E3%83%BB%E3%83%99%E3%82%BE%E3%82%B9", "聖職者の村"],
               ["https://ja.wikipedia.org/wiki/%E3%82%B5%E3%83%86%E3%82%A3%E3%82%A2%E3%83%BB%E3%83%8A%E3%83%87%E3%83%A9", "絶対的な真理"],

               ["https://ja.wikipedia.org/wiki/%E4%B8%89%E8%8F%B1%E5%95%86%E4%BA%8B", "ガイト"],
               ["https://ja.wikipedia.org/wiki/%E3%82%B5%E3%83%86%E3%82%A3%E3%82%A2%E3%83%BB%E3%83%8A%E3%83%87%E3%83%A9", "アンエイ"],
               ["https://ja.wikipedia.org/wiki/%E3%82%B5%E3%83%86%E3%82%A3%E3%82%A2%E3%83%BB%E3%83%8A%E3%83%87%E3%83%A9", "コウトウ"],
               ["https://ja.wikipedia.org/wiki/%E3%82%B5%E3%83%86%E3%82%A3%E3%82%A2%E3%83%BB%E3%83%8A%E3%83%87%E3%83%A9", "ヘイズ"],
               ["https://ja.wikipedia.org/wiki/%E3%82%B5%E3%83%86%E3%82%A3%E3%82%A2%E3%83%BB%E3%83%8A%E3%83%87%E3%83%A9", "シモク"],
               ["https://ja.wikipedia.org/wiki/%E3%82%B5%E3%83%86%E3%82%A3%E3%82%A2%E3%83%BB%E3%83%8A%E3%83%87%E3%83%A9", "タイヤ"],
               ["https://ja.wikipedia.org/wiki/%E3%82%B5%E3%83%86%E3%82%A3%E3%82%A2%E3%83%BB%E3%83%8A%E3%83%87%E3%83%A9", "トウホン"],



               ]

        for round in range(len(box)):
            url = str(box[round][0])
            object = str(box[round][1])

            # print(url)
            print(str(box[round][1]) + "<br><br>")

            path = "./data/quake_data" + str(round+1) + ".txt"

            html = urllib.request.urlopen(url)

            soup = BeautifulSoup(html, "html.parser")

            data_now = str(soup)

            f = open(path, 'r', encoding='UTF-8')
            data_before = f.read()

            if (data_before == data_now):
                # print("no change")
                print()
            else:
                # print("There are some changes")
                print()
                f = open(path, 'w')
                f.write(data_now)

                TOKEN = 'ubh9DRuV9zdbxHuY7bRdyigA1nSVTaMj1O8E2oE9QJt'
                api_url = 'https://notify-api.line.me/api/notify'

                send_contents = "[" + object + "]" + "が動きました。"
                TOKEN_dic = {'Authorization': 'Bearer' + ' ' + TOKEN}
                send_dic = {'message': send_contents}

                requests.post(api_url, headers=TOKEN_dic, data=send_dic)

            f.close()
        return sample

if __name__ == '__main__':
    aaa = zeroWiki_class()
    bbb = aaa.zeroWiki()
    print(bbb)
