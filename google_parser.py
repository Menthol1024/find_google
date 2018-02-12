# coding:utf8
from bs4 import BeautifulSoup


class HtmlParser(object):
    # 解析URL对应的内容
    def parse(self, html_cont):
        self.html_cont = html_cont
        res = []
        # print(self.html_cont)
        # try:
        # print(type(self.html_cont))
        print(self.html_cont)
        #print(html_cont[1], html_cont[0])
        if self.html_cont[1] is None or self.html_cont[0] is None:

            print("没有内容")
        else:
            self.html_cont1 = self.html_cont[1]
        if html_cont[0] is None and self.html_cont1 is None:
            return False
        elif html_cont[0]:
            self.soup = BeautifulSoup(html_cont[0], 'html.parser')
            divs = self.soup.find_all('div', class_="rc")
            for x in range(len(divs)):
                div = divs[x]
                url = div.find_all('a')[0]
                res.append(url['href'])
                res.append(url.get_text())
        elif self.html_cont1:
            self.soup = BeautifulSoup(self.html_cont1, 'html.parser')
            cites = self.soup.find_all('cite')
            print(cites)
        # except Exception as e:
        #     print(e)
        #     return 1101

        return res
