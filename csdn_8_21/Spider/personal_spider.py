import requests
from bs4 import BeautifulSoup
import pymysql



#链接mysql的方法
def connect_mysql():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='mima4748',
        db='csdn_spider',
        port=3306,
        charset='utf8'
    )
    return conn

# 获取文章链接,保存入数据库
def get_csdn_links():
    # 数据库连接对象
    conn=connect_mysql()

    for i in range(1,13):# 13是因为爬取的作者有这么多页内容
        url="https://lexsaints.blog.csdn.net/article/list/"
        url=url+str(i)
        print(url)
        response = requests.get(url,timeout=1)
        print('type(request)', response)
        print('request.status_code', response.status_code)
        print('request.encoding', response.encoding)
        print('request.cookies', response.cookies)

        #使用 BeautifulSoup 解析响应内容
        soup=BeautifulSoup(response.text,'lxml')
        # 该div中包含文章的链接和标题
        articles=soup.find_all('div',{'class':'article-item-box csdn-tracking-statistics'})

        for article in articles:
            cursor=conn.cursor()# 数据库游标
            sql = "INSERT INTO csdn_links(link,title) VALUES (%s,%s);"
            #从 find_all 返回的列表中选择第一个 <a> 标签，也就是文章链接所在的标签。
            link=article.find_all("a")[0].get("href").replace(" ","").replace("\n","")# 获取文章的链接
            title=article.find_all("a")[0].get_text().replace(" ","").replace("\n","")# 获取文章的标题

            #执行 SQL 插入操作，
            cursor.execute(sql,[link,title])
            conn.commit()#并提交事务

            # 关闭游标和数据库
            cursor.close()
    conn.close()


if __name__ == '__main__':
    get_csdn_links()
