# coding:utf8

import google_downloader, google_parser


class SpiderMain(object):
    # 初始化
    def __init__(self):
        self.downloader = google_downloader.HtmlDownloader()
        self.parser = google_parser.HtmlParser()
        # self.root_url = root

    def craw(self, root_url):
        self.res = self.downloader.download(root_url)
        # print(self.res)
        result = self.parser.parse(self.res)

        if result == False:
            return "代理连接超时"
        else:
            # return result
            for i in result:
                print(i)


t = SpiderMain("https://www.google.com.hk/search?q=inurl:php?id=&start=0")
# # t = SpiderMain("https://zh.wikipedia.org/wiki/Wikipedia:%E9%A6%96%E9%A1%B5")
t.craw()
