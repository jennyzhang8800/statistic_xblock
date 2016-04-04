#Script
  包含三个脚本，是xblock调用的脚本；功能是实现学生作业提交的增量统计
  1. statisticNewAdded.py

      实现的功能是：实现学生作业提交的增量统计
      根据“answer”仓库的git log信息，分析出两次统计之间新增加的提交。更新统计结果
      
  2. statistic_new_commit.sh
  
     实现的功能是：提取出指定时间之后的commit信息，只提取commit的时间和commit message这两项信息。
     
  3. statistic.py
  
     实现的功能是：对answer仓库进行全面的统计。
  
#genexericse

   是学生练习题完成情况统计的xblock
   
   具体的执行流程是：
      :sparkles: [点击“statistic”按钮]:首先调用脚本“pullFromGitlab.sh”,把gitlab上"answer"仓库clone一份到服务器的/var/www/zyni/目录下
      然后调用脚本“statisticNewAdded.py”以增量的方式统计练习题完成情况。
      
      
