# 启动文件
from app import create_app
from flask import current_app

app=create_app()



a=current_app

if __name__ == '__main__':
    print('id为'+str(id(app))+'的启动')
    app.run(host='0.0.0.0', debug=app.config['DEBUG'])

# 没有app.runweb服务器居然也能启动，？

# 示例连接地址：
#http://127.0.0.1:5000/book/search/9787501524044/1


