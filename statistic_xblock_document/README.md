#Script
  包含五个脚本，是xblock调用的脚本；功能是实现学生作业提交的增量统计
  1. statisticNewAdded.py

      实现的功能是：实现学生作业提交的增量统计
      根据“answer”仓库的git log信息，分析出两次统计之间新增加的提交。更新统计结果。该脚本中会调用statistic_new_commit.sh，以及pushToGitHubStatistic.sh
      
  2. statistic_new_commit.sh
  
     实现的功能是：提取出指定时间之后的commit信息，只提取commit的时间和commit message这两项信息。
   
  3. pullFromGitlab.sh
  
     实现的功能是：从gitlab把"answer"仓库pull到服务器的'/var/www/zyni'目录下，供统计数据使用

  4. pushToGitHubStatistic.sh
  
     实现的功能是：把统计的结果"statisticByExercise.json" push到github,供表格显示使用
     
  5. statisticByEmail.py
   
     实现的功能是:对所有己提交的题进行全面统计，记录邮箱，题号，提交时间，批改结果。 
     该脚本每天23:30定时执行，脚本位于/var/www/zyni/script/  脚本运行结果位于：/edx/var/edxapp/staticfiles/statistic/
     脚本在运行时的日志：/var/www/zyni/log/statisticByEmail.log  

  5. statistic.py
  
     实现的功能是：对answer仓库进行全面的统计。此脚本备用于手工统计
  
#genexericse

   是学生练习题完成情况统计的xblock
   
   具体的执行流程是：
      :sparkles: [点击“statistic”按钮]:
      
           +首先调用脚本“pullFromGitlab.sh”,把gitlab上"answer"仓库clone一份到服务器的/var/www/zyni/目录下
           +然后调用脚本“statisticNewAdded.py”以增量的方式统计练习题完成情况。
      
      
#statistic

存放的是该xblock 的渲染脚本等静态文件。把该文件夹放到/edx/var/edxapp/staticfiles/目录下
