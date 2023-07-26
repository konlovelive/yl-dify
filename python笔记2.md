#### 包、模块

##### 模块
​	Python 模块 (Module) ，是⼀个 Python ⽂件，以 .py 结尾，包含了 Python 对象定义和 Python 语句。
模块能定义函数，类和变量，模块⾥也能包含可执⾏的代码。
模块分类分为三种：
​	（1） 内置标准模块 （又称标准库），执行help('modules')查看所有python自带模块列表。
​	（2） 第三方开源模块 ，可通过“pip install 模块名”联网安装。  
​	（3） 自定义模块 ，即创建了一个.py文件，就可以称之为模块，可以在另一个程序里导入。

###### 模块的导入

- import 模块名【as 别名】

- from 模块名 import 功能名 （ **可以减少查询次数，提高执行速度**）

- from 模块名 import *  （ **谨慎使用**）

- from 模块名 import 功能名 as 别名

  

  模块的导入顺序：在需要导入的模块类型较多时，一般遵守：    

  （1）导入Python标准库模块，如sys、os、math等；    

  （2）导入第三方库，如numpy、Pandas、Matplotlib等；    

  （3）导入自己开发的模块，即编辑好.py文件。



##### 包

​	包将有联系的模块组织在⼀起，即放到同⼀个⽂件夹下，并且在这个⽂件夹创建⼀个名字

为 __init__.py ⽂件，那么这个⽂件夹就称之为包。

	###### 导入包

​	方式一：

​	`import 包名 . 模块名`

​	`	包名 . 模块名 . ⽬标`

​	举例：

import my_package . my_module1

my_package . my_module1 . info_print1 ()

​	方式二、

​	`from 包名 import *`

​	`模块名 . ⽬标`

举例：

from my_package import *

my_module1 . info_print1 ()



#### 函数

​	【定义】def 函数名():

​	函数封装的代码：

​	1.def是英文define的缩写
​	2.函数名称应该能够表达函数封装代码的功能，方便后续的调用
​	3.函数名称的命名应该符合标识符的命名规则
​	可由字母，下划线和数字组成，不能以数字开头，不能与关键字重名



#### 加密

##### hashlib：不可逆的加密

​	常用加密方法

<img src="C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230726185005381.png" alt="image-20230726185005381" style="zoom:50%;" />

生成加密字符串：

`hashobj = hashlib.md5(b' hello' )`

`result = hashobj. hexdigest()`

`print(result)`

运行结果：>> '6b8bfd346d1dcc17e6940aa59b9c4fa6864064a8'

​	将一个bite类型的‘hello’传入函数md5()中，将哈希对象返回值赋值给hashobj，hashobj调用器内置函数 hexdigest()将加密对象按16进制生成加密字符串

​	举例：

`import hashlib`

`import time`

`base_sign = 'muke'`

`a_timestamp = int(time.time())#生成时间戳，python的时间戳是float类型`

`_token = '%s%s' % (base_sign, a_timestamp)`

`print(_token)`

此时_token值为muke1581997979

`hashobj = hashlib.shal(_token.encode('utf-8'))`

`a_token = hashobj.hexdigest()`

`print(a_token)`



##### base64：通用不可解密

​	常用方法：

![image-20230726192447551](C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230726192447551.png)

`def encode(data):`	

​	`if isinstance(data, str):#判断data是不是字符串` 

​		`data = data.encode('utf-8')`

​	`elif isinstance(data, bytes):`

​		`data = data`

​	`else:`

​		`raise TypeError('data need bytes or str')#抛出错误`

`return base64.encodebytes(data).decode('utf-8')`





#### 日志logging

​	参考链接：[(31条消息) Python的日志输出_python logging 输出到文件_SteveKenny的博客-CSDN博客](https://blog.csdn.net/qq_62789540/article/details/126157460?ops_request_misc=&request_id=&biz_id=102&utm_term=Python中日志&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduweb~default-3-126157460.142^v91^insert_down1,239^v3^control&spm=1018.2226.3001.4187)

​	日志中包含的信息既有正常的程序访问日志，还可能有错误、警告等信息输出。
​	【分类级别】

​	等级最低：debug。帮助我们在开发的过程中查看一些输出信息是否正确。它可以替代print函数。

​	第二个等级是inform。它代表一般的消息类信息，只是为了记录一些程序的行为，比如程序已经执行到了某个位置时进行一些简单的记录。

​	第三个等级是warning，是一种警告。一般来说，程序不会出错，但是可能有一些潜在的风险可以抛出这种日志信息。

​	第四个等级error 。即业务中出现了重大问题。比如异常或者业务逻辑不应该执行到某种情况。

​	最后一种是critical，它是一种比error更高的级别，很少使用
