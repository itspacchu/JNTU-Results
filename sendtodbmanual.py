from pymongo import MongoClient
from jnturesultscrap import JNTUResult
import time
import tqdm
examCode = "1502"
mongo_url = "REDCATED"

mongo_client = MongoClient(mongo_url)
db = mongo_client['jnturesults']['jnturesult']

def sendrolltodb(rollNo):
    jr = JNTUResult(rollNo, examCode)
    jrmethod = jr.recursiveGet()
    result = jrmethod['result']

    try:
        SGPA = jrmethod['sgpa']
    except Exception as e:
        SGPA = "Coudn't Calculate due to > " + str(e)

    resultWithSGPA = {
                'unique': str(rollNo+examCode),
                'rollno': str(rollNo),
                'examcode': str(examCode),
                'result': result,
                'sgpa': SGPA,
                'usr': jrmethod['user']
            }
    if(type(resultWithSGPA['sgpa']) == float or type(resultWithSGPA['sgpa']) == int):
                db.insert_one(resultWithSGPA)

base_id = "18"
clg_id = "32"
some = "1A0"
branches = [4,5]
expanders = "0123456789ABCDEF"
final = range(1,10)

rolls = []
for branch in branches:
    for tenth in expanders:
        for units in final:
            rollNN = f"{base_id}{clg_id}{some}{branch}{tenth}{units}"
            rolls.append(rollNN)

for roll in tqdm.tqdm(rolls):
    try:
        sendrolltodb(roll)
        time.sleep(0.1)
    except Exception as e:
        print("Not added due to " + str(e) + " "+ str(roll) + " " + str(len(roll)))
