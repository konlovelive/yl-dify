###  day3

进度：

1.继续解决蓝屏问题

2.蓝屏解决后，解决docker问题，对照官网检查是否启用虚拟机管理程序、在 BIOS 中启用虚拟化，是否适用于 Linux 的 Windows 子系统、是否[二级地址转换 （SLAT）](https://en.wikipedia.org/wiki/Second_Level_Address_Translation) 的 64 位处理器，WSL 版本 ，Windows 家庭版升级为企业版（变成了未激活的企业版，当时没发现），有关虚拟化因为看不懂文档耗时较久



[(30条消息) Docker Desktop 错误：必须在BIOS中启用 硬件辅助虚拟化和数据执行保护_雁均的博客-CSDN博客](https://blog.csdn.net/yanlin01/article/details/131863703?spm=1001.2014.3001.5502)



### day4

进度：

1.解决docker问题：将windows家庭版升级为企业版，docker再次重装后，再关闭hery-v重启电脑后，用power shell运行 bcdedit /set hypervisorlaunchtype auto后成功。

2.连接git和github

3.docker学习（没咋看懂

4.下载学习markdown，安装typora
