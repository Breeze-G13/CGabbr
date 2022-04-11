# CGabbr

作者：凯捷中国JPT Elite Program 0411/2022期学员 高文韬[breeze822@163.com]  


适用范围：本文为凯捷缩写的自测程序abbrTest.py[v1.0]的说明文档  


程序用途：针对凯捷中国JTP实习营所发【凯捷缩写.pdf】的自测练习程序  
使用环境：Windows/MacOS > 腾讯云服务器 > Python3  


程序访问方法：
1. 若本机为Windows系统，在桌面按Win徽标键+R，运行cmd终端；若本机为MacOS系统，运行Terminal  
2. 连接作者的个人腾讯云服务器：在cmd(Window)或Terminal(MacOS)命令行输入  
   &ensp; ssh root@43.138.23.104  
   如果是第一次访问服务器，可能要求需要输入yes来确定连接服务器  
   提示输入密码[root@43.138.23.104's password]时输入  
   &ensp; Beijing822 然后回车（所输入字符不会显示在命令行）  
   若显示如下提示则为登陆服务器成功  
   &ensp; Last login: XXX XXX  
   &ensp; (base) [root@VM-16-14-centos ~]#  
3. 切换至程序所在路径 输入  
   &ensp; cd /usr/CG/abbr  
   若显示如下提示则为切换路径成功  
   &ensp; (base) [root@VM-16-14-centos abbr]#  
4. 运行程序 输入  
   &ensp; python abbrTest.py  
   即可开始自测

程序使用说明：
1. [XXXX]为标签提示：有[REGION]地区缩写、[TEAM]团队所写、[INDUSTRY]行业缩写、[POSITION]职位缩写、[OTHERS]其他缩写
2. 测试为60个缩写的随机乱序，在目前版本设置中若答对一次则不再出现，若答错则该题回回到待测区并后续随机再次出现
3. 回答不区分大小写，即[REGION] BSV = 答Business Services或business services或Business services或BUSINESS SERVICES均判定为正确
4. 目前版本不承认微小拼写错误或英式拼写为正确回答
5. 在任何一题中输入Done或Stop（不区分大小写）即可终止自测并显示一次答对的正确率即缩写掌握程度

报错反馈：  
微信：breeze_g13  
邮件：breeze822@163.com / breeeeze.g@gmail.com

代码开源：
https://github.com/Breeze-G13/CGabbr
