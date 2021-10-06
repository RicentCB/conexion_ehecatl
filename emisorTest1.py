import sys
import os
from firebase import firebase
from dotenv import load_dotenv

load_dotenv()

# FUNCION PRINCIPAL DEL PROGRAMA
# try:
#Variable con la url de la base de adtos
serverDb = 'https://conexionehecatl2021-default-rtdb.firebaseio.com/'
#Conexion con las base de datos
firebaseApp = firebase.FirebaseApplication(serverDb, None)

datos = {'instruction': 'empezando'}

firebaseApp.post('/instructions',datos)
# while True:
# Leer DB por metodo GET
# readData = firebaseApp.get('/', '')
# values = list(readData.values())

# # Datos leidos
# print("Datos recibidos dato")
# print(readData)
# print(values)
# except:
#     sys.exit("Error al conectarse")
