import requests
# 封装http有关内容

# 发送http请求两种方式，python自带的urllib和第三方库requests（推荐）
class HTTP:

    #在Python中，如果一个类的方法没有使用类的`self`，那么它可能是一个静态方法。
    # 静态方法是一种与类相关联但不依赖于类或实例状态的方法。它们通常用于执行与类相关但不需要访问类或实例状态的任务。
    @staticmethod# 静态方法装饰器
    def get(url,return_json=True):
        r=requests.get(url)# r是对requests结果的封装

        #url访问成功与否
        # if r.status_code==200:
        #     if return_json:
        #         return r.json()
        #     else:
        #         return r.text# 返回不是json数据类型的普通数据
        #     pass
        # else:
        #     if return_json:
        #         return {}#返回一个空字典
        #     else:
        #         return ''# 返回一个空字符串
        #简略写法1——三级表达式
        if r.status_code!=200:
            return {} if return_json else ''
        return r.json() if return_json else r.text