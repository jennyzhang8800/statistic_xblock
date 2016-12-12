#script
  包含五个脚本，是xblock调用的脚本；功能是实现学生作业提交的增量统计 路径为/var/www/zyni/script
  1. statisticNewAdded.py

      实现的功能是：实现学生作业提交的增量统计
      根据“answer”仓库的git log信息，分析出两次统计之间新增加的提交。更新统计结果。该脚本中会调用statistic_new_commit.sh，以及statisticAllByQnumber.py
      
  2. statistic_new_commit.sh
  
     实现的功能是：提取出指定时间之后的commit信息，只提取commit的时间和commit message这两项信息。
   
  3. pullFromGitlab.sh
  
     实现的功能是：从gitlab把"answer"仓库pull到服务器的'/var/www/gitlab/zyni'目录下，供统计数据使用

  4. configStatisticNew.py
  
     实现的功能是：定义日志
     
  5. statisticByEmail.py
   
     实现的功能是:对所有己提交的题进行全面统计，记录邮箱，题号，提交时间，批改结果。 
     该脚本每天23:30定时执行，脚本位于/var/www/zyni/script/  脚本运行结果位于：/edx/var/edxapp/staticfiles/statistic/
     脚本在运行时的日志：/var/www/zyni/log/statisticByEmail.log  

  5. statisticByEmail.py
  
     实现的功能是：对answer仓库进行全面的统计。此脚本备用于手工统计
  
#genexericse

   是学生练习题完成情况统计的xblock
   
   具体的执行流程是：
      :sparkles: [点击“statistic”按钮]:
      
          
           调用脚本“statisticNewAdded.py”以增量的方式统计练习题完成情况。
           首先从gitlab仓库的git log信息中统计出从上一次全面统计（即当天凌晨）之后新增加的commit (通过statistic_new_commit.sh实现)，日志结果保存在/var/www/zyni/log/gitlab_answer_gitlog.log
           然后根据gitlab_answer_gitlog.log进行统计新增加的提交，并更新statisticByEmail.json和statisticAllByQnumber.json
           
   另外每天的00:02会执行三个脚本：pullFromGitlab.sh、statisticByEmail.py、statisticByEmail.py进行一次全面的统计。并记录下统计的时间到/var/www/zyni/log/statisticTime.log.作为增量统计的基准时间。
     
   
#statistic

存放的是该xblock 的渲染脚本等静态文件。把该文件夹放到/edx/var/edxapp/staticfiles/目录下
