## day5：

### 一、进展

1.从github获取项目，并用docker部署

2.登录dify社区，办进行获取OpenAI API Key应用创建

![image-20230724153151298](C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230724153151298.png)

### 二、问题：

1.对docker不熟悉，跟着dify官方文档做后，不知道达到了什么样的结果。特别是docker compose部署完后，文档上写着“运行我们的 [docker-compose.yml](https://github.com/langgenius/dify/blob/main/docker/docker-compose.yaml) 文件”，不知道这个文件需要如何用docker运行

2.dify官方文档也不怎么能看懂，给出的命令经常不知道要在哪里运行，又用本地源码部署 Dify 社区版去了（没成功，命令直接运行出错



### 三、收获

用了个冷门地区（土耳其）的梯子后bing ai稳定多啦



### 四、遇到的问题：

用git从github上拉取连接，报错：![image-20230724091117479](C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230724091117479.png)

bing ai入口消失——换源解决不了，重启

文件已丢失，且文件路径移动过——重装

安装成功，且项目拉取成功

![image-20230724110337542](C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230724110337542.png)



`docker-compose up` 命令部署 3 个业务服务 `api / worker / web`，以及 4 个基础组件 `weaviate / db / redis / nginx`

![image-20230724100313680](C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230724100313680.png)

突然bing ai又消失了，尝试换源，切换微软账号，清楚记录，关闭扩展插件——没用

问chat gpt3.5：

![image-20230724110113401](C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230724110113401.png)

重启启docker

打开docker，拉拉拉

![image-20230724110436900](C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230724110436900.png)

果然网络错误了

![image-20230724113436418](C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230724113436418.png)

将vpn设置为绕过大陆+重启powershell

![image-20230724114053446](C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230724114053446.png)

![image-20230724114200930](C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230724114200930.png)

部署 PostgresSQL / Redis / Weaviate

![image-20230724114344556](C:\Users\41001\AppData\Roaming\Typora\typora-user-images\image-20230724114344556.png)



