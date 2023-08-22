import requests
from lxml import etree
import pymysql



# 链接mysql的方法
def connect_mysql():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='mima4748',
        db='flask_qa',
        port=3306,
        charset='utf8'
    )
    return conn


# 获取文章链接,保存入数据库
def get_index_links():
    # 数据库连接对象
    conn = connect_mysql()


    url = "https://www.csdn.net/?spm=1000.2115.3001.4476"
    head = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36'
    }
    response = requests.get(url, headers=head, proxies=None)

    print(response)
    # 状态码是否正常
    if response.status_code >= 200 or response.status_code < 300:
            # 解析网页
            html = etree.HTML(response.text)

            #首页文章
            content = html.xpath('//*[@id="userSkin"]/div[2]/div/div[2]/div[1]/div[2]/div/div/div[1]/article/a')

            # csdn首页没有页码，只爬取13条数据
            for i in range(1,13):

                # 数据库数据写入
                cursor = conn.cursor()  # 数据库游标
                sql = "INSERT INTO csdn_index_links(link,title,`desc`,agree,disagree,author) VALUES (%s,%s,%s,%s,%s,%s);"

                link=html.xpath(
                    '//a[@target="_blank"]/@href')[i]
                print(link)
                title = html.xpath(
                    '//span[@class="blog-text"]//text()')[i]
                 # type(title)
                desc = html.xpath(
                    '//p[@class="desc"]//text()')[i]

                agree = "2"
                disagree = "3"
                author = html.xpath(
                    '//div[@class="operation-c"]/a//text()')[i]
                print(type(title))
                print(type(disagree))
                # 执行 SQL 插入操作，
                cursor.execute(sql,[str(link), str(title), str(desc), str(agree), str(disagree), str(author)])
                conn.commit()  # 并提交事务

                # 关闭游标
                cursor.close()

            conn.close()
    else:
        print('请求异常，请稍候重试！')




if __name__ == '__main__':
    get_index_links()
