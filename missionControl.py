import random
import requests
import json
from sklearn import tree

features = [[0, 0, 0], [0, 0, 0], [1, 1, 1], [1, 0, 0], [1, 1, 0], [1, 0, 1], [2, 0, 0], [2, 1, 0], [2, 0, 1]]
labels = [0, 0, 1, 0, 0, 1, 0, 0, 1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)

headers = {
'content-type': "application/json"
}
url = "https://hack-stetty.herokuapp.com/createevent"


stayin = True
while stayin:
    betObject = {"launchid": "",
                "launchdata": {
                    "launchgo": 0,
                    "landboost": 0,
                    "deploypay": 0
                }
            }
    random1 = random.randint(1,201)
    dictionary = requests.get('https://launchlibrary.net/1.4/launch?fields=name&limit=1000').json()
    launchnam = dictionary['launches'][random1]['name']
    betObject['launchid'] = launchnam
    namname = json.dumps(betObject)
    something1 = requests.request("POST", url, data=namname, headers=headers)
    print something1
    temp = raw_input("Do something")
    if temp == 'b':
        temp=0
    launchNum = random.randint(1,101)
    if launchNum < 11:
        betObject['launchdata']['launchgo'] = 0
        betObject['launchdata']['landboost'] = 0
        betObject['launchdata']['deploypay'] = 0
        notification = "Launch Has Been Scrubbed"
        print notification
        payload = json.dumps(betObject)
        response = requests.request("POST", url, data=payload, headers=headers)
        print(response.text)
        temp = raw_input("Do something")
        if temp == 'b':
            temp=0
    else:
        if launchNum > 10 and launchNum < 41:
            notification = "Launch Was Delayed"
            betObject['launchdata']['launchgo'] = 1

            sepUpdate = "Separation Confirmed"
            print notification
            payload = json.dumps(betObject)
            response = requests.request("POST", url, data=payload, headers=headers)
            print(response.text)
            temp = raw_input("Do something")
            if temp == 'b':
                temp=0
            boostNum = random.randint(1,101)
            if boostNum < 81:
                betObject['launchdata']['landboost'] = 1
            else:
                betObject['launchdata']['landboost'] = 0
            print notification
            payload = json.dumps(betObject)
            response = requests.request("POST", url, data=payload, headers=headers)
            print(response.text)
            temp = raw_input("Do something")
            if temp == 'b':
                temp=0
            deployNum = random.randint(1,101)
            if deployNum < 85:
                betObject['launchdata']['deploypay'] = 1
            else:
                betObject['launchdata']['deploypay'] = 0
            print notification
            payload = json.dumps(betObject)
            response = requests.request("POST", url, data=payload, headers=headers)
            print(response.text)
            temp = raw_input("Do something")
            if temp == 'b':
                temp=0
        else:
            if launchNum > 40:
                notification = "Launch Took Off On Time"
                betObject['launchdata']['launchgo'] = 2
                # press any key to continue
                sepUpdate = "Separation Confirmed"
                print notification
                payload = json.dumps(betObject)
                response = requests.request("POST", url, data=payload, headers=headers)
                print(response.text)
                temp = raw_input("Do something")
                if temp == 'b':
                    temp=0
                boostNum = random.randint(1,101)
                if boostNum < 81:
                    betObject['launchdata']['landboost'] = 1
                else:
                    betObject['launchdata']['landboost'] = 0
                print notification
                payload = json.dumps(betObject)
                response = requests.request("POST", url, data=payload, headers=headers)
                print(response.text)
                temp = raw_input("Do something")
                if temp == 'b':
                    temp=0
                deployNum = random.randint(1,101)
                if deployNum < 85:
                    betObject['launchdata']['deploypay'] = 1
                else:
                    betObject['launchdata']['deploypay'] = 0
                print notification
                payload = json.dumps(betObject)
                response = requests.request("POST", url, data=payload, headers=headers)
                print(response.text)
                temp = raw_input("Do something")
                if temp == 'b':
                    temp=0
    profit = clf.predict([[betObject['launchdata']['launchgo'], betObject['launchdata']['landboost'], betObject['launchdata']['deploypay']]])
    if profit[0] == 1:
        print "Mission was profitable!"
    else:
        print "Mission was costly!"
    temp = raw_input("Would you like to launch another rocky boi? y/n")
    if temp == 'n':
        stayin = False


print notification
