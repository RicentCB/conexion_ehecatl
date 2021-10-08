# Librerias
import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

class Drone:
    __serverDb = 'https://conexionehecatl2021-default-rtdb.firebaseio.com/'
    __nameCollection = 'instructionsid'
    __idDrone = 1
    __ref = None

    def __init__(self):
        # Inciializar instancia de firebase
        cred = credentials.Certificate("private_key.json")
        firebase_admin.initialize_app(cred, {'databaseURL': self.__serverDb})
        self.__ref = db.reference("/%s%d"%(self.__nameCollection, self.__idDrone))
        self.setReady()
        self.__ref.listen(self.onInstruction)
    
    def setReady(self):
        self.__ref.parent.delete();
        self.__ref.push({'ins': 'ready'})


    def onInstruction(self, dataRecived):
        dataRec = dataRecived.data
        if(dataRec != None and 'ins' in dataRec):
            instruction = dataRec['ins']
            print(instruction)
            if(instruction == 'prepared'):
                self.setReady()