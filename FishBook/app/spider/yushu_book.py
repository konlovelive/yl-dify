from app.libs.httper import HTTP
from flask import current_app# current_app用于指代当前的flask核心对象


# 两种api接口：关键字：http://t.yushu.im/v2/book/search?q={}&start={(}&count=(}
# isbn搜索：http://t.yushu.im/v2/book/isbn/{isbn}
class YuShuBook:
    isbn_url='http://t.talelin.com/v2/book/isbn/{}'
    keyword_url='http://t.talelin.com/v2/book/search?q={}&count={}&start={}'

    def __int__(self):  # 带有self的大多Wie实例方法
        self.tatal = 0
        self.books = []

    def __fill_single(self,data):# 用于处理所有数据为1条记录的结果
        if data:
            self.tatal=1
            self.books.append(data)

    def __fill_collection(self,data):
        self.tatal=data['total']
        self.books=data['books']


    def search_by_isbn(self,isbn):
        url=self.isbn_url.format(isbn)#format函数将{}占位符替换为isbn参数的值，从而生成一个新的字符串。
        result=HTTP.get(url)
        self.__fill_single(result)#通过isbn搜索的结果唯一

    def search_by_keyword(self,keyword,page=1):
        url=self.keyword_url.format(keyword,current_app.config['PER_PAGE'],self.calculate_start(page))
        result=HTTP.get(url)
        self.__fill_collection(result)#通过isbn搜索的结果唯一

    @staticmethod
    def calculate_start(page):
        return (page-1)*current_app.config['PER_PAGE']