import requests
from bs4 import BeautifulSoup
import pymysql




# # 自定义请求头
#     headers = {
#         "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36 Edg/115.0.1901.200",
#     }

# 建立数据库连接
db = pymysql.connect(
    host='localhost',
    user='root',
    password='password',
    db='mydatabase'
)


#  使用 Requests 库抓取网页：
url = 'http://www.example.com'
response = requests.get(url)
html = response.text

# 使用 BeautifulSoup 库解析 HTML：
soup = BeautifulSoup(html, 'html.parser')
data = soup.find_all('a')

# 将数据导入数据库
cursor = db.cursor()
for item in data:
    title = item.string
    url = item.get('href')
    sql = f"INSERT INTO mytable (title, url) VALUES ('{title}', '{url}')"
    cursor.execute(sql)
db.commit()

# 关闭数据库连接
db.close()