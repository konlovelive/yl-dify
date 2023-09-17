# ViewModel可以集中处理数据

# 用于处理单个数据
class BookViewModel:
    def __int__(self, book):
        self.title = book['title']
        self.publisher = book['publisher']
        self.pages = book['pages'] or ''
        self.author = '、'.join(book['author'])  # data['author']的值本身是个列表，用python中的函数将列表变成用、拼接成的字符串
        self.price = book['price']
        self.summary = book['summary'] or ''
        self.image = book['image']


# 处理多个数据
class BookCollection:
    def __int__(self):
        self.total = 0
        self.books = []
        self.keyword = ''

    def fill(self, yushu_book, keyword):
        self.total = yushu_book.total
        self.keyword = keyword
        self.books = [BookViewModel(book) for book in yushu_book.books]


class _BookViewModel:
    @classmethod
    def package_single(cls, data, keyword):  # 处理返回结果只有1本书时
        # 返回字典
        returned = {
            'book': [],
            'total': 0,
            'keyword': keyword
        }
        if data:
            returned['total'] = 1
            returned['book'] = [cls._cut_book_data(data)]
        return returned

    classmethod

    def package_collection(cls, data, keyword):  # 处理返回结果有多本书时
        # returned与上面的returned相同，保证得到不同类型结果后返回给自己的网页的是同样的数据结构
        returned = {
            'book': [],
            'total': 0,
            'keyword': keyword
        }
        if data:
            returned['total'] = data['total']
            returned['book'] = [cls._cut_book_data(data) for book in data['book']]  # 列表推导式
        return returned

    classmethod

    def _cut_book_data(cls, data):
        book = {
            'title': data['title'],
            'publisher': data['publisher'],
            'pages': data['pages'] or '',
            'author': '、'.join(data['author']),  # data['author']的值本身是个列表，用python中的函数将列表变成用、拼接成的字符串
            'price': data['price'],
            'summary': data['summary'] or '',
            'image': data['image']
        }
        return book
