import json

from app.forms.book import SearchForm
from view_models.book import BookCollection

from . import web
from flask import jsonify, request
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook



@web.route('/book/search')
def serch():
    """
    接受四和个参数：q start count isbn
    简化后，两个参数：q：包括普通关键字isbn  page：页码
    :return:
    """
    # q=request.args['q']# request的args参数实际上不是字典类型，而是字典（字典核心特点——不可变）的子类，但是也可以像字典一样使用
    # page = request.args['page']

    # 校验
    form=SearchForm(request.args)# 取参数
    books=BookCollection()#保存多条数据结果
    if form.validate():
        q=form.q.data.strip()
        page = form.page.data# 去掉q参数前后的空格
        isbn_or_key = is_isbn_or_key(q)
        yushu_book=YuShuBook()
        if isbn_or_key == 'isbn':
             yushu_book.search_by_isbn(q)
        else:
             yushu_book.search_by_keyword(q,page)
        books.fill(yushu_book,q)

        #return jsonify(books.__dict__)# 由于books对象了里包含另一个对象，因此不能直接序列化
        return json.dumps(books,default=lambda o: o.__dict__)#序列化含有对象的对象

        #三种返回方式（api）：
        # return result#这种返回结果其实也可以
        #视图函数最后返回的需要为字符串格式，而result是字典类型（因为HTTP.get(url)返回的就是字典），因此result要序列化
        # return json.dumps(result),200,{'content-type':'application/json'}# 序列化result并设定http头（指定content-type为json数据类型
        return jsonify(result)#引用flask的jsonify，可以达到同样效果
    else:
        return jsonify({'msg':'参数校验失败'})
