__author__ = 'zhangyanni'

# -*- coding:utf-8 -*-
import codecs
import json
import os
import time

ISOTIMEFORMAT="%Y-%m-%dT%X"

def get_q_list(path):
    q_list=[]
    answer_list_dir=path

    for parent,dirnames,filenames in os.walk(answer_list_dir):
        for filename in filenames:
            (shortname,extension) = os.path.splitext(filename)
            if shortname.isdigit():
                if int(shortname) not in q_list:
                   q_list.append(int(shortname))
    return q_list

def commit_count(number,path):
    count=0
    answer_list_dir=path
    user_name=[]

    for parent,dirnames,filenames in os.walk(answer_list_dir):
        for filename in filenames:
            (shortname,extension) = os.path.splitext(filename)
            if shortname.isdigit():
                if int(shortname)==int(number):
                   count+=1
                   user_name.append(parent.split('/')[-2])
                  
    return count,user_name
    
def statisticByExercise(path):
    json={}
    json['children']=[]

    q_list=get_q_list(path)
    for item in q_list:
        aExercise={}
        count,user_name_list=commit_count(item,path)
        aExercise['q_number']=item
        aExercise['submitted_count']=count
        aExercise['user_name_list']=user_name_list
        json['children'].append(aExercise)
    json['total_submitted_count']=len(q_list )
    return json

    
def readFile(file_path):
    fileObj=codecs.open(file_path, encoding='utf-8')
    data=fileObj.read()
    return data

def saveFile(file_path,file_name,data):
    output = codecs.open(file_path+ "/"+file_name+".json",'w',"utf-8")
    output.write(data)
    output.close()

def saveLog(file_path,file_name,data):
    output = codecs.open(file_path+ "/"+file_name+".log",'a')
    output.write(data)
    output.close()

if __name__ == '__main__':
    path=r"/var/www/zyni/answer"
    data=statisticByExercise(path)
    data=json.dumps(data)
    saveFile('/var/www/zyni/statistic_xblock/','statisticByExercise',data)
    statistic_time=time.strftime(ISOTIMEFORMAT,time.localtime())
    data=statistic_time+'\n'
    saveLog('/var/www/zyni/','statisticLog',data)
    os.system('/var/www/zyni/script/pushToGitHubStatistic.sh')




