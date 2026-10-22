class SensorTemperatura:
    def __init__(self, id_sensor, temperatura):
        self.id_sensor = id_sensor
        self.temperatura = temperatura
        self.categoria = ""
        self.accion = ""

    def get_temperatura(self):
        return self.temperatura

    def set_temperatura(self, temperatura):
        self.temperatura = temperatura

    def evaluar_temperatura(self):
        if self.temperatura < 18:
            self.categoria = "fría"
            self.accion = "enciende la calefacción"
        elif 18 <= self.temperatura <= 25:
            self.categoria = "óptima"
            self.accion = "sin acción"
        else:
            self.categoria = "caliente"
            self.accion = "activa el aire acondicionado"

    def ver_info(self):
        return f"Sensor {self.id_sensor}: Temp {self.temperatura}°C - {self.categoria} ({self.accion})"


class Edificio:
    def __init__(self):
        self.sensores = []

    def agregar_sensor(self, sensor):
        self.sensores.append(sensor)

    def generar_resumen(self):
        frias = sum(1 for s in self.sensores if s.categoria == "fría")
        optimas = sum(1 for s in self.sensores if s.categoria == "óptima")
        calientes = sum(1 for s in self.sensores if s.categoria == "caliente")
        return f"Resumen: {frias} habitaciones frías, {optimas} óptimas, {calientes} calientes."
