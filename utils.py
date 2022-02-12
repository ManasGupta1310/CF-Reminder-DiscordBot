import requests
import json
import csv
import pandas as pd


def store_contest():
    csv_file=open('CF-contest.csv','w',encoding='UTF-8')

    csv_writer=csv.writer(csv_file)
    csv_writer.writerow(["Id","Contest","Time remaining","Link"])
    API="https://codeforces.com/api/contest.list"

    res=requests.get(API)
    res=json.loads(res.text)

    print('JSON Loaded!!')

    contests=res["result"]
    for contest in contests:
        if contest["phase"]=="FINISHED": break
        
        id=contest["id"]
        name=contest["name"]
        start_time=(((contest["relativeTimeSeconds"]*(-1))//60)//60)
        link="https://codeforces.com/contest/"+str(id)

        if start_time<24:
            print(str(id)+" "+str(name)+" "+str(start_time)+" hours")
            csv_writer.writerow([id,name,start_time,link])
    
    csv_file.close()

def get_contest():
    data=pd.read_csv("CF-contest.csv")
    return data
    
def get_problems(x,y):
    RATING_UP=x
    RATING_DOWN=y
    csv_file=open('CF-problem.csv','w',encoding='UTF-8')
    csv_writer=csv.writer(csv_file)
    csv_writer.writerow(["Serial No.","Id","Index","Name","Rating","Link"])
    API="https://codeforces.com/api/problemset.problems"

    res=requests.get(API)
    res=json.loads(res.text)

    print('JSON Loaded!!')

    problems=res["result"]["problems"]
    serial_no=1
    for problem in problems:
        if "rating" in problem.keys():
            if problem["rating"]<=RATING_UP and  problem["rating"]>=RATING_DOWN: 
                id=problem["contestId"]
                name=problem["name"]
                idx=problem["index"]
                rating=problem["rating"]
                link="https://codeforces.com/problemset/problem/"+str(id)+"/"+str(idx)


                print(str(id)+" "+str(name)+" "+str(idx))
                csv_writer.writerow([serial_no,id,idx,name, rating,link])
                serial_no+=1
        

    csv_file.close()

def get_contest():
    data=pd.read_csv("CF-problem.csv")
    return data

