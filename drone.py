# Librerias
import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

class Drone:
    serverDb = 'https://conexionehecatl2021-default-rtdb.firebaseio.com/'
    nameCollection = 'instructionsid'
    __idDrone = 1
    __ref = None

    def __init__(self):
        # Inciializar instancia de firebase
        cred = credentials.Certificate("private_key.json")
        firebase_admin.initialize_app(cred, {'databaseURL': self.serverDb})
        self.__ref = db.reference("/%s%d"%(self.nameCollection, self.__idDrone))
        self.__ref.listen(self.onInstruction)
        self.__ref.push({'ins': 'ready'})

    def onInstruction(self, dataRecived):
        dataRec = dataRecived.data
        if('ins' in dataRec):
            instruction = dataRec['ins']
            print(instruction)
