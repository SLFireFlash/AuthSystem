import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("env/serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

def GetFireData(UserName):
    doc_ref = db.collection(u'users').document(UserName)
    doc = doc_ref.get()
    if doc.exists:
        return 1
    else:
       return 0
def Lkeygen(pkey):
  return pkey[::-1]    

def addLid():
    username = input("enter user name:")
    productKey = input("enter Product key:")
    Lid = Lkeygen(productKey)
    checkname = GetFireData(username)
    if checkname ==1:
       doc_ref = db.collection(u'users').document(username)
       doc = doc_ref.get()
       doc = doc.to_dict()
       doc['LId']=Lid
       print(doc)
       db.collection("users").document(username).set(doc)
       res = GetFireData(username)
       if res == 1:
            doc_ref = db.collection(u'users').document(username)
            doc = doc_ref.get()
            doc = doc.to_dict()
            print(doc)


addLid()