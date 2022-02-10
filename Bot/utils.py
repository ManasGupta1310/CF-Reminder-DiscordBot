import requests
import json
import csv
import pandas as pd
import numpy as np


def store_problems():
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

        if start_time<100:
            print(str(id)+" "+str(name)+" "+str(start_time)+" hours")
            csv_writer.writerow([id,name,start_time,link])
    
    csv_file.close()

def get_problems():
    data=pd.read_csv("CF-contest.csv")
    return data
    

