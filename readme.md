## Para uso general
Se necesita configurar el proyecto en firebase y tener los siguientes paquetes instalados
```bash
    sudo pip install firebase-admin
    sudo pip3 install firebase-admin
```

## Para uso en Raspberry
Se necesitan tener git para clonar el repostiorio, y el manejador de paquetes "pip".
```bash
    sudo apt update
    sudo apt install git
    sudo apt-get update
    sudo apt-get install python-pip
```
**Tambien es necesario correr el script con una version de python >= 3**, pro deafult las operaciones matematicas no generan "luagares decimales", por eso es necesarioa agregar el argumento **`-Qnew`**
```bash
    python3 -Qnew main.py
```

Crear un archivo en la raiz del proyecto llamado **`private_key.json`**, el cual sera otorgado por el administrador del proyecto de firebase.