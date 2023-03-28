import threading
import time
from random import uniform
from sensorModel import SensorModel
from database import Database

# Setando BD e model
db = Database(database="bancoiot", collection="sensores")
db.resetDatabase()
sensor = SensorModel(database=db)


# Thread para os sensores
def thread_sensor(nomeSensor, intervalo):
    while True:
        # Lendo leitores do sensor e testando o alarme
        read = sensor.read_sensor_by_name(nomeSensor)
        if not read["sensorAlarmado"]:
            # Numero aleatório, float com 2 casas decimais
            random_value = round(uniform(30, 40), 2)
            print(f'Temperatura do {nomeSensor}: {random_value} {read["unidadeMedida"]}')
            sensor.update_sensor(nomeSensor, random_value)
        else:
            print(f'Atenção! Temperatura  muito  alta! Verificar Sensor {nomeSensor}!')

        time.sleep(intervalo)


# Criando Sensores
sensor.create_sensor("Temp1", "C°")
sensor.create_sensor("Temp2", "C°")
sensor.create_sensor("Temp3", "C°")

# Abrindo e executando Threads
x = threading.Thread(target=thread_sensor, args=("Temp1", 5))
y = threading.Thread(target=thread_sensor, args=("Temp2", 5))
z = threading.Thread(target=thread_sensor, args=("Temp3", 5))
x.start()
y.start()
z.start()
