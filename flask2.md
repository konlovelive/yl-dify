day8:



### 响应

#### 响应报文



可以是字符串、可以是元组(tuple)(response, status, headers)或(response, headers)



响应元组

<1>response———响应内容

 <2>status——响应状态码 

<3>headers——响应头信息

使用make_response代替

![image-20230728112346124](C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230728112346124.png)

​	{}中的内容是新增的响应头中的信息

![image-20230728112933546](C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230728112933546.png)

aaa

![image-20230728113220722](C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230728113220722.png)

![image-20230728113248177](C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230728113248177.png)

响应HTML

![image-20230728113417935](C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230728113417935.png)

从文件中响应html

​		![image-20230728114150357](C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230728114150357.png)

​		注意所有文件html文件

![image-20230728114109094](C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230728114109094.png)





### 内部视图

​	重定向

​		redirect()：实现重定向

​		abort():处理错误

<img src="C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230728115110567.png" alt="image-20230728115110567" style="zoom:67%;" />

ab

<img src="C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230728115202756.png" alt="image-20230728115202756" style="zoom:67%;" />

重定向到一个没有权限的页面——错误异常处理

<img src="C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230728115332915.png" alt="image-20230728115332915" style="zoom:67%;" />



### 模板

​	flask中默认使用jinja2作为默认模板引擎

#### 默认配置

##### 渲染机制

​	模板引擎在浏览器展示HTML的步骤：

​		从磁盘读取html字符串

​		将满足特定规则的内容进行替换

​		发送给浏览器展示

##### 具体实现

`template_folder='templates'`—-模板的默认目录（指定模板的文件夹）

或者也可以自己指定目录

![image-20230728150439606](C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230728150439606.png)

 `render_template()`——(x)html自动转义

​	从磁盘template目录下找到对应的模板文件并读出渲染到浏览器中

<img src="C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230728150622143.png" alt="image-20230728150622143" style="zoom:67%;" />

 `render_template_string()`―—字符串自动转义

​		直接把一个HTML的字符串渲染到浏览器中，没有从磁盘中读取

<img src="C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230728151331189.png" alt="image-20230728151331189" style="zoom:50%;" />

`{% autoescape%}`——手动设置是否转义 

​	转义：把有特殊意义的字符显示出来



#### 转义字符

![image-20230728140143986](C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230728140143986.png)



#### 全局对象

config——Flask的配置信息

request——请求对象

session——会话对象

g——请求相关的全局变量(如：g.user)



#### 上下文处理器

​	在模板的上下文中添加新的内容内容可以是变量，也可以是函数`@app.context_processor`

`def inject_user():`

​		`return dict(user=g.user)`



#### 全局函数

​	url_for（）：URL解析函数，（如静态文件地址解析、链接跳转地址链接）

​	get_flashed_messages()：会话消息



####  模板变量的使用

##### 普通类型

<img src="C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230728154010863.png" alt="image-20230728154010863" style="zoom:50%;" />

<img src="C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230728153937597.png" alt="image-20230728153937597" style="zoom:50%;" />

浏览器效果：

<img src="C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230728154038574.png" alt="image-20230728154038574" style="zoom:50%;" />

##### 字典dict类型

​		【语法】`{{object.attribute}}`或`{{object['attribute']}}`

<img src="C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230728154530638.png" alt="image-20230728154530638" style="zoom:50%;" />

​		在.html文件中

<img src="C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230728154657803.png" alt="image-20230728154657803" style="zoom: 50%;" />



##### list/tuple类型

​		通过下标<img src="C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230728154825384.png" alt="image-20230728154825384" style="zoom:50%;" />

<img src="C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230728154846048.png" alt="image-20230728154846048" style="zoom:50%;" />



##### list/tuple嵌套类型

app.py文件：

<img src="C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230728160250962.png" alt="image-20230728160250962" style="zoom:50%;" />

.html文件：

<img src="C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230728160214776.png" alt="image-20230728160214776" style="zoom:50%;" />

运行结果：

<img src="C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230728160129398.png" alt="image-20230728160129398" style="zoom:50%;" />















































## bing ai

​	微软大号无法使用bing ai聊天：登录成功状态要求登录，点击登录也无效

![image-20230728191505357](C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230728191505357.png)

今天偶然可以使用了，但是也还是有问题

![image-20230728190605774](C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230728190605774.png)

刷新页面后又回到了第一种状态，查找原因可能是因为是国内qq邮箱注册且第一次的地区设置为了中国

只能用新号了

