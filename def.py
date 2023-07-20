import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import random
import time
import json 

cred = credentials.Certificate("env/serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

def ProId():
    keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    productKey =[]
    outkey = ""
    for num in range(0,16):
        productKey.append(random.choice(keys)) 
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
    doc_ref = db.collection(u'users').document(UserName)
    doc = doc_ref.get()
    if doc.exists:
        return 1
    else:
       return 0

def LogIn():
    print("============================")
    print("=====Welcome To PyBoost=====")
    print("============================")

    while True:
        print("\n\t 1 To LogIn\n\t 2 To SignUp\n\t 0 To Exit")
        logAns = input("\n\t:")
        if logAns == '1':
            print("login")
        elif logAns == '2':
            SignUp()
        elif logAns == '0':
            print("====================================")
            print("=====Find Me YT/Tk @SLFIREFLASH=====")
            print("====================================")
            time.sleep(1)
            exit()
        else:
            print("wrong input Try Again")

def SignUp():
    print("===welcome to signUp===")
    print('=======================')
    while True:
        username = input("\tType New UserName:")
        checkname = GetFireData(username)
        if checkname == 1:
            print("user name already exist try another one")
        else:
            print('\tHi ' + username)
            with open("env/config.json","r")as ReadF:
                configData = json.load(ReadF)
            if len(configData['Product']['product_key']) == 0:
                pid = ProId()
                
                configData['Product']['product_key'] = pid
                with open("env/config.json","w")as WriteF:
                    json.dump(configData,WriteF,indent=4)
                
            else:
                print("You Already SignUp from this device")
                print("=====================================================")
                print("your product key:"+configData['Product']['product_key'])
                print("=====================================================")
                print("IF you forget username or password goto support")
                print("discord Server: https://discord.gg/VhZPurRWf8")
                print("================================================")
                print("press enter to exit")
                input()
                exit()



            password = input("\ttype new Password:")
            data ={"userId":username,"Status":False,'Password':password,"PId":pid,"LId":""}
            db.collection("users").document(username).set(data)
            print(username +" your Account created")
            time.sleep(2)
            print("To get full access to the Script Follow this steps")
            print("==================================================")
            print("01. Join this discord Server: https://discord.gg/VhZPurRWf8")
            print("02. reqest License Key from Admin or Dev")
            print("03. give this key if they ask for product id")
            print("======================")
            print("04. product Id:" + pid)
            print("======================")
            print("05.Wait until the admin or dev gives you full access to the script")
            print("Press Enter To Exit")
            input()
            exit()






LogIn()