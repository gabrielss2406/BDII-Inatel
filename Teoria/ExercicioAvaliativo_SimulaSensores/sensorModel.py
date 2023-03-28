class SensorModel:
    def __init__(self, database):
        self.db = database

    def create_sensor(self, nomeSensor: str, unidadeMedida: str):
        try:
            res = self.db.collection.insert_one({"nomeSensor": nomeSensor,
                                                 "valorSensor": 0,
                                                 "unidadeMedida": unidadeMedida,
                                                 "sensorAlarmado": False})
            return res.inserted_id
        except Exception as e:
            print(f"An error occurred while creating sensor: {e}")
            return None

    def read_sensor_by_name(self, nomeSensor: str):
        try:
            res = self.db.collection.find_one({"nomeSensor": nomeSensor})
            return res
        except Exception as e:
            print(f"An error occurred while reading sensor: {e}")
            return None

    def update_sensor(self, nomeSensor: str, valorSensor: float):
        try:
            if valorSensor > 38:
                sensorAlarmado = True
            else:
                sensorAlarmado = False
            res = self.db.collection.update_one({"nomeSensor": nomeSensor},
                                                {"$set": {"valorSensor": valorSensor, "sensorAlarmado": sensorAlarmado}})
            if valorSensor > 38:
                print(f'Atenção! Temperatura  muito  alta! Verificar Sensor {nomeSensor}!')
            return res.modified_count
        except Exception as e:
            print(f"An error occurred while updating sensor: {e}")
            return None
