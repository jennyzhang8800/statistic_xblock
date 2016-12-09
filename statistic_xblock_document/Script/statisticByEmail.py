__author__ = 'zhangyanni'

# -*- coding:utf-8 -*-
import codecs
import json
import os
import time
import re
import traceback
ISOTIMEFORMAT="%Y-%m-%dT%X"

def statistic_by_name(path):
    name_list=[]
    answer_list_dir=path

    for parent,dirnames,filenames in os.walk(answer_list_dir):
        for filename in filenames:
            (shortname,extension) = os.path.splitext(filename)
            
            if shortname.isdigit():
                try:
                    file_path=os.path.join(parent,filename)
                    data=readFile(file_path)
                    data_dict=json.loads(data)
                    email=data_dict["student"]["email"]
                    tried=len(data_dict["answer"])
                    commit_time=data_dict["answer"][tried-1]["time"]
                    if(data_dict["answer"][tried-1]["answer"]==data_dict["question"]["answer"]):
                        grade="true"
                    else:
                        grade="false"
                    temp={}
                    temp["email"]=email
                    temp["commit_time"]=commit_time
                    temp["grade"]=grade
                    temp["q_number"]=shortname
                    name_list.append(temp)
                except:
                    f=open("/var/www/zyni/log/statisticByEmail.log",'a')
                    traceback.print_exc(file=f)
                    f.write("filepath:"+file_path+"\n")
                    f.flush()
                    f.close()
                     
    data=json.dumps(name_list,sort_keys=True,indent=4)    
    return data

def readFile(file_path):
    fileObj=codecs.open(file_path, encoding='utf-8')
    data=fileObj.read()
    return data

def saveFile(file_path,file_name,data):
    output = codecs.open(file_path+ "/"+file_name,'w',"utf-8")
    output.write(data)
    output.close()

def saveLog(file_path,file_name,data):
    output = codecs.open(file_path+ "/"+file_name+".log",'a')
    output.write(data)
    output.close()

if __name__ == '__main__':
    path=r"/var/www/zyni/answer"
    data=statistic_by_name(path)
    saveFile(r"/edx/var/edxapp/staticfiles/statistic","statisticByEmail_result.json",data)



