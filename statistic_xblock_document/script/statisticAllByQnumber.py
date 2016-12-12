__author__ = 'zhangyanni'
import codecs
import json
import os
import time
ISOTIMEFORMAT='%Y-%m-%d'
def statisticAllByQnumber(path):
    fileObj=readFile(path)
    jsonDict=json.load(fileObj)
    result={}
    result["children"]=[]
    qnumberList=[]


    qnumberCount=""
    for item in jsonDict:
        if(item["q_number"] not in qnumberList):
            qnumberList.append(item["q_number"])
            newOne={}
            newOne["q_number"]=item["q_number"]
            newOne["latest_commit"]=item["commit_time"]
            newOne["email_list"]=[]
            temp={}
            temp["email"]=item["email"]
            temp["commit_time"]=item["commit_time"]
            temp["grade"]=item["grade"]
            newOne["email_list"].append(temp)
            newOne["email_count"]=1
            result["children"].append(newOne)

        else:
            for item_q in result["children"]:
                if(item_q["q_number"]==item["q_number"]):
                    temp={}
                    temp["email"]=item["email"]
                    temp["commit_time"]=item["commit_time"]
                    temp["grade"]=item["grade"]
                    item_q["email_list"].append(temp)
                    item_q["email_count"]=len(item_q["email_list"])
                    if(item_q["latest_commit"]<item["commit_time"]):
                        item_q["latest_commit"]=item["commit_time"]
    result["q_number_count"]=len(qnumberList)
    data=json.dumps(result,sort_keys=True,indent=4)
    #print data
    return data

def readFile(path):
    fileObj=codecs.open(path,encoding='utf-8')
    return fileObj

def saveFile(file_path,file_name,data):
    output = codecs.open(file_path+ "/"+file_name,'w',"utf-8")
    output.write(data)
    output.close()
if __name__ == '__main__':
    path=r"/edx/var/edxapp/staticfiles/statistic/statisticByEmail_result.json"
    data=statisticAllByQnumber(path)
    saveFile(r"/edx/var/edxapp/staticfiles/statistic/","statisticByQnumber_result.json",data)
    statistic_time=time.strftime(ISOTIMEFORMAT,time.localtime())
    saveFile(r"/var/www/zyni/log/","statisticTime.log",statistic_time)
