__author__ = 'zhangyanni'

# -*- coding:utf-8 -*-
import codecs
import json
import os
import time

ISOTIMEFORMAT='%Y-%m-%dT%X'
def statisticNewAdded(path_log,path):
    fileObj=readFile(path_log)
    commitNewAdded=[]
    for line in fileObj:
        commitMe=line.split(',')[-1]
        if(commitMe.split(' ')[0]=='create'):
            cur_path=commitMe.split(' ')[-1].strip()
            q_number=cur_path.split('/')[-2]
            
            filePath=os.path.join('/var/www/zyni/answer/',cur_path)
            data=readFile(filePath).read()
            data_dict=eval(data)
            email=data_dict["student"]["email"]
            obj={}
            obj["q_number"]=q_number
            obj["email"]=email
            commitNewAdded.append(obj)
    if commitNewAdded:
        data_old=readFile(path).read()
        data_old_dict=eval(data_old)
        for item in commitNewAdded:
            q_number=item["q_number"]
            email=item["email"]
            flag=0
            for obj in data_old_dict["children"]:
                if(int(obj["q_number"])==int(q_number)):
                    flag=1    
                    obj["user_name_list"].append(email)
                    obj["submitted_count"]+=1
            if flag==0:
                obj={}
                obj["q_number"]=q_number
                obj["submitted_count"]=1
                obj["user_name_list"]=[]
                obj["user_name_list"].append(email)
                data_old_dict["children"].append(obj)
        data_old_dict["total_submitted_count"]=len(data_old_dict["children"])
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
    path=r"/var/www/zyni/statistic_xblock/statisticByExercise.json"
    path_log=r"/var/www/zyni/gitlab_answer_gitlog.log"
    statistic_time=time.strftime(ISOTIMEFORMAT,time.localtime())
    data=readFile('/var/www/zyni/statisticLog.log')
    statisticTime=[]
    for line in data:
        statisticTime.append(line.strip())
    last_statistic_time=statisticTime[-1]
    os.system('/var/www/zyni/script/statistic_new_commit.sh '+last_statistic_time)
    
    data=statisticNewAdded(path_log,path)
    if data is not 0:
        data=json.dumps(data)
        saveFile('/var/www/zyni/statistic_xblock/','statisticByExercise',data)
        os.system('/var/www/zyni/script/pushToGitHubStatistic.sh')
        data=statistic_time+'\n'
        saveLog('/var/www/zyni/','statisticLog',data)
    






