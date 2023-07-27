#### MTV模型

[Django的框架模式——MTV - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/362268440)

MTV模型中，视图一定存在

<img src="C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230727141701197.png" alt="image-20230727141701197" style="zoom:50%;" />

#### 启动选及调试

##### 启动服务器步骤

1：设置环境变量Windows :

 `set FLASK_APP=flasker.py` 

步骤2：flask run启动内置web服务器

指定IP及端口：`flask run --host=0.0.0.0 --port=8001 # 变更启动地址或者端口号` 

或：`flask run -h 0.0.0.0 -p 8001`

host指主机，ip地址：0.0.0.0  端口号：8001

![image-20230727143050579](C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230727143050579.png)

按ctrl+c结束后：

![image-20230727143331531](C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230727143331531.png)

localhost等同于127.0.0.1



##### 开启调试模式

​	【目的】代码修改后可以自动重启服务器

​	【步骤】`set FLASK_ENV=development`

​					`flask run # 启动服务器`

​		【注意】在生产环境下不要开启调试模式，即



#### flask安装错误解决

1.flask安装成功验证：

cmd中输入

`python`

`import flask`

`flask.__version__#注意前后都有两个下划线`

此时会输出`'2.2.5'`类似的字符



#### URL

​	【介绍】URL是统一资源定位符，对可以从互联网上得到的资源的位置和访问方法的一种简洁的表示，是互联网上标准资源的地址，互联网上的每个文件都有一个唯一的URL

基本URL包含**模式**（或称协议）、**服务器名称**（或IP地址）、 **路径和文件名**`scheme://host[:port#]/path/../[;url-params][?querystring][#anchor]`

`scheme`是模式、协议，`?querystring`是查询参数，可有可无，`#anchor`是锚点连接



##### url协议

http——超文本传输协议资源

https——用安全套接字层传送的超文本传输协议

ftp——文件传输协议



##### 常见http请求方式

​	GET:可以用浏览器直接访问,请求可以携带参数，但是有长度限制，请求参数是直接放在URL后面的

​	POST：不能用浏览器直接访问



##### http常见状态码

2xx请求成功

3xx重定向

4xx请求错误

5xx服务器错误



#### URL配置

##### url与函数的关系

通过浏览器访问URL（IP+端口+指定的一个名称）对应到一个视图函数  来处理

<img src="C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230727153855381.png" alt="image-20230727153855381" style="zoom:50%;" /> 

（也可以多个url对应同一个视图函数）

​	路由过程：在浏览器当中输入一个唯一的URL，它去找到对应的视图函数进行响应、得到返回的过程



##### 路由配置

###### 配置方式

方式一：使用装饰器

【语法规则】`@app.route(url_name, methods)`

【参数解释】url：匹配的URL地址

​					methods:所支持的请求方式（['GET','POST']）

【示例】：`@app.route('/login', methods=['GET', 'POST'])`



方式二：使用API配置

【语法规则】`app.add url rule(url, url name, view name)`

【参数解释】url：匹配的URL地址

​						url name:给URL的命名

​						view name:视图函数

【示例】：`@app.route('/login', methods=['GET', 'POST'])`



###### 配置规则

匹配整个文字`@app.route('/hello')`

传递参数`@app.route('/user/<username>')`

指定参数类型`@app.route('/post/<int:post_id>')`

可指定的类型

![image-20230727161458291](C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230727161458291.png)



#### 请求-响应

​	【运行过程】

（1）写完了flask程序之后，通过命令`flask run`，或通过IDE工具的运行，启动了一个flask的服务器，此时就可以通过浏览器去访问刚刚创建的URL，此时（访问url这个动作）会发送一个请求到这个服务器；

（2）服务器接收到这个请求之后，会根据用户输入的url找到对应的视图函数进行处理，处理完后，会把结果发送到浏览器端；

（3）浏览器接收返回的内容并呈现出来。

<img src="C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230727190042252.png" alt="image-20230727190042252" style="zoom:50%;" />



##### 请求分派

​	也就是路由分发，每个URL的规则都会有与之对应的一个视图函数来进行

<img src="C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230727190335236.png" alt="image-20230727190335236" style="zoom:50%;" />

###### 应用上下对象

​	也称为程序上下文，针对写好的flask程序。

​	【分类】current_app：当前应用的实例。那这个实例指的是谁呢？就是我们代码当中，大家看第二行得到了这个APP，

<img src="C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230727190808104.png" alt="image-20230727190808104" style="zoom:50%;" />

​					g：处理请求时的一个临时的存储对象，每一次请求都会重新设置这个变量的值。

​		![image-20230727191344370](C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230727191344370.png)

程序运行并访问指定页面[127.0.0.1:5000/index](http://127.0.0.1:5000/index)后有：
![image-20230727191500474](C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230727191500474.png)

可以得到：**current_app只是当前实例的一个引用，但不是同一个**



##### 请求上下文对象

request：请求对象，封装了客户端发出的HTTP请求中的内容

session：用户会话（dict)，各请求之间的数据共享

​		比如用户的浏览器a中的cookie（以字典的键值对形式保存数据）中存有数据，那么浏览器向服务端发送请求时都会带上cookie，服务端就会根据该cookie返回指定的session

![image-20230727192346197](C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230727192346197.png)



##### 请求报文

![image-20230727193052499](C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230727193052499.png)



###### 请求报文常用参数

method:请求的类型（GET/POST/OPTIONS等）

form:POST请求数据dict

args:GET请求数据dict

values:POST请求和GET请求数据集合dict

files:上传的文件数据dict

cookies:请求中的cookie dict

headers:HTTP请求头



​		请求报文练习：

​	（1）获取GET参数

![image-20230727194623761](C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230727194623761.png)

![image-20230727194640120](C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230727194640120.png)

​			（2）解析请求头中的ip地址























































#### 安装pipenv报错及解决

在cmd中输入了命令pipenv --python 3.7，但是运行结果为Fatal error in launcher: Unable to create process using '"d:\python\python.exe" "D:\yan\Environ\python\Scripts\pipenv.exe" --python 3.7': ???????????，

![image-20230727092416592](C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230727092416592.png)

可能是由于我移动python文件夹后导致的问题

<img src="C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230727112710902.png" alt="image-20230727112710902" style="zoom:50%;" />

但是：输入后没反应

![image-20230727104303486](C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230727104303486.png)

![image-20230727105320151](C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230727105320151.png)

并且

<img src="C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230727112850738.png" alt="image-20230727112850738" style="zoom:50%;" />

<img src="C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230727104541359.png" alt="image-20230727104541359" style="zoom:50%;" />



还的是bing

<img src="C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230727113043238.png" alt="image-20230727113043238" style="zoom:50%;" />

直接运行pipenv脚本

<img src="C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230727105745853.png" alt="image-20230727105745853" style="zoom:67%;" />



卸载pipenv

<img src="C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230727110432436.png" alt="image-20230727110432436" style="zoom:50%;" />

确保pip还在

<img src="C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230727110552864.png" alt="image-20230727110552864" style="zoom:50%;" />

不过卸载后这个虚拟环境还是在的

<img src="C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230727110653100.png" alt="image-20230727110653100" style="zoom:50%;" />



解决了pipenv找不到路径的问题

![image-20230727110819100](C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230727110819100.png)

pipenv直接安装失败

<img src="C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230727110724683.png" alt="image-20230727110724683" style="zoom:50%;" />

查找发现此命令需要pip对应的python解释器在c盘

https://blog.csdn.net/weixin_45122740/article/details/110350799

那就换源搞

命令：pip install 包名 -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com

来源链接：[(32条消息) python使用pip安装包报错的解决办法（ERROR: Could not find a version that satisfies the requirement XXX）_遗忘的迟来的风的博客-CSDN博客](https://blog.csdn.net/qq_43490217/article/details/126639981?ops_request_misc=&request_id=&biz_id=102&utm_term=ERROR: Could not find a versio&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduweb~default-2-126639981.142^v91^insert_down1,239^v3^control&spm=1018.2226.3001.4187)

<img src="C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230727112422478.png" alt="image-20230727112422478" style="zoom:50%;" />

安装好后直接使用虚拟环境，发现

![image-20230727113432165](C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230727113432165.png)

还是卸载前的虚拟环境，没有另外创建

然后安装flask

![image-20230727113646010](C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230727113646010.png)