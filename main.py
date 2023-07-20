import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import random

def ProId():
    keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    productKey =[]
    outkey = ""
    for num in range(0,16):
        productKey.append(random.choice(keys)) 
    print(productKey)

    keycount =0
    for x in range(1,5):
        for num in range(0,4):
            outkey += productKey[keycount]
            keycount +=1
        outkey += "-"
        
    outkey = outkey[:-1]
    outkey = outkey.upper()
    return outkey


def GetFireData(UserName):
    cred = credentials.Certificate("env/serviceAccountKey.json")
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    doc_ref = db.collection(u'users').document(UserName)
    doc = doc_ref.get()
    if doc.exists:
        doc = doc.to_dict()
        print(doc['Status'])
    else:
        print(u'No such document!')



Username = input("Enter user name:")
GetFireData(Username)