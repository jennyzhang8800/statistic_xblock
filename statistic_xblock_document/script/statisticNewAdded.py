__author__ = 'zhangyanni'

# -*- coding:utf-8 -*-
import codecs
import json
import os
import time
from configStatisticNew import Config
ISOTIMEFORMAT='%Y-%m-%d'
def statisticNewAdded(path_log,path):
    fileObj=readFile(path_log)
    commitNewAdded=[]
    for line in fileObj:
        commitMe=line.split(',')[-1]
        if(commitMe.split(' ')[0]=='create'):
            cur_path=commitMe.split(' ')[-1].strip()
            q_number=cur_path.split('/')[-2]
            
            filePath=os.path.join('/var/www/zyni/gitlab/answer/',cur_path)
            data=readFile(filePath).read()
            data_dict=json.loads(data)
            email=data_dict["student"]["email"]
            commit_time=data_dict["answer"][0]["time"]
            if data_dict["answer"][0]["answer"]==data_dict["question"]["answer"]:
                grade="true"
            else:
                grade="false"
            obj={}
            obj["q_number"]=str(q_number)
            obj["email"]=email
            obj["commit_time"]=commit_time
            obj["grade"]=grade

            commitNewAdded.append(obj)
#    print json.dumps(commitNewAdded)
    if commitNewAdded:
        data_old=readFile(path).read()
        data_old_dict=json.loads(data_old)
        for item in commitNewAdded:
            q_number=item["q_number"]
            email=item["email"]
            num=0
            for obj in data_old_dict:
                if(int(obj["q_number"]) == int(q_number)) and (email == obj["email"]):
                    break
                else:
                    num=num+1
            if num==0:
                data_old_dict.append(item)
        return data_old_dict
    else:
        return 0
   
            
  
   

    
def readFile(file_path):
    fileObj=codecs.open(file_path, encoding='utf-8')
    return fileObj
    

def saveFile(file_path,file_name,data):
    output = codecs.open(file_path+ "/"+file_name+".json",'w',"utf-8")
    output.write(data)
    output.close()
def saveLog(file_path,file_name,data):
    output = codecs.open(file_path+ "/"+file_name+".log",'a',"utf-8")
    output.write(data)
    output.close()

if __name__ == '__main__':
    conf=Config()
    logger=conf.getLog()
    logger.info("Statistic Xblock invoke")
    path=r"/edx/var/edxapp/staticfiles/statistic/statisticByEmail_result.json"
    path_log=r"/var/www/zyni/log/gitlab_answer_gitlog.log"
    data=readFile('/var/www/zyni/log/statisticTime.log')
    statisticTime=[]
    for line in data:
        statisticTime.append(line.strip())
    last_statistic_time=statisticTime[-1]
    logger.info("lastest statistic time is:"+last_statistic_time)
    os.system('/var/www/zyni/script/statistic_new_commit.sh '+last_statistic_time)
    log=readFile(path_log).read()
    if len(log) != 0:
        logger.info("there are new commit")
        logger.info("statisticNewAdded function invoke")
        data=statisticNewAdded(path_log,path)
        if data is not 0:
            data=json.dumps(data)
            saveFile('/edx/var/edxapp/staticfiles/statistic/','statisticByEmail_result',data)
            logger.info("Save file statisticByEmail_result.json")
           
            os.system('python /var/www/zyni/script/statisticAllByQnumber.py')   
            logger.info("statisticAllByQnumber.py invoke")
    else:
        logger.info("There is no new commit")





