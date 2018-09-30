from 爬虫.AndroidSpider import html_downloader
from 爬虫.AndroidSpider import html_parser
from 爬虫.AndroidSpider import url_manager
from 爬虫.AndroidSpider import html_output
'''
爬取百度百科 Android 关键词相关词及简介并输出为一个HTML tab网页

Extra module:
BeautifulSoup
'''
class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownLoader()
        self.parser = html_parser.HtmlParser()
        self.out_put = html_output.HtmlOutput()

    def craw(self, root_url):
        count = 1
        flage=True
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print("craw %d : %s" % (count, new_url))
                headers = {
                    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.100 Safari/537.36"
                }
                html_content = self.downloader.download(new_url, retry_count=2, headers=headers)
                if flage:print("html_content",html_content.decode('utf-8'))
                new_urls, new_data = self.parser.parse(new_url, html_content, "utf-8")
                if flage: print(" new_urls, new_data",new_urls,new_data)
                self.urls.add_new_urls(new_urls)
                self.out_put.collect_data(new_data)
                if count >= 30:
                    break
                count = count + 1
                flage = False
            except Exception as e:
                print("craw failed!\n"+str(e))
        self.out_put.output_html()

if __name__ == "__main__":
    rootUrl = "http://baike.baidu.com/item/Android"
    objSpider = SpiderMain()
    objSpider.craw(rootUrl)
