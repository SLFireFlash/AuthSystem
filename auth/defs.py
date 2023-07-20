import random
import json

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

def LogWrite():          
    productKey= ProId()

    with open("logs.json","r")as Rlog:
        logLoad = json.load(Rlog)
        logkey = logLoad['Product']['product_key']

    if len(logkey) == 0:
        print("no product key")
        logLoad['Product']['product_key']= productKey
    else:
        print("product key found")

    with open("logs.json","w")as wlog:
        json.dump(logLoad,wlog,indent=4)


def checkProKeyFromLog():
    with open("logs.json","r")as Rlog:
        logData = json.load(Rlog)
        productKey = logData["Product"]["product_key"]
        print(productKey)
    if len(productKey) != 0:
        pass
    else:
        print("no key")

def convert_to_byte_file(input_file, output_file):
    with open(input_file, 'rb') as file:
        byte_data = file.read()

    with open(output_file, 'wb') as byte_file:
        byte_file.write(byte_data)

if __name__ == "__main__":
    # Replace 'your_input_file.txt' with the name of the file you want to convert to bytes
    input_file_name = 'your_input_file.txt'

    # Replace 'output_byte_file.bin' with the name you want for the output byte file
    output_file_name = 'output_byte_file.bin'

    convert_to_byte_file(input_file_name, output_file_name)



LogWrite()
checkProKeyFromLog()