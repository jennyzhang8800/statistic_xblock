#Script
  包含三个脚本，是xblock调用的脚本；功能是实现学生作业提交的增量统计
  1. statisticNewAdded.py
      实现的功能是：实现学生作业提交的增量统计
      根据“answer”仓库的git log信息，分析出两次统计之间新增加的提交。更新统计结果
      
  2. statistic_new_commit.sh
     实现的功能是：提取出指定时间之后的commit信息，只提取commit的时间和commit message这两项信息。
     
  3. statistic.py
     实现的功能是：对answer仓库进行全面的统计。
  
