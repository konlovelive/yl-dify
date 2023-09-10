from app.forms.book import SearchForm

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
    form=SearchForm(request.args)
    if form.validate():
        q=form.q.data.strip()
        page = form.page.data# 去掉q参数前后的空格
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = YuShuBook.search_by_isbn(q)
        else:
            result = YuShuBook.search_by_keyword(q,page)
        #三种返回方式（api）：
        # return result#这种返回结果其实也可以
        #视图函数最后返回的需要为字符串格式，而result是字典类型（因为HTTP.get(url)返回的就是字典），因此result要序列化
        # return json.dumps(result),200,{'content-type':'application/json'}# 序列化result并设定http头（指定content-type为json数据类型
        return jsonify(result)#引用flask的jsonify，可以达到同样效果
    else:
        return jsonify({'msg':'参数校验失败'})
