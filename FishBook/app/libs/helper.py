
# 判断传入url的参数是isbn编号还是书名
def is_isbn_or_key(word):
    # 默认传入的q参数表示关键字
    isbn_or_key = 'key'
    # isbn序列号有两种，isbn13（13个0-9数字组成），isbn10（10个0-9数字和一些'-'）
    if len(word) == 13 and word.isdigit():  # 判断q是否全由数字组成
        isbn_or_key = 'isbn'
    short_word = word.replace('-', '')
    if '-' in word and len(short_word) == 10 and short_word.isdigit():
        isbn_or_key = 'isbn'
    return isbn_or_key