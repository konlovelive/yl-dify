### 第一章——基础语法



#### 头注释——脚本头

​	头注释：写在python脚本第一行的用#号开头表示的信息就是头注释，包括：注释符号和注释内容。非强制需要，也称为特殊规则

​	作用：被系统或者解释器调用（比如告诉系统python解释器在哪，告诉python解释器：脚本编码的格式又是什么）

​	 有些不只是一个#，但都是以#开头

#coding:utf-8 定义coding 告诉系统脚本是何编码格式（utf-8内含有中文的编码）非必须



#### python函数的导入

​	导入：是将python的一些功能函数放到当前的脚本中使用，不导入功能无法直接在当前脚本使用（除了python自带的内置函数）

​	导入位置：在头注释的下方，业务代码的上方

​	导入函数举例：import os （这里import是内置函数，也就是导入关键字，os则是被导入的功能模块）

 

#### 内置函数

代码执行顺序：自上而下，逐行执行

​	内置函数：python中不需要导入就可以使用的函数

​	最常用的内置函数：print函数



#####   print函数——在cmd上打印

​	【格式】：print(object, end= ' ' )

​		print是函数名，也就是执行函数

​		(object, end= ' ' )是函数的参数体，参数体是函数执行的必要数据，有此数据才能执行函数。

​	object：需要打印的信息（包含文字、数字），多信息用逗号隔开

​	end：当print打印完信息后的操作，可不给end传递任何信息（即不使用end）， end= ' ' 表示默认打印完之后空一行，也可以给end改变值让print函数执行后不换行



##### 	type函数--判断变量类型

【返回类型】变量的类型

【格式】type(已被赋值的变量名或变量)

（注：变量就是存储在内存某一块地址中的数值，其值是可以改变的 变量名就是使用者在程序中使用这块地址时的命名）

​		例：cout=50

​		print(type(cout))

​		print(type(3.14))

​	

 ##### 内置函数id()——返回变量的内存地址

​    作用：返回变量的内存地址，格式： 数字地址= id(变量)



##### 内置函数len

​      【 作用】：返回字符串的长度，但是无法**返回数字类型的长度**，因为数字类型没有长度

​     【格式】： 返回值 = len(字符串)

​     （经常用于检查字符串有没有超出规定长度）（如密码长度）

​		每个字母、空格、汉字都是一个字符，查看类型函数type()

<img src="C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230725193724001.png" alt="image-20230725193724001" style="zoom:50%;" />



##### 内置成员运算符in

​	成员运算符——用来判断某个数据中有无指定的成员（元素）

​	【格式】'查找的字符' in '待查找的一串字符'  (注意in的左右各有一个空格)

​	【返回值】True 或者False

​	此外还有 ***not in***  运算符



##### 内置函数max    (与之相反作用的时内置函数min)

​	【作用】取传入多个参数中的最大值，或传入的可迭代对象（也就是可for循环的对象）元素中的最大值（一个参数时）

​	【格式】max(需判断的数据)

​	【返回值】最大的值

​	【判断方法】默认数值型参数：取最大值

​	字符型参数：按字母表排序靠后者0

​    （**中文字符 > 字母 > 数字 > 英文字符**

 	中文按拼音首字母算（abc…xyz的顺序依次增大））

具体见：[(31条消息) 10.Python——max()的用法_python的max函数_董十贝的博客-CSDN博客](https://blog.csdn.net/mrdonghe/article/details/99936106)

​	

#### 注释

单行：#

多行：''' 注释内容'''   """ 注释内容"""



#### 脚本执行入口（非必要

​	它也是程序的一部分

​	注意if后面有一个空格，必不可少

<img src="C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230725141545162.png" alt="image-20230725141545162" style="zoom:33%;" />

​	脚本入口作用：

​		1一个种好的规范，让代码结构清晰容易维护。可以把需要的业务代码写在脚本上方，在入口语句的缩进代码中统一执行，

​		2：python向其他严格要求有入口程序标准的语言看齐



#### 缩进：冒号:后面要有1个缩进

​	起始位置都是一样（开头齐平）的程序代表的是统一的代码块程序

​	结束缩进：只要在最新一行代码的起始位置回到上一级

<img src="C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230725145019985.png" alt="image-20230725145019985" style="zoom: 80%;" />



##### 常见关键字：

​	1.内置常量：False,None,True…

​	2.逻辑与或非：and,or,not

​	3.判断、与：if…elif…else,is,in

​	4.循环：for,while,break,continue

​	5.导入模块、包：import,form

​	6.函数：def,lambda,pass,return,yied

​	7.异常处理：try…except…finally,raise

​	8.重命名：as

​	9.变量：global,nonlocal

​	10.类：calss

​	11.删除：del

​	12.上下文管理：with



#### 运算符

![image-20230725194951662](C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230725194951662.png)

​	幂运算符c**a就是c的a次方

​	除法运算符是返回完整的结果

​	取整运算符是只返回结果的整数部分



#### 数据类型

​	python中一切都是对象，每个对象都有自己的属性与方法，对象里的特点就是它的属性，它的功能就是它的方法

python中的数据类型：

​	目的：为了让计算机高效的处理和展示数据

​	分类：数字类型(整型int,浮点型float)，字符串类型（str），布尔类型，空类型，列表类型，元组类型、字典类型



##### 布尔类型bool

​	【作用】：判断真假，布尔值只有True（真）  False （假）

​	【函数】bool（既可以代表布尔类型，也可以对于结果进行真假的判断）

​	其他类型和布尔类型的联系

​	int 类型： 0:False,  非0：True

​	float 类型:0.0：false，非0.0：true（0.00，0.0000，…此类都表示false）

​	str 空字符串：false，非空字符串true

​	计算机开发中01是计算机最原始的形态，放个占用空间最小，在使用中也常常用0表示false，1表示true

 

##### 空类型

​	不属于任何数据类型，也没有任何可操作的功能，空类型是属于False范畴

​	【固定值】：None（固有值唯一）

​	【作用】若不确定某对象的类型，可使用空类型



#### 列表list——[]   （可变

​	（1）是各种数据的集合，也是一种无限制长度的数据结构

​	列表有序、内容可重复、集合类型

​	列表中的元素存与一个[]中，用逗号,隔开

​	【索引序号】：**从左往右数从0开始，从右往左数从-1开始**

<img src="C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230725162151654.png" alt="image-20230725162151654" style="zoom:50%;" />

<img src="C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230725162358449.png" alt="image-20230725162358449" style="zoom:50%;" />

（2）在列表中可使用关键字 ***in 、max、 min*** ，注意此时元素类型统一

<img src="C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230725162748236.png" alt="image-20230725162748236" style="zoom:50%;" />

​	（3）【与数组对比】

| 同   | 数组里支持嵌套（二维数组）             |
| ---- | -------------------------------------- |
| 异   | 不支持混合（二维数组必须为同类型数据） |



 ##### list操作函数

| 函数名                | 功能                                         | 格式                              | 备注                                                         |                                                              |
| --------------------- | -------------------------------------------- | --------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| append                | 将一个成员添加到当前列表末尾上               | list.append(new_item)             | new_item是添加进列表的新成员                                 |                                                              |
| insert                | 将一成员添加到列表指定位置中                 | list.insert(index,new_item)       | index:新元素的位置（数字）  new_item：新成员                 | !['djJL')  print(list) ](data:image/png;base64,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) |
| count                 | 返回当前字符串中某个成员的个数               | num=list.count(item)              | item:查询的元素                                              |                                                              |
| remove                | 删除列表中指定的元素                         | list.remove(item)                 |                                                              | 1.删除成员不存在时报错  2.被删除元素有多个时只会删除第一个  3.不会返回新列表，是在原有列表上操作 |
| del  (不止对列表有效) | 将变量完全删除                               | del 变量                          |                                                              |                                                              |
| reverse               | 将列表反转                                   | list.reverse()                    |                                                              |                                                              |
| sort                  | 按一定规律排序                               | list.sort(key=None,reverse=False) | 1.key:参数比较  reverse=True降序  reverse=False升序（默认）  2.列表中元素类型必相同 |                                                              |
| clear                 | 将列表中得到数据清空                         | list.clear()                      |                                                              |                                                              |
| copy                  | 复制一份相同列表，两个列表内容相同，地址不同 | newlist=list.copy()               | 1.与二次赋值相区别，不在同一地址，数据也不同享变更  2.属于浅拷贝 |                                                              |
| extend                | 将其他列表或元组中的全部元素导入到当前列表中 | list.extend(itreable)             | lterable:代表列表或元组  无返回值                            |                                                              |
| pop                   | 通过索引号删除列表中指定的元素               | list.pop(num)                     |                                                              | ![list. pop (O)  print (list) ](data:image/png;base64,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) |

 



#### 元组tuple——()  （不可变

​	与列表类似，都是可以存储多种数据结构的队列，且也是有序、元素可重复的集合、长度无限制的数据结构、能在自身内无线嵌套



##### 	 列表与元组区别

​	1.元组比列表占用资源更小

​	2.列表是可变的，元组不可变

举例：有a、b两个元组，将他们相加后赋给a，查看a前后地址对比，地址改变，所以是用一个新的元组存储结果，而非覆盖修改原有元组

<img src="C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230725163348517.png" alt="image-20230725163348517" style="zoom:80%;" />

###### 	元组的类型

​	              <img src="C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230725163609926.png" alt="image-20230725163609926" style="zoom: 50%;" /> 

<img src="C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230725163717301.png" alt="image-20230725163717301" style="zoom: 50%;" />

当元组的元素为列表时，元素列表就不能再进行修改了

##### 	同样可以使用 max in min



#### 字典dict——{key：value，}

​	【基本概念】python中用dict代表字典并可以创建一个字典，用{}将一个个key和value存入字典

​	【格式】{'key':value, 'key':value}

​		key：支持字符串，数字和元组类型，但*不支持列表*, **key值唯一**

​		value：支持所有python的数据类型

​		python3.7后字典都有序

​	<img src="C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230725194912411.png" alt="image-20230725194912411" style="zoom:67%;" />

	##### 在列表和元组中定义字典

​	列表中：dict_arry=[{1:1, 2:2}, {'one' :1, 'two' :2}] (有两个字典，都是两个键值段)

​	元组中：dict_tuple=({1:1, 2:2}, {'one' :1, 'two' :2})

列表和元组函数（除了说明，都是只列表可使用）







#### 字符串str

​	单引号''和双引号""包括起来的字符

​	空字符串长度为0

​	注意：***字符串不可改变***

​    比如：name = 'a'     赋值后name会为‘a’分配储存空间

​    再有：name = 'b'      

​	改变的只是变量name，不是字符串 'a' ，原来的‘a’仍在自己的储存空间内，没有改变也无法改变，只是name被新的存储空间的‘b’赋值了而已，此时‘a’已经被清理了，如果想要在字符串里面再引用引号，用双引号引用时里面使用单引号，单引号里引用双引号

​	如果再有name = 'a'，此时name的地址和最开始a的地址不一样 

​	为了防止name = 'b'  后字符串a丢失，可以将name = 'a' 后，将name赋值给另一个新的变量name1=name，这时候name1里就存有a ，与name中的a地址一样（也就是对应同一个a）

​	 

##### 字符串的拼接：用”+ "

​	[注意]每次拼接第三个拼接，a=a+b后，a里面存放的内容地址改变了，因此这种拼接是产生了一个新的内容，而不是在原有内容基础上更新

​	<img src="C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230725194633977.png" alt="image-20230725194633977" style="zoom:67%;" />



##### 操作函数：

| 函数名                  | 功能                                                         | 格式                                                       | 说明                                                         |
| :---------------------- | ------------------------------------------------------------ | ---------------------------------------------------------- | ------------------------------------------------------------ |
| capitalize              | 将字符串的首字母大写，其他字母小写                           | newstr =string.capitalize()                                |                                                              |
| upper                   | 将字符串中所有字母大写                                       | newstr = string.capitalize()                               |                                                              |
| swapcase                | 将字符串中所有字母大小写互换                                 | newstr = string.swapcase()                                 |                                                              |
| count                   | 返回当前字符串中某个成员（元素）的个数                       | num=string.count('string中的某个字母或字母组合')           |                                                              |
| zfill                   | 为字符串定义长度，长度不够再左边用0补，长度刚好或者超过了width就不发生变化 | newstr = string.zfill(width)                               |                                                              |
| starswith和  endswith   | startswith判断字符串的开始位是不是某成员(成员可以是单个字符，也可以是一串)  endswith判断字符串的结束位是不是某成员 | string.startswith('字符')   string.endswith('字符')        | string.startswith('string')  string.endswith('string')  都是true |
| find和index             | 返回某成员再字符串中的位置                                   | string.find('成员')string.index('成员')                    | 1.从左往右，以0开始的  2.find找不到元素会返回-1  index找不到就会程序报错 |
| strip  lstrip  和rstrip | strip去掉字符串左右两边指定的元素，默认空格  lstrip是去掉字符串开头指定的元素，默认为空格  rstrip是去掉字符串开头指定的元素，默认为空格 | newstr=string.strip('item')                                | item是欲去除的元素，也可不填写的为默认值                     |
| replace                 | 将字符串中的就元素替换成新元素，并能指定替换的数量           | newstr=string.replace(old,new,max)                         | old：被替换的元素  new：替换old的元素  max：替换的个数，默认为全部替换 |
| isspace                 | 判断字符串是否仅由空格组成，返回布尔类型（返回值为true 或者false） | booltype=string.isspace()                                  |                                                              |
| istitle                 | 判断字符串是否是一个标题类型（也就是每个字符串是首字母大写），返回布尔类型 | booltype=string.istitle()                                  |                                                              |
| isupper和islower        | isupper判断字符串中的字母是否都是大写  islower判断字符串中的字母是否都是小写 | booltype=string.isupper()     booltype=string.islower()    |                                                              |
| casefold和lower         | 将字符串中的字母全部小写                                     | newstr = string.casefold()       1·newstr = string.lower() |                                                              |



##### 格式化符号

​	【定义】一个固定的字符串中有部分元素是跟据变量的值而改变的字符串

| 符号 | 说明                       |
| ---- | -------------------------- |
| %s   | 格式化字符串，通用类型     |
| %d   | 格式化整型                 |
| %f   | 格式化浮点型               |
| %u   | 格式化无符号整型（正整型） |
| %c   | 格式化字符                 |
| %o   | 格式化无符号八进制数       |
| %x   | 格式化无符号16进制数       |
| %e   | 科学计数法格式化浮点数     |

python中%s是一种通用格式化符号，任何类型都可以用它

%c只支持int和char类型，int范围是7位数，表示ASCII码，char类型只支持一个字符，并且就是该字符本身



##### 格式化函数format

​		【格式】string.format(data,data,data…)

​			使用format的字符串主体用大括号{}来替代格式符

​			例如：

​		`print（"我叫{0}，今年{0}！"，format（"张三"22））`

​		`print("我叫{1},今年{1}！",format("张三"_22)）`

​		`		print("我叫{2},今年{1}！".format("张三"_22)）`

​		输出：

​		我叫张三，今年22！

​		我叫张三，今年22！

​		我叫22，今年张三！

​	

【具体操作】

1.使用位置参数：format会将参数按位置顺序填充到字符串中，参数从0开始，123…一次递增，也可以不输入数字，也会按顺序填充

2.使用关键字参数，利用key=value来实现一一对应

<img src="C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230726113828086.png" alt="image-20230726113828086" style="zoom:67%;" />

 

3.数字格式化

​	<img src="C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230726113910787.png" alt="image-20230726113910787" style="zoom:67%;" />

4.补充说明：输出花括号需要用花括号本身来转义



##### f-string格式化

​	【步骤】1定义一个变量

​			 2字符串前加f符号

​			 3需要格式化的位置使用{变量名 }

​			<img src="C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230726114842347.png" alt="image-20230726114842347" style="zoom:67%;" />



##### 进制转换函数

​		十进制转十六进制：hex(),返回字符串

​		十进制转二进制：bin()

​		十进制转八进制:oct()



#### 集合set

​	【定义】是一个无序不重复元素序列，

​	【作用】常用来对两个列表进行交并差的处理性，与列表list一样，支持所有的数据类型

​	【对比】集合与列表的区别

<img src="C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230726141406126.png" alt="image-20230726141406126" style="zoom: 50%;" />

​	【创建方法】通过set函数、或者有值的{}（如{1,‘hh’}）（不能使用空的大括号如{}，会理解为字典类型）

​	注意，使用{}直接创建集合时，{}里的数据类型需要**不可变型，如字符串、元组、数字**等，而字典dict和列表list不能放在{}中，否则报错



​	a_set = set()	->表示空集合

​	a_set = set([1 , 2 , 3]) 	->参数：传入列表或元组 

​	b_set = {1, 2, 3}	->传入元素

​	 c_set = {}	->错误

​	【作用】

​	可以用于列表list元素的去重复

<img src="C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230726143847478.png" alt="image-20230726143847478" style="zoom:67%;" />

运行结果：

![image-20230726143913568](C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230726143913568.png)

##### 操作

| 函数名       | 功能                                                         | 格式                         | 说明                                        |
| ------------ | ------------------------------------------------------------ | ---------------------------- | ------------------------------------------- |
| add          | 向集合中添加元素                                             | set.add(item)                |                                             |
| update       | 向集合中加入一个新的集合/列表/元组/字符串，若已存在则忽视    | set.update(iterable)         |                                             |
| remove       | 移除集合中的某个元素，若改元素存在则报错                     | set.remove(item)             |                                             |
| clear        | 清空当前集合中的所有元素                                     | set.clear()                  |                                             |
| union        | 多个集合的并集，即包含了所有集合的元素，重复的元素只会出现一  次 | a_set.union(b_set...)        | 参数：b_set...：与当前集合对比的1或多个集合 |
| difference   | 差集                                                         | a_set.(b_set)                | b_set：当前集合需要对比的集合               |
| intersection | 交集                                                         | a_set.intersection(b_set...) | b_set..：与当前集合对比的1或多个集合        |
| isdisjoint   | 判断两个集合是否包含相同的元素，如果没有返回True，否则返回   False | a_set.(b_set)                | b_set:与当前集合用来判断的集合              |
