import threading
import random
import time
from database import Database

db = Database(database="bancoiot", collection="sensores")

#gerando a temperatura
def gerar_temperatura():
    return round(random.uniform(30, 40), 2)


#simulando a leitura da temperatura
def simular_leitura(sensor_name, db):
    while True:
        temperatura = gerar_temperatura()
        print(f"{sensor_name}: {temperatura} C°")

        time.sleep(5)


# Lista de sensores
sensores = ["Temp1", "Temp2", "Temp3"]

# Inicializando threads
threads = []
for sensor in sensores:
    thread = threading.Thread(target=simular_leitura, args=(sensor, None))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

db.insert_sensor_data(sensores)