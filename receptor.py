# Librerias
import json
import const
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


cred = credentials.Certificate("private_key.json")

firebase_admin.initialize_app(cred, {'databaseURL': const.serverDb})

def onInstruction(newInstruction):
    # data = json.load(newInstruction.data)
    print(newInstruction.data) 

# def main():
ref = db.reference("/instructionsid1")
values = ref.listen(onInstruction)
print(values)

# if __name__ == '__main__':
#     main()