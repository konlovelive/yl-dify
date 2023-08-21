

import mysql.connector
from datetime import datetime

from conf import conn
from utils import constants

# 创建表accounts_user
def create_sqlform_accounts_user():
    ''' create_user_table_query 是一个变量名，用于存储 SQL 查询语句字符串。
    表示多行字符串的开始和结束标记。在这里，它表示一个多行的文本块，可以包含多行文字。'''
    # 创建用户表
    create_user_table_query = '''
    CREATE TABLE IF NOT EXISTS accounts_user (
        id INT AUTO_INCREMENT PRIMARY KEY,-- AUTO_INCREMENT：表示这列的值会自动递增
        username VARCHAR(64) UNIQUE NOT NULL,-- NOT NULL:是一个列约束，用于指定该列在插入数据时不能为空值。
        nickname VARCHAR(64),
        password VARCHAR(256) NOT NULL,
        avatar VARCHAR(256),-- 头像
        status SMALLINT DEFAULT 1,-- 是否有效，无效用户不能登录，默认为1  SMALLINT 是一种整数数据类型，用于存储较小范围的整数值
        is_super SMALLINT DEFAULT 0,-- 是否是管理员
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,-- 创建时间
        updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP-- 最后修改时间
    )
    '''
    cursor = conn.cursor()
    cursor.execute(create_user_table_query)  # 执行创建表 语句

    # # 插入用户数据
    # insert_user_query = '''
    # INSERT INTO accounts_user
    # (username, nickname, password, avatar, status, is_super, created_at, updated_at)
    # VALUES
    # (%s, %s, %s, %s, %s, %s, %s, %s)
    # '''
    # user_data = ('user123', 'User One', 'hashed_password', None, 1, 0, datetime.now(), datetime.now())
    # cursor.execute(insert_user_query, user_data)

    # 提交事务并关闭连接
    conn.commit()
    cursor.close()
    # conn.close() # 设为在退出登录后关闭



class User():
    """ 用户模型 """

    # 知道用户名
    # def __init__(self,username):
    #     # 查询该用户名的账号
    #     select_user_query = '''
    #                     SELECT * FROM accounts_user
    #                     WHERE username = %s
    #                     LIMIT 1  --LIMIT 1 表示查询只返回满足条件的第一条记录，即使有多条记录满足条件
    #                     '''
    #     cursor = conn.cursor()  # 游标
    #     # 执行查询
    #     cursor.execute(select_user_query, (username))
    #
    #     # 获取查询结果的第一行数据
    #     self.username_record = cursor.fetchone()
    #     cursor.close()
    #     # 现在 username_record 变量中保存了满足条件的第一个记录，如果没有找到则 username_record 为 None
    #     print(self.username_record)
    #
    # #@property
    # def get_name_record(self):
    #     return self.__class__.username_record
    #
    # # 知道用户名和密码
    # def __init__(self,username,password):
    #     # 查询该用户名的账号
    #     select_user_query = '''
    #                     SELECT * FROM accounts_user
    #                     WHERE username = %s AND password = %s
    #                     LIMIT 1  -- LIMIT 1 表示查询只返回满足条件的第一条记录，即使有多条记录满足条件
    #                     '''
    #     cursor = conn.cursor()  # 游标
    #     # 执行查询
    #     cursor.execute(select_user_query, (username,password))
    #
    #     # 获取查询结果的第一行数据
    #     self.username_pwd_record = cursor.fetchone()
    #     cursor.close()
    #     # 现在 username_record 变量中保存了满足条件的第一个记录，如果没有找到则 username_record 为 None
    #     print(self.username_pwd_record)
    #
    # #@property
    # def get_name_pwd_record(self):
    #     return self.__class__.username_pwd_record
    def __init__(self,username,password=None):
        if password is None:
            # 查询该用户名的账号
            select_user_query = '''
                                    SELECT * FROM accounts_user
                                    WHERE username = %s 
                                    LIMIT 1  --LIMIT 1 表示查询只返回满足条件的第一条记录，即使有多条记录满足条件
                                    '''
            cursor = conn.cursor()  # 游标
            # 执行查询
            cursor.execute(select_user_query, (username))

            # 获取查询结果的第一行数据
            self.username_record = cursor.fetchone()
            cursor.close()
            # 现在 username_record 变量中保存了满足条件的第一个记录，如果没有找到则 username_record 为 None
            print(self.username_record)
        else:
            # 知道用户名和密码
            select_user_query = '''
                                    SELECT * FROM accounts_user
                                    WHERE username = %s AND password = %s
                                    LIMIT 1  -- LIMIT 1 表示查询只返回满足条件的第一条记录，即使有多条记录满足条件
                                    '''
            cursor = conn.cursor()  # 游标
            # 执行查询
            cursor.execute(select_user_query, (username, password))

            # 获取查询结果的第一行数据
            self.username_pwd_record = cursor.fetchone()
            cursor.close()
            # 现在 username_record 变量中保存了满足条件的第一个记录，如果没有找到则 username_record 为 None
            print(self.username_pwd_record)


    #@property
    def get_name_record(self):
        return self.__class__.username_record



    #@property
    def get_name_pwd_record(self):
        return self.__class__.username_pwd_record



    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        """ 有效的用户才能登录系统 """
        return self.status == constants.UserStatus.USER_ACTIVE.value

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return '{}'.format(self.id)

    def __str__(self):
        return self.nickname
        # 创建游标
    # cursor = conn.cursor()
    #
    # # 执行查询语句获取数据
    # query = "SELECT id, username,nickname,password,avatar,status,is_super,created_at,updated_at FROM accounts_user"
    # cursor.execute(query)
    #
    # cursor.execute(query, (username, password))
    #
    # # 获取查询结果
    # result = cursor.fetchall()
    #
    # # 关闭游标和连接
    # cursor.close()
    #
    #
    # # 将数据存储到变量中
    # id = [row[0] for row in result]
    # username = [row[1] for row in result]
    # nickname= [row[2] for row in result]
    # password= [row[3] for row in result]
    # avatar= [row[4] for row in result]
    # status= [row[5] for row in result]
    # is_super= [row[6] for row in result]
    # created_at= [row[7] for row in result]
    # updated_at= [row[8] for row in result]