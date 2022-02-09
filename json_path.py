import requests
import json
import csv


csv_file=open('CF-conntest','w',encoding='UTF-8')

csv_writer=csv.writer(csv_file)
csv_writer.writerow(["Id","Contest","Start Time remaining"])

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

    if start_time<12:
        print(str(id)+" "+str(name)+" "+str(start_time)+" hours")
        csv_writer.writerow([id,name,start_time])


csv_file.close()