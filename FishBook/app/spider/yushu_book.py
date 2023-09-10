from app.libs.httper import HTTP
from flask import current_app# current_app用于指代当前的flask核心对象


# 两种api接口：关键字：http://t.yushu.im/v2/book/search?q={}&start={(}&count=(}
# isbn搜索：http://t.yushu.im/v2/book/isbn/{isbn}
class YuShuBook:
    isbn_url='http://t.talelin.com/v2/book/isbn/{}'
    keyword_url='http://t.talelin.com/v2/book/search?q={}&count={}&start={}'

    @classmethod# 类函数，用cls来访问类属性
    def search_by_isbn(cls,isbn):
        url=cls.isbn_url.format(isbn)#format函数将{}占位符替换为isbn参数的值，从而生成一个新的字符串。
        result=HTTP.get(url)
        return result
    @classmethod
    def search_by_keyword(cls,keyword,page=1):
        url=cls.keyword_url.format(keyword,current_app.config['PER_PAGE'],cls.calculate_start(page))
        result=HTTP.get(url)
        return result

    @staticmethod
    def calculate_start(page):
        return (page-1)*current_app.config['PER_PAGE']