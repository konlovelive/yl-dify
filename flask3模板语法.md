## 模板

### 模板标签

	在Flask中，模板标签是由Jinja2模板引擎提供的。Jinja2是一种流行的模板引擎，它被广泛用于Flask框架中用于生成动态HTML页面。

Jinja2模板标签是一种特殊的语法，用于在HTML模板中插入动态内容或执行逻辑控制。它们被包含在`{% %}`中，如下所示：

1. 控制结构标签：
   - `{% if condition %}`: 用于执行条件判断，根据条件是否满足来显示不同的内容。
   - `{% for item in items %}`: 用于进行循环遍历，将变量逐一取出并进行操作。
   - `{% while condition %}`: 用于执行循环，直到指定条件不再满足为止。
   - `{% else %}`: 在`if`和`for`等标签的结束处添加`else`分支，用于在条件不满足或循环结束后执行其他操作。

2. 变量标签：
   - `{{ variable }}`: 用于在HTML模板中插入变量的值，将动态数据显示在页面上。

3. 注释标签：
   - `{# This is a comment #}`: 用于添加注释，不会在页面上显示，仅作为开发者的备注。

4. 宏标签：
   - `{% macro name(param1, param2) %}`: 用于定义模板中的宏（类似于函数），可在模板中多处调用。

5. 继承标签：
   - `{% extends "base.html" %}`: 用于指定当前模板继承自另一个模板，实现模板的重用和层次化布局。

6. 引入标签：
   - `{% include "partial.html" %}`: 用于将另一个模板（partial.html）引入当前模板，实现模板的复用。

这些标签使得在Flask中的HTML模板中可以插入动态的数据和执行逻辑控制，从而使得生成的页面内容更加灵活和动态。



具体：

#### 变量与赋值

​	【语法】

​		形式1：`{% tag %}`

​		形式2：`{% tag %} 内容  {% endtag %}`

设置变量，赋值操作

​	先设置，后使用，可以通过import导入

​	`{% set key, value = (1, 2) %}`

使用with代码块，实现块级作用域

`{% with %}`

​		`	{% set value = 42 %}`	 

​		`	{{ value}}#只在代码块中有效`	

`{% endwith %}`

html中，下面的变量temp只在这段with代码块内有效

​	<img src="C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230729101341352.png" alt="image-20230729101341352" style="zoom:50%;" />



#### 控制结构

​		标签中可包含表达式，如：if条件控制

​		【条件表达式】

```HTML
{% if condition_a %}
	满足了A条件a
{% elif condition_b %}
	满足了B条件
{% else %}
	都不满足
{% endif %}
```

​		【if标签中的is判断】

​				`{% if value is defined %}  内容  {% endif %}`

​		【内置的判断条件】	

​		defined/undefined——变量是否已经定义

​		none——变量是否为Nonenumber/string一—数字/字符串判断 

​		even/odd——奇偶判断

​		upper/lower——大小写判断

![image-20230728165639525](C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230728165639525.png)

举例：

![image-20230728165812148](C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230728165812148.png)

![image-20230728165731972](C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230728165731972.png)

![image-20230728182800827](C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230728182800827.png)

![image-20230728183539962](C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230728183539962.png)



.py文件

<img src="C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230728191232995.png" alt="image-20230728191232995" style="zoom:50%;" />

html文件：

<img src="C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230728191031651.png" alt="image-20230728191031651" style="zoom:50%;" />

<img src="C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230728191104181.png" alt="image-20230728191104181" style="zoom:50%;" />

效果：（通过loop.cycle()函数实现）

<img src="C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230728191012998.png" alt="image-20230728191012998" style="zoom:50%;" />

`loop.cycle()`函数是Jinja2中的一个循环函数，它的作用是在给定的一组参数中进行循环，并在每次调用时返回下一个参数。在这里，`loop.cycle('odd', 'even')`表示交替返回`'odd'`和`'even'`两个参数。

```
# 为模板引擎添加扩展，支持break/continue语法
app.jinja_env.add_extension('jinja2.ext.loopcontrols')
```



#### 注释

​	html注释：`<!-- 内容-->`（在网页检查源码时可见）

​	模板注释：`{# 注释内容 #}（`在网页检查源码时不可见）





#### 去除HTML中多于空白

在块的开始或结束放置一个减号（-）

`{% for item in seq -%}{{ item }}{%- endfor %}`

​	<img src="C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230729100409513.png" alt="image-20230729100409513" style="zoom:67%;" />

对比效果：

​	<img src="C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230729100512022.png" alt="image-20230729100512022" style="zoom:50%;" /><img src="C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230729100531508.png" alt="image-20230729100531508" style="zoom:50%;" />



#### 转义字符的显示

方式一：视为字符串 ，如`{{'{{}} {%%}'}`

方式二：使用raw标签

```HTML
{% raw %}
	{% for key, vàlue in data.items %}
		{{ key }}:{{ value }}
	{% endfor %}
{% endraw %}

```

### 过滤器

	在Flask中，过滤器是由Jinja2模板引擎提供的一种功能，用于对模板中的变量进行处理或格式化，类似于编程语言中的函数。过滤器允许您在模板中对变量进行各种转换、操作和处理，从而在页面中呈现更加灵活和符合需求的内容。



#### 定义方式

Jinja2的过滤器使用`|`管道符号来应用于模板中的变量，语法如下：

```html
{{ variable | filter_name(arguments) }}
```

其中，`variable`是模板中的变量，`filter_name`是过滤器的名称，`arguments`是过滤器可能需要的参数，`(arguments)` 可有可无。

也可以链式调用，如：

​	`{{name|striptags|title}}`

​	(name值用过滤器striptags处理后会得到一个新的值，这个新值会被title再次处理又得到一个新的值)



下面是一个使用过滤器的示例：

```html
<!DOCTYPE html>
<html>
<head>
    <title>Flask Filter Example</title>
</head>
<body>
    <h1>{{ username | capitalize }}</h1>
    <p>{{ description | truncate(30) }}</p>
    <p>Length of the list: {{ my_list | length }}</p>
    <p>{{ non_existent_variable | default('Not found') }}</p>
</body>
</html>
```

在这个例子中，`{{ username | capitalize }}`会将变量`username`的值首字母大写。`{{ description | truncate(30) }}`会截断`description`变量的值到30个字符，并加上省略符号。`{{ my_list | length }}`会获取`my_list`列表的长度。`{{ non_existent_variable | default('Not found') }}`用于处理`non_existent_variable`变量不存在的情况，并显示默认值"Not found"。

通过使用过滤器，您可以方便地对模板中的变量进行转换和处理，以满足不同的显示需求。



#### 使用方法

​	1.用管道符号（|）

```HTML
{{ variable | filter_name(arguments) }}
```

​	2.使用标签

```HTML
{% filter 过滤器名 %}
	需要过滤器处理的参数
{% endfilter %}
```



#### 内置过滤器

​	Flask中的过滤器有很多内置的，同时也可以定义自己的过滤器。以下是一些常用的内置过滤器：

1. `safe`: 将字符串标记为安全，不进行HTML转义。
2. `capitalize`: 将字符串的首字母大写，其他字符小写。
3. `upper`: 将字符串全部转换为大写。
4. `lower`: 将字符串全部转换为小写。
5. `title`: 将字符串中每个单词的首字母大写。
6. `truncate`: 截断字符串到指定长度，并可以指定省略符。
7. `length`: 获取列表或字符串的长度。
8. `default`: 如果变量为false或空，则返回默认值。
9. `abs`：求绝对值，如{{value|abs}}
10. `default()`：设置默认值显示`{{value|default('默认值')}}`、 `{{value|d('默认值')}}`，注意这个默认值是指未定义的，如何已经被定义了，如var=None，那么将不会被赋默认值，此时想要被赋默认值，则可再添加一个参数True，格式如：`{{value|d('默认值'),True}}`
11. escape或e：html转义`{{value|escape}}`或`{{value|e}}`



#### 自定义过滤器

​	方式1：使用装饰器注册（推荐）

```python
@app.template_filter('reverse')
def reverse filter(s): 
    	return s[::-1]	
```

​	方式2：调用函数注册

```python
# 定义自定义过滤器函数
def reverse_string(s):
    return s[::-1]

# 注册过滤器函数
app.jinja_env.filters['reverse'] = reverse_string

# 路由和视图函数等...
```

reverse是指过滤器名，s是指待处理的值名

<img src="C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230729111828568.png" alt="image-20230729111828568" style="zoom:50%;" />

<img src="C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230729111919067.png" alt="image-20230729111919067" style="zoom:50%;" />

效果：

<img src="C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230729111849210.png" alt="image-20230729111849210" style="zoom:50%;" />



### 全局函数

​	可以通过`app.jinja_env.globals`字典来定义模板的全局函数

以下是一些常用的自定义模板全局函数示例：

1. `range`函数：
   格式：`range([start,] stop[, step])`
   作用：用于生成一个数字序列，类似于Python中的`range()`函数。`start`参数表示序列的起始值（可选，默认为0），`stop`参数表示序列的结束值（必选），`step`参数表示序列的步长（可选，默认为1）。

   示例：
   ```html
   {% for i in range(1, 5) %}
       {{ i }}
   {% endfor %}
   ```
   输出：`1234`

2. `dict`函数：
   格式：`dict(**kwargs)`
   作用：用于创建一个字典，类似于Python中的字典定义。`**kwargs`表示关键字参数，用于指定字典的键值对。

   示例：
   ```html
   {% set user = dict(username='John', age=30) %}
   {{ user.username }}, {{ user.age }}
   ```
   输出：`John, 30`

3. `cycle`函数：
   格式：`cycle(*args)`
   作用：用于在多个值之间进行循环切换，类似于Python中的`itertools.cycle()`。它通常与`for`循环和CSS类名交替使用，实现表格或列表的斑马线效果。

   示例：
   ```html
   {% for i in range(1, 5) %}
       <p class="{{ cycle('odd', 'even') }}">{{ i }}</p>
   {% endfor %}
   ```
   输出：
   ```html
   <p class="odd">1</p>
   <p class="even">2</p>
   <p class="odd">3</p>
   <p class="even">4</p>
   ```

   <img src="C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230729121218428.png" alt="image-20230729121218428" style="zoom:50%;" />
   
   <img src="C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230729121239211.png" alt="image-20230729121239211" style="zoom:50%;" />
   
   效果：
   
   <img src="C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230729121153319.png" alt="image-20230729121153319" style="zoom:50%;" />
   
4. `joiner`函数：
   格式：`joiner(separator)`
   作用：用于在模板中合并多个元素，并指定一个分隔符，类似于Python中的`str.join()`。`separator`表示要用于分隔元素的字符串。

   示例：
   ```html
   {% set fruits = ['apple', 'banana', 'orange'] %}
   {{ joiner(', ') (fruits) }}
   ```
   输出：`apple, banana, orange`

5. `url_for`函数：
   格式：`url_for(endpoint, **values)`
   作用：用于生成URL，类似于Flask中的`url_for`函数。`endpoint`是视图函数的名称（字符串），`values`是一系列关键字参数，用于构建URL中的变量部分。

   示例：
   ```html
   <a href="{{ url_for('index') }}">Home</a>
   ```
   上面的代码会生成一个指向`index`视图函数的URL链接。

​		![image-20230729122213115](C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230729122213115.png)

![image-20230729122252512](C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230729122252512.png)

效果:设置了网页标题和背景的颜色

<img src="C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230729122313677.png" alt="image-20230729122313677" style="zoom:50%;" />



### 宏

​	是把常用功能抽取出来，实现可重用简单

​	理解：宏  约等于  函数

​	宏可以写在单独的html文件中

​	【定义】

宏的定义格式如下：

```html
{% macro macro_name(arg1, arg2, ...) %}
    {# 宏的内容 #}
	...
{% endmacro %}
```

- `macro_name`: 宏的名称，用于在模板中调用宏。
- `arg1, arg2, ...`: 宏的参数列表，您可以在宏的内容中使用这些参数。
- `matro`是关键字



示例1：

   ```html
   {% matro input(name, value=", type='text', size=20) -%}
   	<input type="{{ type }}"name="{{ name}}"value="{{ valuele }}" size="{{ size }}">
   	{%- endmacro %}
   ```

`input`是函数名称，也可以是别的函数，（这里的input是html中的一个输入框函数），`name`是必选参数

示例2：

```
{% macro hello(name) %}
    <p>Hello, {{ name }}!</p>
{% endmacro %}
```

在上面的示例中，我们定义了一个名为`hello`的宏，它接受一个参数`name`。在宏的内容中，我们使用`{{ name }}`来插入参数的值，生成一段包含问候语的HTML代码。



​	【使用】

```python
<p> {{input('username')}}</p>
<p> {{input('password',type='password')}}</p>
```



Flask宏中，`class`是HTML标签的一个特殊属性，用于指定元素的CSS类名。CSS类名是用于样式化HTML元素的一种标识，可以通过CSS样式表定义一组样式，并将其应用到拥有相同类名的多个元素上。

在宏中的代码块中，`class="input-control class2"`是一个HTML元素的`class`属性的值。在这里，元素的类名被设置为两个值，即`input-control`和`class2`，中间用空格隔开。这意味着该元素将应用名为`input-control`和`class2`的CSS类的样式。



【文件中的宏】

​	1.【定义】将定义的宏保存为forms.html

​	2.【导入】

   ```python
   {% import 'forms.html' as forms %}
   {% form 'forms.html' import input %}# 另外一种导入法
   ```

​	3.【使用】

   ```python
   <p> {forms.{input('username')}}</p>
   ```



举例：

app.py文件

```python
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/macro')
def macro():
    """ 模板中宏的使用 """
    return render_template('macro.html')

```



macro.html文件

 ```html
 <!DOCTYPE html>
 <html lang="en">
 <head>
     <meta charset="UTF-8">
     <title>模板中宏的使用</title>
     <style type="text/css">/*type="text/css" 表示该 <style> 标签内部的内容是 CSS 样式代码。*/
         {
         /*.input-control 表示要选择具有 class="input-control" 属性的所有 HTML 元素。
         它定义了一个 CSS 样式规则，将所有具有 class="input-control" 属性的 HTML 元素的边框样式设置为 1 像素宽度的红色实线边框。*/
         .input-control <!--css格式类名为"input-control" -->
             border: 1px solid #ff0000;
         }
     </style>
 </head>
 <body>
 <form action="">
     {% macro input(name, type='text', value='')%}
         <div>
             <input class="input-control class2" type="{{ type }}" name="{{ name }}" value="{{ value }}">
         </div>
     {% endmacro %}
     {#  用户名 username  #}
     {{ input('username', value='admin') }}
     {#  密码 password  #}
     {{ input('password', type='password') }}
     {#  年龄 age  #}
     {{ input('age', type='number') }}
     <!--
     <div>
         <input class="input-control class2" type="text" name="username" value="">
     </div>
     <div>
         <input class="input-control class2" type="password" name="password">
     </div>
     <div>
         <input class="input-control class2" type="mumber" name="age">
     </div>
     -->
     {% from 'forms.html' import input as form_input %}
     <h3>通过import导入宏</h3>
     <p>
         {{ form_input('code') }}
     </p>
 </form>
 </body>
 </html>
 ```



css格式类名为"input-control"的显示：

<img src="C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230729153206104.png" alt="image-20230729153206104" style="zoom:33%;" />

### 模板的继承

步骤：

1. 将可变的部分圈出来（base.html)

      ```html
      {% block content %}
      	<！--内容区域-->
      {% endblock %}
      ```

2. 继承父模板

      ```html
      {% extends "base.html" %}
      ```

3. 填充新的内容(index.html)

  ```html
  {% extends "base.html" %}
  {% block content %}
  <！--新的内容-->
  {% endblock %}
  ```

  4.复用父模板的内容（可选）
   ```html
{% extends "base.html" %}
{% block header %}
	{{ super() }}
	<！--新的菜单内容-->
{% endblock %}

   ```



#### 包含

​	步骤一：将可变的部分拆出来(sidebar.html)

```html
<div>
    这是右侧公共的部分
</div>
```

​	步骤二：将拆出来的部分包进来（index.html)

```html
{% extends "base.html" %}
{% block content %}
	<！-页面主要内容区域-->
    {进公用的区域#}
    {% include "sidebar.html" %}<！-包裹部分-->
{% endblock %}
```



#### 复用

当前页面的代码复用

```html
<title>{% block 块名%}\{% endblock %}<title>
<h1>{{ self.块名() }}</h1>#实现复用
{% block content %}
    内容...
{% endblock %}
```



#### 继承与包含区别

继承与包含的区别相关模板标签

```html
{% block sidebar%}{%endblock%}———命名代码
{%extends“base.html”%}——继承模板
{% include 'header.html' %}-——包含代码块
```



### 消息闪现

​	第一步：在视图中产生一个消息(提示/警告/错误)

```html
flash(msg_content, msg_type) 
参数msg_content:消息内容 
参数msg_type:消息类型com
```



​	第二步：在模板中展示消息

`get_flashed_messages(category_filter=["error"])` 

参数category_filter：对产生的消息按类别查询

```html
    {% for category, message in get_flashed_messages(with_categories=true) %}
    <p>{{ message }}</p>
    {% endfor %} 
```
